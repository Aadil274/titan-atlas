from fastapi import APIRouter

from app.simulation.scenario_engine import run_scenario
from app.ai.executive_briefs import generate_brief

router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


@router.get("/scenario/{scenario_id}")
def scenario_report(scenario_id):

    result = run_scenario(scenario_id)

    if not result:
        return {
            "error": "Scenario not found"
        }

    return generate_brief(result)