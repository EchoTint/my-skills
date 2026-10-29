# Study Workflow

Use this workflow for systematic study and targeted drill. Reading-only support
can stop at guidance, explanation, or ingest without requiring a test. Follow
the user's language in conversation. Keep the learner's goal, not the source
category alone, in control of the chosen mode.

Read [wiki-state.md](wiki-state.md) for storage, ownership, canonical goal IDs,
mode state, evidence, and review history. It is the authoritative schema; do not
create a parallel progress system. Read [pedagogy.md](pedagogy.md) when designing
questions or scoring, and [practice-loop.md](practice-loop.md) for application
and remediation.

## 0. Open or Restore

Check existing state before initializing anything. For legacy wiki compatibility,
a book keeps its existing `book-wiki/<book-slug>/` directory. Paper/article and
topic owners use the paths defined in the shared schema. Each study owner has
`study-plan.md` and `mastery-map.md`; preserve existing notes and progress. This
skill is self-contained and does not require any predecessor skill to be installed.

For a new owner, establish these four fields interactively, one at a time. Do
not repeat a question whose answer the user has already supplied:

1. Goal: Why read this? What problem or ability should the study address?
2. Material: Physical book, ebook, PDF, article, paper, notes, or other source?
   What content and edition/version are actually available?
3. Background: Beginner, some background, or experienced? What related work
   has the learner already done?
4. Time: Rough completion timeline and realistic time available per session?

Automatic source classification can suggest a mode, but must not erase this
initialization in strong study. Do not infer the learner's purpose from a title.
If the user wants only an overview, do not make a full study interview a barrier
to answering; retain missing fields for a later switch to study.

Create or update metadata, the plan, and the mastery map using the shared
schema. Use the available source to identify chapters or equivalent learning
units and their core questions. If only part of the source is available, make a
partial plan and identify the missing coverage. Do not invent a table of
contents, quotations, findings, or chapter-specific tests from a title alone.

### Plan By Ability And Dependencies, Not Chapter Number

Use [adaptive-routing.md](adaptive-routing.md) before selecting the first study
unit, even when the entire request was only "learn this book", and when responding
to a practice request. This is automatic, not contingent on the user asking to
reorder. Assess whether the book's order is
actually necessary. Locate the desired ability, inspect its real prerequisites,
and reuse valid learner evidence. Choose goal-first, minimal-bridge, interleaved,
project-first, diagnostic-first, or dependency-ordered work as appropriate; keep
the source order when it has a useful reason, not merely because it is printed.
For a whole-book goal, map the core abilities and intended coverage before
choosing the order. Do not silently replace that goal with a single task, and
do not force the learner to invent a project in order to get a non-linear route.

Keep the source chapter list for coverage and locators, and a separate learning
route in the same plan. Units may be sections or tasks drawing on several
chapters. Explain the choice briefly, then start without requiring approval of
each local reorder. Missing earlier reading is not automatically a missing skill;
unknown prerequisites require a scoped probe or source inspection, not a guessed
dependency chain. Respect explicit user order and genuine cumulative dependencies.

### Restoration priority

On return, or a switch into study/drill:

1. Read the owner's plan, mastery map, saved mode, and pending actions.
2. Resolve shared goals by canonical ID; check their evidence and due dates.
3. In strong study, review due knowledge before advancing to new content.
   Prioritize overdue items and weak prerequisites; use a bounded review batch
   rather than an exhausting backlog. See the review protocol in pedagogy.
4. Resume the pending repair, independent retest, practice, or next ready task
   in the saved learning route, not automatically the next chapter number.
   Reassess only the affected route when goal, source, or performance changes.
5. Briefly state the current position and the recommended next action.

Do not rerun initialization on every return. A user-requested mode switch or
review deferral is allowed: preserve outstanding tests, practice, and due dates,
and do not count the skipped work as passed. A failed prerequisite needs repair
before a dependent task can be declared mastered.

## 1. Before Each Chapter or Learning Unit

Select or confirm the next ready unit against the goal, dependency evidence,
and saved learning route. A later chapter or cross-chapter task can be next;
do not select chapter 1 solely because it is unread. For a selected reading
unit, design 2-3 concrete pre-reading questions. Use the same approach for a
paper section or topic unit when appropriate:

- Tie one question to the learner's original goal or real situation.
- Activate a relevant prior concept, without pretending it is mastered if the
  record does not support that claim.
- Ask for an expectation, prediction, or choice to compare with the source.

These are warm-ups, not formal mastery scores. Present a manageable amount at
once; the learner may take the questions into their reading. Set the unit to
`Guided`, then `Reading` when they begin.

An immediate practice request may instead start with a diagnostic/coached task
from [practice-loop.md](practice-loop.md). Do not require all associated chapters
to be read or passed first. The task can expose the smallest missing prerequisite;
this does not waive the independent test and Practice gates for formal mastery.

### Beginner and prerequisite rescue

An unread topic is not a failed recall test. Check only the prerequisites needed
for this unit with a short concrete probe. If a prerequisite is missing, teach a
minimal explanation or worked example, let the learner reason through a smaller
case, and return to the unit. Do not recursively launch a complete prerequisite
course. Distinguish lack of prior exposure from a misconception or an application
gap. Assisted success prepares the learner; it does not prove independent
mastery of the prerequisite.

## 2. Read and Ingest

Accept source text, highlights, notes, a file, or the learner's verbal summary.
Compile the available content using [page-templates.md](page-templates.md).
Preserve source locations and distinguish the author's account, the learner's
interpretation, and the assistant's explanation.

- Extract relevant concepts, models, cases, quotes, and open questions.
- Leave personal understanding/takeaway sections unfilled when the learner has
  not provided them; never turn AI prose into a purported learner answer.
- Identify a small set of meaningful learning goals for this unit. Check for
  existing canonical goals before adding duplicates across sources.
- Mark the chapter/unit `Ingested` and newly added goals `Untested`.
- Existing valid mastery evidence is not erased by another source mentioning
  the same goal. A genuinely different scope needs its own goal or a recorded
  extension, not an automatic inherited pass.
- Update the owner, index, cross-references, and operation log as specified in
  the shared schema. Report what was compiled and ask whether to test now.

Ingest is not mastery. If the learner declines testing, keep the work compiled
and pending. Open questions can be answered before any formal assessment.

## 2b. Reconstruct And Correct Before The Test

In strong study, do not jump from AI compilation of raw source text to a claim
of understanding. Collect the learner's own reconstruction before showing a
detailed AI synthesis when feasible: ask 1-2 prompts about the core problem or
mechanism, a new example, or a relevant boundary. Reuse an actual reconstruction
already supplied instead of demanding it again. Raw passages and copied highlights
are not the learner's reconstruction.

Diagnose what is correct, vague, unsupported, or mistaken. Repair only the actual
gap using [practice-loop.md](practice-loop.md), then have the learner explain
what changed in their own words. For an unread topic or missing prerequisite,
provide the minimum teaching first. This is coaching, not a scored independent
pass. Use a new equivalent task for the subsequent formal test.

An ingest-only or reading-only request leaves this phase pending without an exam.
If the learner explicitly requests an immediate independent exam, let that
attempt supply the initial reconstruction and provide correction after the
attempt; do not pre-reveal its answers in a compulsory coaching phase.

## 3. Independent Mastery Test

Select the required goals from the mastery map and define coverage before
scoring. Every required goal must have relevant evidence; do not select only the
easiest definitions. Assess explanation, a novel application, and a distinction
or boundary as well as factual accuracy.

1. Ask 1-2 questions per round and wait for the learner's response. Use the
   formal-test and scoring rules in pedagogy.
2. Every 3-4 questions, naturally mix an appropriate old concept with the
   current one. If that part fails, record the old goal's review need separately.
3. Obtain the learner's confidence self-assessment before revealing the score
   or answer. Record specific evidence for each rubric point.
4. Require at least 3/4 on every scored question AND at least 80% overall. All
   required goals must be covered and critical misconceptions/misuses resolved.
5. A passing test proceeds to required Practice. It does not yet set `Mastered`.
6. A failing or assisted attempt goes to targeted repair and a new independent
   equivalent check; preserve the failed attempt in the history.

Teaching and assessment have different rules. Outside a formal test, explain,
use hints, answer questions, and demonstrate when useful. If the learner needs
content help during a formal question, pause the independent attempt and switch
to teaching. Correctness after the hint is useful progress, not an independent
pass. After repair, ask for the learner's own restatement, then use a new
equivalent problem rather than scoring their repetition of the supplied answer.

Do not advance a goal through an unresolved critical error merely because the
batch average is high. Do not delete low-scoring attempts or invent evidence to
make the gate pass. A retest may focus on weak goals while retaining still-valid
independent evidence for the others; the decision must identify the complete
coverage and the explicit set of questions used for its score.

## 3b. Required Practice

After the independent test passes, use the practice loop to have the learner
produce something in a new context. A default task is small, about 2-5 minutes,
and connected to the initial goal. State success criteria before the task and
evaluate the learner's output against them.

- Pass: only now mark the supported goals `Mastered`; set the initial next
  review to 1 day after the qualifying completion.
- Fail: diagnose the conceptual, procedural, or transfer gap; repair it and
  retry with a suitable new task. Return to independent testing if the failure
  reveals that its evidence is no longer valid.
- No output or unverifiable completion: keep practice pending/unverified.
- AI-completed work or copied solutions: do not count as the learner's ability.

An integrated artifact can cover several goals only when its evidence actually
supports each of them. Do not infer chapter mastery from one unrelated success.
Record the test and practice evidence using the shared schema. Retention and
proficiency are separate dimensions: one qualifying `Mastered` result does not
establish permanent memory, automaticity, or an internalized highest level.

## 4. Review and Continue

Use the exact interval sequence in pedagogy: 1, 3, 7, 14, 30, then 60 days, with
subsequent successes staying at 60 days. A failure restarts at 1 day. Persist
`review_step`, the attempt history, and the next date; do not reconstruct the
step from the most recent date alone.

Review requires independent retrieval, not rereading or recognizing an answer.
After a bounded review batch, retain any unresolved or unreviewed items as
pending. Do not fabricate background reminders or autonomous future activity;
record the next review and check it on the next session. If the learner chooses
to pause or read without testing, maintain that state without lowering standards.

Use feedback to decide the next action: a missing prerequisite calls for a
small rescue, a misconception for a counterexample and repair, a transfer gap
for another application, and successful evidence for the next relevant ready
task. Revise the learning route from demonstrated gaps or strengths, not by
incrementing the current chapter number. Preserve deferred work and review dates.

## 5. Completion and Recovery

A strong-study plan is mastered only when all required planned goals have
qualified test and Practice passes. Distinguish finishing the reading from
finishing the study; deliberately unstudied units remain visible. Summarize:

- The source's central question and its answer, qualified by available evidence.
- The most useful concepts/models, normally up to five.
- What the learner can now do toward their original goal and what remains open.
- Supported connections or disagreements with other studied sources.
- The remaining review plan; completion does not cancel spaced review.

Update completion metadata using the shared schema. For a book, optionally offer
to help the learner write a review in their own words.

When fatigue or repeated failure appears, reduce the number of goals, shorten
the task, teach differently, or pause. Never reduce the pass threshold to close
the session. Save the current position, unresolved gap, and the smallest next
action so the learner can resume without repeating the whole session.
