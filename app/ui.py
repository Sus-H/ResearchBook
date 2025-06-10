import streamlit as st
import networkx as nx
import matplotlib.pyplot as plt
from app.crawler import fetch_author
from app.graph_builder import build_graph
from app.brief_generator import generate_brief

st.title("ResearchBook: Researcher Social Graph")

source = st.selectbox("Data Source", ["scholar", "odr"])
identifier = st.text_input("Author Name (scholar) or Researcher ID (odr)", "")

if st.button("Build Graph"):
    with st.spinner("Fetching data..."):
        data = fetch_author(source, identifier)
        graph = build_graph(data)
        brief = generate_brief(graph, data.get("name", "Unknown"))
        st.subheader("Intelligence Brief")
        st.text(brief)
        st.subheader("Co-author Graph")
        fig, ax = plt.subplots(figsize=(10, 7))
        nx.draw(graph, with_labels=True, node_color='lightblue', edge_color='gray', node_size=500, font_size=10, ax=ax)
        st.pyplot(fig)
