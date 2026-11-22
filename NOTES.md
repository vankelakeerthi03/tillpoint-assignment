# NOTES

## 1. Report

**Status:** partly fixed

**What I saw:** Duplicate webhook deliveries with the same event ID could be recorded more than once. Also, separate successful payments for the same order could cause the total amount received to exceed the order total.

**Root cause:** The payment handling logic did not prevent duplicate webhook events from being recorded. It also did not identify or flag amounts received beyond the order total. Provider payout reconciliation is not supported by the current payment data.

**Fix and why:** Added duplicate event detection so the same webhook event is processed only once. Added overpayment tracking so any amount received beyond the order total is marked as requiring a refund. Provider payout reconciliation remains outside the implemented scope because settlement and fee information is not available.

**How I verified it:** Added automated tests for duplicate webhook events and separate successful payments. Verified that duplicate events are ignored and excess payment amounts are flagged for refund.

**Commits:** `9f874a3`, `4a0a1fc`

## 2. Report

**Status:** fixed

**What I saw:** Cancelling a pending order did not restore the reserved product stock.

**Root cause:** The cancellation logic released stock only for paid orders and did not handle pending orders.

**Fix and why:** Updated the cancellation logic to release reserved stock for both pending and paid orders. This ensures that cancelled orders do not leave stock unnecessarily reserved.

**How I verified it:** Added a regression test that creates and cancels a pending order, then checks that the reserved stock is restored. The test passes.

**Commits:** `66176ac`

## 3. Report

**Status:** fixed

**What I saw:** The tax amount was calculated using the original price instead of the price after applying the coupon discount.

**Root cause:** The tax calculation happened before the coupon discount was applied.

**Fix and why:** Updated the pricing calculation to apply the coupon discount before calculating tax. This ensures that tax is calculated on the discounted amount.

**How I verified it:** Added a regression test to verify that the coupon reduces the taxable amount and produces the expected tax. The test passes.

**Commits:** `e6f6cad`

## 4. Report

**Status:** fixed

**What I saw:** Sales made around midnight in India could appear under the previous day's report.

**Root cause:** The UTC offset was applied in the wrong direction when calculating the UTC boundaries of a shop-local day.

**Fix and why:** Updated the day-boundary calculation to subtract the UTC offset when converting local-day boundaries to UTC. This correctly handles shops using UTC+5:30.

**How I verified it:** Added a regression test using a payment timestamp of 19:00 UTC, which corresponds to 00:30 the following day in India. Verified that the sale appears in the correct day's report.

**Commits:** `a79da39`

## 5. Report

**Status:** fixed

**What I saw:** Two catalog instances could use stale stock information and both attempt to reserve more units than were available.

**Root cause:** Stock availability was checked separately from the stock update. This allowed concurrent operations to use outdated stock values.

**Fix and why:** Replaced the separate check and update with a conditional SQL UPDATE that decreases stock only when sufficient stock is available. This makes the reservation operation atomic and prevents stock from becoming negative.

**How I verified it:** Added a regression test using two catalog instances with stale cached stock. After the first instance reserves seven units, the second reservation of seven units fails, and the remaining database stock stays at three.

**Commits:** `4d11668`

## 6. Open question

**My decision:** Record both distinct successful payments, but flag the excess amount as requiring a refund. Ignore repeated deliveries of the same webhook event.

**Why:** Two different successful payment events represent separate payment captures, not necessarily a retry. Keeping both records preserves the payment history, while flagging the excess amount makes the issue visible for follow-up.

**What it costs:** The system does not automatically issue refunds. A separate refund process or manual follow-up is required. Until a refund is completed, reports of received payments continue to include the actual captured amounts.

**What I built:** Added a `refund_required_cents` column to the payments table. The payment handler calculates and records the excess amount for each payment. Also added a database migration so existing databases receive the new column.

**How I verified it:** Added a test that sends two distinct successful payment events for the same order. Verified that both payments are stored, the first payment has no refund amount, and the second payment is flagged for the excess amount. Ran the full test suite successfully.

**Commits:** `4a0a1fc`, `36d278a`

## Other things I noticed

Added a database schema migration for the new `refund_required_cents` column to support existing databases. No other unrelated issues were identified.

## Session logs

AI tool used: ChatGPT (OpenAI) for understanding the reported issues, discussing implementation choices, debugging, and reviewing test results.

- `README.md` — Contains the assignment-provided instructions for session logs. It is not a conversation export.

## Terminal commands and results

- `python3 -m unittest -v` — All 13 tests passed.
- `git status --short` — Checked working tree status.
- `git log --oneline -9` — Reviewed commit history.
- `grep -n "TODO" NOTES.md` — Checked for TODO placeholders.
- `ls -lh session_logs` — Checked saved session log files.
- `git add` and `git commit` — Saved assessment changes.
- `zip -r tillpoint_assignment.zip ...` — Created submission ZIP.
- `unzip -l tillpoint_assignment.zip` — Checked ZIP contents.
