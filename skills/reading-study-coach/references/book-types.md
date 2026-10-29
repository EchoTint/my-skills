# Book-Type Adapters

Use this reference after identifying the book and available source scope. Type
changes what to notice and what counts as evidence, not the user's chosen task.

## Automatic Classification

1. Inspect available content, contents, introduction, and representative reading
   units. Use reliable bibliographic metadata when full content is unavailable.
   A title keyword, marketing label, or famous reputation is not enough by itself.
2. Distinguish broad form (expository, imaginative, reference, mixed), function
   (explanation, prescription, experience, lookup), and specific genre/discipline.
3. Select a `primary` adapter and an optional `secondary`; explain the evidence,
   confidence, and practical effect in plain language. Mark metadata-only routing
   as provisional rather than pretending the text has been read.
4. Reclassify when chapter evidence changes the initial judgment. A book may
   require different adapters for theory, exercises, historical cases, and advice.

| Type | Main reading target |
| --- | --- |
| Practical/prescriptive | Ends, means, conditions, action, and consequences |
| Technical/programming/manual | Mechanisms, procedures, versions, failures, and independent use |
| Science | Phenomena, models, methods, observations, and inference |
| Mathematics/formal work | Definitions, assumptions, examples, and reconstructible proof |
| History/biography | Events, sources, selection, chronology, and interpretation |
| Philosophy | Questions, distinctions, definitions, arguments, objections, and replies |
| Social science | Data, models, methods, values, causal inference, and recommendations |
| Theology/sacred texts | Tradition, authority, interpretation, practice, and evaluative standpoint |
| Fiction/drama/poetry | Experience, form, voice, action, images, and text-grounded interpretation |
| Digest/anthology/reference | Selection, provenance, missing context, and appropriate lookup |

Examples: a political novel remains primarily literature; historical fiction is
not automatically historical evidence. Popular psychology may combine social
science and practical advice. A programming text may combine technical practice
with mathematics. Do not infer a new classification merely from a single topic.

## Shared Boundaries

- The user's goal determines reading depth. Any type may receive a gist-only
  answer. Systematic learning uses [study-workflow.md](study-workflow.md), including
  technical books; a manual is not a reason to default to passive summarization.
- In Study, keep pre-reading questions, user reconstruction, rigorous mastery
  checks, required practice, and spaced review. Adapt the evidence of learning,
  not the requirement to demonstrate it. Use [practice-loop.md](practice-loop.md).
- A contents order is not automatically a prerequisite chain. Use
  [adaptive-routing.md](adaptive-routing.md) to choose a goal-aligned route or
  combine sections; preserve real proof/build/safety dependencies and explicit
  user order. Narrative/argument continuity and spoiler limits remain relevant.
- In Analysis, retain the three-stage discipline in
  [reading-modes.md](reading-modes.md), but translate concepts, propositions,
  reasoning, and criticism into genre-appropriate objects. Do not impose 15
  expository fields on every poem or novel.
- Mixed works need explicit boundaries: say which passage uses which adapter.
  Interpretation may be plural without being arbitrary; support it with text.
- A lesson or assistant output is not proof of user mastery. Candidate source
  notes may be ingested before mastery under [wiki-state.md](wiki-state.md).

## Practical Books

- Ask what change the author wants, for whom, under what circumstances, and why
  the goal is worth pursuing. Distinguish direct rules from principles of action.
- Outline diagnosis, goal, means, sequence, examples, objections, and constraints.
- Separate empirical effectiveness from value judgments and persuasive rhetoric.
  Advice can fail because of its goal, means, audience, costs, or missing limits.
- Practice: apply one recommendation to the user's real problem, state success
  signals and exceptions, and test a counterexample. A reasoned decision not to
  apply unsuitable advice can demonstrate learning; passive agreement cannot.
- Evaluate desirability, feasibility, evidence, risks, and misuse, not popularity.

## Technical, Programming, And Tool Manuals

- Distinguish tutorial, textbook, cookbook, architecture book, API reference,
  troubleshooting guide, and tool manual. Read tutorials sequentially when
  dependencies matter; use references by task rather than mastering every entry.
- Track the language/tool/library version and environment actually supported by
  the source. Mark unknown or outdated behavior instead of silently modernizing it.
- Explain mechanisms and assumptions before memorizing steps. Relate procedures,
  examples, interfaces, and failure modes to the underlying model.
- Practice: the user explains, predicts, and independently modifies or constructs
  a small example; inspect edge cases and failures. Prefer a suitable real project,
  otherwise use a minimal exercise. Copied code running once is not mastery.
- Evaluate correctness, version fit, constraints, maintainability, and safe usage.
  Distinguish source examples from assistant proposals and observed test results.
- For proof-heavy chapters, add Mathematics; for measured experimental claims,
  add Science. Follow the user's explicit lookup/gist request without forcing study.

## Science

- Identify field, level, and form: classic, textbook, popular explanation, or
  synthesis. Locate the phenomenon, question, hypothesis, and explanatory model.
- Track definitions, variables, assumptions, measurements, experiments, results,
  and inference. Separate what was observed from what was inferred or assumed.
- Practice: reconstruct how evidence supports a conclusion, interpret a diagram
  or result, and identify what observation would challenge the explanation.
- Evaluate method, reproducibility, uncertainty, alternatives, and scope. Separate
  historical importance from current adequacy; simplification is not full proof.

## Mathematics And Formal Work

- Follow definitions and notation, assumptions/axioms, lemmas, theorems, proofs,
  examples, and applications in their dependency order.
- Reconstruct each necessary proof step. Do not call a proof understood because
  its conclusion sounds familiar; name missing prerequisites and repair them.
- Practice: solve a related example, explain a symbolic step, draw the relevant
  construction, or test a changed assumption with a counterexample.
- Evaluate validity and hidden assumptions first; then generality, explanation,
  and elegance. State exactly what was proven and under which conditions.

## History, Biography, And Autobiography

- Identify time, place, actors, scope, sources, and the story being constructed.
  Outline chronological and causal movement as well as thematic organization.
- Separate event, evidence, interpretation, and proposed lesson. Check source
  selection, omissions, retrospective framing, and competing causal explanations.
- Biography: examine the life pattern constructed and its evidence. Autobiography:
  distinguish remembered experience, self-presentation, justification, and limits.
- Practice: explain a causal account using evidence and an alternative account;
  distinguish a supported fact from inference without inventing missing sources.
- Contested history may need [topic-study.md](topic-study.md). Do not turn every
  historical episode into a universal action rule. For current events, distinguish
  reporting, interpretation, commentary, and what is too recent to know.

## Philosophy

- Find the precise question and style: dialogue, treatise, commentary, aphorism,
  or objection-response. Outline distinctions, premises, objections, and replies.
- Preserve the author's meanings, especially ordinary words used technically.
  Reconstruct the strongest reasoning before rejecting a conclusion.
- Practice: explain a distinction, rebuild an argument or thought experiment,
  test a disputed premise, and answer an objection in the user's own words.
- Locate disagreement precisely: definition, premise, inference, consequence,
  or completeness. An unresolved question is not automatic failure of learning.

## Social Science

- Identify discipline, method, social problem, and units being studied. Familiar
  vocabulary may hide technical definitions or ideological differences.
- Separate data, statistical/model inference, case interpretation, causal claim,
  value assumption, and recommendation. Do not mistake correlation for causation.
- Practice: trace a claim to its evidence, test population/context limits, offer
  a counter-hypothesis, or apply a model while stating its assumptions.
- Evaluate data quality, representativeness, definitions, methods, causal support,
  and policy feasibility. Use [topic-study.md](topic-study.md) when strong judgment
  needs multiple authors; one account need not settle a contested topic.

## Theology, Scripture, And Sacred Classics

- Identify tradition, edition/translation, textual kind, and claimed authority:
  scripture, doctrine, commentary, apologetics, devotional work, or historical text.
- Distinguish narrative, command, doctrine, interpretation, and exhortation.
  Identify the roles of authority, tradition, reason, experience, and textual reading.
- State the standpoint: internal interpretation/coherence, historical study,
  philosophical evaluation, practical meaning, or comparison across traditions.
- Practice: reconstruct an interpretation and its textual grounds, distinguish
  competing readings, or explain a practice implication without demanding assent.
- Evaluate fairly within the stated standpoint; neither dismiss a tradition nor
  treat its authority claims as automatically binding on the reader.

## Imaginative Literature: Spoiler Boundary

Default to the user's already-read range. If progress is unknown, do not reveal
later reversals, resolutions, or endings. Ask for the reading position when it
materially affects guidance. An explicit request for full-book/ending analysis
permits that scope; label spoilers before presenting them.

- Translate "whole" into the central experience, conflict, or movement; "details"
  into voice, images, scenes, rhythm, and form; "soundness" into coherence and
  emotional/formal credibility; "relevance" into perception, experience, or craft.
- Do not equate narrator/character speech with author endorsement. Do not invent
  explicit propositions or argumentative defects when meaning is enacted or implied.
- Novels/stories: trace event, choice, consequence, recognition, viewpoint, motifs,
  and subplots within the allowed range. Evaluate character credibility and unity.
- Drama: attend to speech, confrontation, stage directions, gestures, objects,
  silence, and performance. Ask how speaking or staging changes meaning.
- Poetry: reread and, when useful, read aloud. Track images, ambiguity, sounds,
  rhythm, line/stanza breaks, and turns. Do not reduce a poem to a prose slogan.
- Practice: retell a scene accurately, justify an interpretation with textual
  details, compare viewpoints/readings, or try a formal technique and explain its
  effect. These are demonstrations, not compulsory commercial/project applications.
- Do not require one definitive moral, factual treatise, or explicit lesson.

## Digests, Anthologies, Extracts, And Reference Works

- Identify selector/editor, source provenance, selection principle, abridgment,
  missing context, and the relation between excerpts and commentary.
- Keep original-author claims separate from an editor's summary or interpretation.
  An excerpt may omit the evidence needed to judge the original argument.
- Practice and analysis remain limited to visible material. Do not promote a
  digest into proof of whole-book understanding or invent the omitted context.
- For an important primary text, identify what should be checked in the original.
- Dictionaries, tables, encyclopedias, and API references often serve lookup;
  select relevant entries instead of imposing full sequential reading or testing.
