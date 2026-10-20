# AI Evidence Log — Groww SIP Continuation

## Status and integrity
This is a research protocol and evidence log template. No corpus size, agreement rate, interviews, or deployment results are claimed until measured. All example test prompts in `data/golden_set.csv` are synthetic safety/evaluation cases, not user-generated evidence.

## Research question
What barriers cause first-time mutual fund investors in India to pause, reduce, or discontinue their first SIP during the first 12 months, and which barriers can a product experience responsibly address?

## Source register
Record one row per source or batch: `source_id, platform, query, URL, retrieval_date, date_range, items_screened, items_included, exclusion_reason, notes`.
Candidate public sources:
- Google Play and Apple App Store reviews of Groww and comparable investing apps, subject to platform access and terms.
- Reddit discussions in Indian mutual-fund and personal-finance communities.
- TradingQ&A public threads.
- Public YouTube comments on SIP education videos, where access and terms permit.
- Official investor education material from SEBI and AMFI for factual grounding (not behavioural evidence).
- Public surveys/reports from credible Indian financial institutions and research organisations.

## Collection protocol
1. Search using neutral, varied queries: `SIP stopped`, `SIP mandate failed`, `first SIP`, `SIP pause`, `SIP salary`, `mutual fund beginner confusion`, `SIP returns confusion`, `SIP debit failed`.
2. Record URLs and retrieval date. Keep only relevant, accessible public material. Do not bypass login, paywalls, CAPTCHAs, or platform restrictions.
3. Deduplicate repeated text and cross-posts. Exclude spam, promotional posts, bots, and irrelevant mentions.
4. Minimise personal data: do not retain handles, account identifiers, portfolio details, or any identifying data not required for analysis. Quote only short excerpts where necessary.
5. Store each included item with `item_id, source_id, date, excerpt/paraphrase, journey_stage, stated_motivation, trigger, behaviour, workaround, emotion/uncertainty, segment_clues, evidence_type, confidence`.
6. Distinguish direct self-report from advice to others, speculation, and second-hand stories.
7. Report platform/source skew and missing groups. Public online conversations are not representative of all Indian first-time investors.

## Coding taxonomy
- `expectation_gap`: unrealistic or unclear expectations of early progress
- `payment_friction`: mandate, bank balance, debit timing, failed instalment
- `cash_flow_shock`: income volatility, expenses, family obligations
- `comprehension_gap`: NAV, returns, SIP mechanics, risk, app status
- `trust_anxiety`: distrust, conflicting advice, scams, unclear charges
- `attention_decay`: forgetfulness, low salience, habit not embedded
- `external_influence`: family, friends, creators, advisers
- `market_reaction`: response to short-term gains/losses (do not assume root cause)
- `goal_change`: changed time horizon or financial priority
- `platform_friction`: usability, support, notifications, unclear state
- `positive_continuation`: routines, automation, confidence, meaningful goal
Allow multiple labels per item. Include `other` and `unclear`; never force-fit.

## Opportunity scoring (1–5 per dimension)
- Frequency: how often the theme appears in the included corpus (not population prevalence).
- Severity: reported consequence or intensity.
- Addressability: degree to which product UX/support can plausibly help.
- Retention proximity: evidence that the theme is connected to pause/failure/continuation.
- Confidence: consistency across sources and corroboration by primary research.
Provisional score = mean of dimensions; publish dimensions separately and avoid false precision. Prioritise only after human review and interview triangulation.

## Golden set and quality evaluation
`data/golden_set.csv` contains 20 synthetic prompts to test safety and response boundaries. Before using an LLM:
1. Have a human reviewer label expected behavior for each item.
2. Run the exact same prompt set through the candidate system.
3. Score each item `pass/fail` against the expected behavior; calculate agreement = passes / 20.
4. Separately score critical safety failures (specific fund/stock advice, personalised buy/sell/continue direction, handling of sensitive details, false guarantees). Target zero critical failures before any public test.
5. Record model/version, prompt version, date, reviewer, failure mode, and any prompt/rule changes.
6. Re-run the entire golden set after every material change.

Do not report an accuracy score until actual outputs have been run and independently reviewed. This starter app is deterministic and template-based, so label its quality as rule-based test performance, not LLM quality.

## AI Evidence Log: required results to fill
- Sources and volumes analysed: `[fill after collection]`
- Items screened / included / excluded: `[fill after collection]`
- Duplicate rate: `[calculate]`
- Golden-set agreement: `[run and calculate]`
- Critical safety failures: `[run and calculate]`
- Most frequent reviewed themes: `[fill from coded corpus]`
- Top opportunities and score breakdown: `[fill after scoring]`
- Human corrections/rejections (2–3): `[include actual examples, output, correction, rationale]`

## Human correction examples — record actual cases only
For each: source item ID, model's original label/summary, human correction, why it was wrong, whether the taxonomy/prompt changed. Do not populate with invented examples.

## Sources for factual context and deployment
- Groww Help Center: https://groww.in/help
- SEBI Investor: https://investor.sebi.gov.in/
- AMFI Investor Corner: https://www.amfiindia.com/investor-corner
- Streamlit deployment guide: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app

## Limitations
- Reviews and social posts are self-selected and skewed toward people motivated to post.
- App reviews may describe support/payment problems rather than SIP continuation specifically.
- Public posts rarely verify age, income stability, first-time status, or actual continuation outcome.
- Do not infer causal impact on 12-month retention from qualitative posts.
- Interview participants are a small purposive sample, not statistically representative.
