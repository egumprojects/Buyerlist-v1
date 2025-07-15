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
def recommend_buyers(query_text: str, top_k: int = 5):
    # Load index and metadata
    index = faiss.read_index("vector_store/target_index.faiss")
    target_df = pd.read_csv("vector_store/target_metadata.csv")
    outreach_df = pd.read_csv("data/outreach.csv")
    buyers_df = pd.read_csv("data/buyers.csv")

    # Embed the input target
    query_vec = embed([query_text])
    query_vec = np.array(query_vec).astype("float32")

    # Search FAISS for similar past targets
    D, I = index.search(query_vec, top_k)
    matched_deals = target_df.iloc[I[0]]["deal_id"].tolist()

    # Count buyer engagements
    buyer_scores = {}
    for deal_id in matched_deals:
        engaged = outreach_df[
            (outreach_df["deal_id"] == deal_id) &
            (outreach_df["status"].str.lower() == "engaged")
        ]
        for buyer_id in engaged["buyer_id"]:
            buyer_scores[buyer_id] = buyer_scores.get(buyer_id, 0) + 1

    # Merge scores with buyer profiles
    buyer_profiles = buyers_df.set_index("buyer_id").to_dict("index")
    scored_buyers = []
    for buyer_id, score in sorted(buyer_scores.items(), key=lambda x: -x[1]):
        if buyer_id in buyer_profiles:
            bp = buyer_profiles[buyer_id]
            scored_buyers.append({
                "buyer_id": buyer_id,
                "buyer_name": bp["buyer_name"],
                "score": score,
                "description": f"{bp['buyer_type']} focused on {bp['focus_area']} ({bp['website']})"
            })

    return scored_buyers

