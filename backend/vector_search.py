import pandas as pd
import numpy as np
import faiss

import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..', '..')))

from backend.embed_model import embed




def load_target_data():
    # Load the metadata for embedded targets
    metadata_path = "vector_store/target_metadata.csv"
    targets_df = pd.read_csv(metadata_path)
    return targets_df




def search_similar_targets(query_vec, top_k=5):
    # Load FAISS index
    index_path = "vector_store/target_index.faiss"
    index = faiss.read_index(index_path)


    # Ensure query_vec is in correct shape
    query_vec = np.array(query_vec).astype("float32")
    if len(query_vec.shape) == 1:
        query_vec = query_vec.reshape(1, -1)


    # Run search
    D, I = index.search(query_vec, top_k)
    return I[0]  # Return list of row indices




def recommend_buyers(query_text: str, top_k: int = 5):
    # Embed the query
    query_vec = embed([query_text])
    matched_indices = search_similar_targets(query_vec,top_k=top_k)



    # Load target metadata and buyer info
    targets_df = load_target_data()
    outreach_df = pd.read_csv("data/outreach.csv")
    buyers_df = pd.read_csv("data/buyers.csv")


    # Search similar past targets
    matched_indices = search_similar_targets(query_vec, top_k=top_k)
    matched_deals = targets_df.iloc[matched_indices]["deal_id"].tolist()


    # Score buyers based on engagement across matched deals
    buyer_scores = {}
    for deal_id in matched_deals:
        engaged = outreach_df[
            (outreach_df["deal_id"] == deal_id) &
            (outreach_df["status"].str.lower() == "engaged")
        ]
        for buyer_id in engaged["buyer_id"]:
            buyer_scores[buyer_id] = buyer_scores.get(buyer_id, 0) + 1


    # Merge with buyer metadata
    buyer_profiles = buyers_df.set_index("buyer_id").to_dict("index")
    ranked_buyers = []
    for buyer_id, score in sorted(buyer_scores.items(), key=lambda x: -x[1]):
        if buyer_id in buyer_profiles:
            profile = buyer_profiles[buyer_id]
            ranked_buyers.append({
                "buyer_name": profile["buyer_name"],
                "score": score,
                "description": f"{profile['buyer_type']} focused on {profile['focus_area']} ({profile['website']})"
            })

    print("Matched deals:",matched_deals)
    print("Buyer scores",buyer_scores)
    return ranked_buyers


