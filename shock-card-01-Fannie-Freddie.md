# Shock-card-01-Fannie-Freddie.md

> A shock card is the standard X-ray you take of every event. Same format every time,
> so events can be compared side by side on the dashboard later.

## The event
- **Headline:** [Trump’s $200B Mortgage Debt Order Sparks 6% Small-Cap Stock Surge and Knocks Loan Rates Below 6%]
  <!-- The one-line rule stays: if you can't headline it, you don't understand it yet.
       But complex events get room below. -->
- **When:** [2026-01-08]
- **Why it mattered:** [This government intervention dragged 30-year mortgage rate below 6%. It sparked a 6% surge in Russel 2000, which indicated a domestic economic boom. Because cheaper mortgages for consumers meant a massive wave of business was heading straight for small companies.]
- **Category:** [prices soar]
- **Timeline (optional — for multi-phase events only):** N/A [2–5 dated bullets tracing how the event
  unfolded, e.g. "Feb 28: strikes begin → Mar 8: Brent breaks $100 → Apr 30: Brent peaks $126".
  Skip this for single-moment shocks like a jobs report.]

## Transmission snapshot
1-month target: 2026-02-10

| Asset | 1-day | 1-week | 1-month |
|-------|-------|--------|---------|
| S&P 500 | +0.01% | +0.34% | +0.30% |
| WTI crude | +3.16% | +5.72% | +14.23% |
| Gold | -0.04% | +3.61% | +12.74% |
| DXY (dollar index) | +0.25% | +0.65% | -1.91% |
| VIX (fear gauge) | +0.46% | +2.99% | +15.67% |
| 10Y Treasury yield | +5 bps | +2 bps | +1 bps |
| Tech (XLK) | -1.56% | -0.73% | -2.72% |
| Energy (XLE) | +3.15% | +5.50% | +18.72% |
| Banks (XLF) | +0.52% | -2.23% | -3.70% |

_Fill from `python3 price_pipeline.py` output — never invent numbers._
_Yields in basis points, everything else in %._

**Extended tracking (optional — for events lasting longer than a month):** N/A
<!-- The 1D/1W/1M core stays standard so every card is comparable on the dashboard.
     But long events get a second act: add dated snapshots at each turning point. -->
- [Phase 2 — date + one-line market state, e.g. "Apr 30: Brent peaks $126, equities..."]
- [Phase 3 — ...]

## Channels — what moved first, what moved most
- Moved within 1 day: [Tech(XLK) and Energy(XLE) moved within one day.]
- Moved late or not at all: [S&P500 and 10Y Treasury yield moved little; WTI crude, Gold, and VIX moved significantly later, but I don't think their movements were mostly led by this Fannie-Freddie event; DXY moved little later; Banks(XLF) dropped after one week and continued to drop after one month.]

## Against the textbook
- **Did markets behave the way theory predicts?** [I think assets are basically behave normally, but due to other events such as Iran war, some assets especially S&P500, WTI crude, Gold, and VIX reacted more significantly.]
- **What surprised you?** [I did not know that purchasing $200B MBS will lower the 30Y Mortgage rate, then indirectly led to Russel 2000 surge (small-cap companies).]
- _If she can't defend it out loud, it doesn't ship._

## Open questions
- [Did this action add U.S. national debt?
The $200 billion purchasing was executed using existing cash reserves and non-cash liquidity assets in Fannie and Freddie. It does not directly add U.S. national debt level.]

## You're done when
- Every [bracket] is filled, no invented numbers, and Liu can explain the card out loud in 60 seconds.

---
*Revision history: v2 (2026-10-07) — per Liu's critique: (1) headline + optional timeline instead of
one-line-only; (2) standard 1D/1W/1M core + optional extended tracking for long events;
(3) "Against the textbook / what surprised you" replaces "Does this make economic sense?"*
