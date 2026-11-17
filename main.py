"""Rencana 30 hari: ubah $100 awal jadi $300-450 lewat bounty dan API.

Cara kerjanya: setiap hari kerjakan bounty yang bisa selesai dalam sehari,
kirim kode yang sudah dites dan dibayar USDC on chain, sambil menjalankan
satu API kecil berbayar. Tidak ada trading, tidak ada judi, tidak ada
pengeluaran besar untuk satu taruhan.
"""

import os

# Trigger fallback hari ke-7: kalau sampai hari ke-7 belum ada satu pun
# bounty yang dibayar, bounty dipangkas jadi 2 jam per hari dan waktu yang
# tersisa dipakai menjual API seharga $49 tetap ke 5 agensi per hari,
# sampai 2 agensi membeli. Jadi rencana tidak mandek menunggu bounty.
PLAN = "Day 1: $100 split: $20 hosting and domain, $25 mailbox and sending, $55 reserve until $100 is earned. List open $50-200 bounties on Gitcoin and CodeHawks, pick three finishable in a day, submit the first with tests; paid in USDC on chain. Days 2-7: one bounty a day; API live day 3, one forum a day. Daily: 6h bounties, 2h API support, 1h tracking. Math: 1 win in 6 at $75 average, 30 tries give 5 wins, $375 most likely; floor 2 wins, $150. API: file-format converter on RapidAPI, $0.02/call, 100 free calls; 100 free users, 5% to $29/month, adds $29-58 by day 30. Milestones: $50 by day 7, $150 by day 15, $300-450 by day 30. No bounty paid by day 7: bounties to 2h, sell the API at $49 fixed to 5 agencies a day until 2 buy. Never trade, never gamble, never spend over $20 on one bet, never more than 2 days on one bounty. Edge: a thousand agents trade crypto or pitch promises; this ships finished code first, a merged fix and a live API, to buyers who pay on delivery."


def check_plan(text):
    """Pastikan rencana layak dipakai sebelum ditulis ke output."""
    if not text:
        raise ValueError("PLAN must not be empty")
    if not 1 <= len(text) <= 1000:
        raise ValueError("PLAN must be between 1 and 1000 characters")
    if "Milestones:" not in text:
        raise ValueError("PLAN must contain 'Milestones:'")
    return text


def output_file():
    """Tentukan lokasi entry.txt dari environment, default /output."""
    base = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    return os.path.join(base, "entry.txt")


def main():
    """Validasi PLAN lalu tulis ke entry.txt."""
    plan = check_plan(PLAN)
    target = output_file()
    folder = os.path.dirname(target)
    if folder:
        os.makedirs(folder, exist_ok=True)
    with open(target, "w", encoding="utf-8") as handle:
        handle.write(plan)


if __name__ == "__main__":
    main()
