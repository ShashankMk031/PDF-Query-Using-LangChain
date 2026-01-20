"""
PDF Query System using LangChain
Academic implementation for demonstration purposes
"""

import os
from typing import List, Dict
from langchain.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains import RetrievalQA
from langchain.llms import OpenAI
from dotenv import load_dotenv

class PDFQuerySystem:
    def __init__(self, openai_api_key: str = None):
        """Initialize the PDF Query System"""
        load_dotenv()
        
        # Set up OpenAI API key
        if openai_api_key:
            os.environ["OPENAI_API_KEY"] = openai_api_key
        elif not os.getenv("OPENAI_API_KEY"):
            print("Warning: OpenAI API key not found. Set OPENAI_API_KEY environment variable.")
        
        # Initialize components
        self.embeddings = OpenAIEmbeddings()
        self.llm = OpenAI(temperature=0)
        self.vectorstore = None
        self.qa_chain = None
        self.documents = []
        
    def load_pdf(self, pdf_path: str) -> List[Dict]:
        """Load and process PDF document"""
        print(f"Loading PDF: {pdf_path}")
        
        # Load PDF
        loader = PyPDFLoader(pdf_path)
        documents = loader.load()
        
        # Split text into chunks
        text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len
        )
        
        # Split documents
        split_docs = text_splitter.split_documents(documents)
        self.documents = split_docs
        
        print(f"Loaded {len(documents)} pages, split into {len(split_docs)} chunks")
        return split_docs
    
    def create_vectorstore(self):
        """Create vector store from loaded documents"""
        if not self.documents:
            raise ValueError("No documents loaded. Call load_pdf() first.")
        
        print("Creating vector store...")
        self.vectorstore = FAISS.from_documents(
            documents=self.documents,
            embedding=self.embeddings
        )
        
        # Create QA chain
        self.qa_chain = RetrievalQA.from_chain_type(
            llm=self.llm,
            chain_type="stuff",
            retriever=self.vectorstore.as_retriever(search_kwargs={"k": 3}),
            return_source_documents=True
        )
        
        print("Vector store created successfully!")
    
    def query(self, question: str) -> Dict:
        """Query the PDF document"""
        if not self.qa_chain:
            raise ValueError("Vector store not created. Call create_vectorstore() first.")
        
        print(f"\nProcessing query: {question}")
        
        # Get response
        result = self.qa_chain({"query": question})
        
        # Extract relevant information
        answer = result["result"]
        source_docs = result["source_documents"]
        
        # Format response
        response = {
            "question": question,
            "answer": answer,
            "sources": []
        }
        
        # Add source information
        for i, doc in enumerate(source_docs):
            source_info = {
                "chunk_id": i + 1,
                "page": doc.metadata.get("page", "Unknown"),
                "content_preview": doc.page_content[:200] + "..." if len(doc.page_content) > 200 else doc.page_content
            }
            response["sources"].append(source_info)
        
        return response
    
    def display_results(self, result: Dict):
        """Display query results in a formatted way"""
        print("\n" + "="*60)
        print("QUERY RESULTS")
        print("="*60)
        print(f"Question: {result['question']}")
        print(f"\nAnswer: {result['answer']}")
        print(f"\nSources ({len(result['sources'])} relevant chunks):")
        
        for source in result["sources"]:
            print(f"\n  Chunk {source['chunk_id']} (Page {source['page']}):")
            print(f"  {source['content_preview']}")
        
        print("="*60)

def main():
    """Main demonstration function"""
    # Initialize system
    pdf_system = PDFQuerySystem()
    
    # Example usage (would need actual PDF file)
    pdf_path = "sample_document.pdf"  # Replace with actual PDF path
    
    try:
        # Load PDF
        pdf_system.load_pdf(pdf_path)
        
        # Create vector store
        pdf_system.create_vectorstore()
        
        # Example queries
        sample_queries = [
            "What is the main topic of this document?",
            "Can you summarize the key findings?",
            "What methodology was used in this research?"
        ]
        
        # Process queries
        for query in sample_queries:
            result = pdf_system.query(query)
            pdf_system.display_results(result)
            
    except FileNotFoundError:
        print(f"PDF file not found: {pdf_path}")
        print("Please provide a valid PDF file path.")
    except Exception as e:
        print(f"Error: {str(e)}")

if __name__ == "__main__":
    main()