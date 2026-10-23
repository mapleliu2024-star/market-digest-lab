"""Day 8 backfill: pull 12 months of daily closes for your 9 transmission assets.

WHY THIS SCRIPT EXISTS (the one-line "why" Liu asked for):
Every shock card in Module 1 measures "what did markets do after X happened" —
this file is the price history those measurements are computed from. Run it once,
keep the CSV, and every future shock card reads from it.

HOW TO RUN (same as your other scripts):
1. In VS Code, open your Market-Digest-Lab folder.
2. Create a new file named backfill_12m.py and paste this whole script into it.
3. Right-click -> "Run Python File in Terminal" (or press the play button top-right).
4. Wait ~1 minute. It saves backfill-prices-12m.csv next to the script.

WHAT TO CHECK AFTER IT RUNS (your Day 8 sanity task):
- It should print about 250 rows and a date range from 2025-10-10 to 2026-10-09.
  (2026-10-09 is Friday's close — markets were closed this weekend, so Friday is
  the latest data available. This is expected, not an error.)
- Sanity anchor from YOUR OWN Oct 6 run on this Mac: the 2026-10-06 row should show
  VIX near 15.37 and US10Y_yield near 5.31. If those match, the pull is trustworthy.
- The script prints those two numbers for you — just compare them to 15.37 / 5.31.

QUIRKS (already known, baked in):
- ^TNX prints the real 10Y yield in percent (your Oct 6 run showed 5.31 = 5.31%).
- DX-Y.NYB is the dollar index ticker; CL=F / GC=F are oil and gold futures.
"""
import yfinance as yf

tickers = {
    "SP500": "^GSPC",
    "WTI_crude": "CL=F",
    "Gold": "GC=F",
    "VIX": "^VIX",
    "Dollar_index": "DX-Y.NYB",
    "US10Y_yield": "^TNX",
    "Tech": "XLK",
    "Energy": "XLE",
    "Banks": "XLF",
}

print("Pulling 12 months of daily closes for", len(tickers), "assets...")
codes = list(tickers.values())
df = yf.download(codes, start="2025-10-10", end="2026-10-24",
                 auto_adjust=True, progress=False)

closes = df["Close"].rename(columns={v: k for k, v in tickers.items()})
closes = closes[[name for name in tickers]]  # keep your assets.md order
closes.index.name = "date"
closes.to_csv("backfill-prices-12m.csv")

print("Saved backfill-prices-12m.csv")
print("Rows:", len(closes), "| Range:",
      closes.index.min().date(), "->", closes.index.max().date())
print("Missing values per asset (should be 0 or tiny):")
print(closes.isna().sum())

print("\n--- Sanity check vs YOUR Oct 6 numbers (VIX 15.37, 10Y 5.31) ---")
try:
    anchor = closes.loc["2026-10-06"]
    vix = round(float(anchor["VIX"]), 2)
    y10 = round(float(anchor["US10Y_yield"]), 2)
    print(f"2026-10-06 in this file: VIX = {vix}, US10Y_yield = {y10}")
    print("VIX match:", "YES :)" if abs(vix - 15.37) < 0.05 else "NO - tell Muse")
    print("10Y match:", "YES :)" if abs(y10 - 5.31) < 0.05 else "NO - tell Muse")
except KeyError:
    print("2026-10-06 not found in the data (weekend/holiday gap?) - tell Muse.")
