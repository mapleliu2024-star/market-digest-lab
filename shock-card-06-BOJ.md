# Shock-card-06-BOJ.md

> A shock card is the standard X-ray you take of every event. Same format every time,
> so events can be compared side by side on the dashboard later.

## The event
- **Headline:** [BOJ raised interest rates to a 31-year high to fight persistent inflation pressures]
  <!-- The one-line rule stays: if you can't headline it, you don't understand it yet.
       But complex events get room below. -->
- **When:** [2026-09-18 ET]
- **Why it mattered:** [Raising interest rates led to a weaker yen instead, because of a 7-2 split vote, which indicated a less aggressive future path. This action also highlighted the global geopolitical tense.]
- **Category:** [higher for longer]
- **Timeline (optional — for multi-phase events only):** N/A [2–5 dated bullets tracing how the event
  unfolded, e.g. "Feb 28: strikes begin → Mar 8: Brent breaks $100 → Apr 30: Brent peaks $126".
  Skip this for single-moment shocks like a jobs report.]

## Transmission snapshot
Event: BOJ hikes to 1.25% (2026-09-18)
Market day used: 2026-09-18 | 'Before' close: 2026-09-17
1-week target: 2026-09-25
1-month target: 2026-10-20

| Asset | 1-day | 1-week | 1-month |
|-------|-------|--------|---------|
| S&P 500 | +0.17% | +1.38% | +0.98% |
| WTI crude | -1.58% | -9.32% | -0.12% |
| Gold | +0.57% | -1.78% | -5.84% |
| DXY (dollar index) | +0.00% | +0.75% | +1.51% |
| VIX (fear gauge) | -4.08% | -3.69% | +12.11% |
| 10Y Treasury yield | +5 bps | +24 bps | +17 bps |
| Tech (XLK) | +0.82% | +4.49% | -1.28% |
| Energy (XLE) | -0.26% | -3.21% | +6.04% |
| Banks (XLF) | -0.04% | -1.51% | +0.07% |


_Fill from `python3 price_pipeline.py` output — never invent numbers._
_Yields in basis points, everything else in %._

**Extended tracking (optional — for events lasting longer than a month):** N/A
<!-- The 1D/1W/1M core stays standard so every card is comparable on the dashboard.
     But long events get a second act: add dated snapshots at each turning point. -->
- [Phase 2 — date + one-line market state, e.g. "Apr 30: Brent peaks $126, equities..."]
- [Phase 3 — ...]

## Channels — what moved first, what moved most
- Moved within 1 day: [VIX moved within 1 day.]
- Moved late or not at all: [WTI crude moved after one week. Gold moved after one month. VIX moved volatily. DXY basicially did not move. XLK and XLE moved significantly after one week. But WTI, gold, VIX were driven by other macro factors.]

## Against the textbook
- **Did markets behave the way theory predicts?** [Yes. According to the efficient market theory, symetrical information can reduce the price surprises. The market was expecting the rate hike, so this hike did not surprise the market, and the market has already spent weeks adjusting to this reality. ]
- **What surprised you?** [ I have learned about efficient market theory and uncovered/covered interest parity, but I am not used to connect these theories with the real events.
  There are the direct impacts: 
  1) 10Y Treasury Yield (+5 bps to +24 bps): This asset was directly influenced. As the BOJ raised its policy rate, the relative yield spread between Japanese government bonds and U.S. Treasuries narrowed slightly. This puts structural upward pressure on U.S. yields, as global investors demand higher returns to keep their capital parked in U.S. debt rather than repatriating it to Japan. 
  2) DXY Dollar Index (+0.00% to +1.51%): The dollar index strengthened over the month despite the BOJ rate hike. This happened because the BOJ's cautious, split 7-2 vote signaled that subsequent hikes would be slow, while the U.S. Federal Reserve maintained a relatively firm economic outlook, keeping the dollar dominant.
  3) Tech Sector / XLK (+0.82% to +4.49%): Technology stocks are historically highly sensitive to sudden spikes in the Japanese Yen due to the unwind of the Yen Carry Trade (which often funds speculative tech bets). Because the BOJ executed a smooth, highly anticipated hike without spiking the yen, tech investors experienced a massive relief rally over the 1-week and 1-day windows. 
]
- _If she can't defend it out loud, it doesn't ship._
## Open questions
- [According to the 7-2 split vote, what will the Japanese government do in the next several months to deal with the slower economy and high inflation pressure?]

## You're done when
- Every [bracket] is filled, no invented numbers, and Liu can explain the card out loud in 60 seconds.

---
*Revision history: v2 (2026-10-07) — per Liu's critique: (1) headline + optional timeline instead of
one-line-only; (2) standard 1D/1W/1M core + optional extended tracking for long events;
(3) "Against the textbook / what surprised you" replaces "Does this make economic sense?"*
