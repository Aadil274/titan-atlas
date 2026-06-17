from fastapi import APIRouter, HTTPException

from app.engines.network_summary_engine import (
    generate_network_summary
)

from app.engines.dashboard_engine import (
    generate_dashboard
)

from app.graph.graph_queries import (
    find_node,
    get_node_dependencies
)

from app.engines.atlas_engine import analyze_impact
from app.engines.critical_node_engine import get_critical_nodes
from app.engines.dependency_engine import get_dependency_chain


router = APIRouter(
    prefix="/atlas",
    tags=["Atlas"]
)


def validate_result(result):

    if not result:
        raise HTTPException(
            status_code=404,
            detail="Node not found"
        )

    if isinstance(result, dict) and "error" in result:
        raise HTTPException(
            status_code=404,
            detail=result["error"]
        )

    return result


@router.get("/node/{search_term}")
def get_node(search_term: str):

    node = validate_result(
        find_node(search_term)
    )

    return {
        "node": node["name"],
        "type": node["type"],
        "dependencies": get_node_dependencies(
            node["name"]
        )
    }


@router.get("/impact/{search_term}")
def get_impact(search_term: str):

    return validate_result(
        analyze_impact(search_term)
    )


@router.get("/dependencies/{search_term}")
def dependencies(search_term: str):

    return validate_result(
        get_dependency_chain(search_term)
    )


@router.get("/critical")
def critical_nodes():

    return get_critical_nodes()

@router.get("/dashboard")
def dashboard():

    return generate_dashboard()

@router.get("/network-summary")
def network_summary():

    return generate_network_summary()