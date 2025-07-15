import pandas as pd
import numpy as np
import faiss
from backend.embeddings import embed

def load_target_data():
    df = pd.read_csv("data/targets.csv")
    buyers = pd.read_csv("data/outreach.csv")

    # Embedding cache or re-embed
    vectors = embed(df["description"].tolist())

    # Build FAISS index
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(np.array(vectors))

    # Map deal_id → list of buyers who engaged
    deal_to_buyers = {}
    for _, row in buyers.iterrows():
        if row["status"].lower() == "engaged":
            deal_to_buyers.setdefault(row["deal_id"], []).append(row["buyer_name"])

    return df, vectors, deal_to_buyers

def search_similar_targets(query_vector, df, vector_store, k=5):
    D, I = vector_store.search(query_vector, k)
    return df.iloc[I[0]]
