# Bench & Bolt Repair Queue: Project Record

## Project & status

- **Team:** Aarav Chopra (ac2928), Nandish (Denandis)
- **Repo:** https://github.com/ac2928/bench-and-bolt
- **Customer (simulated):** Maya Chen, Bench & Bolt bike repair, from `customer-kit/scenarios/repair-shop.md`
- **Customer agreement:** [customer-kit/CUSTOMER-NOTES.md](customer-kit/CUSTOMER-NOTES.md)
- **Status:** Review 1 (Plan) complete. Nothing built yet.
- All customer names, data and quotes are fictional. All records are synthetic.

---

## 1 Plan

### Customer need
Repair requests arrive on scraps of paper and in messages. Maya needs one queue so staff can review a request and give an honest status.

### Two scope options compared
| | A · Staff intake | B · Rider intake |
|---|---|---|
| Who enters requests | Shop coordinator | Riders, through a public form |
| What's built | Intake form + queue + status updates | Public form + rider receipt + coordinator queue |
| Extra risk | Small | Needs a permission boundary so riders can't change status |

**Chosen: A, Staff intake.** Reason: better if staff handle entry, to avoid customer confusion; staff catch mistakes at the counter.
**Tradeoff:** riders can't submit or check status online yet.

### Stories and checks
| # | Story | Success check | Failure check |
|---|---|---|---|
| 1 | **Enter a request.** As the coordinator, I enter a walk-in request. | A valid request is saved with status Pending review. | Blank problem, bike type not city/road/other, or overlong text creates **no** record and shows a clear error. Preferred day is never shown as "confirmed." |
| 2 | **See the queue.** As the coordinator, I see all requests, oldest first. | Queue shows the exact values entered. | After the app is restarted, the requests are still there. |
| 3 | **Make a decision.** As the coordinator, I accept, decline or complete a request. | Allowed moves work and the queue updates. | Completing a Pending request is rejected. Changing a Completed or Declined request is rejected. |
| 4 | **Give an honest answer.** As the coordinator, I open one request to tell a rider where it stands. | Detail page shows the same status as the queue and a clear next step. | Page never says "booked" or "paid." |

### Data
| Field | Rule |
|---|---|
| id | Generated automatically |
| rider_label | Synthetic label only, e.g. "Rider 12" |
| bike_type | `city`, `road` or `other` |
| problem | Required, 1–240 non-blank characters |
| preferred_day | Optional, ≤ 40 characters; a wish, not a booking |
| status | See status rules |
| created_order | Used to sort oldest first |

### Status rules
```
Pending review ──► Accepted ──► Completed (final)
       │
       └────────► Declined (final)
```
- Pending review → Completed is **rejected**.
- Accepted means "we'll take the job." It does **not** book a time or charge money.

### Out of scope (deferred)
Public rider form (Option B), real names/phones/emails/addresses, prices/quotes/payments, appointment booking, parts inventory, messaging.

### Architecture sketch
```
Browser (coordinator)
   │
Flask app (app.py: routes / pages)
   │
validation.py: checks a new request (Aarav)
status.py: allowed status changes (Nandish)
db.py: saves and loads requests (Nandish)
   │
SQLite database (requests table), so data survives restart
```
Stack: Python 3.12, Flask, SQLite, pytest, Playwright for browser checks. Same tools as the course labs. Each member works in separate files to avoid merge conflicts.

### Who does what
| | Aarav (Member A) | Nandish (Member B) |
|---|---|---|
| Design | Intake form page and error messages | Queue page and request detail page |
| Development | Project setup, form route, `validation.py` (Story 1) | `db.py`, `status.py`, queue + detail + status routes (Stories 2–4) |
| QA | `tests/test_validation.py`: valid and invalid input | `tests/test_status.py` + restart persistence test |
| Cross-review | Reviews Nandish's pull requests | Reviews Aarav's pull requests |

### Task checklist: First slice (due Thu Nov 19)

**Aarav (Member A)**
- [ ] Set up the project: `app.py`, `requirements.txt`, `tests/` folder, GitHub Actions running pytest
- [ ] Branch `aarav/intake`
- [ ] `validation.py`: reject blank problem, problem over 240 characters, bike type not city/road/other, preferred day over 40 characters
- [ ] Intake form page `/new` that shows clear errors and saves nothing when input is invalid
- [ ] `tests/test_validation.py`: one passing test and one failing-input test per rule
- [ ] Open a pull request and ask Nandish to review
- [ ] Review Nandish's pull request

**Nandish (Member B)**
- [ ] Accept the GitHub collaborator invite and clone the repo
- [ ] Read this SPEC and `customer-kit/CUSTOMER-NOTES.md`, then comment "approved" (or suggest changes) on the plan issue
- [ ] Branch `nandish/queue`
- [ ] `db.py`: create the SQLite `requests` table with the fields above; functions to save one request and list all requests oldest first
- [ ] `status.py`: one function that says whether a status change is allowed (Pending review → Accepted/Declined, Accepted → Completed; everything else rejected)
- [ ] Queue page `/queue` showing all requests oldest first
- [ ] Detail page `/requests/<id>` showing status and next step (never "booked" or "paid")
- [ ] Accept / Decline / Complete buttons that use `status.py` and reject illegal changes
- [ ] `tests/test_status.py`: every allowed and rejected change; a test that data is still there after restarting the app
- [ ] Open a pull request and ask Aarav to review
- [ ] Review Aarav's pull request

### Help received
- Customer kit and scenario from the instructor.
- AI (Claude) role-played the simulated customer and helped draft this plan. Simulated customer agreement is **not** peer review.
- Plan drafted by Aarav with Nandish's agreement (he was at work); Nandish to confirm on GitHub.

---

## 2 First slice
Pending.

## 3 Integrated
Pending.

## 4 Improve & hand off
Pending.
