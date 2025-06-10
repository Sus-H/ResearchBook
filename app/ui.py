# app/ui.py
import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
# ...existing code...
import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from app.crawler import fetch_author_data
from app.graph_builder import build_graph
from app.brief_generator import generate_brief

st.title("ResearchBook: Forskar-nätverk")

author_id = st.text_input("Ange Semantic Scholar Author ID:", "145689385")

if st.button("Bygg graf"):
    with st.spinner("Hämtar data..."):
        data = fetch_author_data(author_id)
        graph = build_graph(data)
        brief = generate_brief(graph, data["name"])
        
        st.subheader("Intelligence Brief")
        st.text(brief)

        st.subheader("Co-author Graf")
        fig, ax = plt.subplots(figsize=(10, 7))
        # Rita grafen med networkx
        nx.draw(
            graph,
            with_labels=True,
            node_color="lightblue",
            edge_color="gray",
            node_size=500,
            font_size=10,
            ax=ax
        )
        st.pyplot(fig)
