# fred_macro.py — pull macro "scoreboard" numbers from the Fed's FRED database.
# Your API key lives in ~/fred_key.txt (NEVER commit that file to GitHub).
# This script contains no secret, so it IS safe to commit to your repo.

import os
from fredapi import Fred

KEY_FILE = os.path.expanduser("~/fred_key.txt")
with open(KEY_FILE) as f:
    API_KEY = f.read().strip()

fred = Fred(api_key=API_KEY)

SERIES = {
    "Fed funds rate, % (FEDFUNDS)": "FEDFUNDS",
    "CPI index (CPIAUCSL)": "CPIAUCSL",
    "Unemployment rate, % (UNRATE)": "UNRATE",
    "Nonfarm payrolls, thousands of jobs (PAYEMS)": "PAYEMS",
    "M2 money supply, $bn (M2SL)": "M2SL",
    "10Y Treasury yield, % (DGS10)": "DGS10",
    "10Y minus 2Y spread (T10Y2Y)": "T10Y2Y",
}

print(f"{'Series':<48}{'Latest date':<14}{'Value':>14}")
print("-" * 78)
for label, sid in SERIES.items():
    s = fred.get_series(sid).dropna()
    if s.empty:
        print(f"{label:<48}{'no data':<14}")
        continue
    print(f"{label:<48}{str(s.index[-1].date()):<14}{s.iloc[-1]:>14,.2f}")
print("-" * 78)
print("Tip: PAYEMS is in thousands of jobs; M2SL is in billions of dollars.")
