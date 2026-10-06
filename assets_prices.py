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

for name, ticker in tickers.items():
    df = yf.download(ticker, period="5d", auto_adjust=True, progress=False)
    last = round(float(df["Close"].squeeze().iloc[-1]), 2)
    print(name, ticker, "->", last)

