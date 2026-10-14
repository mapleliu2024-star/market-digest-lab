# Shock-card-02-Iran.md

> A shock card is the standard X-ray you take of every event. Same format every time,
> so events can be compared side by side on the dashboard later.

## The event
- **Headline:** [US and Israel struck on Iran impacted the whole financial market ]
  <!-- The one-line rule stays: if you can't headline it, you don't understand it yet.
       But complex events get room below. -->
- **When:** [2026-02-28 happened, 2026-03-02 market reacted ET]
- **Why it mattered:** [This war led to oil price surging, inflation pressure soaring globally, and shocked the stock market.]
- **Category:** [oil/energy supply fears]
- **Timeline (optional — for multi-phase events only):** [The war in Iran is still underway.]

## Transmission snapshot
| Asset | 1-day | 1-week | 1-month |
|-------|-------|--------|---------|
| S&P 500 | +0.04% | -1.20% | -4.41% |
| WTI crude | +6.28% | +41.41% | +49.39% |
| Gold | +1.21% | -2.75% | -8.29% |
| DXY (dollar index) | +0.79% | +1.61% | +2.09% |
| VIX (fear gauge) | +7.96% | +28.40% | +23.56% |
| 10Y Treasury yield | +9 bps | +17 bps | +36 bps |
| Tech (XLK) | +0.56% | +0.72% | -2.65% |
| Energy (XLE) | +2.00% | +0.72% | +6.14% |
| Banks (XLF) | -0.25% | -2.14% | -3.38% |

_Fill from `python3 price_pipeline.py` output — never invent numbers._
_Yields in basis points, everything else in %._

**Extended tracking (optional — for events lasting longer than a month):** the war is still underway, the oil price and inflation concerns still exist.
<!-- The 1D/1W/1M core stays standard so every card is comparable on the dashboard.
     But long events get a second act: add dated snapshots at each turning point. -->
- [Phase 2 — date + one-line market state, e.g. "Apr 30: Brent peaks $126, equities..."]
- [Phase 3 — ...]

## Channels — what moved first, what moved most
- Moved within 1 day: [Almost every asset moved withing one day and one month. But the tech and banks were relatively less affected by the event. The WTI crude, Gold, VIX, and 10Y Treasury yield moved.]

## Against the textbook (Liu writes this in her own words)
- **Did markets behave the way theory predicts?** [Yes. When geopolitical events in the Middle East occur, the oil price surged immediately, then spread to other sectors, and raised inflation concerns globally. ]
- **What surprised you?** [The impacts of the Iran war were within my expectations, but no one had expected that the Iran war this year could last for over months, I am not excluded.]
- _If she can't defend it out loud, it doesn't ship._

## Open questions
- [Any sectors were not impacted by the Iran war this year?
No. Every sector was impacted negatively by the Iran war directly or indirectly. But areas like Defense and military contracting benefit from this war.]

## You're done when
- Every [bracket] is filled, no invented numbers, and Liu can explain the card out loud in 60 seconds.

---
*Revision history: v2 (2026-10-07) — per Liu's critique: (1) headline + optional timeline instead of
one-line-only; (2) standard 1D/1W/1M core + optional extended tracking for long events;
(3) "Against the textbook / what surprised you" replaces "Does this make economic sense?"*
