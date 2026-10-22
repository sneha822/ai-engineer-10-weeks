# 🧠 AI Engineer in 10 Weeks — My Learning Journey

My hands-on journey to becoming an AI Engineer, following the
**"AI Engineer in 10 Weeks"** course by *Padho with Pratyush*.

This repo documents everything I build, week by week — real code, real
projects, and notes on what I learned (including the bugs that taught me the
most). The three flagship projects graduate into their own polished repos
(linked below) as I complete them.

---

## 📊 Progress

| Week | Focus | Deliverable | Status |
|-----|-------|-------------|--------|
| 1 | LLM fundamentals + API mastery | Multi-provider chatbot | 🟡 In progress |
| 2 | Prompt engineering for production | Structured-extraction pipeline | ⚪ Not started |
| 3 | RAG foundations | Document Q&A bot (v1) | ⚪ Not started |
| 4 | Advanced RAG + evaluation | Document Q&A bot (v2) + eval report | ⚪ Not started |
| 5 | Agents + tool use | Autonomous research agent | ⚪ Not started |
| 6 | Multi-agent + MCP | Multi-agent workflow + custom MCP server | ⚪ Not started |
| 7 | Observability + guardrails + security | Agent with tracing, evals, guardrails | ⚪ Not started |
| 8 | Deployment + fine-tuning + capstone | Deployed AI product (live URL) | ⚪ Not started |

Legend: 🟢 done · 🟡 in progress · ⚪ not started

## 🚀 Flagship projects (standalone repos)
Links appear here as each one is completed:
- **Document Q&A (RAG)** — _coming in Weeks 3–4_
- **Research / Multi-agent system** — _coming in Weeks 5–6_
- **Capstone (deployed product)** — _coming in Week 8_

---

## 🗂️ Repo structure
```
ai-engineer-10-weeks/
├── week1/ … week8/     # one folder per week; day folders inside
│   └── dayN/           # each day's code + its own README
├── .env.example        # template for API keys (copy to .env, never commit .env)
└── .gitignore          # keeps secrets & venvs out of git
```

## 🔑 Setup
Each day's project is self-contained. To run one:
```bash
cd weekN/dayN
cp ../../.env.example .env   # then paste your real keys into .env
# install deps (uv or pip, per the project)
python <script>.py
```
> ⚠️ The script loads the `.env` **in its own folder**. Keep your keys next to
> the code that uses them, and never commit `.env`.

---

*Learning in public. Follow along!* 🌱
