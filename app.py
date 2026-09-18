from src.data_loader import load_all_documents
from src.vectorstore import FaissVectorStore
from src.search import RAGSearch

if __name__ == "__main__":
    docs = load_all_documents("data")
    store = FaissVectorStore("faiss_store")
    
    # 1. Build the index on the first run (uncommented)
    store.build_from_documents(docs)
    
    # 2. Comment this out until the index actually exists
    # store.load() 
    
    rag_search = RAGSearch()
    query = "What is attention mechanism?"
    summary = rag_search.search_and_summarize(query, top_k=3)
    print("Summary:", summary)