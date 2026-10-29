# Learning and Practice Loop

Use this reference when the learner wants usable knowledge, is stuck after a
test, or needs the required Practice gate. It complements
[study-workflow.md](study-workflow.md) and [pedagogy.md](pedagogy.md); use
[wiki-state.md](wiki-state.md) for evidence and progress storage. Follow the
user's language. Do not make every reading-only request a compulsory exercise.

On a practice request, use [adaptive-routing.md](adaptive-routing.md) to choose
the target and entry point before assigning reading. Practice is not a command
to restart at chapter 1 or finish each previous chapter. Use valid prior evidence,
inspect true dependencies, and combine relevant sections when useful.

## What Counts

Learning progress, an independent test pass, and a Practice pass are different
events. A summary, an assistant-written solution, or the learner's "I get it"
cannot establish ability. `Mastered` requires both the strict independent test
gate and verified learner Practice. Retention and broader proficiency require
their own evidence over time, not a higher label assigned after one exercise.

Practice is generative: the learner makes an example, analysis, plan,
explanation, decision, calculation, procedure, or code artifact in a new context.
Another recall question alone does not replace it. A learner-created explanation
can qualify when it genuinely transfers the idea, handles a boundary, and meets
stated criteria; paraphrasing the assistant's last explanation does not.

Diagnostic or coached exercises may occur before reading or formal assessment.
They reveal readiness and guide minimal teaching; they do not automatically pass
the formal independent test or required Practice gate. Reuse applicable valid
test evidence, but never infer it from chapter coverage or familiarity alone.

## The Loop

### 1. Set a Small Target

Select a relevant canonical goal and a concrete problem from the learner's
context. Prefer an exercise of about 2-5 minutes for the first pass; a larger
project is optional and must fit the learner's actual time and purpose.

Choose the relevant ready task rather than the next chapter in the contents.
When a prerequisite is uncertain, use a bounded probe; if it is missing, bridge
only that needed fragment and return to the target. A failed task does not imply
that every earlier chapter needs reading. Preserve actual safety/build/proof
dependencies and any explicit user sequence.

Before starting, state:

- The task and the specific ability it should demonstrate.
- The output the learner will produce.
- The correctness checks and success criteria, including a relevant limit or
  misuse to avoid.
- Allowed references/tools and which parts must be done by the learner.

Keep the context new, not a copy of the source example or a demonstrated
solution. Novelty can be one changed constraint; it need not be a contrived
far-transfer puzzle. Use safe simulations for tasks with real-world cost or risk.
Reading a technical book is not permission to run commands, change accounts,
deploy code, or operate equipment on the learner's behalf.

### 2. Elicit the Learner's Reconstruction

Let the learner explain their model, make a prediction, or sketch an approach
before seeing the assistant's solution. For a new learner, first provide the
minimal teaching they need; do not demand recall of material they have not met.
Ask 1-2 manageable prompts, not an entire interrogation or a giant worksheet.

If this is a formal scored attempt, use the independent-test rules in pedagogy,
including confidence self-assessment before revealing the evaluation. Otherwise
label it coaching and allow questions without treating them as a test failure.

### 3. Diagnose and Repair

Respond to the learner's actual output. Name the correct part and the specific
gap; use the source or a justified check as the basis. Choose the smallest
useful intervention:

| Observed gap | Next intervention |
|--------------|-------------------|
| Missing prerequisite | Minimal explanation and a smaller prerequisite case |
| Incorrect model | Supported counterexample and explicit model repair |
| Accurate but unexplained | Ask for the mechanism or reasoning; teach if stuck |
| Procedure breaks | Locate the failing step and retry a bounded part |
| Cannot transfer | Change one constraint and connect the idea to the task |
| Confused boundaries | Compare adjacent concepts or ask when not to use it |

Hints, answers, examples, and direct explanations are allowed in coaching.
Record the assistance. Do not turn a repaired answer into retroactive evidence
that the original independent attempt passed.

### 4. Restate, Then Recheck Independently

After repair, ask the learner to explain what changed, why the old reasoning
failed, and the corrected idea in their own words. This catches unexamined
agreement, but a restatement immediately after teaching is not enough for
independent mastery.

When a formal test is required, use a new equivalent question whose answer has
not been shown. Match the intended goal and difficulty without reusing the same
numbers, story, or supplied reasoning. Apply the four-point rubric and the full
gate: every question at least 3/4, overall at least 80%, required-goal coverage,
and no unresolved critical misuse. Retain failed/assisted attempts separately.

If valid independent test evidence already exists, do not repeat the entire
chapter test unnecessarily. Recheck affected goals when practice exposes a gap
that invalidates that evidence.

### 5. Produce and Verify the Practice Artifact

For the formal required Practice gate, after the independent test passes, have
the learner carry out the new task. This ordering does not block earlier
diagnostic or coached exercises.
They must produce the substantive output, explain essential choices, and handle
a relevant changed condition or limitation. Evaluate against the criteria set
in Step 1, not against a newly invented requirement after submission.

Examples, adapted to the user's actual goal:

| Material or purpose | Small transferable artifact |
|---------------------|-----------------------------|
| Programming/tool book | Learner-written minimal solution plus a checked changed input or constraint |
| Quantitative concept | A worked calculation with reasoning and an invalid-use case |
| Business/decision model | A recommendation for the learner's situation, with assumptions and a limit |
| Psychology/social science | A new case analysis distinguishing observation, inference, and competing explanations |
| Paper/method | A reconstruction of a key claim or method in a new example, with its evidence limit |
| Humanities/literature | A learner-created interpretation supported by passages and an alternative reading |

For interpretive work, correctness means a defensible, source-grounded argument,
not agreement with the assistant. For a paper, an analytical exercise does not
claim experimental reproduction; reproduction needs its own artifacts and checks.
For practical skills, verbal plans alone do not prove an operation was executed.

### 6. Probe a Boundary and Use the Feedback

Ask for a counterexample, a common misuse, or a condition under which the output
should change. This can be part of the task rather than an extra quiz. A critical
misuse blocks the pass until repaired and independently handled; a high average
elsewhere cannot hide it.

Then return evidence-based feedback:

- What the learner actually demonstrated.
- What failed or is still unverified, with the reason.
- The next action: a smaller repair, new equivalent check, another transfer
  task, delayed review, or next learning unit.

Save the relevant output and checks using the shared evidence record, including
`conditions.book_access`, `conditions.hints_used`, `user_output`, `score_basis`,
`practice_result`, `source_refs`, and `date`. Link the canonical goal rather than
creating duplicate practice/review queues under each book that mentions it.

## Evidence and Pass Decisions

- Verified pass: the learner's substantive artifact is available and meets the
  declared criteria; the relevant checks support the result.
- Self-reported completion: record it as self-report/unverified when the
  necessary artifact or execution evidence is unavailable. Ask for the smallest
  useful evidence; do not invent logs, results, or a pass.
- Not yet verified: if testing the artifact is unavailable, distinguish an
  inspected proposal from an executed result. State the limitation and keep the
  required practice proof pending.
- AI-completed or copied work: record the help if useful, but do not count the
  artifact as the learner's independent ability. Ask the learner to explain,
  modify, and complete a new bounded task without solution-producing help.
- Failed practice: retain the evidence and diagnose the gap. Simplify the next
  task when appropriate, but keep the same required ability and pass criteria.

Allowed reference use is not automatically failure: some real skills require
documentation. State that condition beforehand and record it. A successful
open-book task demonstrates that documented-use skill, not unsupported recall.
Assistance that supplies the answer or decisive reasoning is different from a
neutral tool or declared source lookup and cannot prove independent mastery.

Only mark the supported goals `Mastered` after the independent test and required
Practice pass. Schedule the initial review for 1 day later through the shared
schema. An artifact may support several goals only when each is demonstrably
covered; do not award unrelated goals a pass by association.

## Fatigue and Recovery

Do not repeat the same failing prompt indefinitely. After repeated difficulty,
change the explanation, isolate a prerequisite, reduce the task size, or offer a
pause. With limited time, do one meaningful step and leave the rest pending.
Reduce workload, not the independent-test threshold or the required Practice
gate. Save the learner's current model, unresolved gap, and smallest next step
so the next session can resume rather than restart.
