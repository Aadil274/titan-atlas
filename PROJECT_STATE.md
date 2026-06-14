# Titan Atlas

Titan Atlas is an AI Supply Chain Risk Intelligence Platform.

Purpose:

- Discover dependency chains
- Identify hidden dependencies
- Simulate failures
- Measure systemic risk
- Detect concentration risks
- Generate executive intelligence

Core Idea:
"What happens if a critical supplier, cloud provider, semiconductor company, or country fails?"

## Atlas

Dependency Intelligence

Endpoints:

GET /atlas/node/{search_term}
GET /atlas/impact/{search_term}
GET /atlas/dependencies/{search_term}
GET /atlas/critical
GET /atlas/dashboard

Engines:

atlas_engine.py
dependency_engine.py
critical_node_engine.py
hidden_dependency_engine.py
portfolio_risk_engine.py
resilience_score_engine.py
risk_ranking_engine.py
systemic_risk_engine.py
dashboard_engine.py

## Titan

Scenario Intelligence

Endpoints:

POST /titan/ask
POST /titan/analyze/{node}
POST /titan/find

Engines:

titan_engine.py
scenario_engine.py
timeline_generator.py
comparison_engine.py
executive_briefs.py
narrative_engine.py
query_analyzer.py
multi_failure_engine.py

ASML
└─> TSMC
└─> NVIDIA
├─> AWS
│ └─> Anthropic
│
├─> Azure
│ └─> OpenAI
│
└─> Google Cloud
└─> Cohere

Completed:

✓ Dependency Discovery
✓ Impact Analysis
✓ Hidden Dependency Detection
✓ Critical Node Detection
✓ Resilience Scores
✓ Vulnerability Scores
✓ Portfolio Concentration Analysis
✓ Systemic Risk Analysis
✓ Failure Simulation
✓ Cascade Propagation
✓ Timeline Generation
✓ Executive Brief Generation
✓ Natural Language Querying
✓ Dashboard API

Current Phase:

Phase 8 - Executive Intelligence

Completion Estimate:
92%

Next Task:
Network Summary Engine

After That:
Frontend Dashboard
Graph Visualization
Demo Preparation
README Finalization

Rules:

1. Do not replace Atlas/Titan architecture.
2. Prefer adding engines over bloating endpoints.
3. Atlas = analysis.
4. Titan = simulation.
5. Every new feature must support:
   - dependency intelligence
   - risk intelligence
   - simulation intelligence
6. Avoid feature creep.

Architecture Status: Frozen

No major folder restructuring until:

- Backend intelligence layer is complete
- Frontend dashboard is complete
- MVP demo is working

Only then evaluate refactoring.
