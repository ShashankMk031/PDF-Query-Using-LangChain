"""
Demo Example - PDF Query System
Shows input/output comparison for academic demonstration
Generates visual images when run
"""

import matplotlib.pyplot as plt
from matplotlib.patches import FancyBboxPatch

class PDFQueryDemo:
    """Simulated demo showing system behavior"""
    
    def __init__(self):
        self.sample_pdf_content = """
        Research Paper: Machine Learning in Healthcare
        
        Abstract: This paper explores the application of machine learning 
        techniques in healthcare diagnostics. We present a comprehensive 
        analysis of various algorithms including neural networks, decision 
        trees, and support vector machines.
        
        Introduction: Healthcare systems worldwide are increasingly adopting 
        artificial intelligence solutions to improve patient outcomes and 
        reduce costs. Machine learning, a subset of AI, has shown particular 
        promise in diagnostic applications.
        
        Methodology: We collected data from 1000 patients across three 
        hospitals. The dataset included medical imaging, lab results, and 
        patient history. We applied preprocessing techniques including 
        normalization and feature selection.
        
        Results: Our neural network model achieved 94% accuracy in 
        diagnostic predictions, outperforming traditional methods by 15%.
        The decision tree model showed 89% accuracy with better 
        interpretability.
        
        Conclusion: Machine learning demonstrates significant potential 
        in healthcare diagnostics, with neural networks showing the 
        highest accuracy rates.
        """
    
    def demonstrate_queries(self):
        """Show example input/output scenarios"""
        
        print("PDF QUERY SYSTEM DEMONSTRATION")
        print("="*50)
        print("\nSample PDF Content (Simulated):")
        print("-" * 30)
        print(self.sample_pdf_content[:300] + "...")
        
        # Example queries and expected outputs
        examples = [
            {
                "input": "What is the accuracy of the neural network model?",
                "output": "The neural network model achieved 94% accuracy in diagnostic predictions, outperforming traditional methods by 15%.",
                "sources": ["Results section, discussing model performance metrics"]
            },
            {
                "input": "What methodology was used in this research?",
                "output": "The researchers collected data from 1000 patients across three hospitals. The dataset included medical imaging, lab results, and patient history. They applied preprocessing techniques including normalization and feature selection.",
                "sources": ["Methodology section, describing data collection and preprocessing"]
            },
            {
                "input": "What are the main machine learning techniques mentioned?",
                "output": "The paper mentions several machine learning techniques including neural networks, decision trees, and support vector machines. Neural networks achieved the highest accuracy at 94%, while decision trees showed 89% accuracy with better interpretability.",
                "sources": ["Abstract and Results sections, discussing various ML algorithms"]
            }
        ]
        
        for i, example in enumerate(examples, 1):
            print(f"\n{'='*50}")
            print(f"EXAMPLE {i}")
            print(f"{'='*50}")
            print(f"INPUT QUERY: {example['input']}")
            print(f"\nOUTPUT ANSWER: {example['output']}")
            print(f"\nSOURCE REFERENCES: {example['sources'][0]}")
            print("-" * 50)
    
    def show_system_architecture(self):
        """Display system architecture overview"""
        print("\nSYSTEM ARCHITECTURE")
        print("="*50)
        
        architecture = """
        1. PDF Loading (PyPDFLoader)
           ↓
        2. Text Splitting (RecursiveCharacterTextSplitter)
           ↓
        3. Embedding Generation (OpenAI Embeddings)
           ↓
        4. Vector Store Creation (FAISS)
           ↓
        5. Query Processing (RetrievalQA Chain)
           ↓
        6. Answer Generation (OpenAI LLM)
        """
        
        print(architecture)
        
        print("\nKEY COMPONENTS:")
        print("- PDF Parser: Extracts text from PDF documents")
        print("- Text Splitter: Breaks text into manageable chunks")
        print("- Embeddings: Converts text to numerical vectors")
        print("- Vector Store: Enables semantic search")
        print("- QA Chain: Combines retrieval and generation")
    
    def generate_demo_image(self):
        """Generate a demo visualization image"""
        fig, ax = plt.subplots(1, 1, figsize=(12, 8))
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 8)
        ax.axis('off')
        
        # Title
        ax.text(5, 7.5, 'PDF Query System Demo', fontsize=18, fontweight='bold', 
                ha='center', va='center')
        
        # Sample PDF visualization
        pdf_box = FancyBboxPatch((0.5, 5.5), 3, 1.5, boxstyle="round,pad=0.1", 
                                facecolor='#FFE0B2', edgecolor='#FF9800', linewidth=2)
        ax.add_patch(pdf_box)
        ax.text(2, 6.2, 'Sample PDF Content', fontsize=12, ha='center', va='center', fontweight='bold')
        ax.text(2, 5.8, 'Machine Learning Research\n94% Accuracy Results', fontsize=10, ha='center', va='center')
        
        # Query box
        query_box = FancyBboxPatch((6, 5.5), 3, 1.5, boxstyle="round,pad=0.1", 
                                  facecolor='#E1F5FE', edgecolor='#03A9F4', linewidth=2)
        ax.add_patch(query_box)
        ax.text(7.5, 6.2, 'User Query', fontsize=12, ha='center', va='center', fontweight='bold')
        ax.text(7.5, 5.8, '"What accuracy did the\nneural network achieve?"', fontsize=10, ha='center', va='center')
        
        # Processing arrow
        ax.annotate('', xy=(5, 4), xytext=(5, 5.3),
                   arrowprops=dict(arrowstyle='->', color='#4CAF50', lw=3))
        ax.text(5, 4.7, 'LangChain Processing', fontsize=11, ha='center', va='center', 
                bbox=dict(boxstyle="round,pad=0.3", facecolor='#C8E6C9'))
        
        # Answer box
        answer_box = FancyBboxPatch((2, 1.5), 6, 1.5, boxstyle="round,pad=0.1", 
                                   facecolor='#E8F5E8', edgecolor='#4CAF50', linewidth=2)
        ax.add_patch(answer_box)
        ax.text(5, 2.5, 'Generated Answer', fontsize=12, ha='center', va='center', fontweight='bold')
        ax.text(5, 2, '"The neural network model achieved 94% accuracy\nin diagnostic predictions"', 
                fontsize=10, ha='center', va='center')
        ax.text(5, 1.7, 'Source: Page 8, Results section', fontsize=9, ha='center', va='center', style='italic')
        
        plt.tight_layout()
        plt.savefig('pdf_query_demo.png', dpi=300, bbox_inches='tight')
        plt.show()
        print("✅ Demo visualization saved as 'pdf_query_demo.png'")

def main():
    """Run the demonstration"""
    demo = PDFQueryDemo()
    demo.demonstrate_queries()
    demo.show_system_architecture()
    demo.generate_demo_image()
    
    print("\n🎨 Generating additional visual diagrams...")
    # Import and run the image generator
    try:
        from image_generator import main as generate_images
        generate_images()
    except ImportError:
        print("Run 'python image_generator.py' to generate additional diagrams")

if __name__ == "__main__":
    main()