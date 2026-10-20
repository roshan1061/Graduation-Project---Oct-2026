# Groww SIP Continuation PM Project — Starter Bundle

## What is included
- `app.py`: working Streamlit prototype, SIP Clarity Companion.
- `data/golden_set.csv`: 20-item manually reviewable evaluation starter set (synthetic test prompts, not user research).
- `AI_Evidence_Log.md`: evidence collection protocol, annotation rubric, evaluation plan, and explicit blanks for results that must be measured.
- `Interview_Guide.md`: consent-led interview guide for 5–6 real participants.
- `User_Test_Plan.md`: usability test plan for at least 3 returning participants.
- `Deck_Content.md`: proposed 10-slide narrative.
- `Groww_SIP_Continuation_Deck.pdf`: 10-slide draft deck.

## Important integrity notes
No user interviews, source volumes, model agreement scores, live deployment, or usability results have been fabricated. Synthetic prompts in the golden set test safety behaviour; they are not evidence of investor behaviour. Replace the draft hypotheses with findings only after collecting and coding real public data and conducting interviews.

## Run locally
```bash
python -m venv .venv
source .venv/bin/activate  # Windows: .venv\Scripts\activate
pip install -r requirements.txt
streamlit run app.py
```

## Public deployment (free option)
1. Create a GitHub account and a **public** repository.
2. Upload `app.py` and `requirements.txt` (plus optional supporting files).
3. Sign in at https://share.streamlit.io and choose Create app.
4. Select the repository, branch, and `app.py`, then deploy.
5. Open the resulting `*.streamlit.app` URL in an incognito window to verify public access.
6. Do not add API keys or secrets to the public repository.

Official guide: https://docs.streamlit.io/deploy/streamlit-community-cloud/deploy-your-app

## Discovery engine — first version
This bundle gives you the repeatable workflow and annotation framework, not a claim that a full web crawler has already collected thousands of posts. Start with public, accessible pages and manually record source URLs, dates, excerpts, and source type in the evidence log. Respect platform terms, robots policies, rate limits, privacy, and copyright. Avoid collecting usernames or personal identifiers. For scale, add a compliant ingestion connector and run the same schema over the collected corpus.

## No investment advice
The prototype does not recommend specific funds or stocks and does not tell users whether to buy, sell, switch, pause, or continue. It uses rule-based safety checks and constrained educational templates. The app must be evaluated and improved before being described as production-ready.
