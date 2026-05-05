#!/usr/bin/env python3
"""
fsm — Full Scope Media Site Manager
Usage: python3 fsm.py
"""

from __future__ import annotations

import subprocess
from pathlib import Path

from textual.app import App, ComposeResult
from textual.binding import Binding
from textual.containers import Horizontal, Vertical
from textual.screen import ModalScreen
from textual.widgets import Button, Footer, Header, Input, Label, RichLog, Static
from textual import work
from rich.text import Text

REPO = Path(__file__).parent
NPM = "/usr/share/nodejs/corepack/shims/npm"

# ─── helpers ──────────────────────────────────────────────────────────────────

def run(*cmd: str, cwd: Path = REPO) -> tuple[int, str]:
    r = subprocess.run(list(cmd), capture_output=True, text=True, cwd=cwd)
    return r.returncode, (r.stdout + r.stderr).strip()


STATUS_STYLE = {"M": "yellow", "A": "green", "D": "red", "R": "cyan", "?": "dim white"}

def parse_git_status(raw: str) -> list[tuple[str, str]]:
    out = []
    for line in raw.splitlines():
        if len(line) >= 4:
            xy = line[:2].strip()
            code = xy[0] if xy and xy[0] != " " else (xy[1] if len(xy) > 1 else "?")
            out.append((code, line[3:]))
    return out


# ─── deploy modal ─────────────────────────────────────────────────────────────

class DeployModal(ModalScreen[str | None]):
    CSS = """
    DeployModal { align: center middle; }
    #box {
        width: 64;
        height: auto;
        border: double $primary;
        background: $surface;
        padding: 2 3;
    }
    #title  { text-style: bold; margin-bottom: 1; }
    #hint   { color: $text-muted; margin-bottom: 1; }
    #msg    { margin-bottom: 1; }
    #btns   { align: right middle; height: auto; margin-top: 1; }
    #btns Button { margin-left: 1; }
    """

    def compose(self) -> ComposeResult:
        with Vertical(id="box"):
            yield Label("⬆  Deploy to GitHub", id="title")
            yield Label("Describe what changed (used as the commit message):", id="hint")
            yield Input(placeholder="e.g. Update pricing, add new portfolio photo", id="msg")
            with Horizontal(id="btns"):
                yield Button("Cancel", variant="default", id="cancel")
                yield Button("Push Live →", variant="primary", id="confirm")

    def on_button_pressed(self, e: Button.Pressed) -> None:
        if e.button.id == "confirm":
            msg = self.query_one("#msg", Input).value.strip()
            self.dismiss(msg or None)
        else:
            self.dismiss(None)

    def on_input_submitted(self, e: Input.Submitted) -> None:
        msg = e.value.strip()
        self.dismiss(msg or None)


# ─── main app ─────────────────────────────────────────────────────────────────

class FSMApp(App):
    TITLE = "Full Scope Media — Site Manager"
    SUB_TITLE = "github.com/MilkWithKnives/FSM"

    CSS = """
    Screen { background: $surface; }

    #body {
        height: 1fr;
        padding: 0 1;
    }

    #left {
        width: 2fr;
        margin-right: 1;
    }

    #right {
        width: 3fr;
    }

    .panel {
        border: round $primary-darken-2;
        height: 1fr;
        padding: 0 1;
    }

    .panel-title {
        color: $accent;
        text-style: bold;
        padding: 0 1;
        background: $primary-darken-3;
        width: 100%;
        margin-bottom: 1;
    }

    #output {
        height: 12;
        border: round $accent-darken-2;
        padding: 0 1;
        margin: 0 1;
    }

    #output-title {
        color: $accent;
        text-style: bold;
        padding: 0 1;
        background: $accent-darken-3;
        width: 100%;
        margin-bottom: 1;
    }

    #actions {
        height: auto;
        padding: 1 1;
        align: center middle;
    }

    #actions Button { margin: 0 1; min-width: 18; }
    """

    BINDINGS = [
        Binding("d", "deploy",       "Deploy",      show=True),
        Binding("r", "dev_server",   "Dev Server",  show=True),
        Binding("b", "build_check",  "Build Check", show=True),
        Binding("s", "refresh",      "Refresh",     show=True),
        Binding("q", "quit",         "Quit",        show=True),
    ]

    def compose(self) -> ComposeResult:
        yield Header()

        with Horizontal(id="body"):
            with Vertical(id="left"):
                with Vertical(classes="panel"):
                    yield Static("  CHANGED FILES", classes="panel-title")
                    yield RichLog(id="status-log", highlight=True, markup=True, wrap=False)

            with Vertical(id="right"):
                with Vertical(classes="panel"):
                    yield Static("  RECENT COMMITS", classes="panel-title")
                    yield RichLog(id="commits-log", highlight=True, markup=True, wrap=False)

        with Vertical(id="output"):
            yield Static("  OUTPUT", id="output-title")
            yield RichLog(id="output-log", highlight=True, markup=True, wrap=True)

        with Horizontal(id="actions"):
            yield Button("⬆  Deploy [D]",      variant="primary", id="btn-deploy")
            yield Button("⚡ Dev Server [R]",   variant="success", id="btn-dev")
            yield Button("✓  Build Check [B]",  variant="default", id="btn-build")
            yield Button("↺  Refresh [S]",      variant="default", id="btn-refresh")
            yield Button("✕  Quit [Q]",         variant="error",   id="btn-quit")

        yield Footer()

    def on_mount(self) -> None:
        self.action_refresh()

    # ── panel helpers ──────────────────────────────────────────────────────────

    def refresh_status(self) -> None:
        log = self.query_one("#status-log", RichLog)
        log.clear()
        _, raw = run("git", "status", "--porcelain")
        if not raw:
            log.write(Text("  ✓  Working tree clean", style="dim green"))
        else:
            for code, path in parse_git_status(raw):
                style = STATUS_STYLE.get(code, "white")
                label = {"M": "modified", "A": "added", "D": "deleted",
                         "R": "renamed",  "?": "untracked"}.get(code, code)
                log.write(Text(f"  {code}  {path}  ", style=style) +
                          Text(f"({label})", style="dim " + style))

        clog = self.query_one("#commits-log", RichLog)
        clog.clear()
        _, raw = run("git", "log", "--oneline", "--decorate", "-20")
        for line in raw.splitlines():
            parts = line.split(" ", 1)
            sha  = Text(f"  {parts[0]} ", style="bold cyan")
            rest = Text(parts[1] if len(parts) > 1 else "", style="white")
            clog.write(sha + rest)

    def out(self, text: str, style: str = "white") -> None:
        log = self.query_one("#output-log", RichLog)
        for line in (text or "").splitlines():
            log.write(Text(line, style=style))

    def divider(self, label: str) -> None:
        self.out(f"── {label}", style="bold cyan")

    # ── button routing ─────────────────────────────────────────────────────────

    def on_button_pressed(self, e: Button.Pressed) -> None:
        dispatch = {
            "btn-deploy":  self.action_deploy,
            "btn-dev":     self.action_dev_server,
            "btn-build":   self.action_build_check,
            "btn-refresh": self.action_refresh,
            "btn-quit":    self.action_quit,
        }
        if e.button.id in dispatch:
            dispatch[e.button.id]()

    # ── actions ────────────────────────────────────────────────────────────────

    def action_refresh(self) -> None:
        self.refresh_status()
        self.out("Status refreshed.", style="dim")

    def action_deploy(self) -> None:
        def on_result(msg: str | None) -> None:
            if msg:
                self._deploy(msg)
        self.push_screen(DeployModal(), on_result)

    @work(thread=True)
    def _deploy(self, msg: str) -> None:
        self.call_from_thread(self.divider, "Staging all changes")
        code, out = run("git", "add", "-A")
        self.call_from_thread(self.out, out or "  Done.")

        self.call_from_thread(self.divider, "Committing")
        code, out = run("git", "commit", "-m", msg)
        if code != 0 and "nothing to commit" not in out:
            self.call_from_thread(self.out, out, "red")
            return
        self.call_from_thread(self.out, out)

        self.call_from_thread(self.divider, "Pushing to GitHub")
        code, out = run("git", "push")
        self.call_from_thread(self.out, out, "green" if code == 0 else "red")

        if code == 0:
            self.call_from_thread(self.out, "✓ Live! Check github.com/MilkWithKnives/FSM", "bold green")
        else:
            self.call_from_thread(self.out, "✗ Push failed — see above.", "bold red")

        self.call_from_thread(self.refresh_status)

    @work(thread=True)
    def action_dev_server(self) -> None:
        self.call_from_thread(self.divider, "Dev server → http://localhost:5173")
        proc = subprocess.Popen(
            [NPM, "run", "dev"],
            cwd=REPO,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            text=True,
        )
        self.call_from_thread(self.out, f"  PID {proc.pid} — press Q to quit this tool (server keeps running)", "dim")
        for line in iter(proc.stdout.readline, ""):
            self.call_from_thread(self.out, line.rstrip())

    @work(thread=True)
    def action_build_check(self) -> None:
        self.call_from_thread(self.divider, "Type-checking")
        code, out = run(NPM, "run", "check")
        style = "green" if code == 0 else "red"
        self.call_from_thread(self.out, out, style)
        msg = "✓ No errors." if code == 0 else "✗ Errors found — fix before deploying."
        self.call_from_thread(self.out, msg, "bold " + style)


# ─── entry ────────────────────────────────────────────────────────────────────

if __name__ == "__main__":
    FSMApp().run()
