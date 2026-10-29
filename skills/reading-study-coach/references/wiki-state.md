# Unified Wiki State And Compatibility

Use before creating/updating study records or restoring a session. This skill
shares the user's established `book-wiki/` format without requiring the old skill.

## Inspect Before Writing

Find the actual workspace/project root and existing index. Respect a confirmed
custom location. Read relevant files before edits; preserve user notes and unknown
fields. Do not regenerate a whole wiki, migrate every old book, or erase history.
Add compatible fields when needed. Prefer a small Markdown record over a database.

Starting systematic study, asking to ingest/save, or maintaining a previously
authorized study object supports local state updates. Do not initialize a wiki
for a one-off summary. Ask before another destination or external write/upload.
Only report writes that succeeded. Keep private project details out of shared
templates; no hidden learner profiling or full conversation dumps.

## Layout

```text
book-wiki/
  index.md
  log.md                         # Append-only operation summaries
  <book-slug>/                   # Existing book layout stays valid
    meta.md
    study-plan.md
    mastery-map.md
    chapters/ concepts/ cases/ models/ quotes/ questions/
    evidence/ practice/ sessions/ # Create only when actually used
  sources/<source-slug>/         # Papers/articles, same base record structure
  topics/<topic-slug>/
    meta.md
    study-plan.md
    mastery-map.md
    question-map.md
    source-map.md
    evidence/ practice/ sessions/ # Only as needed
  cross-book/
    concepts/
    comparisons/
```

Use lowercase hyphenated slugs. Match identity, not just slug similarity; use an
author/year/edition suffix when collisions matter. Never silently merge same-titled
works. References must resolve relative to the wiki or actual note, not be assumed
Obsidian-compatible because they begin with `/`. Prefer correct relative Markdown
links; retain existing valid wiki links and conventions without mass conversion.

## One Object, Three Different Records

1. Material progress: what is accessible, actually read, skipped, or ingested.
2. Understanding/performance: what the user independently demonstrated and with
   which source-backed assessment/practice evidence.
3. Retention/transfer: delayed review results and repeated cross-context use.

Do not turn reading percentage into a mastery percentage. `Mastered` means the
strict test and required practice passed, not automatic long-term internalization.
Book read-through, a selected study plan completed, topic overview completed,
and mastery of all selected objectives are distinct outcomes.

## Metadata And Plan

Keep the existing headings/fields; add these only as needed:

```yaml
object_id: "book:confirmed-slug"
kind: book
title: "Title"
authors: []
edition_or_revision: "unknown"
source_refs: []
identity_status: provisional
access: partial
read_scope: "Actually inspected units"
classification: {primary: technical, secondary: [], confidence: low, basis: "Observed metadata"}
gaps: []
status: in-progress
goal: "User's problem and the ability this plan should produce"
success_criteria: []
time_budget: "User-confirmed or unspecified"
source_position: "Saved source-reading cursor, independent of practice, or unknown"
current_unit: "Active section/question/task, possibly cross-chapter"
learning_route_ref: "study-plan.md#learning-route"
session_mode: study
paused_reason: ""
next_action: "One concrete action"
linked_topics: []
```

`study-plan.md` retains the original chapter table and statuses (Not Started,
Guided, Reading, Ingested, Mastered, Needs Review). For papers/topics, rows are
sections or shared questions. Include selected objectives and dependencies;
source ingestion sets relevant new objectives to Untested, never to Mastered.
Do not invent total chapters or populate unread chapters with guessed claims.

### Learning Route Versus Source Order

Keep the original chapter identifiers/coverage table; it describes the source,
not a mandatory study queue. Add a small `Learning Route` section in the same
plan when study/practice is planned. Its rows can use:

```text
Step | Objective/Task | Source Unit(s) | Prerequisites And Evidence |
Decision (ready/bridge/unknown/deferred) | Reason | Next Action
```

Record only useful dependencies, selected order, inserted repairs, and deferred
material. Use [adaptive-routing.md](adaptive-routing.md). Keep route decisions
separate from assessment outcomes: readiness to try is not `Mastered`, and a
bypassed chapter is neither read nor passed. A completed selected route does
not imply the whole book was finished. Do not rewrite source order to match the
route or create another mastery map/review queue for each arrangement.

`current_unit` follows the active task; `source_position` preserves the saved
reading cursor when a drill visits another unit. Record newly inspected fragments
in `read_scope`; update the reading cursor when actually advancing that reading
route. During study/practice these may differ. Legacy plans
without a route may gain one when needed; an old Current Chapter is not proof
of which earlier units were read or mastered.

## Canonical Objective Ownership

Each assessed knowledge/skill objective has a stable ID and one authoritative
owner row in one `mastery-map.md`. Other books/topics reference that row and its
evidence; they do not duplicate the review schedule. Keep context-specific
objectives separate even when terms match. Existing book-owned rows remain valid;
adding a topic does not silently transfer or reset their history.

Suggested row fields, compatible with the old table:

```text
Objective ID | Concept/Skill | Chapter/Question | Status | Last Tested |
Next Review | Review Step | Evidence | Practice Evidence | Retention | Transfer
```

Keep these statuses distinct: Untested, Learning, Test Passed / Practice Pending,
Mastered, Needs Review. Maintain Reading/Paused in the plan, not as substitutes
for objective evidence. Retention can be not-yet-reviewed / delayed-pass / weak;
transfer can be untested / one-context / repeated-contexts. Do not give a precise
mastery probability or a global learner label from one session.

## Assessment And Practice Evidence

Store an evidence entry only when a meaningful assessment/practice happened.
Reuse an existing evidence section if sufficient; separate files are optional.

```yaml
evidence_id: "YYYY-MM-DD-objective-attempt-1"
objective_id: "owner-id/objective-slug"
date: "User-local date"
source_refs: []
question_or_task: "Actual prompt"
conditions: {book_access: closed, hints_used: false, equivalent_new_task: true}
user_output: "User's actual response or artifact reference"
score: "Actual earned points / assessed total, or not assessed"
score_basis: "Evidence for each rubric criterion; key unresolved error"
practice_result: "not-started / pending / verified-pass / fail / self-reported"
verification: "Observed tests/results or limitation"
outcome: "Learning / Test Passed / Mastered / Needs Review"
next_action: "Repair, practice, or review"
```

Do not record an assistant answer as the user's reconstruction. Hint-assisted
repair remains a learning entry; independent new-task evidence is required for
passing. A source correction/version change can invalidate affected notes or
tests; flag those objectives for targeted revalidation, preserving past records.

## Deterministic Review State

Intervals are `[1, 3, 7, 14, 30, 60]` days. Store `review_step` as the index of
the interval currently scheduled, plus actual attempts in history.

- Initial test + practice pass: `Mastered`, step 0, next review = today + 1 day.
- Successful independent delayed review: step = min(step + 1, 5), next review =
  actual successful review date + intervals[step]. At step 5 repeat 60 days.
- Failed review: `Needs Review`, step 0, next review = today + 1 day. Repair and
  independently recheck affected objectives; do not erase earlier passes/failures.
- Missing an appointment is not evidence of failure. Keep the item overdue until
  reviewed or explicitly rescheduled; never auto-advance the step by elapsed time.

Use the user's timezone/current date. Legacy rows without a step keep their due
date; infer the step only from reliable history, otherwise label it unknown and
use a conservative 1-day schedule after the next actual assessment. In resumed
strong study, handle due objectives first. Batch by dependencies/importance/time,
retain the rest as overdue, and do not schedule a notification automatically.

## Pause And Resume

Save: object identity/version, current goal and task, learning route and its
rationale, actual source position, completed work, unproven objectives,
due/deferred work, reason for stopping, and one smallest next action.
On return read plan, mastery map, and relevant evidence; briefly check meaningful
goal/version changes or forgotten prerequisites. Resume the affected unit/review,
not the entire interview or the next chapter number by default. A paper or topic
can return to an originating book's saved location. Preserve pending work when
the user requests a different mode.

## Index And Log

Update index entries for books, sources, and topics without inventing statistics.
Append date, operation, input scope, pages created/updated, objective/evidence
changes, new links/questions, and next action to `log.md`. Corrections use a new
entry rather than rewriting history. Store verified learning deltas, not every
turn or speculative personality traits.
