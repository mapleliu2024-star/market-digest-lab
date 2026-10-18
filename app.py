"""app.py — Market Digest Lab dashboard (Day 13, first draft).

THE ONE-LINE "WHY": the dashboard is the public face of your Lab. Tab 1 lets
anyone browse your shock cards (how each event moved the 9 assets); Tab 2 shows
your narrative labels and the dominant market story of the week.

HOW TO RUN (on your Mac, just like shock_card.py):
1. Save this file as app.py in your Market-Digest-Lab folder.
2. Terminal: pip install streamlit (one time only) -> streamlit run app.py
3. Your browser opens the dashboard automatically.

GOLDEN RULE: every number below was copied verbatim from your repo files —
never invent a number, only add real ones.
"""

import streamlit as st  # the ONLY extra package you need: pip install streamlit

# --- Page title at the top ---
st.set_page_config(page_title="Market Digest Lab", layout="wide")
st.title("Market Digest Lab — How Markets Digest the World")

# --- load_data() — FUTURE plumbing; ignore it today. Later it will read ---
# backfill-prices-12m.csv from the SAME folder as app.py, so new cards can be
# computed live. Right now it returns nothing: the two finished cards below
# use the numbers already in your repo files.
def load_data():
    prices = None  # later becomes: pd.read_csv("backfill-prices-12m.csv")
    return prices


prices = load_data()  # unused for now — the wiring is here for later

# --- YOUR DATA, verbatim from your repo. To add a finished card: paste its ---
# real table below and add an "elif" branch in Tab 1.
EVENTS = [  # your 15 events, from events-v1.md
    "Event 1 — Jan 8: Fannie/Freddie $200B MBS plan",
    "Event 2 — Feb 28: US-Israel strikes on Iran / Hormuz ban",
    "Event 3 — Jun 5: Broadcom tech selloff",
    "Event 4 — Aug 22: US-Canada trade talks collapse",
    "Event 5 — Sep 16: Fed +25bps to 3.75-4.00%",
    "Event 6 — Sep 18: BOJ hikes to 1.25%",
    "Event 7 — Sep 24: Trump-Xi summit mixed reaction",
    "Event 8 — Sep 30 / Oct 1: Alphabet Gemini 4 Argon unveiling (shares -1.7% Oct 1)",
    "Event 9 — Oct 2: G7 100M-barrel emergency oil release",
    "Event 10 — Oct 2: weak Sept jobs report",
    "Event 11 — Oct 1, 2025: US government shutdown begins",
    "Event 12 — Oct 28, 2025: Microsoft 27% OpenAI stake ($500B)",
    "Event 13 — Apr 7: US-Israel-Iran ceasefire",
    "Event 14 — Mar 18: Fed holds 3.50-3.75%",
    "Event 15 — Mar 13: Q4 2025 GDP falls to 0.7%",
]

# (asset, 1-day, 1-week, 1-month) — VERBATIM from your shock-card-02-Iran.md
CARD_2 = [
    ("S&P 500", "+0.04%", "-1.20%", "-4.41%"),
    ("WTI crude", "+6.28%", "+41.41%", "+49.39%"),
    ("Gold", "+1.21%", "-2.75%", "-8.29%"),
    ("DXY (dollar index)", "+0.79%", "+1.61%", "+2.09%"),
    ("VIX (fear gauge)", "+7.96%", "+28.40%", "+23.56%"),
    ("10Y Treasury yield", "+9 bps", "+17 bps", "+36 bps"),
    ("Tech (XLK)", "+0.56%", "+0.72%", "-2.65%"),
    ("Energy (XLE)", "+2.00%", "+0.72%", "+6.14%"),
    ("Banks (XLF)", "-0.25%", "-2.14%", "-3.38%"),
]

# (asset, 1-day, 1-week, 1-month) — VERBATIM from your shock-card-03-Broadcom.md
CARD_3 = [
    ("S&P 500", "-2.64%", "-2.02%", "-0.54%"),
    ("WTI crude", "-2.69%", "-8.77%", "-22.53%"),
    ("Gold", "-3.10%", "-5.91%", "-8.08%"),
    ("DXY (dollar index)", "+0.66%", "+0.34%", "+1.54%"),
    ("VIX (fear gauge)", "+39.68%", "+14.81%", "+2.86%"),
    ("10Y Treasury yield", "+6 bps", "+1 bps", "+6 bps"),
    ("Tech (XLK)", "-6.66%", "-4.33%", "-3.93%"),
    ("Energy (XLE)", "-1.84%", "-2.04%", "-6.02%"),
    ("Banks (XLF)", "+0.21%", "+2.20%", "+6.79%"),
]

# Your 12 narrative labels, from taxonomy.md (name + your one-line definition)
LABELS = [
    ("AI spending boom", "companies and investors pouring money into AI — chips, data centers, models"),
    ("bond market selloff", "mass bond selling pushes prices down and yields up"),
    ("hawkish comments <-> dovish comments", "the Fed sounds rate-hike-y vs rate-cut-y"),
    ("prices soar", "prices rise fast and significantly"),
    ("higher for longer", "interest rates stay high for a longer time"),
    ("trade dispute", "conflicts between countries over tariffs and trade policy"),
    ("safe haven", "investors flee to gold or the dollar for safety when scared"),
    ("global rate tightening", "central banks raise rates worldwide"),
    ("oil/energy supply fears", "supply running short, pushing oil and energy prices up"),
    ("priced for perfection", "markets punish even good results when expectations are sky-high"),
    ("data surprise repricing", "economic data lands far from expectations, forcing a Fed rethink"),
    ("debt fears", "worry that government borrowing is too high, pushing yields up"),
]

# Your own verdict on this week's dominant story, from cluster-review-2026-10-15.md
DOMINANT_NARRATIVE = "The story actually dominating markets this week is the September CPI report because it shows that the annual inflation rate is up to 3.7% year-over-year."

# --- Small helpers that turn your data into readable tables ---
def card_table(rows):
    """Shock-card table from a list of (asset, 1-day, 1-week, 1-month)."""
    header = ["| Asset | 1-day | 1-week | 1-month |", "|---|---|---|---|"]
    return "\n".join(header + [f"| {a} | {d1} | {w1} | {m1} |" for a, d1, w1, m1 in rows])


def compare_table(rows_a, rows_b):
    """1-day moves of the two finished cards, side by side."""
    header = ["| Asset | Event 2 (Iran/Hormuz) 1-day | Event 3 (Broadcom) 1-day |", "|---|---|---|"]
    return "\n".join(header + [f"| {a[0]} | {a[1]} | {b[1]} |" for a, b in zip(rows_a, rows_b)])


# --- THE TWO TABS — the whole dashboard; everything above is just data ---
tab1, tab2 = st.tabs(["⚡ Transmission Map", "📰 Narrative Tracker"])

with tab1:
    st.header("⚡ Transmission Map")
    st.write("One event at a time: what did all 9 assets do after it?")
    choice = st.selectbox("Pick an event", EVENTS)
    num = EVENTS.index(choice) + 1  # which event number she picked

    if num == 2:
        st.subheader("Event 2 — US-Israel strikes on Iran / Hormuz ban")
        st.caption("From your shock-card-02-Iran.md — real numbers, nothing invented.")
        st.markdown(card_table(CARD_2))
    elif num == 3:
        st.subheader("Event 3 — Broadcom tech selloff")
        st.caption("From your shock-card-03-Broadcom.md — real numbers, nothing invented.")
        st.markdown(card_table(CARD_3))
    else:
        st.info("🚧 Card in progress — not finished yet. Its table will appear here once you paste its real numbers into this file.")

    st.divider()  # a thin line separating the two sections
    st.subheader("Side-by-side: Event 2 vs Event 3 (1-day moves)")
    st.write("Same day-one shockwave, two different events — your textbook comparison in one glance.")
    st.markdown(compare_table(CARD_2, CARD_3))

with tab2:
    st.header("📰 Narrative Tracker")
    st.write("The stories investors tell — your 12-label taxonomy, and which story actually ruled the week.")
    st.subheader("Your 12 narrative labels (from taxonomy.md)")
    for n, (name, meaning) in enumerate(LABELS, 1):  # enumerate gives 1, 2, 3... automatically
        st.write(f"**{n}. {name}** — {meaning}")
    st.divider()
    st.subheader("Dominant narrative of the week")
    st.info(f"🗳️ Your call (from your cluster-review-2026-10-15.md):\n\n> {DOMINANT_NARRATIVE}")
    st.divider()
    st.subheader("Weekly scorecard (coming soon)")
    st.write("Future weeks go here: the dominant story vs what prices actually did — "
             "did the story move markets, or was it just noise?")

st.caption("Market Digest Lab — Day 13 skeleton. More cards unlock here as you finish them.")
