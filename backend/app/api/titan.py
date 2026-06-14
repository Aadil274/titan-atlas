from fastapi import APIRouter

from app.engines.systemic_risk_engine import (
    calculate_systemic_risk
)

from app.engines.scenario_comparison_engine import (
    compare_scenarios
)

from app.engines.portfolio_risk_engine import (
    analyze_portfolio
)

from app.engines.vulnerability_engine import (
    calculate_vulnerability
)

from app.engines.risk_ranking_engine import (
    generate_network_ranking
)

from app.engines.comparative_risk_engine import (
    compare_risk
)

from app.engines.risk_exposure_engine import (
    generate_risk_exposure_report
)

from app.engines.hidden_dependency_engine import (
    find_hidden_dependencies
)

from app.ai.alternative_engine import (
    get_alternatives
)

from app.ai.recommendation_engine import (
    generate_recommendations
)

from app.engines.counterfactual_engine import (
    compare_failure_risk
)

from app.engines.resilience_score_engine import (
    calculate_resilience_score
)

from app.engines.resilience_engine import (
    find_single_points_of_failure,
    recommend_mitigation
)

from app.engines.titan_engine import (
    run_dynamic_simulation
)

from app.simulation.scenario_engine import (
    run_scenario
)

from app.ai.reasoning_engine import (
    analyze_question
)

from app.ai.narrative_engine import (
    generate_narrative
)

from app.engines.multi_simulation_engine import (
    run_multi_simulation
)

from app.engines.root_cause_engine import (
    explain_dependency
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

    analysis = analyze_question(question)

    query_type = analysis["query_type"]

    entities = analysis["entities"]

    if not entities:

        return {
            "question": question,
            "error": "No known entity found"
        }

    if query_type == "failure":

        entity = entities[0]

        result = run_dynamic_simulation(entity)

        narrative = generate_narrative(
            result["simulation"]
        )

        return {
            "question": question,
            "type": "failure",
            "entity": entity,
            "result": result,
            "narrative": narrative
        }

    if query_type == "multi_failure":

        results = run_multi_simulation(
            entities
        )

        return {
            "question": question,
            "type": "multi_failure",
            "entities": entities,
            "results": results
        }

    if query_type == "root_cause":

        entity = entities[0]

        dependency_chain = explain_dependency(
            entity
        )

        return {
            "question": question,
            "type": "root_cause",
            "entity": entity,
            "dependency_chain": dependency_chain
        }

    if query_type == "dependency_failure":

        if len(entities) < 2:

            return {
                "question": question,
                "error": "Dependency target not found"
            }

        dependency = entities[-1]

        result = run_dynamic_simulation(
            dependency
        )

        narrative = generate_narrative(
            result["simulation"]
        )

        return {
            "question": question,
            "type": "dependency_failure",
            "target": dependency,
            "result": result,
            "narrative": narrative
        }

    return {
        "question": question,
        "type": "unknown",
        "message": "Unable to understand question."
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

@router.get("/compare")
def compare_nodes(
    original: str,
    alternative: str
):

    return compare_failure_risk(
        original,
        alternative
    )

@router.get("/resilience/spof")
def spof_analysis():

    return find_single_points_of_failure()

@router.get("/resilience/recommend/{node_name}")
def mitigation(node_name: str):

    return recommend_mitigation(node_name)

@router.get("/resilience/score/{node_name}")
def resilience_score(node_name: str):

    result = calculate_resilience_score(
        node_name
    )

    if not result:
        return {
            "error": "Node not found"
        }

    return result

@router.get("/recommend/{node_name}")
def recommend(node_name: str):

    result = generate_recommendations(
        node_name
    )

    if not result:
        return {
            "error": "Node not found"
        }

    return result

@router.get("/alternatives/{node_name}")
def alternatives(node_name: str):

    return get_alternatives(node_name)

@router.get("/hidden/{node_name}")
def hidden_dependencies(node_name: str):

    result = find_hidden_dependencies(
        node_name
    )

    if not result:
        return {
            "error": "Node not found"
        }

    return result

@router.get("/risk/{node_name}")
def risk_report(node_name: str):

    report = generate_risk_exposure_report(
        node_name
    )

    return report

@router.get("/compare-risk")
def compare_entities(
    node1: str,
    node2: str
):

    return compare_risk(
        node1,
        node2
    )

@router.get("/rankings")
def network_rankings():

    return generate_network_ranking()

@router.get("/vulnerability/{node_name}")
def vulnerability(node_name: str):

    result = calculate_vulnerability(
        node_name
    )

    if not result:
        return {
            "error": "Node not found"
        }

    return result

@router.post("/portfolio")
def portfolio_analysis(nodes: list[str]):

    return analyze_portfolio(
        nodes
    )

@router.post("/compare")
def compare(nodes: list[str]):

    return compare_scenarios(nodes)

@router.get("/systemic-risk/{node_name}")
def systemic_risk(node_name):

    result = calculate_systemic_risk(
        node_name
    )

    if not result:
        return {
            "error": "Node not found"
        }

    return result