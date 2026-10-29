# Adaptive Learning And Practice Routes

Use when planning study, choosing a next unit, or responding to practice/drill.
This is the default first-plan step for "learn this book", not an optional mode
that requires the learner to ask for exercises, a project, or reordered chapters.
Chapter order is a navigation aid, not a mandatory learning sequence. Evaluate
whether it serves the learner's goal before using it. Keep a useful source order;
do not reorder for novelty. Apply [study-workflow.md](study-workflow.md) to the
selected objectives and [practice-loop.md](practice-loop.md) to the exercises.

## Choose The Next Useful Task

For initial whole-book study, first inspect the structure and relevant passages
to map core abilities, supporting/background material, and actual dependencies.
Distinguish cumulative, modular, and mixed organization; use that evidence to
choose an entry point and route rather than copying the contents into a queue.
A broad book-learning goal may remain broad: keep its intended coverage visible
while choosing a useful order, instead of demanding an unrelated real project or
silently shrinking the plan to one convenient later chapter.

1. Restore the confirmed goal, pending work, available time, and valid evidence.
   Do not restart the interview or silently replace a chosen study goal.
   A narrower session drill can coexist with the long-term plan; defer rather
   than delete its unrelated objectives.
2. Translate the goal into an observable task or ability and locate its relevant
   source units; these may be later sections or fragments from several chapters.
   With no concrete practice target, ask one key question about the desired
   ability, or offer a small, clearly labeled diagnostic task to discover a gap.
   Do not ask the learner to select an internal teaching method.
3. Inspect the dependencies actually needed for that task. Distinguish required
   prerequisites, useful context, independent material, and unknown dependencies.
4. Reuse applicable evidence. Valid independent performance can avoid repeated
   teaching/testing of the same scope. Check conditions, version, and relevant
   review needs; do not extend a pass to materially different abilities.
5. Choose the smallest useful route whose prerequisites are ready. If ready,
   start the target even when it occurs late in the book. Otherwise, insert only
   the needed explanation, example, section, or prerequisite exercise, then return.
6. Briefly explain the route and its reason, then proceed. Reassess after actual
   output, not only at chapter boundaries.

A learner's "I know this" is provisional readiness, not mastery evidence. Use a
short probe when that readiness affects the next task. Existing valid evidence
does not require a duplicate probe merely because it appears in another chapter.
Readiness can permit attempting a task without granting `Mastered` to its goals.

## Ground Dependencies In Evidence

Use inspected explanations, explicit formula references, code/import/build
requirements, procedure preconditions, and observed learner work. A table of
contents locates candidate material; headings alone cannot prove a dependency.
Record consequential unknowns as `unknown`, not as invented chapter contents or
prerequisite chains. A book's broad "read earlier chapters" advice may require
inspection to identify the small prerequisite actually needed for this task.

When source access is partial, state the limit, inspect available material, or
use a bounded readiness probe. Ask for the relevant missing excerpt when it
would change the route; do not demand the entire book for every exercise.
For risky work, an unknown safety prerequisite must be resolved before execution;
a safe discussion or simulation can diagnose knowledge without operating it.

Real hard dependencies still constrain order: cumulative mathematical results,
code built on earlier artifacts, and safety-critical sequences cannot be skipped
merely because the learner prefers a later outcome. Identify what is required,
not an obligation to finish every earlier chapter. Respect an explicit user
sequence and literature spoiler boundaries; if a request conflicts with a hard
dependency, explain the conflict and use a safe prerequisite or simulation.

## Route Selection

| Evidence and task | Route | First move |
|---|---|---|
| Relevant prerequisites already supported | Goal-first | Start the target task or later source unit |
| One missing prerequisite blocks the target | Minimal bridge | Teach/probe that fragment, then return |
| Several weakly dependent skills need discrimination | Interleaved | Alternate contrasting tasks after enough initial teaching |
| A real deliverable combines multiple units | Project-first | Break it into bounded tasks and pull source fragments as needed |
| Source has genuine cumulative dependencies | Dependency-ordered | Follow the necessary chain, reusing valid evidence |
| Goal or readiness is unclear | Diagnostic-first | Ask one key goal question or try a small bounded task |

Interleaving is not random hopping. Each move should serve the goal, repair a
demonstrated gap, distinguish confusable concepts, or retrieve relevant knowledge.
An integrated task may span chapters without requiring every related chapter to
be read, tested, or mastered first.

## Diagnostic Practice Is Not A Mastery Shortcut

An exercise can come before reading or formal testing to reveal readiness and
needed material. Label it diagnostic/coaching and state its task and criteria;
do not block it until all associated chapters have passed. Supply minimal
teaching if the learner has not encountered the needed idea.

Keep the formal independent-test and required Practice gates unchanged. A
diagnostic attempt does not automatically satisfy either gate; qualifying
evidence must meet the relevant protocol and be recorded as such. Assisted
success informs routing, but requires a new independent equivalent check when
used for formal mastery. Assess only supported objectives, not whole chapters
by association. Follow the existing workflow rather than inventing new scores.

After success, remove redundant instruction and consider a changed constraint,
next target, or integrated application. After failure, locate the actual missing
concept or procedural step, insert the smallest repair, and retry appropriately.
Do not respond to one failed later-chapter task by assigning all earlier chapters.
If fatigue or the budget changes, shorten the route rather than lower standards.

## Preserve Source Position And Learning State

Use [wiki-state.md](wiki-state.md); do not create a separate progress system.
In the existing plan, keep source locations/material progress distinct from the
ordered learning tasks. Record selected objective IDs, relevant source sections,
route rationale, supported/unknown dependencies, inserted repairs, deferred work,
and the next task only as needed. Preserve the last actual reading location when
practice jumps elsewhere; resume should not falsely report a linear read-through.
When analyzing the author's structure or argument, retain its actual order and
relations; a learner-selected route must not be presented as the author's outline.

Unread, bypassed, and deferred material remains visible and incomplete. Finishing
a selected route is not finishing the whole book. Reuse canonical objectives and
their evidence/review queue across chapters and books; do not schedule duplicate
reviews because the route touches the same concept again. Preserve due/deferred
review debt and use the bounded review protocol when resuming strong study.

Local route changes need a brief explanation, not approval at every step. Confirm
material changes to the user's goal, scope, time/cost budget, or execution
permissions; adaptive sequencing does not authorize external actions.

## Small Examples

- Plotting goal in a programming book: inspect the plotting task and its data
  requirements. Start there if readiness is supported; bridge only a missing
  list/table operation, not every chapter before plotting.
- A later statistical derivation uses a specific matrix identity: verify that
  dependency in the text, probe or teach it, and return to the derivation. Keep
  other earlier sections unread unless the selected task actually needs them.
- A topic project uses search, evaluation, and visualization from three units:
  build one bounded workflow, cite each fragment, and assess each selected goal.
  Project success does not mark the three entire units or sources complete.
