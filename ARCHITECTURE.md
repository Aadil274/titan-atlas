# Titan Atlas Architecture

## Overview

Titan Atlas is an AI Supply Chain Risk Intelligence Platform.

The platform analyzes dependency networks, simulates disruptions, identifies hidden risks, and generates executive intelligence.

---

## High-Level Architecture

Titan Atlas consists of two major systems:

### Atlas

Atlas is responsible for dependency intelligence.

Functions:

- Dependency discovery
- Impact analysis
- Critical node detection
- Hidden dependency analysis
- Portfolio risk analysis
- Resilience scoring
- Systemic risk ranking

---

### Titan

Titan is responsible for simulation intelligence.

Functions:

- Failure simulation
- Cascade propagation
- Timeline generation
- Executive brief generation
- Natural language scenario analysis
- Multi-node failure analysis

---

## Backend Structure

app/

    ai/
    - alternative_engine.py
    - executive_briefs.py
    - explanation_engine.py
    - narrative_engine.py
    - reasoning_enigne.py
    - recommendation_engine.py
    - report_generator.py

    api/

    - atlas.py
    - titan.py

    engines/

    - atlas_engine.py
    - dependency_engine.py
    - critical_node_engine.py
    - hidden_dependency_engine.py
    - resilience_score_engine.py
    - risk_ranking_engine.py
    - portfolio_risk_engine.py
    - systemic_risk_engine.py
    - dashboard_engine.py
    - titan_engine.py
    - multi_failure_engine.py
    - comparative_risk_engine.py
    - counterfactual_engine.py
    - impact_engine.py
    - multi_simulation_engine.py
    - network_summary_engine.py
    - network_discovery_engine.py
    - resilience_engine.py
    - risk_engine.py
    - risk_exposure_engine.py
    - root_cause_engine.py
    - scenario_comparison_engine.py
    - vulnerability_engine.py

    graph/

    - graph_queries.py
    - graph_builder.py

    simulation/

    - scenario_engine.py
    - timeline_generator.py

    database/

    - neo4j.py

    models/

    utils/

---

## Graph Model

Dependency relationships are represented inside Neo4j.

Example:

ASML
-> TSMC
-> NVIDIA
-> AWS
-> Anthropic

ASML
-> TSMC
-> NVIDIA
-> Azure
-> OpenAI

ASML
-> TSMC
-> NVIDIA
-> Google Cloud
-> Cohere

---

## Core Concepts

### Blast Radius

Number of downstream entities affected by a disruption.

### Hidden Dependency

A dependency that is not directly visible to the organization.

Example:

OpenAI

Direct:
Azure

Hidden:
NVIDIA
TSMC
ASML

### Resilience Score

Measures ecosystem resilience.

Higher score = lower risk.

### Systemic Risk

Measures how dangerous a node is to the overall network.

### Portfolio Concentration Risk

Measures whether multiple organizations depend on the same critical suppliers.

---

## Design Principles

1. Atlas handles analysis.
2. Titan handles simulation.
3. Neo4j is the single source of truth.
4. Engines should remain modular.
5. Avoid business logic inside API routes.
6. New features should be added as engines whenever possible.

---

## Current Architecture Status

Architecture Frozen

No major restructuring until MVP completion.
