import streamlit as st
from src.search import RAGSearch

@st.cache_resource
def load_rag():
    return RAGSearch(llm_model="openai/gpt-oss-20b")

st.title("📚 RAG Document Assistant")

rag_search = load_rag()

query = st.text_input("Ask a question about your documents:")
if st.button("Search"):
    if query:
        with st.spinner("Searching and summarizing..."):
            answer = rag_search.search_and_summarize(query, top_k=3)
            st.success("Done!")
            st.write(answer)
    else:
        st.warning("Please enter a question.")