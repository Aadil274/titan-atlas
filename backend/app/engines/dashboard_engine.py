from app.engines.network_summary_engine import (
    generate_network_summary
)

from app.engines.critical_node_engine import (
    get_critical_nodes
)

from app.engines.risk_ranking_engine import (
    generate_network_ranking
)

from app.engines.portfolio_risk_engine import (
    analyze_portfolio
)

def generate_dashboard():

    network_summary = (
        generate_network_summary()
    )

    critical_nodes = (
        get_critical_nodes()
    )

    rankings = (
        generate_network_ranking()
    )

    portfolio_hotspots = analyze_portfolio([
        "OpenAI",
        "Anthropic",
        "Cohere"
    ])

    return {

        "network_summary":
            network_summary,

        "critical_nodes":
            critical_nodes,

        "systemic_rankings":
            rankings["rankings"][:10],

        "portfolio_hotspots":
            portfolio_hotspots
    }