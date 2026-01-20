"""
Visual Flow Diagram Generator
Creates actual image diagrams of the PDF Query System flow
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

def create_system_flow_diagram():
    """Generate ASCII flow diagram"""
    
    diagram = """
    PDF QUERY SYSTEM - VISUAL FLOW
    ================================
    
    INPUT STAGE:
    ┌─────────────┐    ┌──────────────┐
    │ PDF Document│ -> │ User Query   │
    │ (sample.pdf)│    │ "What is...?"│
    └─────────────┘    └──────────────┘
           │                    │
           v                    │
    ┌─────────────┐            │
    │ Text Extract│            │
    │ PyPDFLoader │            │
    └─────────────┘            │
           │                    │
           v                    │
    ┌─────────────┐            │
    │ Text Chunks │            │
    │ Split into  │            │
    │ 1000 chars  │            │
    └─────────────┘            │
           │                    │
           v                    │
    ┌─────────────┐            │
    │ Embeddings  │            │
    │ Vector      │            │
    │ Conversion  │            │
    └─────────────┘            │
           │                    │
           v                    │
    ┌─────────────┐            │
    │ FAISS Store │            │
    │ Vector DB   │            │
    └─────────────┘            │
           │                    │
           └────────┬───────────┘
                    │
                    v
    PROCESSING STAGE:
    ┌─────────────┐
    │ Similarity  │
    │ Search      │
    │ (Top 3)     │
    └─────────────┘
           │
           v
    ┌─────────────┐
    │ Context     │
    │ Assembly    │
    └─────────────┘
           │
           v
    ┌─────────────┐
    │ LLM         │
    │ Processing  │
    │ (OpenAI)    │
    └─────────────┘
           │
           v
    OUTPUT STAGE:
    ┌─────────────┐
    │ Generated   │
    │ Answer      │
    └─────────────┘
           │
           v
    ┌─────────────┐
    │ Source      │
    │ References  │
    └─────────────┘
    """
    
    return diagram

def create_input_output_comparison():
    """Show input vs output examples"""
    
    comparison = """
    INPUT vs OUTPUT COMPARISON
    ==========================
    
    EXAMPLE 1:
    ----------
    INPUT:
    📄 PDF: "Machine Learning Research Paper" (15 pages)
    ❓ Query: "What accuracy did the neural network achieve?"
    
    OUTPUT:
    ✅ Answer: "The neural network model achieved 94% accuracy 
              in diagnostic predictions, outperforming traditional 
              methods by 15%."
    📍 Sources: Page 8, Results section
    🔍 Confidence: High (direct match found)
    
    EXAMPLE 2:
    ----------
    INPUT:
    📄 PDF: "Healthcare AI Study" (22 pages)
    ❓ Query: "What data was collected for this research?"
    
    OUTPUT:
    ✅ Answer: "Data was collected from 1000 patients across 
              three hospitals, including medical imaging, lab 
              results, and patient history."
    📍 Sources: Page 3, Methodology section
    🔍 Confidence: High (comprehensive match)
    
    EXAMPLE 3:
    ----------
    INPUT:
    📄 PDF: "AI Ethics Guidelines" (8 pages)
    ❓ Query: "What are the main ethical concerns mentioned?"
    
    OUTPUT:
    ✅ Answer: "The main ethical concerns include data privacy, 
              algorithmic bias, transparency in decision-making, 
              and patient consent for AI-driven diagnostics."
    📍 Sources: Pages 2-4, Ethics Framework section
    🔍 Confidence: Medium (synthesized from multiple sections)
    """
    
    return comparison

def main():
    """Display visual representations"""
    print(create_system_flow_diagram())
    print("\n" + "="*60 + "\n")
    print(create_input_output_comparison())

if __name__ == "__main__":
    main()