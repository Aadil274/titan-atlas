from app.database.neo4j import neo4j_conn

def seed_graph():

    query = """
    MERGE (usa:Country {name:'USA',
    aliases:[
        'usa',
        'united states',
        'united states of america']})
    MERGE (china:Country {name:'China', aliases:['china']})
    MERGE (south_korea:Country {name:'South Korea', aliases:['south korea']})
    MERGE (japan:Country {name:'Japan', aliases:['japan']})
    MERGE (india:Country {name:'India', aliases:['india']})
    MERGE (taiwan:Country {name:'Taiwan', aliases:['taiwan']})

    MERGE (aws:CloudProvider {
    name:'AWS',
    aliases:[
        'aws',
        'amazon web services',
        'amazon cloud'
    ]
    })
    MERGE (google_cloud:CloudProvider {
    name:'Google Cloud',
    aliases:[
        'google cloud',
        'gcp'
    ]
    })
    MERGE (oracle_cloud:CloudProvider {
    name:'Oracle Cloud',
    aliases:[
        'oracle cloud'
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
    MERGE (meta_ai:AICompany {name:'Meta AI', aliases:['meta ai', 'facebook ai']})
    MERGE (xai:AICompany {name:'xAI', aliases:['xAI', 'x.ai']})
    MERGE (mistral:AICompany {name:'Mistral', aliases:['mistral']})
    MERGE (cohere:AICompany {name:'Cohere', aliases:['cohere']})
    MERGE (anthropic:AICompany {name:'Anthropic'})

    MERGE (tsmc:Semiconductor {name:'TSMC'})
    MERGE (samsung:Semiconductor {name:'Samsung'})
    MERGE (intel:Semiconductor {name:'Intel'})
    MERGE (amd:Semiconductor {name:'AMD'})
    MERGE (broadcom:Semiconductor {name:'Broadcom'})
    MERGE (qualcomm:Semiconductor {name:'Qualcomm'})
    MERGE (asml:Semiconductor {name:'ASML'})
    MERGE (nvidia:Semiconductor {name:'NVIDIA'})

    MERGE (microsoft:TechCompany {name:'Microsoft', aliases:['microsoft']})
    MERGE (google:TechCompany {name:'Google', aliases:['google']})
    MERGE (meta:TechCompany {name:'Meta', aliases:['meta']})
    MERGE (amazon:TechCompany {name:'Amazon', aliases:['amazon']})
    MERGE (apple:TechCompany {name:'Apple', aliases:['apple']})

    MERGE (microsoft)-[:OWNS]->(azure)
    MERGE (amazon)-[:OWNS]->(aws)
    MERGE (google)-[:OWNS]->(gcp)

    MERGE (microsoft)-[:PARTNERS_WITH]->(openai)

    MERGE (amazon)-[:PARTNERS_WITH]->(anthropic)

    MERGE (google)-[:PARTNERS_WITH]->(anthropic)

    MERGE (openai)-[:DEPENDS_ON]->(azure)

    MERGE (anthropic)-[:DEPENDS_ON]->(aws)

    MERGE (cohere)-[:DEPENDS_ON]->(gcp)

    MERGE (azure)-[:DEPENDS_ON]->(nvidia)

    MERGE (aws)-[:DEPENDS_ON]->(nvidia)

    MERGE (gcp)-[:DEPENDS_ON]->(nvidia)

    MERGE (nvidia)-[:DEPENDS_ON]->(tsmc)

    MERGE (tsmc)-[:DEPENDS_ON]->(asml)

    MERGE (nvidia)-[:SUPPLIED_BY]->(tsmc)

    MERGE (aws)-[:LOCATED_IN]->(usa)
    MERGE (tsmc)-[:LOCATED_IN]->(taiwan)

    MERGE (samsung)-[:LOCATED_IN]->(korea)

    MERGE (intel)-[:LOCATED_IN]->(usa)

    MERGE (asml)-[:LOCATED_IN]->(japan)

    MERGE (microsoft)-[:LOCATED_IN]->(usa)

    MERGE (google)-[:LOCATED_IN]->(usa)

    MERGE (amazon)-[:LOCATED_IN]->(usa)


    MERGE (asml)-[:SUPPLIES]->(tsmc)

    MERGE (tsmc)-[:SUPPLIES]->(nvidia)
    MERGE (tsmc)-[:SUPPLIES]->(amd)
    MERGE (tsmc)-[:SUPPLIES]->(apple)

    MERGE (nvidia)-[:SUPPLIES]->(microsoft)
    MERGE (nvidia)-[:SUPPLIES]->(google)
    MERGE (nvidia)-[:SUPPLIES]->(meta)

    MERGE (amd)-[:SUPPLIES]->(google)

    MERGE (nvidia)-[:AFFECTS]->(aws)

    MERGE (aws)-[:HOSTS]->(openai)
    MERGE (microsoft)-[:HOSTS]->(azure)
    MERGE (google)-[:HOSTS]->(gcp)
    MERGE (amazon)-[:HOSTS]->(aws)

    MERGE (azure)-[:HOSTS]->(openai)
    MERGE (aws)-[:HOSTS]->(anthropic)

    MERGE (gcp)-[:HOSTS]->(cohere)

    MERGE (meta)-[:HOSTS]->(metaai)
    """

    with neo4j_conn.driver.session() as session:
        session.run(query)

    print("Graph seeded successfully.")