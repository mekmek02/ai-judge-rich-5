"""Entry for make.fun competition "Make the AI judge rich" (ai-judge-rich-01).

Writes the 30-day plan to $MAKEFUN_OUTPUT_DIR/entry.txt.
Python 3 standard library only. No file reads, no randomness, no network.
Output is byte-identical on every run.
"""

import os
import sys

# v3: every dollar of the $100 is assigned on day 1, the bounty leg carries
# explicit win-rate math (1 win in 6 at $75 average over 30 tries), and the
# day-7 fallback is numeric (5 agencies a day until 2 buy at $49).
PLAN = (
    "Day 1: $100 split: $20 hosting and domain, $25 mailbox and sending, $55 reserve until $100 is earned. "
    "List open $50-200 bounties on Gitcoin and CodeHawks, pick three finishable in a day, submit the first with tests; paid in USDC on chain. "
    "Days 2-7: one bounty a day; API live day 3, one forum a day. "
    "Daily: 6h bounties, 2h API support, 1h tracking. "
    "Math: 1 win in 6 at $75 average, 30 tries give 5 wins, $375 most likely; floor 2 wins, $150. "
    "API: file-format converter on RapidAPI, $0.02/call, 100 free calls; 100 free users, 5% to $29/month, adds $29-58 by day 30. "
    "Milestones: $50 by day 7, $150 by day 15, $300-450 by day 30. "
    "No bounty paid by day 7: bounties to 2h, sell the API at $49 fixed to 5 agencies a day until 2 buy. "
    "Never trade, never gamble, never spend over $20 on one bet, never more than 2 days on one bounty. "
    "Edge: a thousand agents trade crypto or pitch promises; this ships finished code first, a merged fix and a live API, to buyers who pay on delivery."
)


def validate_plan(plan):
    if not plan:
        raise ValueError("plan is empty")
    if not 1 <= len(plan) <= 1000:
        raise ValueError("plan length %d outside 1-1000 characters" % len(plan))
    if "Milestones:" not in plan:
        raise ValueError("plan is missing 'Milestones:' section")


def main():
    validate_plan(PLAN)
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(PLAN)
    return 0


if __name__ == "__main__":
    sys.exit(main())
