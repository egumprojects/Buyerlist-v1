import pandas as pd
import faiss
from backend.embeddings import embed

def find_similar_buyers(description, industry):
    df = pd.read_csv('data/targets.csv')
    vectors = embed(df['description'].tolist())
    index = faiss.IndexFlatL2(vectors.shape[1])
    index.add(vectors)

    query_vec = embed([f"{description}. Industry: {industry}"])
    D, I = index.search(query_vec, 5)
    return df.iloc[I[0]]
