#!/usr/bin/env python3
from weasyprint import HTML

html = """<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<style>
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
  .section-title { font-size: 11px; font-weight: 700; color: #888; text-transform: uppercase; letter-spacing: 0.7px; padding: 16px 0 10px; border-bottom: 1px solid #e8e8e8; margin-bottom: 0; }

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
</style>
</head>
<body>

<div class="header">
  <div class="header-left">
    <div class="logo-box"><span>&#9632;</span></div>
    <div>
      <div class="brand-name">Square Checking</div>
      <div class="brand-sub">Provided by Sutton Bank &nbsp;&middot;&nbsp; Member FDIC</div>
    </div>
  </div>
  <div class="header-right">
    <strong>Account Statement</strong>
    Statement Period: April 1 &ndash; April 30, 2026<br>
    Date Issued: May 1, 2026
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
    <div>Statement Period &nbsp; <span>Apr 1 &ndash; Apr 30, 2026</span></div>
    <div>Page &nbsp; <span>1 of 1</span></div>
  </div>
</div>

<div class="summary-row">
  <div class="summary-card">
    <div class="summary-label">Beginning Balance</div>
    <div class="summary-amount neutral">$3,841.22</div>
  </div>
  <div class="summary-card">
    <div class="summary-label">Total Money In</div>
    <div class="summary-amount positive">+$9,150.00</div>
  </div>
  <div class="summary-card">
    <div class="summary-label">Total Money Out</div>
    <div class="summary-amount negative">&minus;$3,033.63</div>
  </div>
  <div class="summary-card">
    <div class="summary-label">Ending Balance</div>
    <div class="summary-amount blue">$9,957.59</div>
  </div>
</div>

<div class="tx-section">
  <div class="section-title">Transaction History</div>
  <table>
    <thead>
      <tr>
        <th>Date</th>
        <th>Description</th>
        <th>Type</th>
        <th class="num">Money Out</th>
        <th class="num">Money In</th>
        <th class="num">Balance</th>
      </tr>
    </thead>
    <tbody>
      <tr>
        <td class="td-date">Apr 1, 2026</td>
        <td class="td-desc td-opening">Beginning Balance</td>
        <td class="td-type"></td><td class="td-dash"></td><td class="td-dash"></td>
        <td class="td-bal td-opening-bal">$3,841.22</td>
      </tr>
      <tr>
        <td class="td-date">Apr 1, 2026</td>
        <td class="td-desc">Rent &ndash; Vlakhis Group</td>
        <td class="td-type">ACH Transfer</td>
        <td class="td-out">&minus;$1,000.00</td><td class="td-dash">&mdash;</td>
        <td class="td-bal">$2,841.22</td>
      </tr>
      <tr>
        <td class="td-date">Apr 2, 2026</td>
        <td class="td-desc">Invoice #1084 &ndash; Meridian Group</td>
        <td class="td-type">ACH Deposit</td>
        <td class="td-dash">&mdash;</td><td class="td-in">+$2,400.00</td>
        <td class="td-bal">$5,241.22</td>
      </tr>
      <tr>
        <td class="td-date">Apr 3, 2026</td>
        <td class="td-desc">Adobe Creative Cloud</td>
        <td class="td-type">Debit Card</td>
        <td class="td-out">&minus;$54.99</td><td class="td-dash">&mdash;</td>
        <td class="td-bal">$5,186.23</td>
      </tr>
      <tr>
        <td class="td-date">Apr 4, 2026</td>
        <td class="td-desc">Staples &ndash; Office Supplies</td>
        <td class="td-type">Debit Card</td>
        <td class="td-out">&minus;$38.47</td><td class="td-dash">&mdash;</td>
        <td class="td-bal">$5,147.76</td>
      </tr>
      <tr>
        <td class="td-date">Apr 7, 2026</td>
        <td class="td-desc">Invoice #1085 &ndash; Bluewave Digital</td>
        <td class="td-type">ACH Deposit</td>
        <td class="td-dash">&mdash;</td><td class="td-in">+$1,750.00</td>
        <td class="td-bal">$6,897.76</td>
      </tr>
      <tr>
        <td class="td-date">Apr 8, 2026</td>
        <td class="td-desc">Google Workspace</td>
        <td class="td-type">ACH Debit</td>
        <td class="td-out">&minus;$18.00</td><td class="td-dash">&mdash;</td>
        <td class="td-bal">$6,879.76</td>
      </tr>
      <tr>
        <td class="td-date">Apr 9, 2026</td>
        <td class="td-desc">Zoom Pro Subscription</td>
        <td class="td-type">ACH Debit</td>
        <td class="td-out">&minus;$15.99</td><td class="td-dash">&mdash;</td>
        <td class="td-bal">$6,863.77</td>
      </tr>
      <tr>
        <td class="td-date">Apr 10, 2026</td>
        <td class="td-desc">Business Lunch &ndash; Client Meeting</td>
        <td class="td-type">Debit Card</td>
        <td class="td-out">&minus;$74.20</td><td class="td-dash">&mdash;</td>
        <td class="td-bal">$6,789.57</td>
      </tr>
      <tr>
        <td class="td-date">Apr 11, 2026</td>
        <td class="td-desc">Invoice #1086 &ndash; Harmon &amp; Associates</td>
        <td class="td-type">ACH Deposit</td>
        <td class="td-dash">&mdash;</td><td class="td-in">+$3,200.00</td>
        <td class="td-bal">$9,989.57</td>
      </tr>
      <tr>
        <td class="td-date">Apr 12, 2026</td>
        <td class="td-desc">Contractor Pmt &ndash; J. Torres</td>
        <td class="td-type">ACH Transfer</td>
        <td class="td-out">&minus;$450.00</td><td class="td-dash">&mdash;</td>
        <td class="td-bal">$9,539.57</td>
      </tr>
      <tr>
        <td class="td-date">Apr 14, 2026</td>
        <td class="td-desc">QuickBooks Online</td>
        <td class="td-type">ACH Debit</td>
        <td class="td-out">&minus;$30.00</td><td class="td-dash">&mdash;</td>
        <td class="td-bal">$9,509.57</td>
      </tr>
      <tr>
        <td class="td-date">Apr 15, 2026</td>
        <td class="td-desc">Invoice #1083 &ndash; Crestline Co. (Retainer)</td>
        <td class="td-type">ACH Deposit</td>
        <td class="td-dash">&mdash;</td><td class="td-in">+$800.00</td>
        <td class="td-bal">$10,309.57</td>
      </tr>
      <tr>
        <td class="td-date">Apr 16, 2026</td>
        <td class="td-desc">Fuel &ndash; Business Travel</td>
        <td class="td-type">Debit Card</td>
        <td class="td-out">&minus;$61.33</td><td class="td-dash">&mdash;</td>
        <td class="td-bal">$10,248.24</td>
      </tr>
      <tr>
        <td class="td-date">Apr 17, 2026</td>
        <td class="td-desc">Parking &amp; Tolls &ndash; Client Visit</td>
        <td class="td-type">Debit Card</td>
        <td class="td-out">&minus;$22.50</td><td class="td-dash">&mdash;</td>
        <td class="td-bal">$10,225.74</td>
      </tr>
      <tr>
        <td class="td-date">Apr 18, 2026</td>
        <td class="td-desc">Invoice #1087 &ndash; Solano Media Group</td>
        <td class="td-type">ACH Deposit</td>
        <td class="td-dash">&mdash;</td><td class="td-in">+$1,000.00</td>
        <td class="td-bal">$11,225.74</td>
      </tr>
      <tr>
        <td class="td-date">Apr 21, 2026</td>
        <td class="td-desc">Business Insurance &ndash; Monthly</td>
        <td class="td-type">ACH Debit</td>
        <td class="td-out">&minus;$189.00</td><td class="td-dash">&mdash;</td>
        <td class="td-bal">$11,036.74</td>
      </tr>
      <tr>
        <td class="td-date">Apr 22, 2026</td>
        <td class="td-desc">Dropbox Business</td>
        <td class="td-type">ACH Debit</td>
        <td class="td-out">&minus;$16.67</td><td class="td-dash">&mdash;</td>
        <td class="td-bal">$11,020.07</td>
      </tr>
      <tr>
        <td class="td-date">Apr 23, 2026</td>
        <td class="td-desc">Contractor Pmt &ndash; A. Patel</td>
        <td class="td-type">ACH Transfer</td>
        <td class="td-out">&minus;$350.00</td><td class="td-dash">&mdash;</td>
        <td class="td-bal">$10,670.07</td>
      </tr>
      <tr>
        <td class="td-date">Apr 24, 2026</td>
        <td class="td-desc">USPS &ndash; Mailing &amp; Shipping</td>
        <td class="td-type">Debit Card</td>
        <td class="td-out">&minus;$14.75</td><td class="td-dash">&mdash;</td>
        <td class="td-bal">$10,655.32</td>
      </tr>
      <tr>
        <td class="td-date">Apr 25, 2026</td>
        <td class="td-desc">Figma &ndash; Software License</td>
        <td class="td-type">ACH Debit</td>
        <td class="td-out">&minus;$45.00</td><td class="td-dash">&mdash;</td>
        <td class="td-bal">$10,610.32</td>
      </tr>
      <tr>
        <td class="td-date">Apr 28, 2026</td>
        <td class="td-desc">RackNerd &ndash; VPS Hosting</td>
        <td class="td-type">Debit Card</td>
        <td class="td-out">&minus;$15.99</td><td class="td-dash">&mdash;</td>
        <td class="td-bal">$10,594.33</td>
      </tr>
      <tr>
        <td class="td-date">Apr 29, 2026</td>
        <td class="td-desc">T-Mobile &ndash; Business Phone</td>
        <td class="td-type">ACH Debit</td>
        <td class="td-out">&minus;$522.24</td><td class="td-dash">&mdash;</td>
        <td class="td-bal">$10,072.09</td>
      </tr>
      <tr>
        <td class="td-date">Apr 30, 2026</td>
        <td class="td-desc">Monthly Service Fee</td>
        <td class="td-type">Fee</td>
        <td class="td-out">&minus;$15.00</td><td class="td-dash">&mdash;</td>
        <td class="td-bal">$10,057.09</td>
      </tr>
      <tr>
        <td class="td-date">Apr 30, 2026</td>
        <td class="td-desc">Miscellaneous Office Expense</td>
        <td class="td-type">Debit Card</td>
        <td class="td-out">&minus;$99.50</td><td class="td-dash">&mdash;</td>
        <td class="td-bal">$9,957.59</td>
      </tr>
    </tbody>
  </table>
</div>

<div class="period-section">
  <div class="period-header">Inflows &amp; Outflows &mdash; April 2026</div>
  <div class="period-body">
    <div class="period-row total"><span>Total Money In</span><span class="pos">+$9,150.00</span></div>
    <div class="period-row sub"><span>Invoice #1083 &ndash; Crestline Co. (Retainer)</span><span>$800.00</span></div>
    <div class="period-row sub"><span>Invoice #1084 &ndash; Meridian Group</span><span>$2,400.00</span></div>
    <div class="period-row sub"><span>Invoice #1085 &ndash; Bluewave Digital</span><span>$1,750.00</span></div>
    <div class="period-row sub"><span>Invoice #1086 &ndash; Harmon &amp; Associates</span><span>$3,200.00</span></div>
    <div class="period-row sub"><span>Invoice #1087 &ndash; Solano Media Group</span><span>$1,000.00</span></div>

    <div class="period-divider"></div>

    <div class="period-row total"><span>Total Money Out</span><span class="neg">&minus;$3,033.63</span></div>
    <div class="period-row sub"><span>Contractor Payments</span><span>$800.00</span></div>
    <div class="period-row sub"><span>Software &amp; Subscriptions</span><span>$196.64</span></div>
    <div class="period-row sub"><span>Insurance</span><span>$189.00</span></div>
    <div class="period-row sub"><span>Travel &amp; Transportation</span><span>$83.83</span></div>
    <div class="period-row sub"><span>Communications (T-Mobile)</span><span>$522.24</span></div>
    <div class="period-row sub"><span>Rent &ndash; Vlakhis Group</span><span>$1,000.00</span></div>
    <div class="period-row sub"><span>Office &amp; Operational</span><span>$241.92</span></div>

    <div class="period-row net"><span>Net Cash Flow</span><span>+$6,116.37</span></div>
  </div>
</div>

<div class="footer">
  <div>
    <span class="fdic-box">FDIC</span>
    Square Checking is provided by Sutton Bank, Member FDIC.<br>
    Deposits insured up to $250,000 per depositor.<br>
    Sutton Bank &middot; 1 S. Main St., Attica, OH 44807
  </div>
  <div style="text-align:right;">
    Questions? Visit squareup.com/banking or call 1-855-700-6000<br>
    This is a simulated statement for illustrative purposes only.
  </div>
</div>

</body>
</html>"""

HTML(string=html).write_pdf("/home/starryveck/bank_statement.pdf")
print("Done: bank_statement.pdf  (Apr 2026 | revenue $9,150 | net +$6,116.37)")
