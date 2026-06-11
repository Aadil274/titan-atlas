from fastapi import APIRouter
from app.engines.atlas_engine import analyze_impact
from fastapi import HTTPException




from app.graph.graph_queries import (
    find_node,
    get_node_dependencies
)

router = APIRouter(
    prefix="/atlas",
    tags=["Atlas"]
)

# @router.get("/node/{node_name}")
# def get_node(node_name: str):

#     dependencies = get_node_dependencies(
#         node_name
#     )

#     return {
#         "node": node_name,
#         "dependencies": dependencies
#     }

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

@router.get("/impact/{node_name}")
def get_impact(node_name: str):

    return analyze_impact(node_name)