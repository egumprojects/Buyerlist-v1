from sentence_transformers import SentenceTransformer


# Load model once at import
model = SentenceTransformer("all-MiniLM-L6-v2")


def embed(text_list):
    return model.encode(text_list, show_progress_bar=False).tolist()
