"""shock_card.py — Market Digest Lab (Day 10)

WHY THIS SCRIPT EXISTS (the one-line "why" you asked for):
A shock card measures "what did all 9 assets do after ONE event" — this script
does the measuring from your backfill-prices-12m.csv, so you never type a
number by hand. You run it, pick the event, and copy the table into your card.

HOW TO RUN (same as your other scripts):
1. In VS Code, open your Market-Digest-Lab folder.
2. Create a new file named shock_card.py and paste this whole script into it.
3. Make sure backfill-prices-12m.csv is in the same folder.
4. Right-click -> "Run Python File in Terminal" (or the play button top-right).
5. Type the event number from the menu, press Enter.
6. Copy the markdown table into your shock card file.

HOW IT MEASURES (the convention — say this out loud to defend your card):
- "Before" = the close on the last trading day BEFORE the event's market day.
- "1 day" = the close on the event's market day vs before.
- "1 week" = the close 5 trading days later vs before.
- "1 month" = the close 22 trading days later vs before.
So all three columns answer: "how far from where we stood before the event?"
Yields are printed in basis points (your rule), everything else in %.

ONE KNOWN LIMIT (say it, don't hide it):
If an announcement lands AFTER the market closes on its date, the real move
shows up the next day — the "1 day" number then understates it. Check the
"Market day used" line the script prints and judge for yourself.

The event dates below come from YOUR events-v1.md. For two entries I picked
the market-reaction date over the announcement date (Event 8: Oct 1, the day
Alphabet actually fell -1.7%; Event 14: Mar 18, the FOMC decision day). If you
disagree, just type a date like 2026-09-30 instead of the event number.
"""

import pandas as pd

# (number, date, short label) — from Liu's events-v1.md, committed 2026-10-12
EVENTS = [
    (1,  "2026-01-08", "Fannie/Freddie $200B MBS plan"),
    (2,  "2026-02-28", "US-Israel strikes on Iran / Hormuz ban"),
    (3,  "2026-06-05", "Broadcom guidance tech selloff"),
    (4,  "2026-08-22", "US-Canada trade talks collapse"),
    (5,  "2026-09-16", "Fed +25bps to 3.75-4.00%"),
    (6,  "2026-09-18", "BOJ hikes to 1.25%"),
    (7,  "2026-09-24", "Trump-Xi summit mixed reaction"),
    (8,  "2026-10-01", "Alphabet -1.7% (Gemini 4 Argon reaction)"),
    (9,  "2026-10-02", "G7 100M-barrel emergency oil release"),
    (10, "2026-10-02", "Weak Sept jobs report"),
    (11, "2025-10-01", "US government shutdown begins"),
    (12, "2025-10-28", "Microsoft 27% OpenAI stake, $500B"),
    (13, "2026-04-07", "US-Israel-Iran ceasefire"),
    (14, "2026-03-18", "Fed holds 3.50-3.75% (FOMC decision day)"),
    (15, "2026-03-13", "Q4 2025 GDP falls to 0.7%"),
]

# CSV column -> shock-card row label (your assets.md order)
ASSETS = [
    ("SP500",       "S&P 500"),
    ("WTI_crude",   "WTI crude"),
    ("Gold",        "Gold"),
    ("Dollar_index","DXY (dollar index)"),
    ("VIX",         "VIX (fear gauge)"),
    ("US10Y_yield", "10Y Treasury yield"),
    ("Tech",        "Tech (XLK)"),
    ("Energy",      "Energy (XLE)"),
    ("Banks",       "Banks (XLF)"),
]

W1, W1M = 5, 22  # trading days


def main():
    prices = pd.read_csv("backfill-prices-12m.csv")
    # yfinance writes dates as YYYY-MM-DD; parse explicitly (no guessing).
    prices["date"] = pd.to_datetime(prices["date"], format="%Y-%m-%d")
    prices = prices.set_index("date").sort_index().ffill()
    days = list(prices.index)

    print("Your 15 events (from events-v1.md):")
    for n, d, label in EVENTS:
        print(f"  {n:>2}. {d}  {label}")
    print("  (or type any date like 2026-09-30)")
    choice = input("\nWhich event? ").strip()

    by_num = {str(n): d for n, d, _ in EVENTS}
    if choice in by_num:
        event_date = pd.Timestamp(by_num[choice])
        label = dict((str(n), l) for n, _, l in EVENTS)[choice]
    else:
        try:
            event_date = pd.Timestamp(choice)
        except ValueError:
            print(f"\nCouldn't read '{choice}' as a date.")
            print("Type an event number (1-15) or a date like 2026-09-30.")
            return
        label = "custom date"

    if not (days[0] <= event_date <= days[-1]):
        print(f"\nThat date ({event_date.date()}) is outside your price file,")
        print(f"which covers {days[0].date()} -> {days[-1].date()}.")
        print("Pick an event inside that range.")
        return

    # D0 = first trading day on/after the event (the day the market prices it in)
    d0 = next(d for d in days if d >= event_date)
    i0 = days.index(d0)
    if i0 == 0:
        print("No 'before' close available for this date — pick a later event.")
        return
    base = days[i0 - 1]

    targets = {"1-day": i0, "1-week": i0 + W1, "1-month": i0 + W1M}
    last = len(days) - 1

    print(f"\nEvent: {label} ({event_date.date()})")
    print(f"Market day used: {d0.date()} | 'Before' close: {base.date()}")
    print(f"1-week target: {(days[targets['1-week']].date() if targets['1-week'] <= last else 'n/a — beyond your data')}")
    print(f"1-month target: {(days[targets['1-month']].date() if targets['1-month'] <= last else 'n/a — your file ends ' + str(days[-1].date()))}")

    print("\n| Asset | 1-day | 1-week | 1-month |")
    print("|-------|-------|--------|---------|")
    for col, name in ASSETS:
        cells = []
        for key in ("1-day", "1-week", "1-month"):
            i = targets[key]
            if i > last:
                cells.append("n/a")
                continue
            before, after = prices[col].iloc[i0 - 1], prices[col].iloc[i]
            if col == "US10Y_yield":
                cells.append(f"{(after - before) * 100:+.0f} bps")
            else:
                cells.append(f"{(after / before - 1) * 100:+.2f}%")
        print(f"| {name} | {cells[0]} | {cells[1]} | {cells[2]} |")
    print("\nCopy the table above into your shock card. Yields in bps, rest in % — your rule.")


if __name__ == "__main__":
    main()
