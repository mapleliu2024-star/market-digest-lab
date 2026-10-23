# Shock-card-05-Fed.md

> A shock card is the standard X-ray you take of every event. Same format every time,
> so events can be compared side by side on the dashboard later.

## The event
- **Headline:** [The first rate raise in three years leading to record high 10Y Treasury yield]
  <!-- The one-line rule stays: if you can't headline it, you don't understand it yet.
       But complex events get room below. -->
- **When:** [2026-09-16 ET]
- **Why it mattered:** [Due to persistent high inflation, raising rates is adding pressure to the 10Y Treasury yield and shaking the stock market, 8 out of 11 S&P sectors fell that day. Plus the Middle East War continues to fuel inflation, which indicates higher rates for longer. This went against the Fed's initial intention.]
- **Category:** [higher for longer]
- **Timeline (optional — for multi-phase events only):** N/A [2–5 dated bullets tracing how the event
  unfolded, e.g. "Feb 28: strikes begin → Mar 8: Brent breaks $100 → Apr 30: Brent peaks $126".
  Skip this for single-moment shocks like a jobs report.]

## Transmission snapshot
Event: Fed +25bps to 3.75-4.00% (2026-09-16)
Market day used: 2026-09-16 | 'Before' close: 2026-09-15
1-week target: 2026-09-23
1-month target: 2026-10-16

| Asset | 1-day | 1-week | 1-month |
|-------|-------|--------|---------|
| S&P 500 | -0.45% | +1.59% | +0.97% |
| WTI crude | -3.21% | -12.92% | -4.18% |
| Gold | +1.26% | -0.33% | -3.50% |
| DXY (dollar index) | +0.66% | +1.46% | +2.20% |
| VIX (fear gauge) | +2.97% | -11.74% | +16.22% |
| 10Y Treasury yield | +1 bps | +12 bps | +10 bps |
| Tech (XLK) | +0.10% | +6.44% | -0.03% |
| Energy (XLE) | -2.88% | -4.84% | +4.12% |
| Banks (XLF) | -1.62% | -3.72% | -1.99% |

_Fill from `python3 price_pipeline.py` output — never invent numbers._
_Yields in basis points, everything else in %._

**Extended tracking (optional — for events lasting longer than a month):** N/A
<!-- The 1D/1W/1M core stays standard so every card is comparable on the dashboard.
     But long events get a second act: add dated snapshots at each turning point. -->
- [Phase 2 — date + one-line market state, e.g. "Apr 30: Brent peaks $126, equities..."]
- [Phase 3 — ...]

## Channels — what moved first, what moved most
- Moved within 1 day: [WTI crude, Gold, VIX, XLE, XLF]
- Moved late or not at all: [WTI crude shocked significantly in one day, one week, and one month. S&P500, 10Y Treasury yield, and XLK barely moved. DXY moved after one week and one month. XLK moved after one week.]

## Against the textbook (Liu writes this in her own words)
- **Did markets behave the way theory predicts?** [Yes and No. For example, the 10Y Treasury yield rose up after the higher interest rates. (Higher interest rates means lower bond prices, lower prices mean higher yield.) Equities' price fell due to higher discounting rate. Usually, cyclical or heavy-debt sectors are punished by higher interest rates, such as Financials. While defensive sectors tend to survive. So, 8/11 sectors all fell.]
- **What surprised you?** [The S&P 500 barely changed after raising rates. After researching, this is considered as a tug-of-war. Changes in sectors like tech moved up offset the changes in sectors like energy and banks. The minimum change in S&P 500 does not mean no impact from the raising rates, we can tell from the significant change in VIX and DXY.]
- _If she can't defend it out loud, it doesn't ship._

## Open questions
- [How effective is raising rates to control inflation?
Raising interest rates is highly effective at controlling inflation. I don't know what is the best way to measure the effects.]

## You're done when
- Every [bracket] is filled, no invented numbers, and Liu can explain the card out loud in 60 seconds.

---
*Revision history: v2 (2026-10-07) — per Liu's critique: (1) headline + optional timeline instead of
one-line-only; (2) standard 1D/1W/1M core + optional extended tracking for long events;
(3) "Against the textbook / what surprised you" replaces "Does this make economic sense?"*
