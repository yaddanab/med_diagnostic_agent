# """
# Medical Diagnostic Agent System

# This is the main entry point for the Medical Diagnostic Agent application.
# It imports and runs the Streamlit interface for the diagnostic agent.

# Author: [Your Name]
# Date: April 2025
# """

# import os
# import json
# import streamlit as st
# from diagnostic_agent import DiagnosticAgent

# # Ensure the knowledge base file exists
# def setup_knowledge_base():
#     """Create the knowledge base file if it doesn't exist."""
#     kb_path = "knowledge_base.json"
    
#     if not os.path.exists(kb_path):
#         # If knowledge_base.json doesn't exist, create it from the sample file
#         sample_kb_path = "sample_knowledge_base.json"
        
#         # Create the sample knowledge base file if it doesn't exist
#         if not os.path.exists(sample_kb_path):
#             with open(sample_kb_path, 'w') as f:
#                 from knowledge_base_data import knowledge_base
#                 json.dump(knowledge_base, f, indent=2)
        
#         # Copy the sample file to the main knowledge base file
#         with open(sample_kb_path, 'r') as source:
#             with open(kb_path, 'w') as target:
#                 json.dump(json.load(source), target, indent=2)
    
#     return kb_path

# # Create knowledge_base_data.py to store the knowledge base as a Python dictionary
# def create_knowledge_base_module():
#     """Create a Python module with the knowledge base data."""
#     kb_module_path = "knowledge_base_data.py"
    
#     if not os.path.exists(kb_module_path):
#         with open("sample_knowledge_base.json", 'r') as f:
#             kb_data = json.load(f)
        
#         with open(kb_module_path, 'w') as f:
#             f.write("# Knowledge base data for the Medical Diagnostic Agent\n\n")
#             f.write("knowledge_base = ")
#             f.write(json.dumps(kb_data, indent=2))
#             f.write("\n")

# # Main function to run the application
# def main():
#     """Run the Streamlit interface for the Medical Diagnostic Agent."""
#     # Import the Streamlit interface
#     from streamlit_interface import main as run_interface
    
#     # Run the interface
#     run_interface()

# if __name__ == "__main__":
#     # Create the knowledge base module
#     create_knowledge_base_module()
    
#     # Setup the knowledge base
#     setup_knowledge_base()
    
#     # Run the main application
#     main()


"""
Medical Diagnostic Agent System

This is the main entry point for the Medical Diagnostic Agent application.
It imports and runs the enhanced Streamlit interface for the diagnostic agent.

Author: [Your Name]
Date: April 2025
"""

import os
import json
import streamlit as st
from diagnostic_agent import DiagnosticAgent

# Ensure the knowledge base file exists
def setup_knowledge_base():
    """Create the knowledge base file if it doesn't exist."""
    kb_path = "knowledge_base.json"
    
    if not os.path.exists(kb_path):
        # If knowledge_base.json doesn't exist, create it from the sample file
        sample_kb_path = "sample_knowledge_base.json"
        
        # Create the sample knowledge base file if it doesn't exist
        if not os.path.exists(sample_kb_path):
            with open(sample_kb_path, 'w') as f:
                from knowledge_base_data import knowledge_base
                json.dump(knowledge_base, f, indent=2)
        
        # Copy the sample file to the main knowledge base file
        with open(sample_kb_path, 'r') as source:
            with open(kb_path, 'w') as target:
                json.dump(json.load(source), target, indent=2)
    
    return kb_path

# Create knowledge_base_data.py to store the knowledge base as a Python dictionary
def create_knowledge_base_module():
    """Create a Python module with the knowledge base data."""
    kb_module_path = "knowledge_base_data.py"
    
    if not os.path.exists(kb_module_path):
        with open("sample_knowledge_base.json", 'r') as f:
            kb_data = json.load(f)
        
        with open(kb_module_path, 'w') as f:
            f.write("# Knowledge base data for the Medical Diagnostic Agent\n\n")
            f.write("knowledge_base = ")
            f.write(json.dumps(kb_data, indent=2))
            f.write("\n")

# Main function to run the application
def main():
    """Run the Streamlit interface for the Medical Diagnostic Agent."""
    # Import the enhanced Streamlit interface
    from streamlit_interface import main as run_interface
    
    # Run the interface
    run_interface()

if __name__ == "__main__":
    # Create the knowledge base module
    create_knowledge_base_module()
    
    # Setup the knowledge base
    setup_knowledge_base()
    
    # Run the main application
    main()