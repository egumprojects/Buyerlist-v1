import pandas as pd
import numpy as np
import faiss
import os
from sentence_transformers import SentenceTransformer

# Load and prepare data
targets_path = "data/targets.csv"
output_dir = "vector_store"
os.makedirs(output_dir, exist_ok=True)

print("🔄 Loading target data...")
df = pd.read_csv(targets_path)

# Combine relevant fields for embedding
df["text"] = df["target_name"] + ". " + df["description"] + ". Industry: " + df["industry"]

# Load embedding model
print("📦 Loading embedding model...")
model = SentenceTransformer("all-MiniLM-L6-v2")

# Generate embeddings
print("🧠 Embedding descriptions...")
embeddings = model.encode(df["text"].tolist(), show_progress_bar=True)
embeddings = np.array(embeddings).astype("float32")

# Create and save FAISS index
print("📁 Building FAISS index...")
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

faiss.write_index(index, f"{output_dir}/target_index.faiss")
df.drop(columns=["text"]).to_csv(f"{output_dir}/target_metadata.csv", index=False)

print("✅ Embeddings and index saved to 'vector_store/'")


