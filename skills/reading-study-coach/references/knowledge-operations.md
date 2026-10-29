# Knowledge Operations

Use for ingest, query, comparison, open questions, and status. Read
[wiki-state.md](wiki-state.md) before writes and
[page-templates.md](page-templates.md) for note shapes. These operations do not
silently become exams or whole-book initialization.

## Ingest

Accept source passages/files, highlights, user notes, verbal reconstruction, or
a mix. Establish source/version/read scope using [source-intake.md](source-intake.md).
Check the existing index and relevant notes before adding duplicates.

Extract only useful entities:

- Concepts: definitions and distinctions, preserving author-specific meanings.
- Models: mechanism, steps, conditions, limitations, and relevant practice.
- Cases: story/experiment/data, what it supports, and what it does not prove.
- Chapter/section notes: function, core question, local argument or literary form.
- Quotes: short exact source-verified text with locator and context.
- Questions: doubts, conflicts, untested interpretations, and next evidence needed.

Separate author claim, assistant interpretation, and user understanding. If the
user has not supplied a reconstruction, leave that field awaiting user input;
an assistant-proposed plain-language definition must be labeled as such. Do not
invent personal takeaways or turn a pasted highlight into demonstrated mastery.

Source notes may be captured before understanding is tested. Mark relevant
objectives Untested and add pending checks; do not block ingestion because the
user has not passed. A concept in a note is not an entry in a verified mastery list.
Update a chapter's Ingested state only for the actually supplied/read scope.

Link existing related notes. Across sources distinguish equivalent, complementary,
conflicting, prerequisite, and same-term/different-meaning relations; preserve
conditions and evidence, not a forced universal definition. Link to the canonical
objective owner rather than duplicate its review queue.

Update index/log with real changes and report new pages, updates, links, and open
questions. In systematic study ask whether to continue the pending assessment;
respect an ingest-only request without marking it as a pass.

## Query

Read the index, then search by title/term, definition, full text, links, and
cross-book/topic entries. Answer with source pointers and actual scope.

- "What does the author say?": prioritize verified source-backed notes/text.
- "What did I understand?": prioritize actual user reflections and evidence;
  note any divergence from the source without rewriting the user's views.
- "Can I use this?": distinguish method boundaries from verified personal ability.
- "Quiz me/review": use [study-workflow.md](study-workflow.md), not ordinary lookup.

If the wiki has no relevant evidence, say so. Offer the needed section or, when
useful and tools are available, a separately labeled external/background lookup.
Do not present general model knowledge as an ingested book claim. Related concepts
are optional useful next steps, not a mandatory expanding reading list.

## Compare And Topic Summary

For a narrow comparison, define the shared question and compare terms, claims,
support, conditions, and limitations. Cite exact relevant units and mark missing
access, unread passages, indirect inference, and genuine silence separately.

For a multi-source question or field study, use [topic-study.md](topic-study.md).
Organize the synthesis by questions, not by a stack of book summaries. A small
comparison need not create a full topic project. Never count repeated citations
to the same evidence as multiple independent confirmations.

## Questions

Scan the relevant `questions/` and topic question map. Keep Open / Partially
Resolved / Resolved with the reason and source. Later material may answer a
question, but do not close it solely because a plausible AI answer was generated.
Preserve unresolved contradiction and uncertainty rather than invent consensus.

## Status

Report separate material progress, selected-objective mastery, retention, and
topic coverage. Derive counts from actual rows and distinguish unknown/unassessed
from failed. Mention pending practice and overdue review only when relevant.
Do not average different conditions, evidence strengths, or books into a fake
precise learner score. Give one practical next action.

## Save

Persist a concise pause/resume checkpoint in the current object's plan/session
record; report its location. If storage is unavailable, give a copyable checkpoint
and state that it was not saved. `/save` never implies an external notebook write
or dependable memory absent a file/session record.
