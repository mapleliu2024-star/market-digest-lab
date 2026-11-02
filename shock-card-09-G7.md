# Shock-card-09-G7.md

> A shock card is the standard X-ray you take of every event. Same format every time,
> so events can be compared side by side on the dashboard later.

## The event
- **Headline:** [G7's 100M-barrel emergency oil release eased Brent crude oil price to $102.25]
  <!-- The one-line rule stays: if you can't headline it, you don't understand it yet.
       But complex events get room below. -->
- **When:** [2026-10-02 ET]
- **Why it mattered:** [This event was a rare, aggressive action to control oil price. A 50m-barrel diesel release equates to approximately 17% of the EU's emergency stocks of diesel and gasoil.]
- **Category:** [oil/energy supply fears]
- **Timeline (optional — for multi-phase events only):** N/A [2–5 dated bullets tracing how the event
  unfolded, e.g. "Feb 28: strikes begin → Mar 8: Brent breaks $100 → Apr 30: Brent peaks $126".
  Skip this for single-moment shocks like a jobs report.]

## Transmission snapshot
Event: G7 100M-barrel emergency oil release (2026-10-02)
Market day used: 2026-10-02 | 'Before' close: 2026-10-01
1-week target: 2026-10-09
1-month target: n/a — your file ends 2026-10-30

| Asset | 1-day | 1-week | 1-month |
|-------|-------|--------|---------|
| S&P 500 | +0.73% | +1.89% | n/a |
| WTI crude | -1.90% | -1.10% | n/a |
| Gold | -0.95% | +0.33% | n/a |
| DXY (dollar index) | -0.17% | +0.11% | n/a |
| VIX (fear gauge) | -6.59% | -9.46% | n/a |
| 10Y Treasury yield | +4 bps | +1 bps | n/a |
| Tech (XLK) | +1.01% | +0.49% | n/a |
| Energy (XLE) | +0.19% | +3.80% | n/a |
| Banks (XLF) | +0.06% | +2.38% | n/a |

_Fill from `python3 price_pipeline.py` output — never invent numbers._
_Yields in basis points, everything else in %._

**Extended tracking (optional — for events lasting longer than a month):** N/A
<!-- The 1D/1W/1M core stays standard so every card is comparable on the dashboard.
     But long events get a second act: add dated snapshots at each turning point. -->
- [Phase 2 — date + one-line market state, e.g. "Apr 30: Brent peaks $126, equities..."]
- [Phase 3 — ...]

## Channels — what moved first, what moved most
- Moved within 1 day: [WTI crude dropped after the oil release. VIX dropped.]
- Moved late or not at all: [VIX dropped more after one week. S&P 500, XLE, and XLF went up after one week. Gold, DXY, 10Y Treasury yield, and XLK barely moved.]

## Against the textbook (Liu writes this in her own words)
- **Did markets behave the way theory predicts?** [Yes and no. After the oil release, the market became less paniced. So, VIX and WTI both dropped. Inflation pressure was also eased among countries. Sectors like XLK, XLE, and XLF all went up because of elevated confidence to the market. However, since the Middle East war is still underway, this action was not a permanent solution or change to the whole market. Otherwise, a massive supply injection should permanently shift the supply curve and lower equilibrium price.]
- **What surprised you?** [Combined with escalating geopolitical tensions in the Middle East and a strict ban on Russian fuel exports, Brent crude shocked the market by aggressively reversing its initial decline and rocketing past $117 per barrel by late October.]
- _If she can't defend it out loud, it doesn't ship._

## Open questions
- [What if oil price remained the same despite the release? ]

## You're done when
- Every [bracket] is filled, no invented numbers, and Liu can explain the card out loud in 60 seconds.

---
*Revision history: v2 (2026-10-07) — per Liu's critique: (1) headline + optional timeline instead of
one-line-only; (2) standard 1D/1W/1M core + optional extended tracking for long events;
(3) "Against the textbook / what surprised you" replaces "Does this make economic sense?"*
