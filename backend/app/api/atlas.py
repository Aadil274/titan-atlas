from fastapi import APIRouter, HTTPException

from app.graph.graph_queries import (
    find_node,
    get_node_dependencies
)

from app.engines.atlas_engine import (
    analyze_impact
)

from app.engines.critical_node_engine import (
    get_critical_nodes
)

from app.engines.dependency_engine import (
    get_dependency_chain
)

router = APIRouter(
    prefix="/atlas",
    tags=["Atlas"]
)


@router.get("/node/{search_term}")
def get_node(search_term: str):

    node = find_node(search_term)

    if not node:
        raise HTTPException(
            status_code=404,
            detail="Node not found"
        )

    dependencies = get_node_dependencies(
        node["name"]
    )

    return {
        "node": node["name"],
        "type": node["type"],
        "dependencies": dependencies
    }


@router.get("/impact/{search_term}")
def get_impact(search_term: str):

    result = analyze_impact(
        search_term
    )

    if "error" in result:
        raise HTTPException(
            status_code=404,
            detail=result["error"]
        )

    return result


@router.get("/analysis/{search_term}")
def get_analysis(search_term: str):

    result = analyze_impact(
        search_term
    )

    if "error" in result:
        raise HTTPException(
            status_code=404,
            detail=result["error"]
        )

    return result

@router.get("/critical")
def critical_nodes():

    return get_critical_nodes()

@router.get("/dependencies/{search_term}")
def dependencies(search_term: str):

    result = get_dependency_chain(search_term)

    if not result:
        return {
            "error": "Node not found"
        }

    return result