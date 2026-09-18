### <center>📚 RAG Document Assistant</center>
<p>A complete Retrieval-Augmented Generation (RAG) pipeline built to ingest custom academic documents, generate vector embeddings, and answer domain-specific questions using a Large Language Model (LLM). This project features a retrieval backend built with LangChain and FAISS, and an interactive web frontend powered by Streamlit.</p>

----

#### Ingested Data Sources:
The current vector database is pre-loaded with three advanced academic papers regarding retrieval systems and object detection:
<ul>
  <li>AttentionRAG: Attention-Guided Context Pruning in Retrieval-Augmented Generation.<a href="pdf/attention.pdf">PDF</a></li>
  <li>Embedding-Free RAG: An algorithmic framework leveraging LLM reasoning to replace traditional embedding-based retrieval. <a href="pdf/embedding.pdf">PDF</a></li>
  <li>RALF: Retrieval-Augmented Open-Vocabulary Object Detection. <a href="pdf/Object Detection.pdf">PDF</a></li>
</ul>
    
---

### Example Queries:
You can test the RAG model's comprehension by asking it questions based on the ingested corpus:
<ul>
  <li>"What is AttentionRAG and how does it use an answer hint prefix?"</li>
  <li>"How does Embedding-Free RAG use Levenshtein distance for anchor creation?"</li>
  <li>"What are Retrieval-Augmented Losses and visual Features (RALF)?"</li>
  <li>"How does the RAF module augment visual features with verbalized concepts?"</li>
</ul>
