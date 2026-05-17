import json
import os
import subprocess
import sys
from pathlib import Path

from PySide6.QtNetwork import QLocalServer, QLocalSocket

from PySide6.QtCore import (
    QFileInfo,
    QMimeData,
    QSize,
    Qt,
    QUrl,
    Signal,
)
from PySide6.QtGui import (
    QAction,
    QDrag,
    QKeySequence,
)
from PySide6.QtWidgets import (
    QApplication,
    QFileDialog,
    QFileIconProvider,
    QHBoxLayout,
    QLabel,
    QListWidget,
    QListWidgetItem,
    QMenu,
    QMessageBox,
    QPushButton,
    QSystemTrayIcon,
    QToolButton,
    QVBoxLayout,
    QWidget,
)

STATE_FILE = Path.home() / ".config" / "shelfdrop" / "state.json"
IPC_NAME = f"shelfdrop-{os.getuid()}"
ICON_PROVIDER = QFileIconProvider()


def load_state():
    if not STATE_FILE.exists():
        return {"files": [], "geometry": None, "always_on_top": True}
    try:
        return json.loads(STATE_FILE.read_text())
    except Exception:
        return {"files": [], "geometry": None, "always_on_top": True}


def save_state(state):
    STATE_FILE.parent.mkdir(parents=True, exist_ok=True)
    STATE_FILE.write_text(json.dumps(state, indent=2))


class ShelfList(QListWidget):
    files_dropped = Signal(list)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setAcceptDrops(True)
        self.setDragEnabled(True)
        self.setSelectionMode(QListWidget.ExtendedSelection)
        self.setViewMode(QListWidget.IconMode)
        self.setIconSize(QSize(48, 48))
        self.setGridSize(QSize(96, 80))
        self.setResizeMode(QListWidget.Adjust)
        self.setMovement(QListWidget.Static)
        self.setWordWrap(True)
        self.setUniformItemSizes(True)
        self.setSpacing(4)
        self._drag_start = None

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super().dragEnterEvent(event)

    def dragMoveEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()
        else:
            super().dragMoveEvent(event)

    def dropEvent(self, event):
        md = event.mimeData()
        if md.hasUrls():
            paths = [u.toLocalFile() for u in md.urls() if u.toLocalFile()]
            if paths:
                self.files_dropped.emit(paths)
                event.acceptProposedAction()
                return
        super().dropEvent(event)

    def mousePressEvent(self, event):
        if event.button() == Qt.LeftButton:
            self._drag_start = event.position().toPoint()
        super().mousePressEvent(event)

    def mouseMoveEvent(self, event):
        if not (event.buttons() & Qt.LeftButton) or self._drag_start is None:
            return super().mouseMoveEvent(event)
        if (event.position().toPoint() - self._drag_start).manhattanLength() < QApplication.startDragDistance():
            return super().mouseMoveEvent(event)

        items = self.selectedItems()
        if not items:
            return super().mouseMoveEvent(event)

        urls = []
        for it in items:
            p = it.data(Qt.UserRole)
            if p and Path(p).exists():
                urls.append(QUrl.fromLocalFile(p))
        if not urls:
            return

        drag = QDrag(self)
        md = QMimeData()
        md.setUrls(urls)
        drag.setMimeData(md)

        first = items[0]
        icon = first.icon()
        if not icon.isNull():
            drag.setPixmap(icon.pixmap(48, 48))
        drag.exec(Qt.CopyAction | Qt.LinkAction, Qt.CopyAction)


class ShelfWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.state = load_state()

        self.setWindowTitle("ShelfDrop")
        self.setAcceptDrops(True)
        self._apply_always_on_top(self.state.get("always_on_top", True), show=False)
        self.resize(380, 260)

        self._build_ui()
        self._restore_geometry()
        self._restore_files()

    def _build_ui(self):
        root = QVBoxLayout(self)
        root.setContentsMargins(8, 6, 8, 8)
        root.setSpacing(6)

        bar = QHBoxLayout()
        bar.setSpacing(4)

        title = QLabel("ShelfDrop")
        title.setStyleSheet("font-weight: 600;")
        bar.addWidget(title)
        bar.addStretch(1)

        self.count_label = QLabel("0 items")
        self.count_label.setStyleSheet("color: #888; font-size: 11px;")
        bar.addWidget(self.count_label)

        self.menu_btn = QToolButton()
        self.menu_btn.setText("☰")
        self.menu_btn.setPopupMode(QToolButton.InstantPopup)
        self.menu_btn.setMenu(self._build_menu())
        bar.addWidget(self.menu_btn)

        root.addLayout(bar)

        self.list = ShelfList(self)
        self.list.files_dropped.connect(self.add_files)
        self.list.customContextMenuRequested.connect(self._item_context_menu)
        self.list.setContextMenuPolicy(Qt.CustomContextMenu)
        self.list.itemDoubleClicked.connect(self._open_item)
        root.addWidget(self.list, 1)

        self.hint = QLabel("Drop files here  •  drag out to copy")
        self.hint.setAlignment(Qt.AlignCenter)
        self.hint.setStyleSheet("color: #888; font-size: 11px;")
        root.addWidget(self.hint)

    def _build_menu(self):
        m = QMenu(self)

        act_add = QAction("Add files…", self)
        act_add.setShortcut(QKeySequence("Ctrl+O"))
        act_add.triggered.connect(self._pick_files)
        self.addAction(act_add)
        m.addAction(act_add)

        act_clear = QAction("Clear all", self)
        act_clear.setShortcut(QKeySequence("Ctrl+L"))
        act_clear.triggered.connect(self.clear_all)
        self.addAction(act_clear)
        m.addAction(act_clear)

        m.addSeparator()

        self.act_pin = QAction("Always on top", self, checkable=True)
        self.act_pin.setChecked(self.state.get("always_on_top", True))
        self.act_pin.toggled.connect(self._toggle_pin)
        m.addAction(self.act_pin)

        act_hide = QAction("Hide window", self)
        act_hide.setShortcut(QKeySequence("Ctrl+H"))
        act_hide.triggered.connect(self.hide)
        self.addAction(act_hide)
        m.addAction(act_hide)

        m.addSeparator()

        act_about = QAction("About", self)
        act_about.triggered.connect(self._about)
        m.addAction(act_about)

        act_quit = QAction("Quit", self)
        act_quit.setShortcut(QKeySequence("Ctrl+Q"))
        act_quit.triggered.connect(QApplication.instance().quit)
        self.addAction(act_quit)
        m.addAction(act_quit)

        return m

    def _apply_always_on_top(self, on, show=True):
        flags = self.windowFlags()
        if on:
            flags |= Qt.WindowStaysOnTopHint
        else:
            flags &= ~Qt.WindowStaysOnTopHint
        self.setWindowFlags(flags)
        if show:
            self.show()

    def _toggle_pin(self, on):
        self.state["always_on_top"] = on
        self._apply_always_on_top(on, show=True)

    def _restore_geometry(self):
        g = self.state.get("geometry")
        if g and isinstance(g, list) and len(g) == 4:
            self.setGeometry(*g)

    def _restore_files(self):
        files = self.state.get("files", [])
        existing = [p for p in files if Path(p).exists()]
        self.add_files(existing, persist=False)

    def add_files(self, paths, persist=True):
        seen = {self.list.item(i).data(Qt.UserRole) for i in range(self.list.count())}
        for p in paths:
            p = os.path.abspath(p)
            if p in seen:
                continue
            seen.add(p)
            item = QListWidgetItem(Path(p).name)
            item.setData(Qt.UserRole, p)
            item.setToolTip(p)
            item.setIcon(ICON_PROVIDER.icon(QFileInfo(p)))
            self.list.addItem(item)
        self._update_count()
        if persist:
            self._persist_files()

    def clear_all(self):
        self.list.clear()
        self._update_count()
        self._persist_files()

    def _persist_files(self):
        paths = [self.list.item(i).data(Qt.UserRole) for i in range(self.list.count())]
        self.state["files"] = paths
        save_state(self.state)

    def _update_count(self):
        n = self.list.count()
        self.count_label.setText(f"{n} item{'s' if n != 1 else ''}")

    def _pick_files(self):
        files, _ = QFileDialog.getOpenFileNames(self, "Add files", str(Path.home()))
        if files:
            self.add_files(files)

    def _open_item(self, item):
        path = item.data(Qt.UserRole)
        if path:
            subprocess.Popen(["xdg-open", path])

    def _item_context_menu(self, pos):
        item = self.list.itemAt(pos)
        if not item:
            return
        path = item.data(Qt.UserRole)
        m = QMenu(self)
        m.addAction("Open", lambda: subprocess.Popen(["xdg-open", path]))
        m.addAction("Reveal in folder", lambda: subprocess.Popen(["xdg-open", str(Path(path).parent)]))
        m.addAction("Copy path", lambda: QApplication.clipboard().setText(path))
        m.addSeparator()
        m.addAction("Remove from shelf", lambda: self._remove_item(item))
        m.exec(self.list.mapToGlobal(pos))

    def _remove_item(self, item):
        self.list.takeItem(self.list.row(item))
        self._update_count()
        self._persist_files()

    def dragEnterEvent(self, event):
        if event.mimeData().hasUrls():
            event.acceptProposedAction()

    def dropEvent(self, event):
        md = event.mimeData()
        if md.hasUrls():
            paths = [u.toLocalFile() for u in md.urls() if u.toLocalFile()]
            if paths:
                self.add_files(paths)
                event.acceptProposedAction()

    def toggle_visibility(self):
        if self.isVisible() and self.isActiveWindow():
            self.hide()
        else:
            self.show()
            self.raise_()
            self.activateWindow()

    def closeEvent(self, event):
        self.state["geometry"] = [self.x(), self.y(), self.width(), self.height()]
        save_state(self.state)
        super().closeEvent(event)

    def _about(self):
        QMessageBox.information(
            self,
            "ShelfDrop",
            "ShelfDrop — a tiny drag-and-drop shelf.\n\n"
            "Drop files in. Drag them back out into any file manager or app.\n"
            "Right-click an item for open / reveal / copy path / remove.",
        )


def make_tray(window):
    icon = window.style().standardIcon(window.style().StandardPixmap.SP_DirIcon)
    tray = QSystemTrayIcon(icon, window)
    tray.setToolTip("ShelfDrop")
    menu = QMenu()
    menu.addAction("Show / hide", lambda: window.hide() if window.isVisible() else (window.show(), window.raise_(), window.activateWindow()))
    menu.addSeparator()
    menu.addAction("Quit", QApplication.instance().quit)
    tray.setContextMenu(menu)
    tray.activated.connect(lambda reason: (window.show(), window.raise_(), window.activateWindow()) if reason == QSystemTrayIcon.Trigger else None)
    tray.show()
    return tray


def send_to_running(command):
    sock = QLocalSocket()
    sock.connectToServer(IPC_NAME)
    if not sock.waitForConnected(300):
        return False
    sock.write(command.encode() + b"\n")
    sock.flush()
    sock.waitForBytesWritten(300)
    sock.disconnectFromServer()
    return True


def main():
    args = sys.argv[1:]
    is_toggle = "--toggle" in args
    is_show = "--show" in args

    if is_toggle and send_to_running("toggle"):
        return 0
    if is_show and send_to_running("show"):
        return 0
    # If --toggle was passed but no instance is running, fall through and start one.

    app = QApplication(sys.argv)
    app.setQuitOnLastWindowClosed(False)
    app.setApplicationName("ShelfDrop")

    w = ShelfWindow()

    server = QLocalServer()
    QLocalServer.removeServer(IPC_NAME)
    if not server.listen(IPC_NAME):
        print(f"Warning: could not start IPC server: {server.errorString()}", file=sys.stderr)

    def on_new_connection():
        client = server.nextPendingConnection()
        if not client:
            return

        def on_ready():
            data = bytes(client.readAll()).decode(errors="ignore").strip()
            if data == "toggle":
                w.toggle_visibility()
            elif data == "show":
                w.show()
                w.raise_()
                w.activateWindow()
            client.disconnectFromServer()

        client.readyRead.connect(on_ready)

    server.newConnection.connect(on_new_connection)

    if not is_toggle:
        w.show()

    tray = make_tray(w)
    _ = tray  # keep reference

    return app.exec()


if __name__ == "__main__":
    sys.exit(main() or 0)
