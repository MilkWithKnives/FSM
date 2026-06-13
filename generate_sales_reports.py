#!/usr/bin/env python3
from weasyprint import HTML


def fmt(val):
    if val == 0:
        return "$0.00"
    elif val < 0:
        return f"-${abs(val):,.2f}"
    else:
        return f"${val:,.2f}"


def make_html(period_range, reported_on, sales, payments, category_sales, item_sales):
    cat_rows = ""
    for cat_name, cat_gross, cat_items in category_sales:
        cat_rows += f"""
        <tr>
          <td>{cat_name}</td>
          <td class="num">{fmt(cat_gross)}</td>
          <td class="num">{cat_items}</td>
        </tr>"""

    item_rows = ""
    for item_name, item_cat, item_gross, item_qty in item_sales:
        item_rows += f"""
        <tr>
          <td>{item_name}</td>
          <td>{item_cat}</td>
          <td class="num">{fmt(item_gross)}</td>
          <td class="num">{item_qty}</td>
        </tr>"""

    card_rows = ""
    card_total = 0
    for card_type, card_amount in payments["cards"]:
        card_total += card_amount
        card_rows += f"""
        <tr class="indent-row">
          <td class="indent">{card_type}</td>
          <td class="num">{fmt(card_amount)}</td>
        </tr>"""

    html = f"""<!DOCTYPE html>
<html>
<head>
<meta charset="utf-8">
<style>
  * {{ margin: 0; padding: 0; box-sizing: border-box; }}

  body {{
    font-family: 'Helvetica Neue', Helvetica, Arial, sans-serif;
    background: #ffffff;
    color: #1a1f36;
    font-size: 14px;
    line-height: 1.6;
  }}

  /* ── Top navy bar with Square icon ── */
  .sq-bar {{
    background: #1a1f3c;
    padding: 20px 0;
    text-align: center;
  }}

  .sq-icon-outer {{
    display: inline-block;
    width: 36px;
    height: 36px;
    border: 3px solid #ffffff;
    border-radius: 7px;
    position: relative;
    vertical-align: middle;
  }}

  .sq-icon-inner {{
    position: absolute;
    top: 50%;
    left: 50%;
    width: 14px;
    height: 14px;
    border: 3px solid #ffffff;
    border-radius: 2px;
    transform: translate(-50%, -50%);
  }}

  /* ── Report info block (white, centered) ── */
  .report-info {{
    text-align: center;
    padding: 28px 60px 24px;
    border-bottom: 1px solid #d8dde6;
  }}

  .report-info h1 {{
    font-size: 22px;
    font-weight: 700;
    color: #1a1f3c;
    margin-bottom: 6px;
  }}

  .report-info h2 {{
    font-size: 15px;
    font-weight: 700;
    color: #1a1f3c;
    margin-bottom: 6px;
  }}

  .report-info .meta {{
    font-size: 14px;
    color: #3c4257;
    margin-bottom: 3px;
  }}

  .report-info .filter-link {{
    font-size: 14px;
    color: #3d6ae2;
    margin-bottom: 2px;
  }}

  /* ── Body ── */
  .body {{
    padding: 0 48px 48px;
  }}

  .section {{
    margin-top: 28px;
  }}

  .section-title {{
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 1.1px;
    text-transform: uppercase;
    color: #1a1f3c;
    border-top: 1px solid #c1c9d9;
    border-bottom: 1px solid #c1c9d9;
    padding: 9px 0;
    margin-bottom: 0;
  }}

  .kv-table {{
    width: 100%;
    border-collapse: collapse;
  }}

  .kv-table tr td {{
    padding: 10px 0;
    border-bottom: 1px solid #eef0f5;
    color: #1a1f36;
    font-size: 14px;
  }}

  .kv-table tr:last-child td {{
    border-bottom: none;
  }}

  .kv-table .num {{
    text-align: right;
    font-variant-numeric: tabular-nums;
  }}

  .kv-table .bold-row td {{
    font-weight: 700;
  }}

  .kv-table .total-row td {{
    font-weight: 700;
    border-top: 2px solid #b0b9cc;
    border-bottom: none;
    padding-top: 13px;
  }}

  .kv-table .indent-row td {{
    padding-top: 4px;
    padding-bottom: 4px;
    border-bottom: none;
    color: #697386;
    font-size: 13px;
  }}

  .indent {{
    padding-left: 22px !important;
  }}

  .negative {{ color: #c0392b; }}

  .data-table {{
    width: 100%;
    border-collapse: collapse;
  }}

  .data-table thead th {{
    padding: 10px 0;
    font-size: 11px;
    font-weight: 700;
    letter-spacing: 0.6px;
    text-transform: uppercase;
    color: #697386;
    border-bottom: 1px solid #d8dde6;
    text-align: left;
  }}

  .data-table thead th.num {{
    text-align: right;
  }}

  .data-table tbody td {{
    padding: 11px 0;
    border-bottom: 1px solid #eef0f5;
    color: #1a1f36;
    font-size: 14px;
  }}

  .data-table tbody tr:last-child td {{
    border-bottom: none;
  }}

  .data-table .num {{
    text-align: right;
    font-variant-numeric: tabular-nums;
  }}

  .footer {{
    margin-top: 52px;
    padding: 18px 48px;
    border-top: 1px solid #d8dde6;
    text-align: center;
    font-size: 10px;
    color: #9ea8b3;
    letter-spacing: 0.5px;
  }}
</style>
</head>
<body>

<!-- Square icon bar -->
<div class="sq-bar">
  <div class="sq-icon-outer">
    <div class="sq-icon-inner"></div>
  </div>
</div>

<!-- Centered report info -->
<div class="report-info">
  <h1>Sales Report</h1>
  <h2>Full Scope Media LLC</h2>
  <p class="meta">Reported on {reported_on}</p>
  <p class="meta">{period_range}</p>
  <p class="filter-link">All Employees</p>
  <p class="filter-link">All Devices</p>
</div>

<div class="body">

  <div class="section">
    <div class="section-title">Sales</div>
    <table class="kv-table">
      <tr class="bold-row"><td>Gross Sales</td><td class="num">{fmt(sales['gross_sales'])}</td></tr>
      <tr><td>Items</td><td class="num">{fmt(sales['items'])}</td></tr>
      <tr class="bold-row"><td>Service Charges</td><td class="num">{fmt(sales['service_charges'])}</td></tr>
      <tr><td>Returns</td><td class="num">{fmt(sales['returns'])}</td></tr>
      <tr><td>Discounts &amp; Comps</td><td class="num">{fmt(sales['discounts_comps'])}</td></tr>
      <tr class="bold-row"><td>Net Sales</td><td class="num">{fmt(sales['net_sales'])}</td></tr>
      <tr><td>Tax</td><td class="num">{fmt(sales['tax'])}</td></tr>
      <tr><td>Tips</td><td class="num">{fmt(sales['tips'])}</td></tr>
      <tr><td>Gift Card Sales</td><td class="num">{fmt(sales['gift_card_sales'])}</td></tr>
      <tr><td>Refunds by Amount</td><td class="num">{fmt(sales['refunds'])}</td></tr>
      <tr class="total-row"><td>Total</td><td class="num">{fmt(sales['total'])}</td></tr>
    </table>
  </div>

  <div class="section">
    <div class="section-title">Payments</div>
    <table class="kv-table">
      <tr class="bold-row"><td>Total Collected</td><td class="num">{fmt(payments['total_collected'])}</td></tr>
      <tr><td>Cash</td><td class="num">{fmt(payments['cash'])}</td></tr>
      <tr><td>Card</td><td class="num">{fmt(card_total)}</td></tr>
      {card_rows}
      <tr><td>Gift Card</td><td class="num">{fmt(payments['gift_card'])}</td></tr>
      <tr><td>Other</td><td class="num">{fmt(payments['other'])}</td></tr>
      <tr><td>Fees</td><td class="num negative">{fmt(payments['fees'])}</td></tr>
      <tr class="total-row"><td>Net Total</td><td class="num">{fmt(payments['net_total'])}</td></tr>
    </table>
  </div>

  <div class="section">
    <div class="section-title">Category Sales</div>
    <table class="data-table">
      <thead>
        <tr>
          <th>Category</th>
          <th class="num">Gross Sales</th>
          <th class="num">Items</th>
        </tr>
      </thead>
      <tbody>
        {cat_rows}
      </tbody>
    </table>
  </div>

  <div class="section">
    <div class="section-title">Item Sales</div>
    <table class="data-table">
      <thead>
        <tr>
          <th>Item</th>
          <th>Category</th>
          <th class="num">Gross Sales</th>
          <th class="num">Items</th>
        </tr>
      </thead>
      <tbody>
        {item_rows}
      </tbody>
    </table>
  </div>

</div>

<div class="footer">
  &copy; 2026 Block, Inc. &nbsp;&nbsp;|&nbsp;&nbsp; Square &nbsp;&nbsp;|&nbsp;&nbsp;
  1955 Broadway, Suite 600, Oakland, CA 94612
</div>

</body>
</html>"""
    return html


# ── February 2026 ────────────────────────────────────────────────────────────

feb_sales = dict(
    gross_sales=5000.00, items=5000.00, service_charges=0.00,
    returns=0.00, discounts_comps=0.00, net_sales=5000.00,
    tax=0.00, tips=0.00, gift_card_sales=0.00,
    refunds=0.00, total=5000.00,
)
feb_payments = dict(
    total_collected=5000.00, cash=0.00,
    cards=[("Visa", 3000.00), ("Mastercard", 2000.00)],
    gift_card=0.00, other=0.00,
    fees=-175.75, net_total=4824.25,
)
feb_categories = [
    ("Creative Services", 2800.00, 3),
    ("Video Production",  1400.00, 4),
    ("Consulting",         800.00, 2),
]
feb_items = [
    ("Brand Identity Package", "Creative Services", 1500.00, 1),
    ("Social Media Kit",       "Creative Services", 1300.00, 2),
    ("Short-Form Edit",        "Video Production",  1400.00, 4),
    ("Strategy Session",       "Consulting",         800.00, 2),
]

# ── March 2026 ───────────────────────────────────────────────────────────────

mar_sales = dict(
    gross_sales=7000.00, items=7000.00, service_charges=0.00,
    returns=0.00, discounts_comps=0.00, net_sales=7000.00,
    tax=0.00, tips=0.00, gift_card_sales=0.00,
    refunds=0.00, total=7000.00,
)
mar_payments = dict(
    total_collected=7000.00, cash=0.00,
    cards=[("Visa", 4200.00), ("Mastercard", 2800.00)],
    gift_card=0.00, other=0.00,
    fees=-245.75, net_total=6754.25,
)
mar_categories = [
    ("Creative Services", 3800.00, 4),
    ("Video Production",  2200.00, 5),
    ("Consulting",        1000.00, 2),
]
mar_items = [
    ("Brand Campaign Package", "Creative Services", 2000.00, 1),
    ("Social Media Kit",       "Creative Services", 1800.00, 3),
    ("Short-Form Edit",        "Video Production",  1400.00, 4),
    ("Long-Form Edit",         "Video Production",   800.00, 1),
    ("Strategy Session",       "Consulting",         1000.00, 2),
]

# ── April 2026 ───────────────────────────────────────────────────────────────

apr_sales = dict(
    gross_sales=9150.00, items=9150.00, service_charges=0.00,
    returns=0.00, discounts_comps=0.00, net_sales=9150.00,
    tax=0.00, tips=0.00, gift_card_sales=0.00,
    refunds=0.00, total=9150.00,
)
apr_payments = dict(
    total_collected=9150.00, cash=0.00,
    cards=[("Visa", 5400.00), ("Mastercard", 3750.00)],
    gift_card=0.00, other=0.00,
    fees=-321.00, net_total=8829.00,
)
apr_categories = [
    ("Creative Services", 5150.00, 5),
    ("Video Production",  2500.00, 6),
    ("Consulting",        1500.00, 3),
]
apr_items = [
    ("Brand Campaign Package",  "Creative Services", 2400.00, 1),
    ("Social Media Management", "Creative Services", 1500.00, 2),
    ("Graphic Design",          "Creative Services", 1250.00, 2),
    ("Short-Form Edit",         "Video Production",  1750.00, 5),
    ("Long-Form Edit",          "Video Production",   750.00, 1),
    ("Strategy Session",        "Consulting",         1500.00, 3),
]

# ── Render ────────────────────────────────────────────────────────────────────

reports = [
    dict(
        period_range="Feb 01, 2026 12:00 AM  –  Feb 28, 2026 11:59 PM",
        reported_on="Mar 01, 2026 8:42 AM EDT",
        filename="square_sales_report_feb2026.pdf",
        sales=feb_sales, payments=feb_payments,
        category_sales=feb_categories, item_sales=feb_items,
    ),
    dict(
        period_range="Mar 01, 2026 12:00 AM  –  Mar 31, 2026 11:59 PM",
        reported_on="Apr 01, 2026 9:15 AM EDT",
        filename="square_sales_report_mar2026.pdf",
        sales=mar_sales, payments=mar_payments,
        category_sales=mar_categories, item_sales=mar_items,
    ),
    dict(
        period_range="Apr 01, 2026 12:00 AM  –  Apr 30, 2026 11:59 PM",
        reported_on="May 01, 2026 10:30 AM EDT",
        filename="square_sales_report_apr2026.pdf",
        sales=apr_sales, payments=apr_payments,
        category_sales=apr_categories, item_sales=apr_items,
    ),
]

for r in reports:
    html = make_html(r["period_range"], r["reported_on"], r["sales"], r["payments"],
                     r["category_sales"], r["item_sales"])
    out = f"/home/starryveck/{r['filename']}"
    HTML(string=html).write_pdf(out)
    print(f"Generated: {out}")

print("Done.")
