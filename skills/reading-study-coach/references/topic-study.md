# Topic Study

Use this adapter for learning a field or comparing multiple sources around shared questions.
A topic is a first-class learning object, not a batch of independent book summaries.
Books, papers, articles, and documentation are sources serving the topic.

## Select The Depth

Infer depth from the user's outcome; do not infer it from source genre alone.
State a tentative scope and start with a useful small output when the intent is clear.
Ask only when scope, prerequisites, or the desired outcome would materially change the route.

| Layer | User outcome | Main work | Completion evidence |
|---|---|---|---|
| Overview | Understand the field's main shape | Map concepts, relations, approaches, and gaps | Scoped map and, if coaching, a light explanation check |
| Deep issue | Understand or judge a particular question | Compare mechanisms, arguments, assumptions, and evidence | Traceable issue synthesis with uncertainty |
| Mastery | Remember, explain, apply, or implement selected targets | Strict study, testing, practice, and review | Evidence required by the study workflow |

Layers can differ by question in the same project.
An overview can identify a target for mastery without making every source a mastery assignment.
Do not treat completed reading, a polished map, or agreement with the coach as tested mastery.
If the user only wants an overview or summary, do not impose an exam.

## Topic Object And State

Follow [wiki-state.md](wiki-state.md) for creation, restoration, provenance, and updates.
Store the topic under `book-wiki/topics/<topic-slug>/`:

- `meta.md`: topic, scope, exclusions, goal, background, and current depth.
- `study-plan.md`: question-driven route, prerequisites, current unit, and next action.
- `mastery-map.md`: only the knowledge or capability targets selected for mastery.
- `question-map.md`: central questions, dependencies, source answers, issues, and unresolved gaps.
- `source-map.md`: source identities, roles, access, located passages, and actual reading coverage.

Create session, practice, and evidence records only when the activity needs them.
Reuse source objects rather than copying whole books into the topic directory.
Legacy books stay at `book-wiki/<book-slug>/`.
Papers and articles use `book-wiki/sources/<source-slug>/`.
Keep a source-unit pointer for returning to single-source reading.
Reading a passage for a topic must not silently advance the source's whole-book position.
Persist relevant state at pause, mode changes, and session boundaries, not only in conversation memory.

## 1. Define A Working Question Set

Start from what the user wants to understand, decide, or do.
Convert a broad subject into a few questions that can organize the present round.
Separate foundational questions from applications and contested issues.
Record what this round excludes; a bounded overview is not a complete account of a field.
Let source inspection refine the questions rather than treating the first wording as final.
Keep the user's learning goal primary, not a favorite author's chapter sequence.

Useful `question-map.md` fields:

| Field | Purpose |
|---|---|
| Question ID and wording | Stable, neutral anchor for comparison |
| Dependency and priority | What must be understood first |
| Requested depth | Overview, deep issue, or mastery |
| Current answer | Provisional synthesis, with evidence links |
| Disagreement or gap | What remains unsettled or unavailable |
| Next reading or test | Concrete next action tied to this question |

## 2. Inspect And Select A Complementary Source Pool

Use [source-intake.md](source-intake.md) to establish identity and usable content.
Inspect source structure before choosing passages for close reading.
Titles, tables of contents, indexes, abstracts, and headings help locate material.
They do not establish the contents, arguments, or correctness of unread passages.
Use the smallest pool that covers the current questions with meaningful complementary roles.
Possible roles include orientation, foundational explanation, original evidence, alternative view, and practice.
Do not require a fixed number of books or assume more sources produce better understanding.
If the user's supplied pool is narrow, label the resulting map accordingly.
Do not imply an exhaustive literature search or systematic review unless that task was requested and performed.

For every candidate record inclusion, exclusion, or deferral and its reason.
Check for selection bias toward familiar, popular, accessible, recent, or same-school sources.
Seek a missing perspective or primary evidence when it would change a central conclusion.
Do not add an opposing view merely to create artificial balance.

Useful `source-map.md` fields:

| Field | Purpose |
|---|---|
| Source ID, identity, and version | Link to the canonical source object |
| Role and question IDs | Why the source is in this pool |
| Access available | Full text, excerpt, abstract, metadata, or unavailable |
| Located passages | Relevant chapters, sections, pages, figures, or equations |
| Actually read range | Exact units inspected or closely read in this session |
| Treatment and rationale | Close reading, skim, background, defer, or exclude |
| Evidence independence | Shared studies, citations, or dependence on another source |

Keep available content and actually read content separate.
Having a full PDF does not mean the full PDF has been read.
Having a chapter heading does not support a detailed claim about that chapter.

## 3. Read By Question, Not By Book Completion

Choose the next unit by question priority, prerequisite, and current uncertainty.
Locate the passages that answer it, and read enough surrounding context to interpret them fairly.
Mark close-read, skimmed, deferred, and unread units; do not mark the whole source covered.
Use the appropriate source adapter locally, including [paper-reading.md](paper-reading.md) for papers.
The local adapter must serve the topic question, not replace the project's research or reading plan.
Retain the interrupted unit and next action when the user asks a side question.
Return to a book-level route only when the user chooses that shift or the question genuinely requires it.

## 4. Compare Meanings, Answers, And Evidence

Build working vocabulary for the question without adopting one author's terms as the master vocabulary.
Record each author's term and meaning before translating it into a shared term.
Flag same-word/different-meaning and different-word/similar-meaning cases.
If concepts cannot be safely aligned, preserve the difference rather than manufacturing agreement.
Separate empirical claims, theoretical explanations, value judgments, and recommendations.
Distinguish disagreements about definitions, assumptions, context, evidence, and conclusions.

For each question-source pair record the answer and a traceable locator.
Label an answer as direct, indirect interpretation, no answer in inspected text, or text unavailable.
An indirect interpretation must not be presented as the author's explicit position.
Unread or unavailable text is not author silence; inspected silence is not opposition.
Qualify any claim of silence by the inspected range, unless complete relevant coverage supports it.

Compare the strongest fair version of each relevant position before evaluating it.
Assess evidence quality, independence, applicability, and date, not the number of agreeing authors.
Several books repeating one study are not several independent confirmations.
Consensus is informative, but majority agreement does not establish truth.
Neutral comparison does not require equal confidence in unequally supported claims.

## 5. Consolidate At The Selected Layer

For overview, organize the field map by problems and relationships rather than by book titles.
Show core concepts, main approaches, dependencies, important disagreements, and coverage gaps.
If coaching, invite a brief explanation of the map or a concrete distinction between approaches.
This checks orientation; it is not an exam on every source and does not establish application ability.
For a passive overview request, provide the map directly and leave understanding untested.

For deep issues, synthesize answers, conditions, supporting evidence, competing explanations, and uncertainty.
Distinguish source positions, coach inferences, and the user's current judgment.
Do not force a winner when evidence is missing or the answers concern different conditions.
For selected mastery targets, use [study-workflow.md](study-workflow.md) without weakening its gates.
Use [practice-loop.md](practice-loop.md) for target-appropriate application and transfer.
Keep strict questioning, tests, practice, and scheduled review attached to those targets.
Do not create review obligations for every quotation, background source, or summary.

## 6. Stop, Save, And Reopen Deliberately

End the current overview round when its declared scope is mapped, key relations can be explained,
and significant uncertainties or missing perspectives are explicit.
If no explanation check occurred, record map delivery, not demonstrated understanding.
Do not require resolution of every debate or completion of every source to finish an overview.
Stop expanding the pool when additional sources only repeat covered material within the present scope.
A new source is useful when it fills a named gap, changes evidence, or supports a selected deeper target.
Record whether a question is mapped, analyzed, tested, or still open; do not collapse these states.
Save the current question, source unit, actual coverage, and next step through [wiki-state.md](wiki-state.md).
On resume, restore those pointers and review due mastery targets using the study workflow.
Present the next bounded choice: fill a specific gap, deepen an issue, or master a useful capability.
