# Titan Atlas

**AI-Powered Systemic Risk & Dependency Intelligence Platform**

Titan Atlas is a software platform designed to model, analyze, and visualize interconnected dependencies across technology, supply chains, infrastructure, geopolitics, and other critical systems.

The core idea is simple:

> **Understand how systems are connected, identify critical points of failure, and simulate how disruptions can propagate through the network.**

---

## Project Status

**Active Development**

The backend foundation is operational and the frontend is currently being developed.

Current capabilities include:

* Dependency graph modeling using Neo4j
* Node discovery and search
* Dependency analysis
* Impact and blast-radius analysis
* Risk scoring
* Critical-node identification
* Systemic risk ranking
* Portfolio risk analysis
* Dashboard API
* React frontend foundation

Planned capabilities include:

* Interactive global visualization
* Real-time data ingestion
* Scenario simulation
* AI-powered risk explanations
* Geopolitical and infrastructure intelligence
* Real-time risk updates

---

## Core Concept

Titan Atlas represents real-world entities as nodes in an interconnected graph.

Examples include:

```text
Countries
Cloud Providers
AI Companies
Semiconductor Companies
Technology Companies
Infrastructure
Energy Systems
```

Relationships between these entities describe dependencies such as:

```text
DEPENDS_ON
SUPPLIES
SUPPLIED_BY
HOSTS
OWNS
PARTNERS_WITH
LOCATED_IN
AFFECTS
```

This allows Titan Atlas to analyze how a disruption affecting one entity could propagate through the wider system.

### Example

```text
ASML
  ↓
TSMC
  ↓
NVIDIA
  ↓
Cloud Providers
  ↓
AI Companies
```

A disruption at an upstream node can therefore have consequences for multiple downstream systems.

---

## Architecture

The project is divided into a backend and frontend.

```text
Titan Atlas
│
├── backend/
│   └── FastAPI
│       │
│       ├── API
│       ├── Services
│       ├── Engines
│       ├── Repositories
│       ├── Graph Layer
│       └── Neo4j
│
├── frontend/
│   └── React + TypeScript
│
└── docs/
```

### Backend

The backend provides the intelligence and graph-analysis layer.

Primary technologies:

* Python
* FastAPI
* Neo4j
* Pydantic

### Frontend

The frontend provides the user interface for exploring the Titan Atlas intelligence network.

Primary technologies:

* React
* TypeScript
* Vite
* Tailwind CSS

---

## Backend API

Current Atlas endpoints include:

```text
GET /atlas/node/{node}
GET /atlas/impact/{node}
GET /atlas/dependencies/{node}
GET /atlas/critical
GET /atlas/dashboard
```

Additional endpoints will be added as new platform capabilities are implemented.

---

## Data Model

Titan Atlas currently uses Neo4j as its graph database.

The graph contains entities such as:

```text
Country
CloudProvider
AICompany
Semiconductor
TechCompany
```

and relationships describing dependencies between them.

The graph is intentionally designed to support expansion as additional real-world data sources are introduced.

---

## Risk Intelligence

Titan Atlas uses multiple analytical engines to derive risk information from the dependency graph.

Examples include:

* Risk scoring
* Resilience scoring
* Critical-node detection
* Risk ranking
* Impact analysis
* Dependency analysis
* Portfolio risk analysis
* Systemic risk analysis

The objective is not simply to assign a number to an entity, but to explain **why** that entity is important within the wider network.

---

## Data Ingestion

A dedicated ingestion architecture is being developed for external intelligence sources.

```text
backend/app/ingestion/
│
├── cloud/
├── cyber/
├── economy/
├── energy/
├── geopolitics/
└── weather/
```

These modules will eventually allow Titan Atlas to incorporate real-world events and update its risk model dynamically.

---

## Frontend Vision

The final interface is intended to provide an interactive intelligence environment containing:

* Global dependency visualization
* Interactive network graph
* Executive risk dashboard
* Node exploration
* Portfolio analysis
* Scenario simulation
* AI-generated explanations
* Real-time intelligence

The interface is being designed around the principle that complex systemic risk should be understandable without requiring the user to manually inspect the underlying graph.

---

## Development

### Backend

From the project root:

```bash
cd backend
```

Activate the Python virtual environment and install dependencies:

```bash
pip install -r requirements.txt
```

Run the API:

```bash
uvicorn main:app --reload
```

The API will normally be available at:

```text
http://127.0.0.1:8000
```

FastAPI documentation:

```text
http://127.0.0.1:8000/docs
```

---

### Frontend

From the project root:

```bash
cd frontend
```

Install dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

The frontend will normally be available at:

```text
http://localhost:5173
```

---

## Environment Variables

Sensitive credentials should never be committed to Git.

The backend uses environment variables for database configuration.

Example:

```env
NEO4J_URI=your_neo4j_uri
NEO4J_USERNAME=your_neo4j_username
NEO4J_PASSWORD=your_neo4j_password
NEO4J_DATABASE=neo4j
```

Keep `.env` out of version control.

---

## Development Principles

Titan Atlas follows several core principles:

### Build the product first

Architecture should support the product rather than become the product.

### Explain risk

Risk scores should be supported by understandable dependency chains and evidence.

### Avoid unnecessary complexity

New infrastructure should only be introduced when it solves a real problem.

### Keep the graph central

The dependency graph is the foundation of Titan Atlas's systemic-risk analysis.

### Build incrementally

Features should be implemented, tested, and integrated before moving to the next major capability.

---

## Roadmap

### Phase 1 — Foundation

* [x] Neo4j graph
* [x] Dependency relationships
* [x] FastAPI backend
* [x] Risk engines
* [x] Dashboard API
* [x] Portfolio risk analysis

### Phase 2 — Frontend

* [ ] Application layout
* [ ] Dashboard
* [ ] Node search
* [ ] Dependency visualization
* [ ] Interactive globe
* [ ] Portfolio interface

### Phase 3 — Intelligence

* [ ] AI-powered explanations
* [ ] Executive intelligence reports
* [ ] Natural-language queries
* [ ] Risk recommendations

### Phase 4 — Live Intelligence

* [ ] Cloud intelligence
* [ ] Cyber intelligence
* [ ] Geopolitical intelligence
* [ ] Economic intelligence
* [ ] Energy intelligence
* [ ] Weather intelligence

### Phase 5 — Scenario Simulation

* [ ] Failure simulation
* [ ] Cascading impact analysis
* [ ] Timeline visualization
* [ ] Scenario comparison

### Phase 6 — Production

* [ ] Authentication
* [ ] Deployment
* [ ] Monitoring
* [ ] Automated testing
* [ ] CI/CD
* [ ] Performance optimization

---

## Project Structure

```text
titan-atlas/
│
├── backend/
│   ├── app/
│   ├── scripts/
│   ├── tests/
│   ├── requirements.txt
│   └── main.py
│
├── frontend/
│   ├── public/
│   ├── src/
│   ├── package.json
│   └── vite.config.ts
│
├── docs/
│
├── ARCHITECTURE.md
├── README.md
└── .gitignore
```

---

## License

This project is currently under active development.

License and distribution terms will be defined before the first public release.

---

## Vision

Titan Atlas aims to evolve from a dependency graph into a continuously updated intelligence platform capable of answering one fundamental question:

> **"If something changes in the world, what else could be affected—and why?"**
