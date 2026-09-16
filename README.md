Horizon Product Intelligence
A universal product‑opportunity engine built in Python.

Horizon Product Intelligence helps companies decide what product they should build next using structured intelligence across markets, competitors, constraints, internal capabilities, and strategic goals. It produces a clear, defensible, executive‑ready recommendation backed by six analytical engines.

🚀 Overview
Companies routinely waste money building the wrong products due to unclear market signals, fast‑moving competitors, internal biases, misunderstood constraints, and misaligned capabilities. Horizon solves this by providing a Python‑based decision engine that evaluates product opportunities across multiple dimensions and synthesizes them into a board‑ready recommendation.

✨ Key Features
Structured input system for company, market, competitor, and product data

Six intelligence engines:

Market Intelligence

Competitor Intelligence

Product Viability

Constraint Analysis

Strategic Fit

Executive Decision Synthesis

Scoring models for opportunity evaluation

Full orchestration pipeline

Streamlit UI for interactive analysis

Executive summary output

📦 Project Structure
Code
horizon_product_intelligence/
│
├── app.py
├── README.md
├── pyproject.toml
├── .env
│
├── horizon/
│   ├── config/
│   ├── domain/
│   ├── data/
│   ├── engines/
│   ├── orchestrator/
│   ├── ui/
│   └── utils/
│
└── tests/
Directory Breakdown
config/ — environment settings, logging

domain/ — Pydantic models for all inputs/outputs

data/ — loaders, repositories, sample datasets

engines/ — the six intelligence engines

orchestrator/ — main pipeline that runs all engines

ui/ — Streamlit pages and layout components

utils/ — scoring helpers, text utilities, serialization

tests/ — unit tests for each engine and orchestrator

🛠 Installation
Prerequisites
Python 3.10+

Poetry or pip

Streamlit

Install Dependencies
Using Poetry:

bash
poetry install
Using pip:

bash
pip install -r requirements.txt
▶️ Running the App
Start the Streamlit UI:

bash
streamlit run app.py
This launches the Horizon interface where you can:

Enter company profile

Define product opportunities

Input market and competitor data

Run full analysis

View executive‑ready recommendations

📘 Usage Example
Once the app is running:

Enter your company’s industry, segments, capabilities

Define a product opportunity (name, value proposition, features)

Add market and competitor inputs

Specify constraints

Click Run Analysis

Review:

Market score

Competitor score

Viability score

Constraint score

Strategic fit score

Final recommendation

🧠 Intelligence Engines
Each engine is a pure Python module:

market_engine.py

competitor_engine.py

viability_engine.py

constraint_engine.py

strategic_fit_engine.py

decision_engine.py

The orchestrator (product_cycle.py) wires them together into a full analytical pipeline.

📈 Roadmap
MVP
Core engines

Streamlit UI

Basic scoring models

Executive summary output

v1
FastAPI backend

React/Next.js front‑end

Industry intelligence packs

Multi‑opportunity comparison

Enterprise
Custom scoring models

ERP/CRM integrations

Predictive forecasting

Automated product roadmaps

🤝 Contributing
Contributions are welcome.
Please open an issue or submit a pull request.

📄 License
MIT License (or whichever you choose).
