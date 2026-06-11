
from enum import Enum
class NodeType(str, Enum):
    COUNTRY = "Country"

    CloudProvider = "CloudProvider"

    AICompany = "AICompany"

    Semiconductor = "Semiconductor"

    EnergyGrid = "EnergyGrid"

    Port = "Port"

    Network = "Network"

class RelationshipType(str, Enum):
    DEPENDS_ON = "DEPENDS_ON"

    HOSTED_ON = "HOSTED_ON"

    SUPPLIED_BY = "SUPPLIED_BY"

    CONNECTED_TO = "CONNECTED_TO"

    POWERED_BY = "POWERED_BY"

    LOCATED_IN = "LOCATED_IN"

    AFFECTS = "AFFECTS"