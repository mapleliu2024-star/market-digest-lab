# Shock-card-04-Canada.md

> A shock card is the standard X-ray you take of every event. Same format every time,
> so events can be compared side by side on the dashboard later.

## The event
- **Headline:** [US-Canada trade war led to the Dow dropped for two straight weeks]
  <!-- The one-line rule stays: if you can't headline it, you don't understand it yet.
       But complex events get room below. -->
- **When:** [2026, Talks collapsed Aug 22 (Sat); market reaction measured Aug 24 (Mon), ET]
- **Why it mattered:** [This trade collapse disrupted cross-border supply chain, created layoffs and factory pressures, and added pressure on the governments.]
- **Category:** [trade dispute]
- **Timeline (optional — for multi-phase events only):** N/A [2–5 dated bullets tracing how the event
  unfolded, e.g. "Feb 28: strikes begin → Mar 8: Brent breaks $100 → Apr 30: Brent peaks $126".
  Skip this for single-moment shocks like a jobs report.]

## Transmission snapshot
Event: US-Canada trade talks collapse (2026-08-22)
Market day used: 2026-08-24 | 'Before' close: 2026-08-21
1-week target: 2026-08-31
1-month target: 2026-09-23

| Asset | 1-day | 1-week | 1-month |
|-------|-------|--------|---------|
| S&P 500 | -0.28% | +0.15% | +0.41% |
| WTI crude | -2.35% | -1.49% | +5.86% |
| Gold | +0.37% | -4.25% | -7.74% |
| DXY (dollar index) | +0.20% | +0.64% | +2.33% |
| VIX (fear gauge) | +4.76% | -1.39% | +0.33% |
| 10Y Treasury yield | -3 bps | +2 bps | +38 bps |
| Tech (XLK) | -1.78% | +1.74% | +6.69% |
| Energy (XLE) | -0.83% | +0.50% | -1.41% |
| Banks (XLF) | +1.29% | +0.40% | -4.78% |

_Fill from `python3 price_pipeline.py` output — never invent numbers._
_Yields in basis points, everything else in %._

**Extended tracking (optional — for events lasting longer than a month):** N/A
<!-- The 1D/1W/1M core stays standard so every card is comparable on the dashboard.
     But long events get a second act: add dated snapshots at each turning point. -->
- [Phase 2 — date + one-line market state, e.g. "Apr 30: Brent peaks $126, equities..."]
- [Phase 3 — ...]

## Channels — what moved first, what moved most
- Moved within 1 day: [WTI crude, VIX, and XLF moved within one day, but WTI crude were not directly moved due to the tariff war.]
- Moved late or not at all: [S&P500 moved little in one day, one week, and one month. DXY moved after one month. XLK moved later. XLF moved significantly after one month.]

## Against the textbook
- **Did markets behave the way theory predicts?** [Yes. The volatility (VIX) surged after trade war happened. Because tariffs are acted as an immediate tax on supply chain, sectors dependent on cross-border logistics (Tech/Hardware) and cross-border commodities (Energy) suffered first. After the Canadian's retaliatory tariffs, US dollar, as the global commodity pricing currency, surged, because investors were chasing safety (flight-to-liquidity). Because Gold is priced in US dollar as well, gold price dropped.]
- **What surprised you?** [I was not familiar with the trade war's impacts. Basically, trade war has huge impacts on the sectors that are closely related to the supply chain. The dominating currency went up according to Mundell-Fleming model.]
- _If she can't defend it out loud, it doesn't ship._

## Open questions
- [Does this trade war create any benefits to any country?
In theory, bilateral trade wars rarely ccreate a net economic benefit for either participant. Instead, they function as negative-sum games where both primary nations inherit higher costs, supply chain friction, and lower GDP growth.]

## You're done when
- Every [bracket] is filled, no invented numbers, and Liu can explain the card out loud in 60 seconds.

---
*Revision history: v2 (2026-10-07) — per Liu's critique: (1) headline + optional timeline instead of
one-line-only; (2) standard 1D/1W/1M core + optional extended tracking for long events;
(3) "Against the textbook / what surprised you" replaces "Does this make economic sense?"*
