# Shock-card-03-Broadcom.md

> A shock card is the standard X-ray you take of every event. Same format every time,
> so events can be compared side by side on the dashboard later.

## The event
- **Headline:** [Broadcom's disappointing guidance led to a large scale of tech stocks selloff]
  <!-- The one-line rule stays: if you can't headline it, you don't understand it yet.
       But complex events get room below. -->
- **When:** [Guidance released Jun 3; selloff measured Jun 5, 2026 ET]
- **Why it mattered:** [the AI-related stocks dropped sharply]
- **Category:** [data surprise repricing]
- **Timeline (optional — for multi-phase events only):** N/A [2–5 dated bullets tracing how the event
  unfolded, e.g. "Feb 28: strikes begin → Mar 8: Brent breaks $100 → Apr 30: Brent peaks $126".
  Skip this for single-moment shocks like a jobs report.]

## Transmission snapshot
| Asset | 1-day | 1-week | 1-month |
|-------|-------|--------|---------|
| S&P 500 | -2.64% | -2.02% | -0.54% |
| WTI crude | -2.69% | -8.77% | -22.53% |
| Gold | -3.10% | -5.91% | -8.08% |
| DXY (dollar index) | +0.66% | +0.34% | +1.54% |
| VIX (fear gauge) | +39.68% | +14.81% | +2.86% |
| 10Y Treasury yield | +6 bps | +1 bps | +6 bps |
| Tech (XLK) | -6.66% | -4.33% | -3.93% |
| Energy (XLE) | -1.84% | -2.04% | -6.02% |
| Banks (XLF) | +0.21% | +2.20% | +6.79% |

_Fill from `python3 price_pipeline.py` output — never invent numbers._
_Yields in basis points, everything else in %._

**Extended tracking (optional — for events lasting longer than a month):** N/A
<!-- The 1D/1W/1M core stays standard so every card is comparable on the dashboard.
     But long events get a second act: add dated snapshots at each turning point. -->
- [Phase 2 — date + one-line market state, e.g. "Apr 30: Brent peaks $126, equities..."]
- [Phase 3 — ...]

## Channels — what moved first, what moved most
- Moved within 1 day: [S&P 500, VIX, Tech (XLK), Energy (XLE) moved significantly.]
- Moved late or not at all: [WTI and gold reacted on day 1, and the drops deepened over the month; S&P 500 and DXY were relatively stable after 1 week and 1 month; VIX gradually went back to normal levels after 1 week and 1 month; 10Y Treasury yield barely moved; Energy (XLE) and Banks (XLF) moved later.]

## Against the textbook
- **Did markets behave the way theory predicts?** [I don't think this is an event that goes with the textbook theory because AI sector is still developing and the stocks/indexes that are related to AI are usually significantly affected by market expectations.]
- **What surprised you?** [I underweighted the impact of one company's performance on the whole sector. Broadcom's disappointing performance can cause a big selloff in the whole sector.]
- _If she can't defend it out loud, it doesn't ship._

## Open questions
- [Did the selloff in the AI sector influence the other sectors?
Yes. 
Information Technology sector bore the most damage; sectors like Consumer Discretionary and Communication Services were dragged down due to potentially higher interest-rates expectations, while sectors like Financials, Healthcare, and Utilities stayed relatively stable. ]

## You're done when
- Every [bracket] is filled, no invented numbers, and Liu can explain the card out loud in 60 seconds.

---
*Revision history: v2 (2026-10-07) — per Liu's critique: (1) headline + optional timeline instead of
one-line-only; (2) standard 1D/1W/1M core + optional extended tracking for long events;
(3) "Against the textbook / what surprised you" replaces "Does this make economic sense?"*
