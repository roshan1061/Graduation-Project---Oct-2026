# 10-slide deck narrative

## Slide 1: Groww | First-time SIP continuation

A discovery-led growth case study
Business goal: increase the share of first-time mutual fund investors with an active SIP at month 12.

Status: research and prototype starter. Findings must be replaced with verified evidence after data collection and interviews.

## Slide 2: The metric is a chain of behaviours, not a notification problem

North star: % of first-time SIP starters with ≥1 successful instalment in the 30 days before month 12.

Decompose into: successful setup → first debit → repeat successful debits → recover from friction → remain able and willing to invest → active in month 12.

Diagnostic cohorts: mandate success, failed debit recovery, pause/restart, affordability change, app comprehension, and first-12-month retention.

## Slide 3: Discovery engine turns conversations into testable opportunities

Pipeline: public source discovery → compliant capture → deduplication → item-level coding → segment/context extraction → human review → opportunity scoring → primary-research questions.

Theme taxonomy: payment friction, cash-flow shock, expectation gap, comprehension gap, trust anxiety, attention decay, external influence, market reaction, goal change, platform friction, positive continuation.

Do not infer prevalence or causality from self-selected posts.

## Slide 4: Early hypotheses are not yet findings

Hypotheses to test: (1) investors may not understand payment failure states; (2) early progress may not match expectations; (3) income/expense changes may make the commitment feel inflexible; (4) conflicting external advice may create uncertainty.

Evidence status: public-source corpus, counts, theme rankings and AI agreement must be filled from actual collection and review. No unsupported percentages.

## Slide 5: Metric decomposition identifies intervention points

Input/activation: first SIP successfully created and mandate understood.

Early habit: first 1–3 instalments succeed; user understands schedule and status.

Resilience: failed payment is understood; changed affordability can be handled without shame; user can find official help.

Continuation: at least one successful instalment in the month-12 window.

Guardrail: retention is not success if the user cannot afford the investment or feels pressured.

## Slide 6: Primary research selects one segment and one moment

Research plan: 5–6 semi-structured interviews with first-time SIP starters in the last 12–18 months, varying active/paused/failed/stopped status.

Ask for specific episodes, expectations, app checks, workarounds and what happened next. Avoid leading questions about market falls.

Chosen segment and root cause: populate only after interview synthesis; include counterexamples and confidence.

## Slide 7: Problem statement must explain the break in continuation

Template: For [evidence-backed segment], when [specific moment in first 12 months], [unmet need/root cause] makes it difficult to [user task], leading to [observed behaviour]. Current workaround is [observed workaround].

User value: clearer understanding and agency. Business value: fewer avoidable lapses and better recovery from preventable friction. Do not optimise continuation at the expense of affordability.

## Slide 8: MVP: SIP Clarity Companion

A guided educational checklist for missed instalments, app status, short-term changes and changing budgets.

AI's potential role: interpret varied natural-language descriptions and route to an appropriate explanation; non-AI rules/templates are safer and cheaper for common cases. Add an LLM only if evaluation proves incremental value.

MVP starter uses deterministic rules, safety checks and constrained templates; no fund/stock recommendations or personalised continue/stop instructions.

## Slide 9: Eval gate, user testing and measurement

Golden set: 20 synthetic prompts spanning safe education, prohibited advice, sensitive data, uncertainty and guarantees. Score item-level pass/fail and critical failures; re-run after every change.

User tests: 3 returning participants, real tasks, think-aloud, task completion, clarity and safety interpretation.

Metrics: month-12 active SIP rate; successful instalment rate; failed-debit recovery; help resolution; comprehension; critical AI safety failure rate; sensitive-data handling; complaint/pressure guardrails.

## Slide 10: Risks, limitations and next steps

Risks: biased public data; weak segment inference; hallucinated or overconfident financial explanations; false-positive/negative safety gate; engagement nudges that pressure users; privacy leakage; low statistical power.

Mitigate with human review, official sources, conservative fallback, no personalised advice, privacy minimisation, affordability-respecting language, and cohort-based measurement.

Next: collect/cite corpus → run 20-item evaluation → interview 5–6 users → update problem statement → deploy public MVP → test with 3 users → finalise deck.