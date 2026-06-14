from app.engines.titan_engine import run_dynamic_simulation


def compare_failure_risk(
    original_node,
    alternative_node
):

    original = run_dynamic_simulation(
        original_node
    )

    alternative = run_dynamic_simulation(
        alternative_node
    )

    return {
        "original": {
            "node": original_node,
            "blast_radius":
                original["simulation"]["blast_radius"]
        },

        "alternative": {
            "node": alternative_node,
            "blast_radius":
                alternative["simulation"]["blast_radius"]
        },

        "risk_difference":
            original["simulation"]["blast_radius"]
            -
            alternative["simulation"]["blast_radius"]
    }