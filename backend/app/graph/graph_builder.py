from app.database.neo4j import neo4j_conn

def seed_graph():

    query = """
    MERGE (usa:Country {name:'USA'})
    MERGE (taiwan:Country {name:'Taiwan'})

    MERGE (aws:CloudProvider {
    name:'AWS',
    aliases:[
        'aws',
        'amazon web services',
        'amazon cloud'
    ]
    })
    MERGE (azure:CloudProvider {
    name:'Azure',
    aliases:[
        'azure',
        'microsoft azure'
    ]
    })

    MERGE (openai:AICompany {
    name:'OpenAI',
    aliases:['openai','open ai']
    })
    MERGE (anthropic:AICompany {name:'Anthropic'})

    MERGE (tsmc:Semiconductor {name:'TSMC'})
    MERGE (nvidia:Semiconductor {name:'NVIDIA'})

    MERGE (openai)-[:DEPENDS_ON]->(azure)
    MERGE (anthropic)-[:DEPENDS_ON]->(aws)

    MERGE (nvidia)-[:SUPPLIED_BY]->(tsmc)

    MERGE (tsmc)-[:LOCATED_IN]->(taiwan)
    MERGE (aws)-[:LOCATED_IN]->(usa)

    MERGE (tsmc)-[:SUPPLIES]->(nvidia)

    MERGE (nvidia)-[:AFFECTS]->(aws)

    MERGE (aws)-[:HOSTS]->(openai)
    """

    with neo4j_conn.driver.session() as session:
        session.run(query)

    print("Graph seeded successfully.")