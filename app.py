import streamlit as st
import numpy as np
import faiss
from sentence_transformers import SentenceTransformer
import json

# Load embeddings and item URLs
embeddings = np.load("./embeddings.npy", allow_pickle=True)
item_urls = np.load("./items_urls.npy", allow_pickle=True)

# Create the FAISS index
index = faiss.IndexFlatL2(embeddings.shape[1])
index.add(embeddings)

# Load the SentenceTransformer model
model = SentenceTransformer('sentence-transformers/stsb-roberta-base')

def returnTopNSimilar(query_string, n):
    query_vector = model.encode([query_string])
    distances, indices = index.search(query_vector, n)
    similar_items = item_urls[indices]
    return [{'url': url, 'link': f'<a href="{url}" target="_blank">{url}</a>'} for url in similar_items.tolist()]  # Convert ndarray to list

def main():
    st.title("Clothing Similarity Search")

    # Get user input
    query = st.text_input("Enter a query")
    num_links = st.number_input("Number of links to return", min_value=1, value=5)

    if st.button("Search"):
        # Get similar items
        similar_items = returnTopNSimilar(query, num_links)

        # Prepare JSON response
        response = {'similar_items': similar_items}

        # Convert links to HTML rendering
        rendered_links = [item['link'] for item in similar_items]
        rendered_html = '<br>'.join(rendered_links)

        # Display JSON response with clickable links
        st.markdown(f"JSON Response:\n\n```{json.dumps(response, indent=4)}```", unsafe_allow_html=True)


if __name__ == "__main__":
    main()
