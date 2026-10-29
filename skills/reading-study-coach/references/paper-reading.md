# Paper Reading

Use this local adapter for a concrete paper, report, thesis, or selected research fragment.
It supports interactive reading; it does not automatically start a literature search or research project.
Within topic study, follow [topic-study.md](topic-study.md): the topic question remains primary.
Use [source-intake.md](source-intake.md) to establish identity, available text, and actual coverage.

## Goal, Depth, And Workflow Priority

Infer skim or deep reading from the user's outcome, and adjust the route as questions develop.
For an explicit pure-summary request, explain directly without compulsory coaching or an exam.
For active mastery, keep the strict workflow in [study-workflow.md](study-workflow.md).
This adapter changes source navigation and question content, not mastery criteria or practice requirements.
A formal test takes priority over the ordinary answer-first policy until the user exits testing.

| Mode | Focus | Detail policy |
|---|---|---|
| Skim | Problem, contribution, central figures, strongest evidence, limitations | Read method detail needed to understand the main claim |
| Deep | Mechanism, assumptions, reasoning, evidence, limits, transfer | Cover core units within the agreed scope; record deferrals |

Infer narrower goals without making the user choose a formal menu:

- Implementation: inputs, outputs, algorithm, objective, data, hyperparameters, ablations, and edge cases.
- Positioning: claimed gap, related-work contrasts, contribution boundary, and reusable supported claims.
- Presentation: storyline, important figures, evidence, limitations, and likely audience questions.
- Local inquiry: only the selected section, equation, figure, method component, or confusion.

Do not advertise a whole-paper deep read when only one module is covered.

## Start With A Reading Map

With title or metadata only, offer tentative orientation and obtain useful text before specific claims.
With an abstract, distinguish author-reported claims from evidence not yet inspected.
Do not invent results, formulas, baselines, or limitations from the title or prior familiarity.
Use a short opening map unless the user asks for a complete overview:

1. The problem and apparent contribution in one sentence, qualified by the available text.
2. About three useful questions: what problem, what mechanism, and what supporting evidence?
3. An adjustable route through the available units, aligned with the user's goal.

Ask about depth only when it cannot be reasonably inferred and matters to the next step.
Do not declare sections skippable before understanding the user's goal and the claim's dependencies.

## Navigate By The Current Understanding Need

Sections are anchors, not compulsory conversational checkpoints.
Units can be passages, figures, tables, equations, proofs, algorithms, or experimental blocks.
Before a unit, offer a natural reading lens rather than a compulsory quiz.
Retain the current unit when answering a side question; do not silently advance the reading position.
Record the exact units inspected, not merely that the paper file was available.

### Figures And Tables

- Read caption, axes, labels, units, compared conditions, and relevant surrounding text together.
- Distinguish what is directly shown from the explanation the author gives it.
- Identify sample, metric, baseline, uncertainty, and missing comparison where available.
- Do not infer significance, mechanism, causation, or generality from a favorable plot alone.
- If an image is unavailable or unreadable, request it or record the gap rather than guessing.

### Equations, Proofs, And Algorithms

- Establish variable meanings, shapes or domains, assumptions, and inputs and outputs.
- Explain what the equation or step does and why the method needs it.
- Connect local steps to the objective, mechanism, or theorem being supported.
- Separate an optimization objective from an evaluation metric or a formal guarantee.
- Preserve useful mathematical notation; do not substitute an analogy for the actual conditions.
- If a derivation is deferred, retain its conclusion, assumptions, locator, and reason to return.

### Methods And Experiments

- Trace the mechanism from inputs through transformations or decisions to outputs.
- Separate the conceptual contribution from engineering choices and reported implementation details.
- Connect each experiment or ablation to the particular claim it can test.
- Inspect comparison fairness, data splits, metrics, controls, ablations, and relevant uncertainty.
- Distinguish empirical performance from mechanism evidence and from a theoretical guarantee.
- Scope conclusions to tested settings; name unavailable details rather than reconstructing them as facts.

## Answer Questions First, Then Calibrate At Nodes

For a direct reading question, answer it before requesting a demonstration of understanding.
Use a short answer, paper-grounded explanation, and necessary background or analogy.
Distinguish the paper's statement, your inference, and added background when the distinction matters.
A narrow factual clarification usually needs no follow-up question.
For a central concept or a known confusion, add one short distinction or transfer question.

Questioning is node-required, not every-turn-required, in a coaching session.
After confirmation or repair, default to one compact follow-up at these nodes:

- The user paraphrases the mechanism or explains their current understanding.
- The user compares methods, formulas, objectives, assumptions, or guarantees.
- The user critiques a claim, baseline, ablation, or evidence strength.
- The user answers a recall question or reports a presentation or reading takeaway.
- A useful non-trivial node follows several consecutive explanation-only replies.

Target a meaningful distinction rather than asking for agreement or repeating a definition.
Examples include claim versus inference, mechanism versus performance evidence,
assumption versus guarantee, and contribution versus implementation detail.
Do not wrap every reply in a numbered quiz or require a ritual announcement that a section is done.
Do not apply this coaching default to an explicitly summary-only interaction.

## Repair, Boundaries, And Deferral

Preserve the correct part of an answer, repair the important error, then ask a focused follow-up.
Praise specific progress, not every turn or the user's apparent fluency.
After repeated confusion around one central point, offer a brief consolidation before changing units.
At an implicit boundary, offer a short recap and optional one-to-three checks; do not force a final exam.
If the user continues with a direct question, answer it and retain the boundary for later.

When asked to skip, explain the tradeoff and propose a reversible deferral.
Skim may defer derivations and secondary ablations if the main claim remains interpretable.
Deep reading must not silently omit core mechanisms, evidence, assumptions, or acknowledged limits.
Implementation goals require details needed for the agreed implementation scope.
Record a deferred unit, its dependencies, and when it should be revisited.

## Critique A Specific Claim

Identify the claim, reconstruct its strongest fair form, and inspect the evidence relevant to it.
Check missing or weak baselines, absent ablations, restrictive assumptions, and overgeneralization.
Distinguish a serious contradiction from a normal scope limitation or unavailable detail.
Offer a narrower defensible claim when appropriate, and suspend judgment when evidence is insufficient.
Ask what observation or comparison would strengthen or weaken the user's critique.

## Finish And Formal Exam

When the user clearly finishes the coached reading, provide final synthesis and three-to-five recall questions.
Finish signals include a declared completion, moving to the next paper, or asking to wrap up the session.
For an explicitly pure-summary request, provide the synthesis without forcing recall or testing.
The synthesis covers problem, mechanism, evidence, limits, actual reading scope, and remaining gaps.
Include the user's demonstrated understanding and repaired confusions, not just the paper's storyline.
Leave unanswered recall questions untested; asking them is not evidence of mastery.

For a requested formal exam, default to five-to-seven questions unless the user specifies otherwise.
Cover the main claim, mechanism, evidence, limitations, transfer, and fair critique.
Present questions first and wait for the user's attempt before revealing answers or feedback.
Do not supply an answer key in the same reply as the test.
In active mastery or exam mode, do not bypass a test by invoking the ordinary answer-first rule.
If the user chooses teaching or remediation instead, pause the test and keep the target unpassed.
Record hints or assistance; retest with a fresh prompt when independent recall is required.
After an attempt, give specific assessment, repair, and a locator to reread.
Use [study-workflow.md](study-workflow.md) for scoring, mastery gates, interleaving, practice, and review.

## Implementation And Reproduction Boundary

Reading can produce a reproducibility checklist; it does not itself execute reproduction.
Record paper and code versions, dependencies, data version and access, preprocessing,
hardware assumptions, seeds, hyperparameters, expected metrics, and missing details where available.
Unobtained code, unavailable data, and unspecified hardware are gaps, not completed checks.
Distinguish author-reported results, inspected code, attempted runs, and independently observed results.
Do not start training, fetch datasets, run repository code, or incur compute costs from a reading request.
Actual execution requires an explicit request and agreed scope, resources, and limits.
Use [practice-loop.md](practice-loop.md) for authorized implementation or other target-appropriate practice.
Do not claim successful reproduction from a checklist, a small unrepresentative example, or reading alone.

## Persistent Resume State

Use [wiki-state.md](wiki-state.md), not an internal-only memory, for durable session state.
Store the source at `book-wiki/sources/<source-slug>/` with shared object files.
Record kind, title, authors, version, DOI or stable identifier, and content provenance.
Use `meta.md`, `study-plan.md`, and `mastery-map.md`; section notes may use `chapters/`.
Save mode, user goal, current unit, main questions, demonstrated understanding, and confusions.
Also save actual read ranges, deferred units, evidence to revisit, test attempts, and practice status.
Create session, practice, and evidence records only when needed by the activity.
If working inside a topic, link the paper unit to the topic question and preserve both resume pointers.
On pause, save, mode change, or finish, update state and expose a concise next action.
On resume, restore the source version and location before suggesting the next unit.
Do not inflate whole-paper coverage, completeness, or mastery from partial reading or a saved summary.
