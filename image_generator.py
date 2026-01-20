"""
Visual Image Generator for PDF Query System
Creates actual image diagrams when run
"""

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from matplotlib.patches import FancyBboxPatch
import numpy as np

def create_system_flow_diagram():
    """Generate system flow diagram as image"""
    
    fig, ax = plt.subplots(1, 1, figsize=(12, 10))
    ax.set_xlim(0, 10)
    ax.set_ylim(0, 12)
    ax.axis('off')
    
    # Define colors
    input_color = '#E3F2FD'
    process_color = '#FFF3E0'
    output_color = '#E8F5E8'
    arrow_color = '#1976D2'
    
    # Title
    ax.text(5, 11.5, 'PDF Query System Flow', fontsize=20, fontweight='bold', 
            ha='center', va='center')
    
    # Input Stage
    ax.text(1, 10.5, 'INPUT STAGE', fontsize=14, fontweight='bold', color='#1976D2')
    
    # PDF Document box
    pdf_box = FancyBboxPatch((0.5, 9.5), 2, 0.8, boxstyle="round,pad=0.1", 
                            facecolor=input_color, edgecolor='#1976D2', linewidth=2)
    ax.add_patch(pdf_box)
    ax.text(1.5, 9.9, 'PDF Document', fontsize=10, ha='center', va='center', fontweight='bold')
    ax.text(1.5, 9.6, '(sample.pdf)', fontsize=8, ha='center', va='center')
    
    # User Query box
    query_box = FancyBboxPatch((7.5, 9.5), 2, 0.8, boxstyle="round,pad=0.1", 
                              facecolor=input_color, edgecolor='#1976D2', linewidth=2)
    ax.add_patch(query_box)
    ax.text(8.5, 9.9, 'User Query', fontsize=10, ha='center', va='center', fontweight='bold')
    ax.text(8.5, 9.6, '"What is...?"', fontsize=8, ha='center', va='center')
    
    # Processing boxes
    processes = [
        ('Text Extract\n(PyPDFLoader)', 8.5),
        ('Text Chunks\n(1000 chars)', 7.5),
        ('Embeddings\n(Vectors)', 6.5),
        ('FAISS Store\n(Vector DB)', 5.5),
        ('Similarity Search\n(Top 3)', 4.5),
        ('LLM Processing\n(OpenAI)', 3.5)
    ]
    
    for i, (text, y_pos) in enumerate(processes):
        box = FancyBboxPatch((4, y_pos-0.4), 2, 0.8, boxstyle="round,pad=0.1", 
                            facecolor=process_color, edgecolor='#FF9800', linewidth=2)
        ax.add_patch(box)
        ax.text(5, y_pos, text, fontsize=9, ha='center', va='center', fontweight='bold')
    
    # Output Stage
    ax.text(1, 2.5, 'OUTPUT STAGE', fontsize=14, fontweight='bold', color='#4CAF50')
    
    # Answer box
    answer_box = FancyBboxPatch((0.5, 1.5), 2, 0.8, boxstyle="round,pad=0.1", 
                               facecolor=output_color, edgecolor='#4CAF50', linewidth=2)
    ax.add_patch(answer_box)
    ax.text(1.5, 1.9, 'Generated', fontsize=10, ha='center', va='center', fontweight='bold')
    ax.text(1.5, 1.6, 'Answer', fontsize=10, ha='center', va='center', fontweight='bold')
    
    # Sources box
    sources_box = FancyBboxPatch((7.5, 1.5), 2, 0.8, boxstyle="round,pad=0.1", 
                                facecolor=output_color, edgecolor='#4CAF50', linewidth=2)
    ax.add_patch(sources_box)
    ax.text(8.5, 1.9, 'Source', fontsize=10, ha='center', va='center', fontweight='bold')
    ax.text(8.5, 1.6, 'References', fontsize=10, ha='center', va='center', fontweight='bold')
    
    # Arrows
    arrows = [
        # From PDF to first process
        ((1.5, 9.5), (4.5, 8.9)),
        # From query to search
        ((8.5, 9.5), (5.5, 4.9)),
        # Between processes
        ((5, 8.1), (5, 7.9)),
        ((5, 7.1), (5, 6.9)),
        ((5, 6.1), (5, 5.9)),
        ((5, 5.1), (5, 4.9)),
        ((5, 4.1), (5, 3.9)),
        # To outputs
        ((4.5, 3.1), (2, 2.3)),
        ((5.5, 3.1), (8, 2.3))
    ]
    
    for start, end in arrows:
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', color=arrow_color, lw=2))
    
    plt.tight_layout()
    plt.savefig('system_flow_diagram.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("✅ System flow diagram saved as 'system_flow_diagram.png'")

def create_input_output_comparison():
    """Create input/output comparison visualization"""
    
    fig, (ax1, ax2, ax3) = plt.subplots(3, 1, figsize=(14, 12))
    
    examples = [
        {
            'title': 'Example 1: Accuracy Query',
            'input': 'PDF: "ML Research Paper"\nQuery: "What accuracy did the neural network achieve?"',
            'output': 'Answer: "94% accuracy in diagnostic predictions,\noutperforming traditional methods by 15%"\nSource: Page 8, Results section',
            'ax': ax1
        },
        {
            'title': 'Example 2: Methodology Query', 
            'input': 'PDF: "Healthcare AI Study"\nQuery: "What data was collected?"',
            'output': 'Answer: "Data from 1000 patients across three hospitals,\nincluding medical imaging, lab results, patient history"\nSource: Page 3, Methodology section',
            'ax': ax2
        },
        {
            'title': 'Example 3: Ethics Query',
            'input': 'PDF: "AI Ethics Guidelines"\nQuery: "What are the main ethical concerns?"',
            'output': 'Answer: "Data privacy, algorithmic bias, transparency\nin decision-making, patient consent for AI diagnostics"\nSource: Pages 2-4, Ethics Framework',
            'ax': ax3
        }
    ]
    
    for example in examples:
        ax = example['ax']
        ax.set_xlim(0, 10)
        ax.set_ylim(0, 4)
        ax.axis('off')
        
        # Title
        ax.text(5, 3.5, example['title'], fontsize=14, fontweight='bold', 
                ha='center', va='center')
        
        # Input box
        input_box = FancyBboxPatch((0.5, 1), 4, 2, boxstyle="round,pad=0.2", 
                                  facecolor='#E3F2FD', edgecolor='#1976D2', linewidth=2)
        ax.add_patch(input_box)
        ax.text(0.7, 2.7, 'INPUT', fontsize=12, fontweight='bold', color='#1976D2')
        ax.text(2.5, 2, example['input'], fontsize=10, ha='center', va='center')
        
        # Output box
        output_box = FancyBboxPatch((5.5, 1), 4, 2, boxstyle="round,pad=0.2", 
                                   facecolor='#E8F5E8', edgecolor='#4CAF50', linewidth=2)
        ax.add_patch(output_box)
        ax.text(5.7, 2.7, 'OUTPUT', fontsize=12, fontweight='bold', color='#4CAF50')
        ax.text(7.5, 2, example['output'], fontsize=10, ha='center', va='center')
        
        # Arrow
        ax.annotate('', xy=(5.3, 2), xytext=(4.7, 2),
                   arrowprops=dict(arrowstyle='->', color='#FF9800', lw=3))
    
    plt.suptitle('PDF Query System - Input vs Output Examples', fontsize=16, fontweight='bold')
    plt.tight_layout()
    plt.savefig('input_output_comparison.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("✅ Input/Output comparison saved as 'input_output_comparison.png'")

def create_architecture_diagram():
    """Create system architecture diagram"""
    
    fig, ax = plt.subplots(1, 1, figsize=(14, 8))
    ax.set_xlim(0, 14)
    ax.set_ylim(0, 8)
    ax.axis('off')
    
    # Title
    ax.text(7, 7.5, 'PDF Query System Architecture', fontsize=18, fontweight='bold', 
            ha='center', va='center')
    
    # Components
    components = [
        ('PDF\nDocument', 1, 6, '#FFCDD2'),
        ('PyPDF\nLoader', 3, 6, '#F8BBD9'),
        ('Text\nSplitter', 5, 6, '#E1BEE7'),
        ('OpenAI\nEmbeddings', 7, 6, '#C5CAE9'),
        ('FAISS\nVector Store', 9, 6, '#BBDEFB'),
        ('User\nQuery', 1, 3, '#B2DFDB'),
        ('Retrieval\nQA Chain', 5, 3, '#C8E6C9'),
        ('OpenAI\nLLM', 9, 3, '#DCEDC8'),
        ('Generated\nAnswer', 13, 4.5, '#F0F4C3')
    ]
    
    for name, x, y, color in components:
        box = FancyBboxPatch((x-0.7, y-0.5), 1.4, 1, boxstyle="round,pad=0.1", 
                            facecolor=color, edgecolor='#424242', linewidth=2)
        ax.add_patch(box)
        ax.text(x, y, name, fontsize=10, ha='center', va='center', fontweight='bold')
    
    # Arrows showing data flow
    arrows = [
        ((1.7, 6), (2.3, 6)),      # PDF to Loader
        ((3.7, 6), (4.3, 6)),      # Loader to Splitter
        ((5.7, 6), (6.3, 6)),      # Splitter to Embeddings
        ((7.7, 6), (8.3, 6)),      # Embeddings to Vector Store
        ((1.7, 3), (4.3, 3)),      # Query to QA Chain
        ((9, 5.5), (5.7, 3.5)),    # Vector Store to QA Chain
        ((5.7, 3), (8.3, 3)),      # QA Chain to LLM
        ((9.7, 3), (12.3, 4.5))    # LLM to Answer
    ]
    
    for start, end in arrows:
        ax.annotate('', xy=end, xytext=start,
                   arrowprops=dict(arrowstyle='->', color='#1976D2', lw=2))
    
    # Add labels
    ax.text(7, 1, 'Data Processing Pipeline', fontsize=14, fontweight='bold', 
            ha='center', va='center', color='#1976D2')
    ax.text(2, 0.5, 'Document Processing', fontsize=12, ha='center', va='center')
    ax.text(7, 0.5, 'Query Processing', fontsize=12, ha='center', va='center')
    ax.text(12, 0.5, 'Response Generation', fontsize=12, ha='center', va='center')
    
    plt.tight_layout()
    plt.savefig('system_architecture.png', dpi=300, bbox_inches='tight')
    plt.show()
    print("✅ System architecture saved as 'system_architecture.png'")

def main():
    """Generate all visual diagrams"""
    print("🎨 Generating PDF Query System Visual Diagrams...")
    print("=" * 50)
    
    # Generate all diagrams
    create_system_flow_diagram()
    create_input_output_comparison()
    create_architecture_diagram()
    
    print("\n🎉 All diagrams generated successfully!")
    print("Files created:")
    print("- system_flow_diagram.png")
    print("- input_output_comparison.png") 
    print("- system_architecture.png")

if __name__ == "__main__":
    main()