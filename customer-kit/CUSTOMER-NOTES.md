# Our simulated customer agreement

This is fictional customer practice, not a real client interview. One file per
team. Replace Pending only after a real team decision or observed result.

- Team members / shared repository: Aarav Chopra (ac2928) and Nandish; https://github.com/ac2928/bench-and-bolt
- Selected scenario file and customer: `scenarios/repair-shop.md`, Maya Chen, Bench & Bolt (bike repair).
- Current stage / next conversation: Review 1 Plan done. Next conversation: change request after the first slice works.
- Authoritative spec link: [SPEC.md](../SPEC.md)
- Protected finishing week starts: Pending; check the section schedule.

## Discovery and scope

- Customer need / intended user: Repair requests arrive on scraps of paper and in messages. Maya needs one queue so staff can review each request and give an honest status. User: the shop coordinator (staff).
- Two scope options compared: A, Staff intake (coordinator enters walk-in requests, sees the queue, updates status) vs B, Rider intake (public rider form + receipt + coordinator queue, needs a permission boundary).
- Selected option and our reason / tradeoff: **A, Staff intake.** Reason: better if staff handle entry, to avoid customer confusion; staff catch mistakes at the counter. Tradeoff: riders cannot submit or check status online yet.
- Three to five agreed stories and checks: 4 stories (Enter a request, See the queue, Make a decision, Give an honest answer). Full checks in [SPEC.md](../SPEC.md).
- Status names, allowed transitions and what each status promises:
  - New requests start as **Pending review**.
  - Pending review → **Accepted** or **Declined**.
  - Accepted → **Completed**.
  - Completed and Declined are final (no changes).
  - Pending review → Completed is rejected.
  - Accepted means "we'll take the job." It does not book a time or charge money.
- Data fields: generated request ID; synthetic rider label (e.g. "Rider 12"); bike type (city / road / other); problem (required, 1–240 non-blank characters); preferred day (optional, ≤40 characters, a wish, never shown as confirmed); status; creation order (oldest first). Records must survive app restart.
- Deferred features / synthetic-data boundary: No public rider form (Option B), no real names/phones/emails/addresses, no prices/quotes/payments, no appointment booking, no parts inventory, no messaging. All data is fake practice data.
- Assumptions explicitly agreed, with who agreed: Fields, status rules, 4 stories, and deferred list agreed by Aarav with simulated customer on 2026-11-11; Nandish to confirm.
- Open questions: None yet.
- Design/development/QA owners and cross-reviewers: Aarav = Member A (intake form, validation, tests; reviews Nandish). Nandish = Member B (queue, status/history, persistence, tests; reviews Aarav). See [SPEC.md](../SPEC.md).

## Change request: Not introduced

- First working slice and actual check links: Not yet evidenced.
- Change introduced / team impact estimate: Pending.
- Implement / defer decision and reason: Pending.
- Customer's simulated scope agreement: Pending.
- Actual implementation / check evidence: Not yet evidenced.

## Final acceptance: Pending

- Chosen revision / reproducible setup: Pending.
- Happy path, rejected action and restart evidence: Not yet evidenced.
- Simulated customer's acceptance / remaining gaps: Pending.
- Real peer issue, meaningful change and retest: Not yet evidenced; AI is not a peer.
- Each member's actual contribution and AI/starter help: Pending.

Keep proposed, agreed, implemented and checked distinct. A recorded agreement
is not a passing test. A passing test is not evidence of a real human review.