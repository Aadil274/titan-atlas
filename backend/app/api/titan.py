from fastapi import APIRouter
from app.ai.explanation_engine import interpret_query

from app.ai.executive_briefs import generate_brief
from app.engines.titan_engine import (
    run_dynamic_simulation
)

from app.simulation.scenario_engine import (
    run_scenario,
    simulate_failure
)

from app.ai.explanation_engine import (
    extract_entity
)

router = APIRouter(
    prefix="/titan",
    tags=["Titan"]
)

@router.post("/scenario/{scenario_id}")
def execute_scenario(scenario_id: str):

    result = run_scenario(scenario_id)

    if not result:
        return {
            "error": "Scenario not found"
        }

    return result

@router.post("/ask")
def ask_titan(question: str):

    entity = extract_entity(question)

    if not entity:
        return {
            "error": "No known entity found"
        }

    result = run_dynamic_simulation(entity)

    return {
        "question": question,
        "entity": entity,
        "result": result
    }
@router.post("/simulate/{node_name}")
def simulate(node_name: str):

    result = simulate_failure(node_name)

    if not result:
        return {
            "error": "Node not found"
        }

    return result

@router.post("/ask")
def ask_titan(question: str):

    scenario_id = interpret_query(question)

    if not scenario_id:
        return {
            "error": "Unable to identify scenario"
        }

    simulation = run_scenario(scenario_id)

    brief = generate_brief(simulation)

    return {
        "question": question,
        "scenario": scenario_id,
        "report": brief
    }

@router.post("/analyze/{node_name}")
def analyze_node(node_name):

    result = run_dynamic_simulation(
        node_name
    )

    if not result:
        return {
            "error": "Node not found"
        }

    return result