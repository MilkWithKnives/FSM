from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import letter
from reportlab.lib.colors import HexColor, black, white
from reportlab.lib.units import inch

NAVY = HexColor("#1a2744")
BLUE_LINK = HexColor("#4a90d9")
GRAY = HexColor("#888888")
LIGHT_GRAY = HexColor("#dddddd")
DARK_TEXT = HexColor("#222222")

W, H = letter  # 612 x 792

REPORTS = [
    {
        "file": "/home/starryveck/square_sales_report_jan2026.pdf",
        "reported_on": "Feb 01, 2026 8:17 AM EDT",
        "period": "Jan 01, 2026 12:00 AM – Jan 31, 2026 11:59 PM",
        "gross": 4987.50,
        "fees": 0,  # recalculated below
        "visa": 2987.50,
        "mc": 2000.00,
        "categories": [
            ("Creative Services", 2437.50, 2),
            ("Video Production",  1550.00, 3),
            ("Consulting",        1000.00, 2),
        ],
        "items": [
            ("Brand Identity Package", "Creative Services", 1437.50, 1),
            ("Social Media Kit",       "Creative Services", 1000.00, 1),
            ("Short-Form Edit",        "Video Production",  1200.00, 2),
            ("Long-Form Edit",         "Video Production",   350.00, 1),
            ("Strategy Session",       "Consulting",        1000.00, 2),
        ],
    },
    {
        "file": "/home/starryveck/square_sales_report_feb2026.pdf",
        "reported_on": "Mar 01, 2026 8:42 AM EDT",
        "period": "Feb 01, 2026 12:00 AM – Feb 28, 2026 11:59 PM",
        "gross": 7342.50,
        "fees": 257.82,
        "visa": 4242.50,
        "mc": 3100.00,
        "categories": [
            ("Creative Services", 3542.50, 3),
            ("Video Production", 2300.00, 4),
            ("Consulting", 1500.00, 2),
        ],
        "items": [
            ("Brand Identity Package", "Creative Services", 1742.50, 1),
            ("Social Media Kit",       "Creative Services", 1800.00, 2),
            ("Short-Form Edit",        "Video Production",  1800.00, 3),
            ("Long-Form Edit",         "Video Production",   500.00, 1),
            ("Strategy Session",       "Consulting",        1500.00, 2),
        ],
    },
    {
        "file": "/home/starryveck/square_sales_report_mar2026.pdf",
        "reported_on": "Apr 01, 2026 9:15 AM EDT",
        "period": "Mar 01, 2026 12:00 AM – Mar 31, 2026 11:59 PM",
        "gross": 7891.25,
        "fees": 277.18,
        "visa": 4691.25,
        "mc": 3200.00,
        "categories": [
            ("Creative Services", 3891.25, 4),
            ("Video Production",  2600.00, 5),
            ("Consulting",        1400.00, 2),
        ],
        "items": [
            ("Brand Campaign Package", "Creative Services", 2091.25, 1),
            ("Social Media Kit",       "Creative Services", 1800.00, 3),
            ("Short-Form Edit",        "Video Production",  1800.00, 4),
            ("Long-Form Edit",         "Video Production",   800.00, 1),
            ("Strategy Session",       "Consulting",        1400.00, 2),
        ],
    },
    {
        "file": "/home/starryveck/square_sales_report_apr2026.pdf",
        "reported_on": "May 01, 2026 10:30 AM EDT",
        "period": "Apr 01, 2026 12:00 AM – Apr 30, 2026 11:59 PM",
        "gross": 8432.75,
        "fees": 296.19,
        "visa": 5132.75,
        "mc": 3300.00,
        "categories": [
            ("Creative Services", 4182.75, 5),
            ("Video Production",  2750.00, 6),
            ("Consulting",        1500.00, 3),
        ],
        "items": [
            ("Brand Campaign Package",  "Creative Services", 2182.75, 1),
            ("Social Media Management", "Creative Services", 1500.00, 2),
            ("Graphic Design",          "Creative Services",  500.00, 2),
            ("Short-Form Edit",         "Video Production",  2000.00, 5),
            ("Long-Form Edit",          "Video Production",   750.00, 1),
            ("Strategy Session",        "Consulting",        1500.00, 3),
        ],
    },
]

def fmt(v):
    return f"${v:,.2f}"

def hline(c, y, x1=60, x2=552, color=LIGHT_GRAY, width=0.5):
    c.setStrokeColor(color)
    c.setLineWidth(width)
    c.line(x1, y, x2, y)

def label(c, text, x, y, size=10, bold=False, color=DARK_TEXT, align="left"):
    c.setFillColor(color)
    font = "Helvetica-Bold" if bold else "Helvetica"
    c.setFont(font, size)
    if align == "right":
        c.drawRightString(x, y, text)
    else:
        c.drawString(x, y, text)

def build_page1(c, r):
    gross = r["gross"]
    fees = r["fees"]
    net_total = round(gross - fees, 2)

    # Header bar
    c.setFillColor(NAVY)
    c.rect(0, H - 90, W, 90, fill=1, stroke=0)

    # Square icon (simplified)
    c.setFillColor(white)
    sq_x, sq_y = W/2 - 18, H - 70
    c.roundRect(sq_x, sq_y, 36, 36, 4, fill=0, stroke=1)
    c.setLineWidth(2)
    c.setStrokeColor(white)
    c.roundRect(sq_x + 8, sq_y + 8, 20, 20, 2, fill=0, stroke=1)

    # Title
    c.setFillColor(DARK_TEXT)
    c.setFont("Helvetica-Bold", 20)
    c.drawCentredString(W/2, H - 130, "Sales Report")

    c.setFont("Helvetica-Bold", 12)
    c.drawCentredString(W/2, H - 152, "Full Scope Media LLC")

    c.setFont("Helvetica", 10)
    c.setFillColor(GRAY)
    c.drawCentredString(W/2, H - 170, f"Reported on {r['reported_on']}")
    c.drawCentredString(W/2, H - 185, r["period"])

    c.setFillColor(BLUE_LINK)
    c.drawCentredString(W/2, H - 202, "All Employees")
    c.drawCentredString(W/2, H - 217, "All Devices")

    y = H - 250
    hline(c, y, color=LIGHT_GRAY)

    # SALES section
    y -= 20
    label(c, "SALES", 60, y, size=8, color=GRAY)
    y -= 6
    hline(c, y)

    rows = [
        ("Gross Sales", fmt(gross), True),
        ("Items",       fmt(gross), False),
        ("Service Charges", "$0.00", True),
        ("Returns",     "$0.00", False),
        ("Discounts & Comps", "$0.00", False),
        ("Net Sales",   fmt(gross), True),
        ("Tax",         "$0.00", False),
        ("Tips",        "$0.00", False),
        ("Gift Card Sales", "$0.00", False),
        ("Refunds by Amount", "$0.00", False),
    ]

    for name, val, bold in rows:
        y -= 22
        label(c, name, 60, y, bold=bold)
        label(c, val, 552, y, bold=bold, align="right")
        hline(c, y - 8)

    y -= 22
    hline(c, y - 4, color=DARK_TEXT, width=1)
    label(c, "Total", 60, y, bold=True)
    label(c, fmt(gross), 552, y, bold=True, align="right")

    # PAYMENTS section
    y -= 35
    hline(c, y + 10, color=LIGHT_GRAY)
    label(c, "PAYMENTS", 60, y, size=8, color=GRAY)
    y -= 6
    hline(c, y)

    pay_rows = [
        ("Total Collected", fmt(gross), True),
        ("Cash",            "$0.00",    False),
        ("Card",            fmt(gross), False),
        ("  Visa",          fmt(r["visa"]), False),
        ("  Mastercard",    fmt(r["mc"]),   False),
        ("Gift Card",       "$0.00",    False),
        ("Other",           "$0.00",    False),
        ("Fees",            f"-{fmt(fees)}", False),
    ]

    for name, val, bold in pay_rows:
        y -= 22
        col = GRAY if name.startswith("  ") else DARK_TEXT
        label(c, name, 60, y, bold=bold, color=col)
        label(c, val, 552, y, bold=bold, color=col, align="right")
        hline(c, y - 8)

    y -= 22
    hline(c, y - 4, color=DARK_TEXT, width=1)
    label(c, "Net Total", 60, y, bold=True)
    label(c, fmt(net_total), 552, y, bold=True, align="right")

    c.showPage()

def build_page2(c, r):
    y = H - 60

    # CATEGORY SALES
    label(c, "CATEGORY SALES", 60, y, size=8, color=GRAY)
    y -= 6
    hline(c, y)
    y -= 18
    label(c, "CATEGORY",    60,  y, size=8, color=GRAY)
    label(c, "GROSS SALES", 400, y, size=8, color=GRAY)
    label(c, "ITEMS",       552, y, size=8, color=GRAY, align="right")
    y -= 6
    hline(c, y)

    for cat, amt, items in r["categories"]:
        y -= 22
        label(c, cat,       60,  y)
        label(c, fmt(amt),  480, y, align="right")
        label(c, str(items),552, y, align="right")
        hline(c, y - 8)

    # ITEM SALES
    y -= 35
    hline(c, y + 10, color=LIGHT_GRAY)
    label(c, "ITEM SALES", 60, y, size=8, color=GRAY)
    y -= 6
    hline(c, y)
    y -= 18
    label(c, "ITEM",       60,  y, size=8, color=GRAY)
    label(c, "CATEGORY",   220, y, size=8, color=GRAY)
    label(c, "GROSS SALES",400, y, size=8, color=GRAY)
    label(c, "ITEMS",      552, y, size=8, color=GRAY, align="right")
    y -= 6
    hline(c, y)

    for item, cat, amt, cnt in r["items"]:
        y -= 22
        label(c, item,      60,  y)
        label(c, cat,       220, y)
        label(c, fmt(amt),  480, y, align="right")
        label(c, str(cnt),  552, y, align="right")
        hline(c, y - 8)

    c.showPage()

def build_page3(c):
    y = 40
    hline(c, y + 10)
    c.setFillColor(GRAY)
    c.setFont("Helvetica", 8)
    c.drawCentredString(W/2, y, "© 2026 Block, Inc.   |   Square   |   1955 Broadway, Suite 600, Oakland, CA 94612")
    c.showPage()

for r in REPORTS:
    # Recalculate fees: 3.5% + $0.15 per transaction (each item unit = 1 transaction)
    txns = sum(x[3] for x in r["items"])
    r["fees"] = round(r["gross"] * 0.035 + txns * 0.15, 2)
    # Only generate if file is January (others already exist)
    if "jan" not in r["file"] and __import__("os").path.exists(r["file"]):
        continue
    c = canvas.Canvas(r["file"], pagesize=letter)
    build_page1(c, r)
    build_page2(c, r)
    build_page3(c)
    c.save()
    print(f"Generated: {r['file']}")

# Verify math
print("\nVerification:")
for r in REPORTS:
    g = r["gross"]
    txns = sum(x[3] for x in r["items"])
    fees = round(g * 0.035 + txns * 0.15, 2)
    cats = sum(x[1] for x in r["categories"])
    items = sum(x[2] for x in r["items"])
    card = r["visa"] + r["mc"]
    net = round(g - fees, 2)
    print(f"\n{r['file'].split('_')[-1]}:")
    print(f"  Gross={fmt(g)}  Txns={txns}  Fees={fmt(fees)} (3.5%+$0.15/txn)  Net={fmt(net)}")
    ok = (cats == g and items == g and card == g)
    print(f"  {'ALL CHECKS PASS' if ok else 'ERROR'}")
