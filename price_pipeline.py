import yfinance as yf

ASSETS = {
    "S&P 500 (US stocks)": "^GSPC",
    "WTI crude (US oil)": "CL=F",
    "Gold": "GC=F",
    "DXY (dollar index)": "DX-Y.NYB",
    "VIX (fear gauge)": "^VIX",
    "10Y Treasury yield": "^TNX",
    # Liu: add your 2-3 sector ETFs from assets.md here, e.g.:
    # "Tech ETF (XLK)": "XLK",
    # "Energy ETF (XLE)": "XLE",
}


def pct_change(latest, earlier):
    return (latest / earlier - 1) * 100


def main():
    print(f"{'Asset':<24}{'Latest':>12}{'1D %':>9}{'1W %':>9}{'1M %':>9}")
    print("-" * 66)
    for name, ticker in ASSETS.items():
        hist = yf.Ticker(ticker).history(period="3mo")
        if hist.empty or len(hist) < 25:
            print(f"{name:<24}{'no data':>12}")
            continue
        # .squeeze() flattens Yahoo's extra column label (same fix as assets_prices.py)
        close = hist["Close"].squeeze()
        latest = close.iloc[-1]
        d1 = pct_change(latest, close.iloc[-2])
        w1 = pct_change(latest, close.iloc[-6])
        m1 = pct_change(latest, close.iloc[-22])
        print(f"{name:<24}{latest:>12.2f}{d1:>+8.2f}%{w1:>+8.2f}%{m1:>+8.2f}%")
    print("-" * 66)
    print("Note: for ^TNX, 'Latest' is the 10Y yield in percent (e.g. 5.31 means 5.31%).")


if __name__ == "__main__":
    main()
