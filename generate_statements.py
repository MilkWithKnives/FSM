#!/usr/bin/env python3
from weasyprint import HTML

CSS = """
* { margin: 0; padding: 0; box-sizing: border-box; }
body { font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', sans-serif; font-size: 13px; color: #1a1a1a; background: #fff; }
.header { background: #3375e0; color: white; padding: 22px 36px; display: flex; justify-content: space-between; align-items: flex-start; }
.header-left { display: flex; align-items: center; gap: 14px; }
.logo-box { width: 38px; height: 38px; background: white; border-radius: 6px; display: flex; align-items: center; justify-content: center; }
.logo-box span { font-size: 22px; font-weight: 900; color: #3375e0; line-height: 1; }
.brand-name { font-size: 26px; font-weight: 700; letter-spacing: -0.3px; }
.brand-sub { font-size: 11px; opacity: 0.85; margin-top: 2px; }
.header-right { text-align: right; font-size: 12px; line-height: 1.7; }
.header-right strong { font-size: 14px; font-weight: 700; display: block; }
.account-section { padding: 20px 36px 16px; border-bottom: 1px solid #e8e8e8; display: flex; justify-content: space-between; align-items: flex-start; }
.acct-name { font-size: 16px; font-weight: 700; margin-bottom: 6px; }
.acct-meta { font-size: 12px; color: #555; line-height: 1.8; }
.acct-meta span { font-weight: 600; color: #1a1a1a; }
.acct-right { text-align: right; font-size: 12px; color: #555; line-height: 1.8; }
.acct-right span { font-weight: 600; color: #1a1a1a; }
.summary-row { display: flex; gap: 0; padding: 20px 36px; border-bottom: 1px solid #e8e8e8; }
.summary-card { flex: 1; padding: 14px 18px; border: 1px solid #e8e8e8; border-radius: 8px; margin-right: 12px; }
.summary-card:last-child { margin-right: 0; border: 2px solid #3375e0; }
.summary-label { font-size: 10px; font-weight: 600; color: #888; text-transform: uppercase; letter-spacing: 0.5px; margin-bottom: 6px; }
.summary-amount { font-size: 22px; font-weight: 700; }
.summary-amount.neutral { color: #1a1a1a; }
.summary-amount.positive { color: #1a8a4a; }
.summary-amount.negative { color: #d93025; }
.summary-amount.blue { color: #3375e0; }
.tx-section { padding: 0 36px 20px; }
.section-title { font-size: 11px; font-weight: 700; color: #888; text-transform: uppercase; letter-spacing: 0.7px; padding: 16px 0 10px; border-bottom: 1px solid #e8e8e8; }
table { width: 100%; border-collapse: collapse; }
thead th { font-size: 10px; font-weight: 700; color: #888; text-transform: uppercase; letter-spacing: 0.5px; padding: 10px 8px; text-align: left; border-bottom: 1px solid #e8e8e8; }
thead th.num { text-align: right; }
tbody tr { border-bottom: 1px solid #f2f2f2; }
tbody tr:last-child { border-bottom: none; }
tbody td { padding: 10px 8px; font-size: 12.5px; vertical-align: middle; }
.td-date { color: #666; white-space: nowrap; width: 100px; }
.td-desc { font-weight: 500; }
.td-type { color: #888; font-size: 11.5px; width: 100px; }
.td-out { text-align: right; color: #d93025; font-weight: 500; width: 100px; }
.td-in { text-align: right; color: #1a8a4a; font-weight: 500; width: 100px; }
.td-bal { text-align: right; font-weight: 600; color: #1a1a1a; width: 100px; }
.td-dash { text-align: right; color: #bbb; }
.td-opening { font-weight: 700; font-size: 13px; }
.td-opening-bal { text-align: right; font-weight: 700; font-size: 13px; }
.period-section { margin: 10px 36px 0; border: 1px solid #e0e8f7; border-radius: 8px; overflow: hidden; }
.period-header { background: #eef3fb; padding: 12px 18px; font-size: 11px; font-weight: 700; color: #3375e0; text-transform: uppercase; letter-spacing: 0.7px; }
.period-body { padding: 16px 18px; }
.period-row { display: flex; justify-content: space-between; padding: 4px 0; font-size: 12.5px; }
.period-row.total { font-weight: 700; font-size: 13.5px; margin-bottom: 4px; }
.period-row.sub { padding-left: 18px; color: #555; }
.period-row.net { font-weight: 700; font-size: 14px; color: #3375e0; border-top: 1px solid #dde6f5; margin-top: 10px; padding-top: 10px; }
.period-divider { height: 10px; }
.pos { color: #1a8a4a; }
.neg { color: #d93025; }
.footer { margin: 20px 36px 0; padding: 16px 0 24px; border-top: 1px solid #e8e8e8; display: flex; justify-content: space-between; align-items: flex-start; font-size: 10.5px; color: #888; line-height: 1.7; }
.fdic-box { border: 1.5px solid #aaa; border-radius: 3px; padding: 1px 5px; font-size: 9px; font-weight: 700; color: #555; display: inline-block; margin-right: 6px; vertical-align: middle; }
"""

def make_html(period_short, period_long, date_issued, beg_bal, total_in, total_out, ending_bal, net_flow,
              transactions, summary_in_items, summary_out_items):
    tx_rows = ""
    for t in transactions:
        date, desc, ttype, out, inp, bal = t
        out_td = f'<td class="td-out">&minus;${out}</td>' if out else '<td class="td-dash">&mdash;</td>'
        in_td  = f'<td class="td-in">+${inp}</td>'        if inp else '<td class="td-dash">&mdash;</td>'
        if desc == "Beginning Balance":
            tx_rows += f"""<tr><td class="td-date">{date}</td>
              <td class="td-desc td-opening">Beginning Balance</td>
              <td class="td-type"></td><td class="td-dash"></td><td class="td-dash"></td>
              <td class="td-bal td-opening-bal">${bal}</td></tr>"""
        else:
            tx_rows += f"""<tr><td class="td-date">{date}</td>
              <td class="td-desc">{desc}</td><td class="td-type">{ttype}</td>
              {out_td}{in_td}<td class="td-bal">${bal}</td></tr>"""

    in_rows  = "".join(f'<div class="period-row sub"><span>{k}</span><span>${v}</span></div>' for k,v in summary_in_items)
    out_rows = "".join(f'<div class="period-row sub"><span>{k}</span><span>${v}</span></div>' for k,v in summary_out_items)

    return f"""<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8">
<style>{CSS}</style></head><body>
<div class="header">
  <div class="header-left">
    <div class="logo-box"><span>&#9632;</span></div>
    <div><div class="brand-name">Square Checking</div>
    <div class="brand-sub">Provided by Sutton Bank &nbsp;&middot;&nbsp; Member FDIC</div></div>
  </div>
  <div class="header-right">
    <strong>Account Statement</strong>
    Statement Period: {period_long}<br>Date Issued: {date_issued}
  </div>
</div>
<div class="account-section">
  <div>
    <div class="acct-name">Champion Creative LLC</div>
    <div class="acct-meta">Account Type &nbsp; <span>Business Checking</span></div>
    <div class="acct-meta">Account Number &nbsp; <span>&bull;&bull;&bull;&bull; &bull;&bull;&bull;&bull; 7304</span></div>
  </div>
  <div class="acct-right">
    <div>Routing Number &nbsp; <span>041 215 663</span></div>
    <div>Statement Period &nbsp; <span>{period_short}</span></div>
    <div>Page &nbsp; <span>1 of 1</span></div>
  </div>
</div>
<div class="summary-row">
  <div class="summary-card"><div class="summary-label">Beginning Balance</div><div class="summary-amount neutral">${beg_bal}</div></div>
  <div class="summary-card"><div class="summary-label">Total Money In</div><div class="summary-amount positive">+${total_in}</div></div>
  <div class="summary-card"><div class="summary-label">Total Money Out</div><div class="summary-amount negative">&minus;${total_out}</div></div>
  <div class="summary-card"><div class="summary-label">Ending Balance</div><div class="summary-amount blue">${ending_bal}</div></div>
</div>
<div class="tx-section">
  <div class="section-title">Transaction History</div>
  <table>
    <thead><tr>
      <th>Date</th><th>Description</th><th>Type</th>
      <th class="num">Money Out</th><th class="num">Money In</th><th class="num">Balance</th>
    </tr></thead>
    <tbody>{tx_rows}</tbody>
  </table>
</div>
<div class="period-section">
  <div class="period-header">Inflows &amp; Outflows &mdash; {period_short}</div>
  <div class="period-body">
    <div class="period-row total"><span>Total Money In</span><span class="pos">+${total_in}</span></div>
    {in_rows}
    <div class="period-divider"></div>
    <div class="period-row total"><span>Total Money Out</span><span class="neg">&minus;${total_out}</span></div>
    {out_rows}
    <div class="period-row net"><span>Net Cash Flow</span><span>+${net_flow}</span></div>
  </div>
</div>
<div class="footer">
  <div><span class="fdic-box">FDIC</span>Square Checking is provided by Sutton Bank, Member FDIC.<br>
  Deposits insured up to $250,000 per depositor.<br>Sutton Bank &middot; 1 S. Main St., Attica, OH 44807</div>
  <div style="text-align:right;">Questions? Visit squareup.com/banking or call 1-855-700-6000<br>
  This is a simulated statement for illustrative purposes only.</div>
</div>
</body></html>"""


# ── FEBRUARY 2026  Revenue $5,000  Out $2,800  Net $2,200 ───────────────────
feb_tx = [
    ("Feb 1, 2026",  "Beginning Balance",                              "",             "",         "",         "2,840.15"),
    ("Feb 1, 2026",  "Rent &ndash; Vlakhis Group",                     "ACH Transfer", "1,000.00", "",         "1,840.15"),
    ("Feb 3, 2026",  "Adobe Creative Cloud",                           "Debit Card",   "54.99",    "",         "1,785.16"),
    ("Feb 4, 2026",  "Invoice #1071 &ndash; Northgate Creative",       "ACH Deposit",  "",         "1,500.00", "3,285.16"),
    ("Feb 5, 2026",  "Staples &ndash; Office Supplies",                "Debit Card",   "38.50",    "",         "3,246.66"),
    ("Feb 6, 2026",  "Invoice #1072 &ndash; Bluewave Digital",         "ACH Deposit",  "",         "1,200.00", "4,446.66"),
    ("Feb 7, 2026",  "Google Workspace",                               "ACH Debit",    "18.00",    "",         "4,428.66"),
    ("Feb 8, 2026",  "Zoom Pro Subscription",                          "ACH Debit",    "15.99",    "",         "4,412.67"),
    ("Feb 9, 2026",  "Business Lunch &ndash; Client Meeting",          "Debit Card",   "52.30",    "",         "4,360.37"),
    ("Feb 10, 2026", "Contractor Pmt &ndash; J. Torres",               "ACH Transfer", "300.00",   "",         "4,060.37"),
    ("Feb 11, 2026", "Invoice #1073 &ndash; Harmon &amp; Associates",  "ACH Deposit",  "",         "800.00",   "4,860.37"),
    ("Feb 12, 2026", "QuickBooks Online",                              "ACH Debit",    "30.00",    "",         "4,830.37"),
    ("Feb 14, 2026", "Invoice #1074 &ndash; Crestline Co. (Retainer)", "ACH Deposit",  "",         "800.00",   "5,630.37"),
    ("Feb 16, 2026", "Fuel &ndash; Business Travel",                   "Debit Card",   "35.00",    "",         "5,595.37"),
    ("Feb 17, 2026", "Parking &amp; Tolls &ndash; Client Visit",       "Debit Card",   "12.00",    "",         "5,583.37"),
    ("Feb 18, 2026", "Business Insurance &ndash; Monthly",             "ACH Debit",    "189.00",   "",         "5,394.37"),
    ("Feb 19, 2026", "Dropbox Business",                               "ACH Debit",    "16.67",    "",         "5,377.70"),
    ("Feb 20, 2026", "Contractor Pmt &ndash; A. Patel",                "ACH Transfer", "200.00",   "",         "5,177.70"),
    ("Feb 21, 2026", "USPS &ndash; Mailing &amp; Shipping",            "Debit Card",   "9.25",     "",         "5,168.45"),
    ("Feb 21, 2026", "Invoice #1075 &ndash; Park View Studios",        "ACH Deposit",  "",         "700.00",   "5,868.45"),
    ("Feb 22, 2026", "Figma &ndash; Software License",                 "ACH Debit",    "45.00",    "",         "5,823.45"),
    ("Feb 23, 2026", "Client Entertainment",                           "Debit Card",   "45.00",    "",         "5,778.45"),
    ("Feb 24, 2026", "RackNerd &ndash; VPS Hosting",                   "Debit Card",   "15.99",    "",         "5,762.46"),
    ("Feb 25, 2026", "T-Mobile &ndash; Business Phone",                "ACH Debit",    "522.24",   "",         "5,240.22"),
    ("Feb 26, 2026", "Advertising &ndash; Social Media",               "ACH Debit",    "64.50",    "",         "5,175.72"),
    ("Feb 27, 2026", "Software Tools &ndash; Annual Prorate",          "ACH Debit",    "30.00",    "",         "5,145.72"),
    ("Feb 27, 2026", "Travel &ndash; Mileage Reimbursement",           "Debit Card",   "29.17",    "",         "5,116.55"),
    ("Feb 28, 2026", "Miscellaneous Office Expense",                   "Debit Card",   "61.40",    "",         "5,055.15"),
    ("Feb 28, 2026", "Monthly Service Fee",                            "Fee",          "15.00",    "",         "5,040.15"),
]

feb_in = [
    ("Invoice #1071 &ndash; Northgate Creative",        "1,500.00"),
    ("Invoice #1072 &ndash; Bluewave Digital",          "1,200.00"),
    ("Invoice #1073 &ndash; Harmon &amp; Associates",   "800.00"),
    ("Invoice #1074 &ndash; Crestline Co. (Retainer)",  "800.00"),
    ("Invoice #1075 &ndash; Park View Studios",         "700.00"),
]

feb_out = [
    ("Contractor Payments",          "500.00"),
    ("Software &amp; Subscriptions", "226.64"),
    ("Insurance",                    "189.00"),
    ("Travel &amp; Transportation",  "76.17"),
    ("Communications (T-Mobile)",    "522.24"),
    ("Rent &ndash; Vlakhis Group",   "1,000.00"),
    ("Office &amp; Operational",     "285.95"),
]

html1 = make_html(
    period_short="Feb 1 &ndash; Feb 28, 2026",
    period_long="February 1 &ndash; February 28, 2026",
    date_issued="March 1, 2026",
    beg_bal="2,840.15",
    total_in="5,000.00",
    total_out="2,800.00",
    ending_bal="5,040.15",
    net_flow="2,200.00",
    transactions=feb_tx,
    summary_in_items=feb_in,
    summary_out_items=feb_out,
)
HTML(string=html1).write_pdf("/home/starryveck/bank_statement_feb2026.pdf")
print("Generated: bank_statement_feb2026.pdf  (revenue $5,000 | net +$2,200)")


# ── MARCH 2026  Revenue $7,000  Out $3,000  Net $4,000 ──────────────────────
mar_tx = [
    ("Mar 1, 2026",  "Beginning Balance",                              "",             "",         "",         "5,040.15"),
    ("Mar 1, 2026",  "Rent &ndash; Vlakhis Group",                     "ACH Transfer", "1,000.00", "",         "4,040.15"),
    ("Mar 2, 2026",  "Invoice #1076 &ndash; Meridian Group",           "ACH Deposit",  "",         "2,000.00", "6,040.15"),
    ("Mar 3, 2026",  "Adobe Creative Cloud",                           "Debit Card",   "54.99",    "",         "5,985.16"),
    ("Mar 4, 2026",  "Staples &ndash; Office Supplies",                "Debit Card",   "48.60",    "",         "5,936.56"),
    ("Mar 5, 2026",  "Invoice #1077 &ndash; Bluewave Digital",         "ACH Deposit",  "",         "1,750.00", "7,686.56"),
    ("Mar 6, 2026",  "Google Workspace",                               "ACH Debit",    "18.00",    "",         "7,668.56"),
    ("Mar 7, 2026",  "Zoom Pro Subscription",                          "ACH Debit",    "15.99",    "",         "7,652.57"),
    ("Mar 9, 2026",  "Business Lunch &ndash; Client Meeting",          "Debit Card",   "67.40",    "",         "7,585.17"),
    ("Mar 10, 2026", "Invoice #1078 &ndash; Harmon &amp; Associates",  "ACH Deposit",  "",         "1,650.00", "9,235.17"),
    ("Mar 11, 2026", "Contractor Pmt &ndash; J. Torres",               "ACH Transfer", "350.00",   "",         "8,885.17"),
    ("Mar 12, 2026", "QuickBooks Online",                              "ACH Debit",    "30.00",    "",         "8,855.17"),
    ("Mar 13, 2026", "Invoice #1079 &ndash; Crestline Co. (Retainer)", "ACH Deposit",  "",         "800.00",   "9,655.17"),
    ("Mar 16, 2026", "Fuel &ndash; Business Travel",                   "Debit Card",   "52.30",    "",         "9,602.87"),
    ("Mar 17, 2026", "Parking &amp; Tolls &ndash; Client Visit",       "Debit Card",   "20.00",    "",         "9,582.87"),
    ("Mar 18, 2026", "Business Insurance &ndash; Monthly",             "ACH Debit",    "189.00",   "",         "9,393.87"),
    ("Mar 19, 2026", "Dropbox Business",                               "ACH Debit",    "16.67",    "",         "9,377.20"),
    ("Mar 20, 2026", "Contractor Pmt &ndash; A. Patel",                "ACH Transfer", "250.00",   "",         "9,127.20"),
    ("Mar 21, 2026", "USPS &ndash; Mailing &amp; Shipping",            "Debit Card",   "16.50",    "",         "9,110.70"),
    ("Mar 23, 2026", "Invoice #1080 &ndash; Apex Design Co.",          "ACH Deposit",  "",         "800.00",   "9,910.70"),
    ("Mar 24, 2026", "Figma &ndash; Software License",                 "ACH Debit",    "45.00",    "",         "9,865.70"),
    ("Mar 24, 2026", "Travel &ndash; Mileage Reimbursement",           "Debit Card",   "20.07",    "",         "9,845.63"),
    ("Mar 25, 2026", "RackNerd &ndash; VPS Hosting",                   "Debit Card",   "15.99",    "",         "9,829.64"),
    ("Mar 26, 2026", "Professional Development",                       "ACH Debit",    "50.00",    "",         "9,779.64"),
    ("Mar 27, 2026", "T-Mobile &ndash; Business Phone",                "ACH Debit",    "522.24",   "",         "9,257.40"),
    ("Mar 28, 2026", "Advertising &ndash; Social Media",               "ACH Debit",    "82.75",    "",         "9,174.65"),
    ("Mar 28, 2026", "Software Tools &ndash; Annual Prorate",          "ACH Debit",    "40.00",    "",         "9,134.65"),
    ("Mar 30, 2026", "Miscellaneous Office Expense",                   "Debit Card",   "79.50",    "",         "9,055.15"),
    ("Mar 31, 2026", "Monthly Service Fee",                            "Fee",          "15.00",    "",         "9,040.15"),
]

mar_in = [
    ("Invoice #1076 &ndash; Meridian Group",            "2,000.00"),
    ("Invoice #1077 &ndash; Bluewave Digital",          "1,750.00"),
    ("Invoice #1078 &ndash; Harmon &amp; Associates",   "1,650.00"),
    ("Invoice #1079 &ndash; Crestline Co. (Retainer)",  "800.00"),
    ("Invoice #1080 &ndash; Apex Design Co.",           "800.00"),
]

mar_out = [
    ("Contractor Payments",          "600.00"),
    ("Software &amp; Subscriptions", "236.64"),
    ("Insurance",                    "189.00"),
    ("Travel &amp; Transportation",  "92.37"),
    ("Communications (T-Mobile)",    "522.24"),
    ("Rent &ndash; Vlakhis Group",   "1,000.00"),
    ("Office &amp; Operational",     "359.75"),
]

html2 = make_html(
    period_short="Mar 1 &ndash; Mar 31, 2026",
    period_long="March 1 &ndash; March 31, 2026",
    date_issued="April 1, 2026",
    beg_bal="5,040.15",
    total_in="7,000.00",
    total_out="3,000.00",
    ending_bal="9,040.15",
    net_flow="4,000.00",
    transactions=mar_tx,
    summary_in_items=mar_in,
    summary_out_items=mar_out,
)
HTML(string=html2).write_pdf("/home/starryveck/bank_statement_mar2026.pdf")
print("Generated: bank_statement_mar2026.pdf  (revenue $7,000 | net +$4,000)")
