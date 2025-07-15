import pandas as pd

def load_target_data():
    # Simulate loading some fake deal and buyer data
    targets_df = pd.DataFrame({
        "deal_id": [1, 2],
        "description": ["AI company in healthcare", "Cloud logistics platform"]
    })

    embeddings = [[0.0] * 384, [0.0] * 384]  # Dummy vectors

    deal_to_buyers = {
        1: ["Alpha Partners", "Beta Capital"],
        2: ["Gamma Ventures"]
    }

    buyer_meta = {
        "Alpha Partners": "Private equity firm focused on tech-enabled services.",
        "Beta Capital": "Middle-market investor in software.",
        "Gamma Ventures": "Growth equity for logistics and mobility."
    }

    return targets_df, embeddings, deal_to_buyers, buyer_meta

def search_similar_targets(query_vec, targets_df, embeddings):
    # Just return all rows for now
    return targets_df
