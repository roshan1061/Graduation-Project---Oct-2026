import streamlit as st
import re, json, csv, io
from datetime import datetime

st.set_page_config(page_title="SIP Clarity Companion", page_icon="🌱", layout="centered")
st.title("🌱 SIP Clarity Companion")
st.caption("A prototype for understanding SIP mechanics and building a sustainable investing habit.")

st.info("Educational support only — not investment advice. This tool does not recommend funds, stocks, allocations, or whether you should buy, sell, pause, or continue an investment.")
st.markdown("### What would you like help understanding?")
task = st.selectbox("Choose a task", [
    "Understand a missed SIP instalment",
    "Understand why my SIP amount may not have been debited",
    "Make sense of short-term portfolio changes",
    "Plan for a changing monthly budget",
    "Understand SIP basics",
    "Something else"
])
question = st.text_area("Describe the situation (do not include account numbers, PAN, bank details, or portfolio screenshots)", height=120,
    placeholder="Example: My SIP instalment did not go through this month. What should I check?")
st.caption("Please keep your description general and remove personal or account-specific information.")

# Deterministic safety gate before any answer generation.
unsafe_patterns = [
    r'\b(which|best|top|recommend|choose|suggest)\b.{0,40}\b(fund|stock|share|etf|scheme)\b',
    r'\b(should i|tell me to|decide for me)\b.{0,50}\b(buy|sell|switch|redeem|invest in|stop my sip|continue my sip)\b',
    r'\b(guaranteed return|assured return|risk-free return)\b'
]
sensitive_patterns = [r'\bPAN\b', r'\b\d{10,}\b', r'\baccount number\b', r'\bIFSC\b', r'\bAadhaar\b']
combined = (task + " " + question).strip()
unsafe = any(re.search(p, combined, re.I) for p in unsafe_patterns)
sensitive = any(re.search(p, combined, re.I) for p in sensitive_patterns)

def safe_answer(task, q):
    ql = q.lower()
    if "missed" in task.lower() or "debit" in task.lower() or "instalment" in task.lower():
        return [
            "Start with the factual status rather than assuming the SIP has been cancelled.",
            "Check the SIP order status and the bank/UPI mandate status in the official app or statement.",
            "Check whether the scheduled date was a holiday, whether the linked payment method was active, and whether the bank reported a failure reason.",
            "Avoid sharing credentials or sensitive details with anyone offering to fix the payment.",
            "If the status remains unclear, contact the platform or bank through its official support channel. A missed instalment does not by itself tell you what action is right for your finances."
        ]
    if "short-term" in task.lower() or "portfolio" in task.lower() or any(w in ql for w in ["negative", "loss", "down", "fall", "return"]):
        return [
            "Short-term values can move up or down, and a short observation window does not establish what will happen next.",
            "Separate the fact you can verify (the displayed value and date) from the interpretation you are making about it.",
            "Check the scheme's official documents and investor communication for definitions, risks and time horizon. Do not rely on a single screenshot or social-media prediction.",
            "This tool cannot assess your personal suitability or tell you to buy, sell, switch, pause or continue. For personalised advice, consult a qualified, appropriately registered professional."
        ]
    if "budget" in task.lower() or any(w in ql for w in ["salary", "income", "budget", "expense", "emergency"]):
        return [
            "First list essential expenses, near-term obligations and any change in reliable income.",
            "Compare those obligations with your available cash flow before making a decision about any investment commitment.",
            "Review the SIP's official pause, cancellation and mandate terms in the platform or AMC documentation; procedures can vary.",
            "This tool cannot decide what amount is appropriate for you. Consider a qualified financial adviser if you need personalised guidance."
        ]
    if "basics" in task.lower() or "sip" in ql:
        return [
            "A Systematic Investment Plan (SIP) is a method of investing a set amount at a chosen frequency into a mutual fund; it is not a separate fund and does not guarantee returns.",
            "Instalment processing, mandate status, holidays and cancellation rules can depend on the provider and payment method.",
            "For product-specific details, use the official Groww help centre, the relevant AMC's official documents, and SEBI/AMFI investor education resources.",
            "This tool provides general education only, not a recommendation about any investment."
        ]
    return [
        "I can help organise the question, but I do not have enough reliable context to answer this safely.",
        "Please check Groww's official help centre, your bank or payment provider, and the relevant AMC's official documents.",
        "For personalised investment decisions, consult a qualified professional. I will not recommend specific funds or tell you whether to buy, sell, switch, pause or continue."
    ]

if st.button("Get a safe checklist", type="primary"):
    if not question.strip():
        st.warning("Describe the situation in general terms first.")
    elif sensitive:
        st.error("Safety check: your text may contain personal or account-sensitive information. Remove it and try again. Do not enter PAN, account numbers, bank details, or credentials.")
    elif unsafe:
        st.warning("Safety gate activated: this request appears to ask for a specific investment recommendation or personal buy/sell/continue decision. I can't provide that. I can explain general concepts and point you to official sources.")
        st.markdown("**Safe alternative:** rephrase the question as a general process or concept question, without asking which investment to choose.")
    else:
        answer = safe_answer(task, question)
        st.success("Quality check passed: general educational response; no fund selection or personal investment instruction detected.")
        st.markdown("### Suggested checklist")
        for item in answer:
            st.markdown(f"- {item}")
        st.caption("Prototype quality gate: deterministic rule checks plus constrained response templates. This is not a production-grade AI model or a validated financial-advice classifier.")

with st.expander("Why this tool uses a quality gate"):
    st.write("The prototype checks for requests seeking specific investment recommendations and for likely sensitive data before returning a constrained, general checklist. When a request is outside scope, it refuses or points to official sources. The starter version uses deterministic rules rather than a live LLM so it can be tested without API costs. The evaluation set and limitations are included in the project bundle.")

st.markdown("---")
st.markdown("**Official starting points**")
st.markdown("- [Groww Help Center](https://groww.in/help)")
st.markdown("- [SEBI Investor](https://investor.sebi.gov.in/)")
st.markdown("- [AMFI Investor Corner](https://www.amfiindia.com/investor-corner)")
st.caption("Never upload portfolio screenshots or enter PAN, bank account numbers, passwords, or other identifying financial information.")
