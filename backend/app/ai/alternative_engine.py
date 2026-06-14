ALTERNATIVES = {

    "AWS": [
        "Azure",
        "Google Cloud"
    ],

    "Azure": [
        "AWS",
        "Google Cloud"
    ],

    "Google Cloud": [
        "AWS",
        "Azure"
    ],

    "NVIDIA": [
        "AMD"
    ],

    "TSMC": [],

    "ASML": []
}


def get_alternatives(node_name):

    alternatives = ALTERNATIVES.get(
        node_name,
        []
    )

    return {
        "node": node_name,
        "alternatives": alternatives
    }