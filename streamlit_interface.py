# # # # """
# # # # Streamlit interface for the Medical Diagnostic Agent.

# # # # This module provides the user interface for interacting with the diagnostic agent.
# # # # """

# # # # import streamlit as st
# # # # import json
# # # # import os
# # # # from diagnostic_agent import DiagnosticAgent

# # # # # Page configuration
# # # # def configure_page():
# # # #     """Configure the Streamlit page settings."""
# # # #     st.set_page_config(
# # # #         page_title="Medical Diagnostic Agent",
# # # #         page_icon="🏥",
# # # #         layout="wide"
# # # #     )

# # # # # Initialize the agent
# # # # @st.cache_resource
# # # # def get_agent():
# # # #     """Initialize and cache the diagnostic agent."""
# # # #     kb_path = "knowledge_base.json"
# # # #     return DiagnosticAgent(kb_path)

# # # # # Display the agent's explanation for a diagnosis
# # # # def display_explanation(explanation):
# # # #     """Format and display the agent's explanation."""
# # # #     st.markdown(explanation)

# # # # # Display the agent's recommendations for a diagnosis
# # # # def display_recommendations(recommendations):
# # # #     """Format and display the agent's recommendations."""
# # # #     st.markdown(recommendations)

# # # # # Main function to run the Streamlit interface
# # # # def main():
# # # #     """Run the Streamlit interface for the Medical Diagnostic Agent."""
# # # #     # Configure the page
# # # #     configure_page()
    
# # # #     # Title and description
# # # #     st.title("Medical Diagnostic Agent System")
# # # #     st.markdown("""
# # # #     This intelligent agent uses a best-first search algorithm to suggest possible 
# # # #     diagnoses based on reported symptoms. Please select your symptoms from the list below.
    
# # # #     **Note: This is a prototype for educational purposes only and is not a substitute for professional medical advice.**
# # # #     """)
    
# # # #     # Get the agent
# # # #     agent = get_agent()
    
# # # #     # Create two columns
# # # #     col1, col2 = st.columns([1, 2])
    
# # # #     with col1:
# # # #         st.subheader("Select Your Symptoms")
        
# # # #         # Extract all symptom names from the knowledge base
# # # #         all_symptoms = [symptom['name'] for symptom_id, symptom in agent.symptoms.items()]
# # # #         all_symptoms.sort()
        
# # # #         # Create multiselect for symptoms
# # # #         selected_symptoms = st.multiselect(
# # # #             "Choose all that apply:",
# # # #             all_symptoms
# # # #         )
        
# # # #         # Add a search duration input (for educational purposes to show the search process)
# # # #         max_diagnoses = st.slider(
# # # #             "Maximum number of diagnoses to show:",
# # # #             min_value=1,
# # # #             max_value=5,
# # # #             value=3
# # # #         )
        
# # # #         # Add a diagnose button
# # # #         diagnose_button = st.button("Get Diagnosis")
    
# # # #     # Display results in the second column
# # # #     with col2:
# # # #         if diagnose_button and selected_symptoms:
# # # #             st.subheader("Diagnostic Results")
            
# # # #             # Process the symptoms
# # # #             agent.perceive(selected_symptoms)
            
# # # #             # Get diagnoses
# # # #             results = agent.act(max_diagnoses)
            
# # # #             if not results['diagnoses']:
# # # #                 st.warning("Not enough information to make a diagnosis. Please provide more symptoms.")
# # # #             else:
# # # #                 # Display each diagnosis
# # # #                 for i, diagnosis in enumerate(results['diagnoses']):
# # # #                     with st.expander(f"{i+1}. {diagnosis['condition_name']} (Confidence: {diagnosis['confidence']:.2f})"):
# # # #                         st.markdown("### Explanation")
# # # #                         display_explanation(results['explanations'][diagnosis['condition_id']])
                        
# # # #                         st.markdown("### Recommendations")
# # # #                         display_recommendations(results['recommendations'][diagnosis['condition_id']])
                
# # # #                 # Add a disclaimer
# # # #                 st.markdown("""
# # # #                 ---
# # # #                 **Disclaimer:** This is an educational prototype. The diagnoses provided are based on a simplified model
# # # #                 and should not be used for actual medical decisions. Always consult with a healthcare professional for
# # # #                 proper diagnosis and treatment.
# # # #                 """)
# # # #         elif diagnose_button:
# # # #             st.warning("Please select at least one symptom.")
# # # #         else:
# # # #             st.info("Select symptoms and click 'Get Diagnosis' to receive possible diagnoses.")
            
# # # #             # Show some information about the agent
# # # #             st.markdown("""
# # # #             ### How This Works
            
# # # #             This diagnostic agent uses a best-first search algorithm to navigate through a knowledge base of medical conditions and their associated symptoms. The search prioritizes conditions that most closely match your reported symptoms, considering factors such as:
            
# # # #             - The strength of association between symptoms and conditions
# # # #             - The presence of primary symptoms for specific conditions
# # # #             - The prevalence of different conditions
            
# # # #             For each potential diagnosis, the agent calculates a confidence score based on how well your symptoms match the condition's typical presentation.
# # # #             """)
    
# # # #     # Add information about the project at the bottom
# # # #     st.markdown("""
# # # #     ---
# # # #     ### About This Project
    
# # # #     This Medical Diagnostic Agent System was developed as a final project for ITEC 781: Artificial Intelligence and Informatics I. 
# # # #     It demonstrates the application of intelligent agent architecture and search algorithms in the healthcare domain.
    
# # # #     The system uses:
# # # #     - A reactive agent architecture with perception, reasoning, and action components
# # # #     - Best-first search algorithm for diagnosis identification
# # # #     - A knowledge base with conditions, symptoms, and their relationships
# # # #     """)

# # # # if __name__ == "__main__":
# # # #     main()


# # # """
# # # Enhanced Streamlit interface for the Medical Diagnostic Agent.

# # # This module provides an improved user interface with:
# # # 1. Color-coded confidence scores
# # # 2. Symptom categories
# # # 3. Symptom search
# # # 4. Interactive body map
# # # 5. Results visualization
# # # 6. Responsive design
# # # 7. Explanation visualization
# # # 8. Dark mode option
# # # """

# # # import streamlit as st
# # # import json
# # # import os
# # # import pandas as pd
# # # import matplotlib.pyplot as plt
# # # import numpy as np
# # # from diagnostic_agent import DiagnosticAgent
# # # from io import BytesIO
# # # import base64

# # # # Page configuration
# # # def configure_page():
# # #     """Configure the Streamlit page settings."""
# # #     st.set_page_config(
# # #         page_title="Medical Diagnostic Agent",
# # #         page_icon="🏥",
# # #         layout="wide",
# # #         initial_sidebar_state="expanded"
# # #     )

# # # # Initialize the agent
# # # @st.cache_resource
# # # def get_agent():
# # #     """Initialize and cache the diagnostic agent."""
# # #     kb_path = "knowledge_base.json"
# # #     return DiagnosticAgent(kb_path)

# # # # Group symptoms by body system
# # # def group_symptoms_by_system(symptoms):
# # #     """Group symptoms by body system for better organization."""
# # #     # Define body system categories
# # #     body_systems = {
# # #         "Respiratory": ["Cough", "Shortness of breath", "Wheezing", "Runny nose", "Sore throat"],
# # #         "Digestive": ["Nausea", "Vomiting", "Diarrhea", "Abdominal pain", "Loss of appetite"],
# # #         "Neurological": ["Headache", "Confusion", "Dizziness", "Loss of taste or smell"],
# # #         "General": ["Fever", "Fatigue", "Muscle pain", "Joint pain", "Rash", "Chest pain"]
# # #     }
    
# # #     # Categorize symptoms
# # #     categorized = {system: [] for system in body_systems}
# # #     other = []
    
# # #     for symptom_id, symptom_data in symptoms.items():
# # #         symptom_name = symptom_data["name"]
# # #         categorized_flag = False
        
# # #         for system, system_symptoms in body_systems.items():
# # #             if symptom_name in system_symptoms:
# # #                 categorized[system].append((symptom_id, symptom_name))
# # #                 categorized_flag = True
# # #                 break
                
# # #         if not categorized_flag:
# # #             other.append((symptom_id, symptom_name))
    
# # #     # Add 'Other' category if needed
# # #     if other:
# # #         categorized["Other"] = other
        
# # #     return categorized

# # # # Generate color for confidence score
# # # def get_confidence_color(score):
# # #     """Return color based on confidence score."""
# # #     if score >= 0.7:
# # #         return "green"
# # #     elif score >= 0.4:
# # #         return "orange"
# # #     else:
# # #         return "red"

# # # # Create confidence gauge chart
# # # def create_confidence_gauge(score):
# # #     """Create a gauge chart for the confidence score."""
# # #     fig, ax = plt.subplots(figsize=(3, 2), subplot_kw={'projection': 'polar'})
    
# # #     # Gauge settings
# # #     theta = np.linspace(0, 180, 100) * np.pi / 180
# # #     r = np.ones_like(theta)
    
# # #     # Color sections
# # #     ax.barh(0, 1, 0.6, theta[0], color='red', alpha=0.4)
# # #     ax.barh(0, 1, 0.6, theta[33], color='orange', alpha=0.4)
# # #     ax.barh(0, 1, 0.6, theta[66], color='green', alpha=0.4)
    
# # #     # Needle
# # #     needle_theta = score * 180 * np.pi / 180
# # #     ax.plot([0, needle_theta], [0, 0.5], color='black', linewidth=2)
    
# # #     # Clean up
# # #     ax.set_yticks([])
# # #     ax.set_xticks([])
# # #     ax.set_ylim(0, 1)
# # #     ax.set_title(f'Confidence: {score:.2f}', size=10)
# # #     ax.spines['polar'].set_visible(False)
    
# # #     return fig

# # # # Create explanation visualization
# # # def create_explanation_viz(diagnosis, agent):
# # #     """Create a visualization of symptom matches for a diagnosis."""
# # #     condition_id = diagnosis['condition_id']
# # #     condition = agent.conditions[condition_id]
    
# # #     # Get all symptoms for this condition
# # #     all_condition_symptoms = [(s_id, agent.symptoms[s_id]['name'], weight) 
# # #                              for s_id, weight in condition['symptoms'].items()]
    
# # #     # Sort by weight descending
# # #     all_condition_symptoms.sort(key=lambda x: x[2], reverse=True)
    
# # #     # Prepare data for visualization
# # #     symptom_names = [s[1] for s in all_condition_symptoms]
# # #     weights = [s[2] for s in all_condition_symptoms]
    
# # #     # Mark matched symptoms
# # #     matched = [s[1] in diagnosis['matched_symptoms'] for s in all_condition_symptoms]
# # #     colors = ['#2ecc71' if m else '#e74c3c' for m in matched]
    
# # #     # Create horizontal bar chart
# # #     fig, ax = plt.subplots(figsize=(8, max(3, len(symptom_names)*0.4)))
# # #     bars = ax.barh(symptom_names, weights, color=colors)
    
# # #     # Add legend
# # #     from matplotlib.patches import Patch
# # #     legend_elements = [
# # #         Patch(facecolor='#2ecc71', label='Matched'),
# # #         Patch(facecolor='#e74c3c', label='Not Present')
# # #     ]
# # #     ax.legend(handles=legend_elements, loc='upper right')
    
# # #     # Add labels
# # #     ax.set_title(f'Symptom Analysis for {condition["name"]}')
# # #     ax.set_xlabel('Symptom Weight')
    
# # #     # Improve appearance
# # #     ax.spines['top'].set_visible(False)
# # #     ax.spines['right'].set_visible(False)
    
# # #     return fig

# # # # Create a human body map
# # # def create_body_map():
# # #     """Create a simple human body map with clickable regions."""
# # #     # This is a placeholder HTML for a clickable body map
# # #     # In a production app, you would use a proper SVG or canvas-based solution
    
# # #     body_map_html = """
# # #     <style>
# # #     .body-map {
# # #         position: relative;
# # #         width: 200px;
# # #         height: 400px;
# # #         margin: 0 auto;
# # #         background-color: #f0f0f0;
# # #         border-radius: 100px 100px 0 0;
# # #     }
# # #     .body-region {
# # #         position: absolute;
# # #         cursor: pointer;
# # #         border: 1px solid #ddd;
# # #         border-radius: 4px;
# # #         text-align: center;
# # #         font-size: 10px;
# # #         color: #555;
# # #     }
# # #     .head {
# # #         top: 20px;
# # #         left: 75px;
# # #         width: 50px;
# # #         height: 50px;
# # #         border-radius: 25px;
# # #     }
# # #     .chest {
# # #         top: 80px;
# # #         left: 50px;
# # #         width: 100px;
# # #         height: 80px;
# # #     }
# # #     .abdomen {
# # #         top: 170px;
# # #         left: 50px;
# # #         width: 100px;
# # #         height: 80px;
# # #     }
# # #     .limbs {
# # #         top: 260px;
# # #         left: 30px;
# # #         width: 140px;
# # #         height: 120px;
# # #     }
# # #     </style>
    
# # #     <div class="body-map">
# # #         <div class="body-region head" onclick="selectRegion('head')" title="Head & Neck">Head & Neck</div>
# # #         <div class="body-region chest" onclick="selectRegion('chest')" title="Chest & Back">Chest & Back</div>
# # #         <div class="body-region abdomen" onclick="selectRegion('abdomen')" title="Abdomen">Abdomen</div>
# # #         <div class="body-region limbs" onclick="selectRegion('limbs')" title="Arms & Legs">Arms & Legs</div>
# # #     </div>
    
# # #     <script>
# # #     function selectRegion(region) {
# # #         // This would ideally communicate with Streamlit
# # #         // For now, we'll just show an alert
# # #         alert('Selected region: ' + region);
# # #     }
# # #     </script>
# # #     """
    
# # #     return body_map_html

# # # # Main function to run the Streamlit interface
# # # def main():
# # #     """Run the enhanced Streamlit interface for the Medical Diagnostic Agent."""
# # #     # Configure the page
# # #     configure_page()
    
# # #     # Get the agent
# # #     agent = get_agent()
    
# # #     # Add dark mode toggle in sidebar
# # #     st.sidebar.title("Settings")
# # #     dark_mode = st.sidebar.checkbox("Dark Mode", value=False)
    
# # #     if dark_mode:
# # #         # Add dark theme CSS
# # #         st.markdown("""
# # #         <style>
# # #         .stApp {
# # #             background-color: #1E1E1E;
# # #             color: #FFFFFF;
# # #         }
# # #         .stButton>button {
# # #             background-color: #4e4e4e;
# # #             color: white;
# # #         }
# # #         .stExpander {
# # #             background-color: #2d2d2d;
# # #         }
# # #         </style>
# # #         """, unsafe_allow_html=True)
    
# # #     # Title and description
# # #     st.title("Medical Diagnostic Agent System")
# # #     st.markdown("""
# # #     This intelligent agent uses a best-first search algorithm to suggest possible 
# # #     diagnoses based on reported symptoms. Please select your symptoms from the list below.
    
# # #     **Note: This is a prototype for educational purposes only and is not a substitute for professional medical advice.**
# # #     """)
    
# # #     # Create layout with columns for better organization
# # #     col1, col2 = st.columns([1, 2])
    
# # #     with col1:
# # #         st.subheader("Select Your Symptoms")
        
# # #         # Group symptoms by body system
# # #         categorized_symptoms = group_symptoms_by_system(agent.symptoms)
        
# # #         # Add symptom search
# # #         search_query = st.text_input("Search symptoms:", "")
        
# # #         # Show body map toggle
# # #         show_body_map = st.checkbox("Show body map", value=False)
        
# # #         if show_body_map:
# # #             st.components.v1.html(create_body_map(), height=450)
        
# # #         # Create symptom selection with categories
# # #         selected_symptoms = []
        
# # #         # Display symptoms with categorization and search filtering
# # #         for system, symptoms in categorized_symptoms.items():
# # #             if symptoms:  # Only show categories with symptoms
# # #                 with st.expander(f"{system} Symptoms", expanded=True):
# # #                     for symptom_id, symptom_name in symptoms:
# # #                         # Filter based on search query
# # #                         if search_query.lower() in symptom_name.lower() or not search_query:
# # #                             if st.checkbox(symptom_name, key=symptom_id):
# # #                                 selected_symptoms.append(symptom_name)
        
# # #         # Add a search duration input
# # #         max_diagnoses = st.slider(
# # #             "Maximum number of diagnoses to show:",
# # #             min_value=1,
# # #             max_value=5,
# # #             value=3
# # #         )
        
# # #         # Add a diagnose button
# # #         diagnose_button = st.button("Get Diagnosis", use_container_width=True)
    
# # #     # Display results in the second column
# # #     with col2:
# # #         if diagnose_button and selected_symptoms:
# # #             st.subheader("Diagnostic Results")
            
# # #             # Process the symptoms
# # #             agent.perceive(selected_symptoms)
            
# # #             # Get diagnoses
# # #             results = agent.act(max_diagnoses)
            
# # #             if not results['diagnoses']:
# # #                 st.warning("Not enough information to make a diagnosis. Please provide more symptoms.")
# # #             else:
# # #                 # Create bar chart for all diagnoses
# # #                 diagnosis_names = [d['condition_name'] for d in results['diagnoses']]
# # #                 confidence_scores = [d['confidence'] for d in results['diagnoses']]
                
# # #                 # Create DataFrame for the chart
# # #                 df = pd.DataFrame({
# # #                     'Condition': diagnosis_names,
# # #                     'Confidence': confidence_scores
# # #                 })
                
# # #                 # Create confidence score visualization
# # #                 st.subheader("Confidence Comparison")
# # #                 fig, ax = plt.subplots(figsize=(10, 5))
# # #                 bars = ax.barh(df['Condition'], df['Confidence'], color=[get_confidence_color(score) for score in df['Confidence']])
# # #                 ax.set_xlim(0, 1)
# # #                 ax.set_xlabel('Confidence Score')
# # #                 ax.set_title('Diagnosis Confidence Comparison')
                
# # #                 # Add value labels to the bars
# # #                 for i, v in enumerate(df['Confidence']):
# # #                     ax.text(v + 0.01, i, f'{v:.2f}', va='center')
                
# # #                 st.pyplot(fig)
                
# # #                 # Display each diagnosis with improved visuals
# # #                 for i, diagnosis in enumerate(results['diagnoses']):
# # #                     confidence_color = get_confidence_color(diagnosis['confidence'])
                    
# # #                     # Create an expander with colored header based on confidence
# # #                     with st.expander(
# # #                         f"{i+1}. {diagnosis['condition_name']} - Confidence: {diagnosis['confidence']:.2f}",
# # #                         expanded=(i == 0)  # Expand only the first result by default
# # #                     ):
# # #                         # Create two columns for explanation and visualization
# # #                         exp_col1, exp_col2 = st.columns([3, 2])
                        
# # #                         with exp_col1:
# # #                             st.markdown("### Explanation")
# # #                             st.markdown(results['explanations'][diagnosis['condition_id']])
                            
# # #                             st.markdown("### Recommendations")
# # #                             st.markdown(results['recommendations'][diagnosis['condition_id']])
                        
# # #                         with exp_col2:
# # #                             # Add confidence gauge
# # #                             st.markdown("#### Confidence Score")
# # #                             gauge_fig = create_confidence_gauge(diagnosis['confidence'])
# # #                             st.pyplot(gauge_fig)
                            
# # #                             # Add symptom match visualization
# # #                             st.markdown("#### Symptom Analysis")
# # #                             explanation_fig = create_explanation_viz(diagnosis, agent)
# # #                             st.pyplot(explanation_fig)
                
# # #                 # Add a disclaimer
# # #                 st.markdown("""
# # #                 ---
# # #                 **Disclaimer:** This is an educational prototype. The diagnoses provided are based on a simplified model
# # #                 and should not be used for actual medical decisions. Always consult with a healthcare professional for
# # #                 proper diagnosis and treatment.
# # #                 """)
# # #         elif diagnose_button:
# # #             st.warning("Please select at least one symptom.")
# # #         else:
# # #             st.info("Select symptoms and click 'Get Diagnosis' to receive possible diagnoses.")
            
# # #             # Show improved information about the agent
# # #             st.markdown("""
# # #             ### How This Works
            
# # #             This diagnostic agent uses a best-first search algorithm to navigate through a knowledge base of medical conditions and their associated symptoms. The search prioritizes conditions that most closely match your reported symptoms, considering factors such as:
# # #             """)
            
# # #             # Use bullet points for better readability
# # #             st.markdown("""
# # #             - **Symptom-Condition Association**: The strength of relationship between symptoms and conditions
# # #             - **Primary Symptoms**: The presence of key symptoms that are strongly indicative of specific conditions
# # #             - **Condition Prevalence**: How common different conditions are in the general population
# # #             """)
            
# # #             st.markdown("""
# # #             ### Understanding Confidence Scores
            
# # #             The confidence score is calculated using the following formula:
            
# # #             `Confidence = 0.7 * (MatchedWeight / TotalWeight) + 0.3 * (PrimarySymptomMatch / TotalPrimarySymptoms)`
            
# # #             This balances the breadth of symptom matching (70%) with the presence of primary symptoms (30%) to provide a more nuanced assessment of diagnostic likelihood.
# # #             """)
            
# # #             # Add example image for better explanation
# # #             st.image("https://via.placeholder.com/800x300?text=Diagnostic+Process+Visualization", 
# # #                     caption="Simplified representation of the diagnostic process", use_column_width=True)
    
# # #     # Add information about the project at the bottom
# # #     st.markdown("""
# # #     ---
# # #     ### About This Project
    
# # #     This Medical Diagnostic Agent System was developed as a final project for ITEC 781: Artificial Intelligence and Informatics I. 
# # #     It demonstrates the application of intelligent agent architecture and search algorithms in the healthcare domain.
    
# # #     The system uses:
# # #     - A reactive agent architecture with perception, reasoning, and action components
# # #     - Best-first search algorithm for diagnosis identification
# # #     - A knowledge base with conditions, symptoms, and their relationships
# # #     """)

# # # if __name__ == "__main__":
# # #     main()










# # """
# # Fully Enhanced Streamlit interface for the Medical Diagnostic Agent.

# # This module provides an improved user interface with:
# # 1. Color-coded confidence scores
# # 2. Symptom categories
# # 3. Symptom search
# # 4. Interactive body map
# # 5. Results visualization
# # 6. Responsive design
# # 7. Explanation visualization
# # 8. Dark mode option

# # Additional upgrades:
# # 1. Symptom Timeline Integration
# # 2. Simple Printable Report
# # 3. Bookmark/Save Feature
# # 4. Contextual Help Tooltips
# # 5. Related Conditions Section
# # 6. Minimal Animation
# # 7. Input Validation
# # 8. Simplified Medical Terminology
# # """

# # import streamlit as st
# # import json
# # import os
# # import pandas as pd
# # import matplotlib.pyplot as plt
# # import numpy as np
# # from diagnostic_agent import DiagnosticAgent
# # import time
# # from datetime import datetime, timedelta
# # import uuid
# # import base64
# # from io import BytesIO
# # import re

# # # Page configuration
# # def configure_page():
# #     """Configure the Streamlit page settings."""
# #     st.set_page_config(
# #         page_title="Medical Diagnostic Agent",
# #         page_icon="🏥",
# #         layout="wide",
# #         initial_sidebar_state="expanded"
# #     )

# # # Initialize the agent
# # @st.cache_resource
# # def get_agent():
# #     """Initialize and cache the diagnostic agent."""
# #     kb_path = "knowledge_base.json"
# #     return DiagnosticAgent(kb_path)

# # # Group symptoms by body system
# # def group_symptoms_by_system(symptoms):
# #     """Group symptoms by body system for better organization."""
# #     # Define body system categories
# #     body_systems = {
# #         "Respiratory": ["Cough", "Shortness of breath", "Wheezing", "Runny nose", "Sore throat"],
# #         "Digestive": ["Nausea", "Vomiting", "Diarrhea", "Abdominal pain", "Loss of appetite"],
# #         "Neurological": ["Headache", "Confusion", "Dizziness", "Loss of taste or smell"],
# #         "General": ["Fever", "Fatigue", "Muscle pain", "Joint pain", "Rash", "Chest pain"]
# #     }
    
# #     # Categorize symptoms
# #     categorized = {system: [] for system in body_systems}
# #     other = []
    
# #     for symptom_id, symptom_data in symptoms.items():
# #         symptom_name = symptom_data["name"]
# #         categorized_flag = False
        
# #         for system, system_symptoms in body_systems.items():
# #             if symptom_name in system_symptoms:
# #                 categorized[system].append((symptom_id, symptom_name))
# #                 categorized_flag = True
# #                 break
                
# #         if not categorized_flag:
# #             other.append((symptom_id, symptom_name))
    
# #     # Add 'Other' category if needed
# #     if other:
# #         categorized["Other"] = other
        
# #     return categorized

# # # Generate color for confidence score
# # def get_confidence_color(score):
# #     """Return color based on confidence score."""
# #     if score >= 0.7:
# #         return "green"
# #     elif score >= 0.4:
# #         return "orange"
# #     else:
# #         return "red"

# # # Create confidence gauge chart
# # def create_confidence_gauge(score):
# #     """Create a gauge chart for the confidence score."""
# #     fig, ax = plt.subplots(figsize=(3, 2), subplot_kw={'projection': 'polar'})
    
# #     # Gauge settings
# #     theta = np.linspace(0, 180, 100) * np.pi / 180
# #     r = np.ones_like(theta)
    
# #     # Color sections
# #     ax.barh(0, 1, 0.6, theta[0], color='red', alpha=0.4)
# #     ax.barh(0, 1, 0.6, theta[33], color='orange', alpha=0.4)
# #     ax.barh(0, 1, 0.6, theta[66], color='green', alpha=0.4)
    
# #     # Needle
# #     needle_theta = score * 180 * np.pi / 180
# #     ax.plot([0, needle_theta], [0, 0.5], color='black', linewidth=2)
    
# #     # Clean up
# #     ax.set_yticks([])
# #     ax.set_xticks([])
# #     ax.set_ylim(0, 1)
# #     ax.set_title(f'Confidence: {score:.2f}', size=10)
# #     ax.spines['polar'].set_visible(False)
    
# #     return fig

# # # Create explanation visualization
# # def create_explanation_viz(diagnosis, agent):
# #     """Create a visualization of symptom matches for a diagnosis."""
# #     condition_id = diagnosis['condition_id']
# #     condition = agent.conditions[condition_id]
    
# #     # Get all symptoms for this condition
# #     all_condition_symptoms = [(s_id, agent.symptoms[s_id]['name'], weight) 
# #                              for s_id, weight in condition['symptoms'].items()]
    
# #     # Sort by weight descending
# #     all_condition_symptoms.sort(key=lambda x: x[2], reverse=True)
    
# #     # Prepare data for visualization
# #     symptom_names = [s[1] for s in all_condition_symptoms]
# #     weights = [s[2] for s in all_condition_symptoms]
    
# #     # Mark matched symptoms
# #     matched = [s[1] in diagnosis['matched_symptoms'] for s in all_condition_symptoms]
# #     colors = ['#2ecc71' if m else '#e74c3c' for m in matched]
    
# #     # Create horizontal bar chart
# #     fig, ax = plt.subplots(figsize=(8, max(3, len(symptom_names)*0.4)))
# #     bars = ax.barh(symptom_names, weights, color=colors)
    
# #     # Add legend
# #     from matplotlib.patches import Patch
# #     legend_elements = [
# #         Patch(facecolor='#2ecc71', label='Matched'),
# #         Patch(facecolor='#e74c3c', label='Not Present')
# #     ]
# #     ax.legend(handles=legend_elements, loc='upper right')
    
# #     # Add labels
# #     ax.set_title(f'Symptom Analysis for {condition["name"]}')
# #     ax.set_xlabel('Symptom Weight')
    
# #     # Improve appearance
# #     ax.spines['top'].set_visible(False)
# #     ax.spines['right'].set_visible(False)
    
# #     return fig

# # # Create a human body map
# # def create_body_map():
# #     """Create a simple human body map with clickable regions."""
# #     # This is a placeholder HTML for a clickable body map
# #     body_map_html = """
# #     <style>
# #     .body-map {
# #         position: relative;
# #         width: 200px;
# #         height: 400px;
# #         margin: 0 auto;
# #         background-color: #f0f0f0;
# #         border-radius: 100px 100px 0 0;
# #     }
# #     .body-region {
# #         position: absolute;
# #         cursor: pointer;
# #         border: 1px solid #ddd;
# #         border-radius: 4px;
# #         text-align: center;
# #         font-size: 10px;
# #         color: #555;
# #     }
# #     .head {
# #         top: 20px;
# #         left: 75px;
# #         width: 50px;
# #         height: 50px;
# #         border-radius: 25px;
# #     }
# #     .chest {
# #         top: 80px;
# #         left: 50px;
# #         width: 100px;
# #         height: 80px;
# #     }
# #     .abdomen {
# #         top: 170px;
# #         left: 50px;
# #         width: 100px;
# #         height: 80px;
# #     }
# #     .limbs {
# #         top: 260px;
# #         left: 30px;
# #         width: 140px;
# #         height: 120px;
# #     }
# #     </style>
    
# #     <div class="body-map">
# #         <div class="body-region head" onclick="selectRegion('head')" title="Head & Neck">Head & Neck</div>
# #         <div class="body-region chest" onclick="selectRegion('chest')" title="Chest & Back">Chest & Back</div>
# #         <div class="body-region abdomen" onclick="selectRegion('abdomen')" title="Abdomen">Abdomen</div>
# #         <div class="body-region limbs" onclick="selectRegion('limbs')" title="Arms & Legs">Arms & Legs</div>
# #     </div>
    
# #     <script>
# #     function selectRegion(region) {
# #         // This would ideally communicate with Streamlit
# #         // For now, we'll just show an alert
# #         alert('Selected region: ' + region);
# #     }
# #     </script>
# #     """
    
# #     return body_map_html

# # # Generate PDF report
# # def generate_report(patient_name, symptoms, results, agent, simplified_language):
# #     """Generate a printable report of the diagnosis."""
# #     from matplotlib.backends.backend_pdf import PdfPages
# #     import matplotlib.pyplot as plt
# #     from matplotlib.gridspec import GridSpec
# #     import io
    
# #     buffer = io.BytesIO()
    
# #     with PdfPages(buffer) as pdf:
# #         # Title page
# #         fig = plt.figure(figsize=(8.5, 11))
# #         plt.text(0.5, 0.9, "Medical Diagnostic Report", ha='center', fontsize=24)
# #         plt.text(0.5, 0.85, f"Patient: {patient_name}", ha='center', fontsize=16)
# #         plt.text(0.5, 0.8, f"Date: {datetime.now().strftime('%B %d, %Y')}", ha='center', fontsize=16)
# #         plt.text(0.5, 0.75, "Generated by Medical Diagnostic Agent System", ha='center', fontsize=14)
# #         plt.text(0.5, 0.7, "(Educational Prototype - Not for Clinical Use)", ha='center', fontsize=12, style='italic')
# #         plt.axis('off')
# #         pdf.savefig()
# #         plt.close()
        
# #         # Symptoms page
# #         fig = plt.figure(figsize=(8.5, 11))
# #         plt.text(0.5, 0.95, "Reported Symptoms", ha='center', fontsize=18)
        
# #         y_pos = 0.9
# #         for i, symptom in enumerate(symptoms):
# #             plt.text(0.1, y_pos - i*0.03, f"• {symptom}", fontsize=12)
        
# #         plt.text(0.1, y_pos - (len(symptoms) + 2)*0.03, f"Symptom onset: {results.get('symptom_onset', 'Not specified')}", fontsize=12)
        
# #         plt.axis('off')
# #         pdf.savefig()
# #         plt.close()
        
# #         # Results page
# #         if results['diagnoses']:
# #             # Create a page for each diagnosis
# #             for i, diagnosis in enumerate(results['diagnoses']):
# #                 fig = plt.figure(figsize=(8.5, 11))
# #                 gs = GridSpec(3, 1, height_ratios=[1, 1, 2])
                
# #                 # Diagnosis name and confidence
# #                 ax0 = plt.subplot(gs[0])
# #                 title = "Potential Diagnosis" if i > 0 else "Primary Diagnosis"
# #                 ax0.text(0.5, 0.8, title, ha='center', fontsize=18)
# #                 ax0.text(0.5, 0.5, diagnosis['condition_name'], ha='center', fontsize=24)
# #                 ax0.text(0.5, 0.3, f"Confidence: {diagnosis['confidence']:.2f}", ha='center', fontsize=16)
# #                 ax0.axis('off')
                
# #                 # Explanation
# #                 ax1 = plt.subplot(gs[1])
# #                 explanation_text = results['explanations'][diagnosis['condition_id']]
                
# #                 if simplified_language:
# #                     # Simplify medical terminology
# #                     explanation_text = simplify_medical_terms(explanation_text)
                
# #                 ax1.text(0.1, 0.9, "Why This Diagnosis?", fontsize=14, fontweight='bold')
# #                 wrapped_text = wrap_text(explanation_text, 80)
# #                 for j, line in enumerate(wrapped_text.split('\n')):
# #                     if j < 15:  # Limit number of lines to prevent overflow
# #                         ax1.text(0.1, 0.8 - j*0.06, line, fontsize=10)
# #                 ax1.axis('off')
                
# #                 # Recommendations
# #                 ax2 = plt.subplot(gs[2])
# #                 recommendations_text = results['recommendations'][diagnosis['condition_id']]
                
# #                 if simplified_language:
# #                     # Simplify medical terminology
# #                     recommendations_text = simplify_medical_terms(recommendations_text)
                
# #                 ax2.text(0.1, 0.9, "Recommendations", fontsize=14, fontweight='bold')
# #                 wrapped_recs = wrap_text(recommendations_text, 80)
# #                 for j, line in enumerate(wrapped_recs.split('\n')):
# #                     if j < 10:  # Limit number of lines
# #                         ax2.text(0.1, 0.8 - j*0.06, line, fontsize=10)
                
# #                 disclaimer = "IMPORTANT: This is an educational prototype and should not replace professional medical advice."
# #                 ax2.text(0.1, 0.2, disclaimer, fontsize=9, style='italic', bbox=dict(facecolor='lightgray', alpha=0.5))
                
# #                 ax2.axis('off')
                
# #                 pdf.savefig()
# #                 plt.close()
        
# #         else:
# #             # No diagnoses found
# #             fig = plt.figure(figsize=(8.5, 11))
# #             plt.text(0.5, 0.5, "No diagnoses found based on the provided symptoms.", ha='center', fontsize=16)
# #             plt.text(0.5, 0.45, "Please consult with a healthcare professional.", ha='center', fontsize=14)
# #             plt.axis('off')
# #             pdf.savefig()
# #             plt.close()
    
# #     buffer.seek(0)
# #     return buffer

# # # Create download link for PDF
# # def get_pdf_download_link(pdf_bytes, filename="medical_diagnosis_report.pdf"):
# #     """Generate a link to download the PDF file."""
# #     b64 = base64.b64encode(pdf_bytes.read()).decode()
# #     href = f'<a href="data:application/pdf;base64,{b64}" download="{filename}">Download PDF Report</a>'
# #     return href

# # # Suggest related symptoms based on selected symptoms
# # def suggest_related_symptoms(selected_symptoms, agent):
# #     """Suggest related symptoms based on currently selected symptoms."""
# #     if not selected_symptoms:
# #         return []
    
# #     related_symptoms = []
# #     selected_conditions = []
    
# #     # Find conditions related to selected symptoms
# #     for symptom_name in selected_symptoms:
# #         for symptom_id, symptom_data in agent.symptoms.items():
# #             if symptom_data['name'].lower() == symptom_name.lower():
# #                 # Find conditions that have this symptom
# #                 for condition_id, condition in agent.conditions.items():
# #                     if symptom_id in condition['symptoms']:
# #                         selected_conditions.append(condition_id)
    
# #     # Find other symptoms from these conditions
# #     for condition_id in selected_conditions:
# #         condition = agent.conditions[condition_id]
# #         for symptom_id in condition['symptoms']:
# #             symptom_name = agent.symptoms[symptom_id]['name']
# #             if symptom_name not in selected_symptoms and symptom_name not in related_symptoms:
# #                 related_symptoms.append(symptom_name)
    
# #     # Return top 5 related symptoms
# #     return related_symptoms[:5]

# # # Find related conditions
# # def find_related_conditions(condition_id, agent, max_conditions=3):
# #     """Find related conditions based on symptom overlap."""
# #     condition = agent.conditions[condition_id]
# #     condition_symptoms = set(condition['symptoms'].keys())
    
# #     related = []
# #     for other_id, other_condition in agent.conditions.items():
# #         if other_id != condition_id:
# #             other_symptoms = set(other_condition['symptoms'].keys())
# #             overlap = len(condition_symptoms.intersection(other_symptoms))
# #             if overlap > 0:
# #                 similarity = overlap / len(condition_symptoms.union(other_symptoms))
# #                 related.append((other_id, other_condition['name'], similarity))
    
# #     # Sort by similarity and return top results
# #     related.sort(key=lambda x: x[2], reverse=True)
# #     return related[:max_conditions]

# # # Tooltip HTML
# # def tooltip(text, tooltip_text):
# #     """Create HTML for a text with tooltip."""
# #     return f"""
# #     <span class="tooltip">{text}
# #         <span class="tooltiptext">{tooltip_text}</span>
# #     </span>
# #     """

# # # Add tooltip CSS
# # def get_tooltip_css():
# #     """Return CSS for tooltips."""
# #     return """
# #     <style>
# #     .tooltip {
# #         position: relative;
# #         display: inline-block;
# #         border-bottom: 1px dotted #ccc;
# #         cursor: help;
# #     }
    
# #     .tooltip .tooltiptext {
# #         visibility: hidden;
# #         width: 200px;
# #         background-color: #555;
# #         color: #fff;
# #         text-align: center;
# #         border-radius: 6px;
# #         padding: 5px;
# #         position: absolute;
# #         z-index: 1;
# #         bottom: 125%;
# #         left: 50%;
# #         margin-left: -100px;
# #         opacity: 0;
# #         transition: opacity 0.3s;
# #     }
    
# #     .tooltip:hover .tooltiptext {
# #         visibility: visible;
# #         opacity: 0.9;
# #     }
# #     </style>
# #     """

# # # Wrap text to a specific width
# # def wrap_text(text, width):
# #     """Wrap text to specified width."""
# #     words = text.split()
# #     lines = []
# #     current_line = []
    
# #     for word in words:
# #         if len(' '.join(current_line + [word])) <= width:
# #             current_line.append(word)
# #         else:
# #             lines.append(' '.join(current_line))
# #             current_line = [word]
    
# #     if current_line:
# #         lines.append(' '.join(current_line))
    
# #     return '\n'.join(lines)

# # # Check for contradictory symptoms
# # def check_contradictory_symptoms(symptoms, agent):
# #     """Check for contradictory symptom combinations."""
# #     contradictory_pairs = [
# #         ("Loss of appetite", "Increased appetite"),
# #         ("Fever", "Hypothermia"),
# #         ("Diarrhea", "Constipation"),
# #         ("Insomnia", "Excessive sleepiness")
# #     ]
    
# #     for pair in contradictory_pairs:
# #         if pair[0] in symptoms and pair[1] in symptoms:
# #             return f"{pair[0]} and {pair[1]} are contradictory symptoms."
    
# #     return None

# # # Simplify medical terminology
# # def simplify_medical_terms(text):
# #     """Replace complex medical terms with simpler alternatives."""
# #     simplifications = {
# #         "myocardial infarction": "heart attack",
# #         "cerebrovascular accident": "stroke",
# #         "dyspnea": "shortness of breath",
# #         "pyrexia": "fever",
# #         "emesis": "vomiting",
# #         "syncope": "fainting",
# #         "edema": "swelling",
# #         "myalgia": "muscle pain",
# #         "cephalgia": "headache",
# #         "arthralgia": "joint pain",
# #         "pruritus": "itching",
# #         "erythema": "redness of skin",
# #         "lethargy": "tiredness",
# #         "vertigo": "dizziness",
# #         "anorexia": "loss of appetite",
# #         "dysphagia": "difficulty swallowing",
# #         "tachycardia": "rapid heart rate",
# #         "bradycardia": "slow heart rate",
# #         "hypertension": "high blood pressure",
# #         "hypotension": "low blood pressure"
# #     }
    
# #     # Case-insensitive replacement
# #     pattern = re.compile('|'.join(r'\b%s\b' % re.escape(key) for key in simplifications.keys()), re.IGNORECASE)
# #     result = pattern.sub(lambda match: simplifications[match.group(0).lower()], text)
    
# #     return result

# # # Initialize session state
# # def init_session_state():
# #     """Initialize session state variables."""
# #     if 'bookmarks' not in st.session_state:
# #         st.session_state.bookmarks = {}
    
# #     if 'fade_in' not in st.session_state:
# #         st.session_state.fade_in = False
    
# #     if 'language_simplified' not in st.session_state:
# #         st.session_state.language_simplified = False

# # # Main function to run the Streamlit interface
# # def main():
# #     """Run the enhanced Streamlit interface for the Medical Diagnostic Agent."""
# #     # Initialize session state
# #     init_session_state()
    
# #     # Configure the page
# #     configure_page()
    
# #     # Insert tooltip CSS
# #     st.markdown(get_tooltip_css(), unsafe_allow_html=True)
    
# #     # Add fade-in animation CSS
# #     st.markdown("""
# #     <style>
# #     @keyframes fadein {
# #         from { opacity: 0; }
# #         to   { opacity: 1; }
# #     }
    
# #     .fade-in {
# #         animation: fadein 1s;
# #     }
# #     </style>
# #     """, unsafe_allow_html=True)
    
# #     # Get the agent
# #     agent = get_agent()
    
# #     # Sidebar settings
# #     st.sidebar.title("Settings")
    
# #     # Dark mode toggle
# #     dark_mode = st.sidebar.checkbox("Dark Mode", value=False)
    
# #     # Simplified language toggle
# #     simplified_language = st.sidebar.checkbox("Simplified Medical Terms", value=st.session_state.language_simplified,
# #                                             help="Use simpler language instead of medical terminology")
# #     st.session_state.language_simplified = simplified_language
    
# #     # Add bookmark section to sidebar
# #     st.sidebar.markdown("---")
# #     st.sidebar.subheader("Saved Diagnoses")
    
# #     if st.session_state.bookmarks:
# #         for bookmark_id, bookmark in st.session_state.bookmarks.items():
# #             if st.sidebar.button(f"{bookmark['date']} - {bookmark['primary_diagnosis']}",
# #                                key=f"bookmark_{bookmark_id}"):
# #                 # Load this bookmark
# #                 st.session_state.selected_symptoms = bookmark['symptoms']
# #                 st.session_state.symptom_onset = bookmark['symptom_onset']
# #                 st.experimental_rerun()
# #     else:
# #         st.sidebar.write("No saved diagnoses yet.")
    
# #     if dark_mode:
# #         # Add dark theme CSS
# #         st.markdown("""
# #         <style>
# #         .stApp {
# #             background-color: #1E1E1E;
# #             color: #FFFFFF;
# #         }
# #         .stButton>button {
# #             background-color: #4e4e4e;
# #             color: white;
# #         }
# #         .stExpander {
# #             background-color: #2d2d2d;
# #         }
# #         </style>
# #         """, unsafe_allow_html=True)
    
# #     # Title and description
# #     st.title("Medical Diagnostic Agent System")
    
# #     # Create tooltip for educational purpose
# #     edu_tooltip = tooltip(
# #         "This intelligent agent uses a best-first search algorithm to suggest possible diagnoses based on reported symptoms.",
# #         "This is an educational prototype and should not replace professional medical advice."
# #     )
    
# #     st.markdown(f"""
# #     {edu_tooltip} Please select your symptoms from the list below.
    
# #     **Note: This is a prototype for educational purposes only and is not a substitute for professional medical advice.**
# #     """, unsafe_allow_html=True)
    
# #     # Create layout with columns for better organization
# #     col1, col2 = st.columns([1, 2])
    
# #     with col1:
# #         st.subheader("Select Your Symptoms")
        
# #         # Initialize selected symptoms in session state if not present
# #         if 'selected_symptoms' not in st.session_state:
# #             st.session_state.selected_symptoms = []
        
# #         # Add symptom search
# #         search_query = st.text_input("Search symptoms:", "")
        
# #         # Group symptoms by body system
# #         categorized_symptoms = group_symptoms_by_system(agent.symptoms)
        
# #         # Show body map toggle
# #         show_body_map = st.checkbox("Show body map", value=False)
        
# #         if show_body_map:
# #             st.components.v1.html(create_body_map(), height=450)
        
# #         # Create symptom selection with categories
# #         selected_symptoms = []
        
# #         # Display symptoms with categorization and search filtering
# #         for system, symptoms in categorized_symptoms.items():
# #             if symptoms:  # Only show categories with symptoms
# #                 with st.expander(f"{system} Symptoms", expanded=True):
# #                     for symptom_id, symptom_name in symptoms:
# #                         # Filter based on search query
# #                         if search_query.lower() in symptom_name.lower() or not search_query:
# #                             # Use session state to maintain selections
# #                             key = f"symptom_{symptom_id}"
# #                             if key not in st.session_state:
# #                                 st.session_state[key] = symptom_name in st.session_state.selected_symptoms
                            
# #                             if st.checkbox(symptom_name, key=key):
# #                                 selected_symptoms.append(symptom_name)
        
# #         # Update session state with current selections
# #         st.session_state.selected_symptoms = selected_symptoms
        
# #         # Add symptom timeline - NEW FEATURE
# #         st.subheader("Symptom Timeline")
        
# #         # Initialize symptom onset in session state
# #         if 'symptom_onset' not in st.session_state:
# #             st.session_state.symptom_onset = "Today"
        
# #         # Get symptom onset time
# #         onset_options = ["Today", "Yesterday", "2-3 days ago", "This week", "Last week", "This month", "Over a month ago"]
# #         symptom_onset = st.selectbox("When did symptoms begin?", onset_options, 
# #                                    index=onset_options.index(st.session_state.symptom_onset))
        
# #         # Update session state
# #         st.session_state.symptom_onset = symptom_onset
        
# #         # Add a slider for diagnoses
# #         max_diagnoses = st.slider(
# #             "Maximum number of diagnoses to show:",
# #             min_value=1,
# #             max_value=5,
# #             value=3
# #         )
        
# #         # Show suggested related symptoms - NEW FEATURE
# #         if selected_symptoms:
# #             related_symptoms = suggest_related_symptoms(selected_symptoms, agent)
# #             if related_symptoms:
# #                 st.markdown("#### You might also consider:")
# #                 for symptom in related_symptoms:
# #                     if symptom not in selected_symptoms and st.button(f"+ {symptom}", key=f"add_{symptom}"):
# #                         # Add this symptom
# #                         st.session_state.selected_symptoms.append(symptom)
# #                         st.experimental_rerun()
        
# #         # Check for contradictory symptoms - NEW FEATURE
# #         contradiction = check_contradictory_symptoms(selected_symptoms, agent)
# #         if contradiction:
# #             st.warning(contradiction)
        
# #         # Add a diagnose button
# #         diagnose_button = st.button("Get Diagnosis", use_container_width=True)
    
# #     # Display results in the second column
# #     with col2:
# #         # Store results for report generation
# #         results = None
        
# #         if diagnose_button and selected_symptoms:
# #             # Use fade-in animation
# #             st.session_state.fade_in = True
            
# #             # Set fade-in class if animation is enabled
# #             fade_class = "fade-in" if st.session_state.fade_in else ""
            
# #             st.markdown(f'<div class="{fade_class}">', unsafe_allow_html=True)
            
# #             st.subheader("Diagnostic Results")
            
# #             # Process the symptoms
# #             agent.perceive(selected_symptoms)
            
# #             # Get diagnoses
# #             results = agent.act(max_diagnoses)
            
# #             # Add symptom timeline to results
# #             results['symptom_onset'] = symptom_onset
            
# #             if not results['diagnoses']:
# #                 st.warning("Not enough information to make a diagnosis. Please provide more symptoms.")
# #             else:
# #                 # Create bar chart for all diagnoses
# #                 diagnosis_names = [d['condition_name'] for d in results['diagnoses']]
# #                 confidence_scores = [d['confidence'] for d in results['diagnoses']]
                
# #                 # Create DataFrame for the chart
# #                 df = pd.DataFrame({
# #                     'Condition': diagnosis_names,
# #                     'Confidence': confidence_scores
# #                 })
                
# #                 # Create confidence score visualization
# #                 st.subheader("Confidence Comparison")
# #                 fig, ax = plt.subplots(figsize=(10, 5))
# #                 bars = ax.barh(df['Condition'], df['Confidence'], color=[get_confidence_color(score) for score in df['Confidence']])
# #                 ax.set_xlim(0, 1)
# #                 ax.set_xlabel('Confidence Score')
# #                 ax.set_title('Diagnosis Confidence Comparison')
                
# #                 # Add value labels to the bars
# #                 for i, v in enumerate(df['Confidence']):
# #                     ax.text(v + 0.01, i, f'{v:.2f}', va='center')
                
# #                 st.pyplot(fig)
                
# #                 # Display each diagnosis with improved visuals
# #                 for i, diagnosis in enumerate(results['diagnoses']):
# #                     confidence_color = get_confidence_color(diagnosis['confidence'])
                    
# #                     # Create an expander with colored header based on confidence
# #                     with st.expander(
# #                         f"{i+1}. {diagnosis['condition_name']} - Confidence: {diagnosis['confidence']:.2f}",
# #                         expanded=(i == 0)  # Expand only the first result by default
# #                     ):
# #                         # Create two columns for explanation and visualization
# #                         exp_col1, exp_col2 = st.columns([3, 2])
                        
# #                         with exp_col1:
# #                             st.markdown("### Explanation")
                            
# #                             # Apply simplified language if enabled - NEW FEATURE
# #                             explanation_text = results['explanations'][diagnosis['condition_id']]
# #                             if simplified_language:
# #                                 explanation_text = simplify_medical_terms(explanation_text)
                            
# #                             st.markdown(explanation_text)
                            
# #                             st.markdown("### Recommendations")
                            
# #                             # Apply simplified language if enabled
# #                             recommendations_text = results['recommendations'][diagnosis['condition_id']]
# #                             if simplified_language:
# #                                 recommendations_text = simplify_medical_terms(recommendations_text)
                                
# #                             st.markdown(recommendations_text)
                            
# #                             # Add related conditions section - NEW FEATURE
# #                             st.markdown("### Related Conditions")
# #                             related_conditions = find_related_conditions(diagnosis['condition_id'], agent)
                            
# #                             for rel_id, rel_name, similarity in related_conditions:
# #                                 similarity_pct = int(similarity * 100)
# #                                 st.markdown(f"- {rel_name} ({similarity_pct}% symptom overlap)")
                        
# #                         with exp_col2:
# #                             # Add confidence gauge
# #                             st.markdown("#### Confidence Score")
# #                             gauge_fig = create_confidence_gauge(diagnosis['confidence'])
# #                             st.pyplot(gauge_fig)
                            
# #                             # Add symptom match visualization
# #                             st.markdown("#### Symptom Analysis")
# #                             explanation_fig = create_explanation_viz(diagnosis, agent)
# #                             st.pyplot(explanation_fig)
                
# #                 # Add bookmark and report generation features - NEW FEATURES
# #                 st.markdown("---")
# #                 report_col1, report_col2 = st.columns(2)
                
# #                 with report_col1:
# #                     # Bookmark feature
# #                     if st.button("Save This Diagnosis"):
# #                         # Generate unique ID
# #                         bookmark_id = str(uuid.uuid4())
                        
# #                         # Create bookmark
# #                         st.session_state.bookmarks[bookmark_id] = {
# #                             'date': datetime.now().strftime("%Y-%m-%d"),
# #                             'symptoms': selected_symptoms,
# #                             'symptom_onset': symptom_onset,
# #                             'primary_diagnosis': results['diagnoses'][0]['condition_name'] if results['diagnoses'] else "No diagnosis"
# #                         }
                        
# #                         st.success("Diagnosis saved! You can access it from the sidebar.")
                
# #                 with report_col2:
# #                     # Report generation
# #                     patient_name = st.text_input("Patient name for report (optional):", "")
                    
# #                     if st.button("Generate Printable Report"):
# #                         # Generate PDF report
# #                         pdf_buffer = generate_report(patient_name, selected_symptoms, results, agent, simplified_language)
                        
# #                         # Create download link
# #                         st.markdown(get_pdf_download_link(pdf_buffer), unsafe_allow_html=True)
                
# #                 # Add a disclaimer
# #                 st.markdown("""
# #                 ---
# #                 **Disclaimer:** This is an educational prototype. The diagnoses provided are based on a simplified model
# #                 and should not be used for actual medical decisions. Always consult with a healthcare professional for
# #                 proper diagnosis and treatment.
# #                 """)
            
# #             # Close fade-in div
# #             st.markdown('</div>', unsafe_allow_html=True)
            
# #         elif diagnose_button:
# #             st.warning("Please select at least one symptom.")
# #         else:
# #             st.info("Select symptoms and click 'Get Diagnosis' to receive possible diagnoses.")
            
# #             # Show improved information about the agent
# #             st.markdown("""
# #             ### How This Works
            
# #             This diagnostic agent uses a best-first search algorithm to navigate through a knowledge base of medical conditions and their associated symptoms. The search prioritizes conditions that most closely match your reported symptoms, considering factors such as:
# #             """)
            
# #             # Use bullet points with tooltips for better readability - NEW FEATURE
# #             st.markdown(f"""
# #             - {tooltip("Symptom-Condition Association", "The strength of relationship between symptoms and conditions based on medical knowledge")}
# #             - {tooltip("Primary Symptoms", "Key symptoms that are strongly indicative of specific conditions")}
# #             - {tooltip("Condition Prevalence", "How common different conditions are in the general population")}
# #             """, unsafe_allow_html=True)
            
# #             st.markdown("""
# #             ### Understanding Confidence Scores
            
# #             The confidence score is calculated using the following formula:
            
# #             `Confidence = 0.7 * (MatchedWeight / TotalWeight) + 0.3 * (PrimarySymptomMatch / TotalPrimarySymptoms)`
            
# #             This balances the breadth of symptom matching (70%) with the presence of primary symptoms (30%) to provide a more nuanced assessment of diagnostic likelihood.
# #             """)
            
# #             # Add feature explanations
# #             st.markdown("""
# #             ### Features
            
# #             - **Symptom Timeline**: Indicate when your symptoms began to help with diagnosis
# #             - **Bookmarking**: Save your symptom sets and diagnoses for future reference
# #             - **Printable Report**: Generate a PDF report of your diagnosis to share with healthcare providers
# #             - **Related Symptoms**: Get suggestions for related symptoms you might be experiencing
# #             - **Simplified Language**: Toggle between medical terminology and simpler language
# #             - **Related Conditions**: See other conditions with similar symptom profiles
# #             """)
    
# #     # Add information about the project at the bottom
# #     st.markdown("""
# #     ---
# #     ### About This Project
    
# #     This Medical Diagnostic Agent System was developed as a final project for ITEC 781: Artificial Intelligence and Informatics I. 
# #     It demonstrates the application of intelligent agent architecture and search algorithms in the healthcare domain.
    
# #     The system uses:
# #     - A reactive agent architecture with perception, reasoning, and action components
# #     - Best-first search algorithm for diagnosis identification
# #     - A knowledge base with conditions, symptoms, and their relationships
# #     """)

# # if __name__ == "__main__":
# #     main()










# """
# Fully Enhanced Streamlit interface for the Medical Diagnostic Agent.

# This module provides an improved user interface with all original features plus:
# - Fixed PDF generation
# - Working save feature
# - Functional simplified medical terms
# - AI integration for enhanced diagnosis
# """

# import streamlit as st
# import json
# import os
# import pandas as pd
# import matplotlib.pyplot as plt
# import numpy as np
# from diagnostic_agent import DiagnosticAgent
# import time
# from datetime import datetime, timedelta
# import uuid
# import base64
# from io import BytesIO
# import re
# import pickle
# from fpdf import FPDF
# import requests

# # Page configuration
# def configure_page():
#     """Configure the Streamlit page settings."""
#     st.set_page_config(
#         page_title="Medical Diagnostic Agent",
#         page_icon="🏥",
#         layout="wide",
#         initial_sidebar_state="expanded"
#     )

# # Initialize the agent
# @st.cache_resource
# def get_agent():
#     """Initialize and cache the diagnostic agent."""
#     kb_path = "knowledge_base.json"
#     return DiagnosticAgent(kb_path)

# # Group symptoms by body system
# def group_symptoms_by_system(symptoms):
#     """Group symptoms by body system for better organization."""
#     # Define body system categories
#     body_systems = {
#         "Respiratory": ["Cough", "Shortness of breath", "Wheezing", "Runny nose", "Sore throat"],
#         "Digestive": ["Nausea", "Vomiting", "Diarrhea", "Abdominal pain", "Loss of appetite"],
#         "Neurological": ["Headache", "Confusion", "Dizziness", "Loss of taste or smell"],
#         "General": ["Fever", "Fatigue", "Muscle pain", "Joint pain", "Rash", "Chest pain"]
#     }
    
#     # Categorize symptoms
#     categorized = {system: [] for system in body_systems}
#     other = []
    
#     for symptom_id, symptom_data in symptoms.items():
#         symptom_name = symptom_data["name"]
#         categorized_flag = False
        
#         for system, system_symptoms in body_systems.items():
#             if symptom_name in system_symptoms:
#                 categorized[system].append((symptom_id, symptom_name))
#                 categorized_flag = True
#                 break
                
#         if not categorized_flag:
#             other.append((symptom_id, symptom_name))
    
#     # Add 'Other' category if needed
#     if other:
#         categorized["Other"] = other
        
#     return categorized

# # Generate color for confidence score
# def get_confidence_color(score):
#     """Return color based on confidence score."""
#     if score >= 0.7:
#         return "green"
#     elif score >= 0.4:
#         return "orange"
#     else:
#         return "red"

# # Create confidence gauge chart
# def create_confidence_gauge(score):
#     """Create a gauge chart for the confidence score."""
#     fig, ax = plt.subplots(figsize=(3, 2), subplot_kw={'projection': 'polar'})
    
#     # Gauge settings
#     theta = np.linspace(0, 180, 100) * np.pi / 180
#     r = np.ones_like(theta)
    
#     # Color sections
#     ax.barh(0, 1, 0.6, theta[0], color='red', alpha=0.4)
#     ax.barh(0, 1, 0.6, theta[33], color='orange', alpha=0.4)
#     ax.barh(0, 1, 0.6, theta[66], color='green', alpha=0.4)
    
#     # Needle
#     needle_theta = score * 180 * np.pi / 180
#     ax.plot([0, needle_theta], [0, 0.5], color='black', linewidth=2)
    
#     # Clean up
#     ax.set_yticks([])
#     ax.set_xticks([])
#     ax.set_ylim(0, 1)
#     ax.set_title(f'Confidence: {score:.2f}', size=10)
#     ax.spines['polar'].set_visible(False)
    
#     return fig

# # Create explanation visualization
# def create_explanation_viz(diagnosis, agent):
#     """Create a visualization of symptom matches for a diagnosis."""
#     condition_id = diagnosis['condition_id']
#     condition = agent.conditions[condition_id]
    
#     # Get all symptoms for this condition
#     all_condition_symptoms = [(s_id, agent.symptoms[s_id]['name'], weight) 
#                              for s_id, weight in condition['symptoms'].items()]
    
#     # Sort by weight descending
#     all_condition_symptoms.sort(key=lambda x: x[2], reverse=True)
    
#     # Prepare data for visualization
#     symptom_names = [s[1] for s in all_condition_symptoms]
#     weights = [s[2] for s in all_condition_symptoms]
    
#     # Mark matched symptoms
#     matched = [s[1] in diagnosis['matched_symptoms'] for s in all_condition_symptoms]
#     colors = ['#2ecc71' if m else '#e74c3c' for m in matched]
    
#     # Create horizontal bar chart
#     fig, ax = plt.subplots(figsize=(8, max(3, len(symptom_names)*0.4)))
#     bars = ax.barh(symptom_names, weights, color=colors)
    
#     # Add legend
#     from matplotlib.patches import Patch
#     legend_elements = [
#         Patch(facecolor='#2ecc71', label='Matched'),
#         Patch(facecolor='#e74c3c', label='Not Present')
#     ]
#     ax.legend(handles=legend_elements, loc='upper right')
    
#     # Add labels
#     ax.set_title(f'Symptom Analysis for {condition["name"]}')
#     ax.set_xlabel('Symptom Weight')
    
#     # Improve appearance
#     ax.spines['top'].set_visible(False)
#     ax.spines['right'].set_visible(False)
    
#     return fig

# # Create a human body map
# def create_body_map():
#     """Create a simple human body map with clickable regions."""
#     # This is a placeholder HTML for a clickable body map
#     body_map_html = """
#     <style>
#     .body-map {
#         position: relative;
#         width: 200px;
#         height: 400px;
#         margin: 0 auto;
#         background-color: #f0f0f0;
#         border-radius: 100px 100px 0 0;
#     }
#     .body-region {
#         position: absolute;
#         cursor: pointer;
#         border: 1px solid #ddd;
#         border-radius: 4px;
#         text-align: center;
#         font-size: 10px;
#         color: #555;
#     }
#     .head {
#         top: 20px;
#         left: 75px;
#         width: 50px;
#         height: 50px;
#         border-radius: 25px;
#     }
#     .chest {
#         top: 80px;
#         left: 50px;
#         width: 100px;
#         height: 80px;
#     }
#     .abdomen {
#         top: 170px;
#         left: 50px;
#         width: 100px;
#         height: 80px;
#     }
#     .limbs {
#         top: 260px;
#         left: 30px;
#         width: 140px;
#         height: 120px;
#     }
#     </style>
    
#     <div class="body-map">
#         <div class="body-region head" onclick="selectRegion('head')" title="Head & Neck">Head & Neck</div>
#         <div class="body-region chest" onclick="selectRegion('chest')" title="Chest & Back">Chest & Back</div>
#         <div class="body-region abdomen" onclick="selectRegion('abdomen')" title="Abdomen">Abdomen</div>
#         <div class="body-region limbs" onclick="selectRegion('limbs')" title="Arms & Legs">Arms & Legs</div>
#     </div>
    
#     <script>
#     function selectRegion(region) {
#         // This would ideally communicate with Streamlit
#         // For now, we'll just show an alert
#         alert('Selected region: ' + region);
#     }
#     </script>
#     """
    
#     return body_map_html

# # FIXED: Generate PDF report using FPDF
# def generate_pdf_report(patient_name, symptoms, results, agent, simplified_language):
#     """Generate a printable report of the diagnosis using FPDF."""
#     # Initialize PDF
#     pdf = FPDF()
#     pdf.add_page()
    
#     # Set up fonts
#     pdf.set_font("Arial", "B", 16)
    
#     # Title
#     pdf.cell(0, 10, "Medical Diagnostic Report", ln=True, align="C")
#     pdf.ln(5)
    
#     # Patient info
#     pdf.set_font("Arial", "B", 12)
#     pdf.cell(0, 10, f"Patient: {patient_name if patient_name else 'Anonymous'}", ln=True)
#     pdf.cell(0, 10, f"Date: {datetime.now().strftime('%B %d, %Y')}", ln=True)
#     pdf.ln(5)
    
#     # Disclaimer
#     pdf.set_font("Arial", "I", 10)
#     pdf.multi_cell(0, 5, "Educational Prototype - Not for Clinical Use")
#     pdf.ln(5)
    
#     # Symptoms section
#     pdf.set_font("Arial", "B", 12)
#     pdf.cell(0, 10, "Reported Symptoms:", ln=True)
#     pdf.set_font("Arial", "", 12)
    
#     for symptom in symptoms:
#         pdf.cell(0, 8, f"• {symptom}", ln=True)
    
#     pdf.cell(0, 8, f"Symptom onset: {results.get('symptom_onset', 'Not specified')}", ln=True)
#     pdf.ln(5)
    
#     # Diagnoses section
#     if results['diagnoses']:
#         pdf.set_font("Arial", "B", 12)
#         pdf.cell(0, 10, "Diagnostic Results:", ln=True)
        
#         for i, diagnosis in enumerate(results['diagnoses']):
#             pdf.set_font("Arial", "B", 12)
#             pdf.cell(0, 10, f"{i+1}. {diagnosis['condition_name']} (Confidence: {diagnosis['confidence']:.2f})", ln=True)
            
#             # Explanation
#             pdf.set_font("Arial", "", 10)
#             explanation_text = results['explanations'][diagnosis['condition_id']]
#             if simplified_language:
#                 explanation_text = simplify_medical_terms(explanation_text)
            
#             pdf.multi_cell(0, 5, explanation_text)
#             pdf.ln(3)
            
#             # Recommendations
#             pdf.set_font("Arial", "B", 11)
#             pdf.cell(0, 8, "Recommendations:", ln=True)
#             pdf.set_font("Arial", "", 10)
            
#             recommendations_text = results['recommendations'][diagnosis['condition_id']]
#             if simplified_language:
#                 recommendations_text = simplify_medical_terms(recommendations_text)
                
#             pdf.multi_cell(0, 5, recommendations_text)
#             pdf.ln(5)
#     else:
#         pdf.set_font("Arial", "I", 12)
#         pdf.cell(0, 10, "No diagnoses found based on the provided symptoms.", ln=True)
#         pdf.cell(0, 10, "Please consult with a healthcare professional.", ln=True)
    
#     # Disclaimer footer
#     pdf.ln(10)
#     pdf.set_font("Arial", "I", 8)
#     pdf.multi_cell(0, 4, "DISCLAIMER: This report was generated by an educational prototype and should not replace professional medical advice. Always consult with a healthcare provider for proper diagnosis and treatment.")
    
#     # Return PDF as bytes
#     return pdf.output(dest='S').encode('latin1')

# # Create download link for PDF
# def get_pdf_download_link(pdf_bytes, filename="medical_diagnosis_report.pdf"):
#     """Generate a link to download the PDF file."""
#     b64 = base64.b64encode(pdf_bytes).decode()
#     href = f'<a href="data:application/pdf;base64,{b64}" download="{filename}" target="_blank">Download PDF Report</a>'
#     return href

# # FIXED: Save bookmarks to file
# def save_bookmarks(bookmarks):
#     """Save bookmarks to a file."""
#     try:
#         with open('bookmarks.pkl', 'wb') as f:
#             pickle.dump(bookmarks, f)
#         return True
#     except Exception as e:
#         st.error(f"Error saving bookmarks: {e}")
#         return False

# # FIXED: Load bookmarks from file
# def load_bookmarks():
#     """Load bookmarks from a file."""
#     try:
#         if os.path.exists('bookmarks.pkl'):
#             with open('bookmarks.pkl', 'rb') as f:
#                 return pickle.load(f)
#         return {}
#     except Exception as e:
#         st.error(f"Error loading bookmarks: {e}")
#         return {}

# # Suggest related symptoms based on selected symptoms
# def suggest_related_symptoms(selected_symptoms, agent):
#     """Suggest related symptoms based on currently selected symptoms."""
#     if not selected_symptoms:
#         return []
    
#     related_symptoms = []
#     selected_conditions = []
    
#     # Find conditions related to selected symptoms
#     for symptom_name in selected_symptoms:
#         for symptom_id, symptom_data in agent.symptoms.items():
#             if symptom_data['name'].lower() == symptom_name.lower():
#                 # Find conditions that have this symptom
#                 for condition_id, condition in agent.conditions.items():
#                     if symptom_id in condition['symptoms']:
#                         selected_conditions.append(condition_id)
    
#     # Find other symptoms from these conditions
#     for condition_id in selected_conditions:
#         condition = agent.conditions[condition_id]
#         for symptom_id in condition['symptoms']:
#             symptom_name = agent.symptoms[symptom_id]['name']
#             if symptom_name not in selected_symptoms and symptom_name not in related_symptoms:
#                 related_symptoms.append(symptom_name)
    
#     # Return top 5 related symptoms
#     return related_symptoms[:5]

# # Find related conditions
# def find_related_conditions(condition_id, agent, max_conditions=3):
#     """Find related conditions based on symptom overlap."""
#     condition = agent.conditions[condition_id]
#     condition_symptoms = set(condition['symptoms'].keys())
    
#     related = []
#     for other_id, other_condition in agent.conditions.items():
#         if other_id != condition_id:
#             other_symptoms = set(other_condition['symptoms'].keys())
#             overlap = len(condition_symptoms.intersection(other_symptoms))
#             if overlap > 0:
#                 similarity = overlap / len(condition_symptoms.union(other_symptoms))
#                 related.append((other_id, other_condition['name'], similarity))
    
#     # Sort by similarity and return top results
#     related.sort(key=lambda x: x[2], reverse=True)
#     return related[:max_conditions]

# # Tooltip HTML
# def tooltip(text, tooltip_text):
#     """Create HTML for a text with tooltip."""
#     return f"""
#     <span class="tooltip">{text}
#         <span class="tooltiptext">{tooltip_text}</span>
#     </span>
#     """

# # Add tooltip CSS
# def get_tooltip_css():
#     """Return CSS for tooltips."""
#     return """
#     <style>
#     .tooltip {
#         position: relative;
#         display: inline-block;
#         border-bottom: 1px dotted #ccc;
#         cursor: help;
#     }
    
#     .tooltip .tooltiptext {
#         visibility: hidden;
#         width: 200px;
#         background-color: #555;
#         color: #fff;
#         text-align: center;
#         border-radius: 6px;
#         padding: 5px;
#         position: absolute;
#         z-index: 1;
#         bottom: 125%;
#         left: 50%;
#         margin-left: -100px;
#         opacity: 0;
#         transition: opacity 0.3s;
#     }
    
#     .tooltip:hover .tooltiptext {
#         visibility: visible;
#         opacity: 0.9;
#     }
#     </style>
#     """

# # Check for contradictory symptoms
# def check_contradictory_symptoms(symptoms, agent):
#     """Check for contradictory symptom combinations."""
#     contradictory_pairs = [
#         ("Loss of appetite", "Increased appetite"),
#         ("Fever", "Hypothermia"),
#         ("Diarrhea", "Constipation"),
#         ("Insomnia", "Excessive sleepiness")
#     ]
    
#     for pair in contradictory_pairs:
#         if pair[0] in symptoms and pair[1] in symptoms:
#             return f"{pair[0]} and {pair[1]} are contradictory symptoms."
    
#     return None

# # FIXED: Simplify medical terminology with more robust implementation
# def simplify_medical_terms(text):
#     """Replace complex medical terms with simpler alternatives."""
#     simplifications = {
#         "myocardial infarction": "heart attack",
#         "cerebrovascular accident": "stroke",
#         "dyspnea": "shortness of breath",
#         "pyrexia": "fever",
#         "emesis": "vomiting",
#         "syncope": "fainting",
#         "edema": "swelling",
#         "myalgia": "muscle pain",
#         "cephalgia": "headache",
#         "arthralgia": "joint pain",
#         "pruritus": "itching",
#         "erythema": "redness of skin",
#         "lethargy": "tiredness",
#         "vertigo": "dizziness",
#         "anorexia": "loss of appetite",
#         "dysphagia": "difficulty swallowing",
#         "tachycardia": "rapid heart rate",
#         "bradycardia": "slow heart rate",
#         "hypertension": "high blood pressure",
#         "hypotension": "low blood pressure",
#         "upper respiratory": "nose and throat",
#         "respiratory tract": "breathing system",
#         "gastrointestinal": "stomach and intestines",
#         "inflammation": "swelling",
#         "condition": "health problem",
#         "diagnoses": "findings",
#         "diagnosis": "finding",
#         "prevalence": "frequency",
#         "symptoms": "signs",
#         "consultation": "visit",
#         "primary": "main",
#         "practitioner": "doctor",
#         "medication": "medicine",
#         "prescribed": "ordered",
#         "therapeutic": "treatment",
#         "diagnostic": "testing",
#         "assessment": "check-up",
#         "physician": "doctor"
#     }
    
#     # Case-insensitive replacement with word boundary check
#     for med_term, simple_term in simplifications.items():
#         # Use regex with word boundaries for more precise replacement
#         pattern = re.compile(r'\b' + re.escape(med_term) + r'\b', re.IGNORECASE)
#         text = pattern.sub(simple_term, text)
    
#     return text

# # # NEW: AI Integration - Get OpenAI Analysis
# # def get_ai_analysis(symptoms, diagnosis, api_key):
# #     """Get AI analysis of symptoms and diagnosis using OpenAI API."""
# #     if not api_key:
# #         return "Please provide an API key to use AI analysis."
    
# #     headers = {
# #         "Content-Type": "application/json",
# #         "Authorization": f"Bearer {api_key}"
# #     }
    
# #     prompt = f"""
# #     I'm a medical diagnostic assistant. Based on the following symptoms:
# #     {', '.join(symptoms)}
    
# #     My system suggests the diagnosis of: {diagnosis['condition_name']} with confidence {diagnosis['confidence']:.2f}.
    
# #     Please provide:
# #     1. Your assessment of this diagnosis
# #     2. Any other conditions that should be considered
# #     3. Additional questions that would be helpful to ask the patient
# #     4. General advice for someone with these symptoms
    
# #     Reply in a concise, helpful format. Remember this is for educational purposes only.
# #     """
    
# #     data = {
# #         "model": "gpt-3.5-turbo",
# #         "messages": [{"role": "user", "content": prompt}],
# #         "temperature": 0.7,
# #         "max_tokens": 500
# #     }
    
# #     try:
# #         response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=data)
# #         if response.status_code == 200:
# #             return response.json()["choices"][0]["message"]["content"]
# #         else:
# #             return f"Error: {response.status_code} - {response.text}"
# #     except Exception as e:
# #         return f"Error connecting to OpenAI API: {str(e)}"

# # # NEW: AI Integration - Get Claude Analysis
# # def get_claude_analysis(symptoms, diagnosis, api_key):
# #     """Get AI analysis of symptoms and diagnosis using Claude API."""
# #     if not api_key:
# #         return "Please provide an API key to use AI analysis."
    
# #     headers = {
# #         "Content-Type": "application/json",
# #         "x-api-key": api_key,
# #         "anthropic-version": "2023-06-01"
# #     }
    
# #     prompt = f"""
# #     I'm a medical diagnostic assistant. Based on the following symptoms:
# #     {', '.join(symptoms)}
    
# #     My system suggests the diagnosis of: {diagnosis['condition_name']} with confidence {diagnosis['confidence']:.2f}.
    
# #     Please provide:
# #     1. Your assessment of this diagnosis
# #     2. Any other conditions that should be considered
# #     3. Additional questions that would be helpful to ask the patient
# #     4. General advice for someone with these symptoms
    
# #     Reply in a concise, helpful format. Remember this is for educational purposes only.
# #     """
    
# #     data = {
# #         "model": "claude-2.0",
# #         "prompt": f"\n\nHuman: {prompt}\n\nAssistant:",
# #         "max_tokens_to_sample": 500,
# #         "temperature": 0.7
# #     }
    
# #     try:
# #         response = requests.post("https://api.anthropic.com/v1/complete", headers=headers, json=data)
# #         if response.status_code == 200:
# #             return response.json()["completion"]
# #         else:
# #             return f"Error: {response.status_code} - {response.text}"
# #     except Exception as e:
# #         return f"Error connecting to Claude API: {str(e)}"

# # Initialize session state
# def init_session_state():
#     """Initialize session state variables."""
#     if 'bookmarks' not in st.session_state:
#         st.session_state.bookmarks = load_bookmarks()
    
#     if 'fade_in' not in st.session_state:
#         st.session_state.fade_in = False
    
#     if 'language_simplified' not in st.session_state:
#         st.session_state.language_simplified = False
        
#     if 'selected_symptoms' not in st.session_state:
#         st.session_state.selected_symptoms = []
        
#     if 'symptom_onset' not in st.session_state:
#         st.session_state.symptom_onset = "Today"
    
#     if 'openai_api_key' not in st.session_state:
#         st.session_state.openai_api_key = ""
        
#     if 'claude_api_key' not in st.session_state:
#         st.session_state.claude_api_key = ""
        
#     if 'ai_provider' not in st.session_state:
#         st.session_state.ai_provider = "OpenAI"



# # Main function to run the Streamlit interface
# def main():
#     """Run the enhanced Streamlit interface for the Medical Diagnostic Agent."""
#     # Initialize session state
#     init_session_state()
    
#     # Configure the page
#     configure_page()
    
#     # Insert tooltip CSS
#     st.markdown(get_tooltip_css(), unsafe_allow_html=True)
    
#     # Add fade-in animation CSS
#     st.markdown("""
#     <style>
#     @keyframes fadein {
#         from { opacity: 0; }
#         to   { opacity: 1; }
#     }
    
#     .fade-in {
#         animation: fadein 1s;
#     }
#     </style>
#     """, unsafe_allow_html=True)
    
#     # Get the agent
#     agent = get_agent()
    
#     # Sidebar settings
#     st.sidebar.title("Settings")
    
#     # Dark mode toggle
#     dark_mode = st.sidebar.checkbox("Dark Mode", value=False)
    
#     # Simplified language toggle
#     simplified_language = st.sidebar.checkbox("Simplified Medical Terms", value=st.session_state.language_simplified,
#                                             help="Use simpler language instead of medical terminology")
#     st.session_state.language_simplified = simplified_language
    
#     # # AI Integration Settings
#     # st.sidebar.markdown("---")
#     # st.sidebar.subheader("AI Integration")
    
#     # # AI provider selection
#     # ai_provider = st.sidebar.radio("AI Provider", ["OpenAI", "Claude", "None"], 
#     #                               index=["OpenAI", "Claude", "None"].index(st.session_state.ai_provider))
#     # st.session_state.ai_provider = ai_provider
    
#     # # API Key input
#     # if ai_provider == "OpenAI":
#     #     openai_api_key = st.sidebar.text_input("OpenAI API Key", value=st.session_state.openai_api_key, 
#     #                                          type="password", help="Enter your OpenAI API key")
#     #     st.session_state.openai_api_key = openai_api_key
#     # elif ai_provider == "Claude":
#     #     claude_api_key = st.sidebar.text_input("Claude API Key", value=st.session_state.claude_api_key, 
#     #                                         type="password", help="Enter your Claude API key")
#     #     st.session_state.claude_api_key = claude_api_key
    
#     # Add bookmark section to sidebar
#     st.sidebar.markdown("---")
#     st.sidebar.subheader("Saved Diagnoses")
    
#     if st.session_state.bookmarks:
#         for bookmark_id, bookmark in st.session_state.bookmarks.items():
#             if st.sidebar.button(f"{bookmark['date']} - {bookmark['primary_diagnosis']}",
#                                key=f"bookmark_{bookmark_id}"):
#                 # Load this bookmark
#                 st.session_state.selected_symptoms = bookmark['symptoms']
#                 st.session_state.symptom_onset = bookmark['symptom_onset']
#                 st.experimental_rerun()
#     else:
#         st.sidebar.write("No saved diagnoses yet.")
    
#     if dark_mode:
#         # Add dark theme CSS
#         st.markdown("""
#         <style>
#         .stApp {
#             background-color: #1E1E1E;
#             color: #FFFFFF;
#         }
#         .stButton>button {
#             background-color: #4e4e4e;
#             color: white;
#         }
#         .stExpander {
#             background-color: #2d2d2d;
#         }
#         </style>
#         """, unsafe_allow_html=True)
    
#     # Title and description
#     st.title("Medical Diagnostic Agent System")
    
#     # Create tooltip for educational purpose
#     edu_tooltip = tooltip(
#         "This intelligent agent uses a best-first search algorithm to suggest possible diagnoses based on reported symptoms.",
#         "This is an educational prototype and should not replace professional medical advice."
#     )
    
#     st.markdown(f"""
#     {edu_tooltip} Please select your symptoms from the list below.
    
#     **Note: This is a prototype for educational purposes only and is not a substitute for professional medical advice.**
#     """, unsafe_allow_html=True)
    
#     # Create layout with columns for better organization
#     col1, col2 = st.columns([1, 2])
    
#     with col1:
#         st.subheader("Select Your Symptoms")
        
#         # Add symptom search
#         search_query = st.text_input("Search symptoms:", "")
        
#         # Group symptoms by body system
#         categorized_symptoms = group_symptoms_by_system(agent.symptoms)
        
#         # Show body map toggle
#         show_body_map = st.checkbox("Show body map", value=False)
        
#         if show_body_map:
#             st.components.v1.html(create_body_map(), height=450)
        
#         # Create symptom selection with categories
#         selected_symptoms = []
        
#         # Display symptoms with categorization and search filtering
#         for system, symptoms in categorized_symptoms.items():
#             if symptoms:  # Only show categories with symptoms
#                 with st.expander(f"{system} Symptoms", expanded=True):
#                     for symptom_id, symptom_name in symptoms:
#                         # Filter based on search query
#                         if search_query.lower() in symptom_name.lower() or not search_query:
#                             # Use session state to maintain selections
#                             key = f"symptom_{symptom_id}"
#                             if key not in st.session_state:
#                                 st.session_state[key] = symptom_name in st.session_state.selected_symptoms
                            
#                             if st.checkbox(symptom_name, key=key):
#                                 selected_symptoms.append(symptom_name)
        
#         # Update session state with current selections
#         st.session_state.selected_symptoms = selected_symptoms
        
#         # Add symptom timeline - NEW FEATURE
#         st.subheader("Symptom Timeline")
        
#         # Get symptom onset time
#         onset_options = ["Today", "Yesterday", "2-3 days ago", "This week", "Last week", "This month", "Over a month ago"]
#         symptom_onset = st.selectbox("When did symptoms begin?", onset_options, 
#                                    index=onset_options.index(st.session_state.symptom_onset))
        
#         # Update session state
#         st.session_state.symptom_onset = symptom_onset
        
#         # Add a slider for diagnoses
#         max_diagnoses = st.slider(
#             "Maximum number of diagnoses to show:",
#             min_value=1,
#             max_value=5,
#             value=3
#         )
        
#         # Show suggested related symptoms - NEW FEATURE
#         if selected_symptoms:
#             related_symptoms = suggest_related_symptoms(selected_symptoms, agent)
#             if related_symptoms:
#                 st.markdown("#### You might also consider:")
#                 for symptom in related_symptoms:
#                     if symptom not in selected_symptoms:
#                         if st.button(f"+ {symptom}", key=f"add_{symptom}"):
#                             # Add this symptom
#                             st.session_state.selected_symptoms.append(symptom)
#                             st.experimental_rerun()
        
#         # Check for contradictory symptoms - NEW FEATURE
#         contradiction = check_contradictory_symptoms(selected_symptoms, agent)
#         if contradiction:
#             st.warning(contradiction)
        
#         # Add a diagnose button
#         diagnose_button = st.button("Get Diagnosis", use_container_width=True)
    
#     # Display results in the second column
#     with col2:
#         # Store results for report generation
#         results = None
        
#         if diagnose_button and selected_symptoms:
#             # Use fade-in animation
#             st.session_state.fade_in = True
            
#             # Set fade-in class if animation is enabled
#             fade_class = "fade-in" if st.session_state.fade_in else ""
            
#             st.markdown(f'<div class="{fade_class}">', unsafe_allow_html=True)
            
#             st.subheader("Diagnostic Results")
            
#             # Process the symptoms
#             agent.perceive(selected_symptoms)
            
#             # Get diagnoses
#             results = agent.act(max_diagnoses)
            
#             # Add symptom timeline to results
#             results['symptom_onset'] = symptom_onset
            
#             if not results['diagnoses']:
#                 st.warning("Not enough information to make a diagnosis. Please provide more symptoms.")
#             else:
#                 # Create bar chart for all diagnoses
#                 diagnosis_names = [d['condition_name'] for d in results['diagnoses']]
#                 confidence_scores = [d['confidence'] for d in results['diagnoses']]
                
#                 # Create DataFrame for the chart
#                 df = pd.DataFrame({
#                     'Condition': diagnosis_names,
#                     'Confidence': confidence_scores
#                 })
                
#                 # Create confidence score visualization
#                 st.subheader("Confidence Comparison")
#                 fig, ax = plt.subplots(figsize=(10, 5))
#                 bars = ax.barh(df['Condition'], df['Confidence'], color=[get_confidence_color(score) for score in df['Confidence']])
#                 ax.set_xlim(0, 1)
#                 ax.set_xlabel('Confidence Score')
#                 ax.set_title('Diagnosis Confidence Comparison')
                
#                 # Add value labels to the bars
#                 for i, v in enumerate(df['Confidence']):
#                     ax.text(v + 0.01, i, f'{v:.2f}', va='center')
                
#                 st.pyplot(fig)
                
#                 # Display each diagnosis with improved visuals
#                 for i, diagnosis in enumerate(results['diagnoses']):
#                     confidence_color = get_confidence_color(diagnosis['confidence'])
                    
#                     # Create an expander with colored header based on confidence
#                     with st.expander(
#                         f"{i+1}. {diagnosis['condition_name']} - Confidence: {diagnosis['confidence']:.2f}",
#                         expanded=(i == 0)  # Expand only the first result by default
#                     ):
#                         # Create three columns for explanation, visualization, and AI analysis
#                         exp_col1, exp_col2, exp_col3 = st.columns([2, 2, 2])
                        
#                         with exp_col1:
#                             st.markdown("### Explanation")
                            
#                             # Apply simplified language if enabled
#                             explanation_text = results['explanations'][diagnosis['condition_id']]
#                             if simplified_language:
#                                 explanation_text = simplify_medical_terms(explanation_text)
                            
#                             st.markdown(explanation_text)
                            
#                             st.markdown("### Recommendations")
                            
#                             # Apply simplified language if enabled
#                             recommendations_text = results['recommendations'][diagnosis['condition_id']]
#                             if simplified_language:
#                                 recommendations_text = simplify_medical_terms(recommendations_text)
                                
#                             st.markdown(recommendations_text)
                        
#                         with exp_col2:
#                             # Add confidence gauge
#                             st.markdown("#### Confidence Score")
#                             gauge_fig = create_confidence_gauge(diagnosis['confidence'])
#                             st.pyplot(gauge_fig)
                            
#                             # Add symptom match visualization
#                             st.markdown("#### Symptom Analysis")
#                             explanation_fig = create_explanation_viz(diagnosis, agent)
#                             st.pyplot(explanation_fig)
                            
#                             # Add related conditions section
#                             st.markdown("### Related Conditions")
#                             related_conditions = find_related_conditions(diagnosis['condition_id'], agent)
                            
#                             for rel_id, rel_name, similarity in related_conditions:
#                                 similarity_pct = int(similarity * 100)
#                                 st.markdown(f"- {rel_name} ({similarity_pct}% symptom overlap)")
                        
#                         # Add AI analysis in the third column
#                         with exp_col3:
#                             st.markdown("### AI Second Opinion")
                            
#                             if st.session_state.ai_provider == "OpenAI" and st.session_state.openai_api_key:
#                                 with st.spinner("Getting AI analysis..."):
#                                     ai_analysis = get_ai_analysis(
#                                         selected_symptoms, 
#                                         diagnosis, 
#                                         st.session_state.openai_api_key
#                                     )
#                                     st.markdown(ai_analysis)
#                             elif st.session_state.ai_provider == "Claude" and st.session_state.claude_api_key:
#                                 with st.spinner("Getting AI analysis..."):
#                                     ai_analysis = get_claude_analysis(
#                                         selected_symptoms, 
#                                         diagnosis, 
#                                         st.session_state.claude_api_key
#                                     )
#                                     st.markdown(ai_analysis)
#                             else:
#                                 st.info("AI analysis is available with OpenAI or Claude API keys. Configure in the sidebar.")
                                
#                                 # Show sample AI analysis format
#                                 st.markdown("""
#                                 #### Sample AI Analysis Format:
                                
#                                 1. **Assessment of Diagnosis**: 
#                                    - Evaluation of the proposed diagnosis based on symptoms
                                
#                                 2. **Other Conditions to Consider**:
#                                    - Alternative diagnoses to consider
                                
#                                 3. **Additional Questions**:
#                                    - Questions that would help clarify the diagnosis
                                
#                                 4. **General Advice**:
#                                    - Recommendations for someone with these symptoms
#                                 """)
                
#                 # Add bookmark and report generation features
#                 st.markdown("---")
#                 report_col1, report_col2 = st.columns(2)
                
#                 with report_col1:
#                     # Bookmark feature - FIXED
#                     if st.button("Save This Diagnosis"):
#                         # Generate unique ID
#                         bookmark_id = str(uuid.uuid4())
                        
#                         # Create bookmark
#                         st.session_state.bookmarks[bookmark_id] = {
#                             'date': datetime.now().strftime("%Y-%m-%d"),
#                             'symptoms': selected_symptoms,
#                             'symptom_onset': symptom_onset,
#                             'primary_diagnosis': results['diagnoses'][0]['condition_name'] if results['diagnoses'] else "No diagnosis"
#                         }
                        
#                         # Save bookmarks to file
#                         if save_bookmarks(st.session_state.bookmarks):
#                             st.success("Diagnosis saved! You can access it from the sidebar.")
#                         else:
#                             st.error("Failed to save diagnosis. Please try again.")
                
#                 with report_col2:
#                     # Report generation - FIXED
#                     patient_name = st.text_input("Patient name for report (optional):", "")
                    
#                     if st.button("Generate Printable Report"):
#                         try:
#                             # Generate PDF report
#                             with st.spinner("Generating PDF report..."):
#                                 pdf_bytes = generate_pdf_report(
#                                     patient_name, 
#                                     selected_symptoms, 
#                                     results, 
#                                     agent, 
#                                     simplified_language
#                                 )
                                
#                                 # Create download link
#                                 st.markdown(
#                                     get_pdf_download_link(pdf_bytes), 
#                                     unsafe_allow_html=True
#                                 )
#                         except Exception as e:
#                             st.error(f"Error generating report: {str(e)}")
                
#                 # Add a disclaimer
#                 st.markdown("""
#                 ---
#                 **Disclaimer:** This is an educational prototype. The diagnoses provided are based on a simplified model
#                 and should not be used for actual medical decisions. Always consult with a healthcare professional for
#                 proper diagnosis and treatment.
#                 """)
            
#             # Close fade-in div
#             st.markdown('</div>', unsafe_allow_html=True)
            
#         elif diagnose_button:
#             st.warning("Please select at least one symptom.")
#         else:
#             st.info("Select symptoms and click 'Get Diagnosis' to receive possible diagnoses.")
            
#             # Show improved information about the agent
#             st.markdown("""
#             ### How This Works
            
#             This diagnostic agent uses a best-first search algorithm to navigate through a knowledge base of medical conditions and their associated symptoms. The search prioritizes conditions that most closely match your reported symptoms, considering factors such as:
#             """)
            
#             # Use bullet points with tooltips for better readability
#             st.markdown(f"""
#             - {tooltip("Symptom-Condition Association", "The strength of relationship between symptoms and conditions based on medical knowledge")}
#             - {tooltip("Primary Symptoms", "Key symptoms that are strongly indicative of specific conditions")}
#             - {tooltip("Condition Prevalence", "How common different conditions are in the general population")}
#             """, unsafe_allow_html=True)
            
#             st.markdown("""
#             ### Understanding Confidence Scores
            
#             The confidence score is calculated using the following formula:
            
#             `Confidence = 0.7 * (MatchedWeight / TotalWeight) + 0.3 * (PrimarySymptomMatch / TotalPrimarySymptoms)`
            
#             This balances the breadth of symptom matching (70%) with the presence of primary symptoms (30%) to provide a more nuanced assessment of diagnostic likelihood.
#             """)
            
#             # Add AI integration explanation
#             st.markdown("""
#             ### AI Integration
            
#             This system now includes AI integration to provide a second opinion on diagnoses:
            
#             1. **Configure an AI Provider**: Choose between OpenAI (GPT) or Claude in the sidebar
#             2. **Enter Your API Key**: Provide your API key for secure access
#             3. **Get AI Analysis**: When you run a diagnosis, the AI will analyze the results and provide:
#                - Assessment of the diagnosis accuracy
#                - Alternative conditions to consider
#                - Additional questions to ask
#                - General advice for someone with these symptoms
            
#             The AI analysis provides a valuable second perspective to complement the rule-based diagnostic system.
#             """)
            
#             # Add feature explanations
#             st.markdown("""
#             ### Features
            
#             - **Symptom Timeline**: Indicate when your symptoms began to help with diagnosis
#             - **Bookmarking**: Save your symptom sets and diagnoses for future reference
#             - **Printable Report**: Generate a PDF report of your diagnosis to share with healthcare providers
#             - **Related Symptoms**: Get suggestions for related symptoms you might be experiencing
#             - **Simplified Language**: Toggle between medical terminology and simpler language
#             - **Related Conditions**: See other conditions with similar symptom profiles
#             - **AI Second Opinion**: Get an AI-powered analysis of your symptoms and diagnosis
#             """)
    
#     # Add information about the project at the bottom
#     st.markdown("""
#     ---
#     ### About This Project
    
#     This Medical Diagnostic Agent System was developed as a final project for ITEC 781: Artificial Intelligence and Informatics I. 
#     It demonstrates the application of intelligent agent architecture and search algorithms in the healthcare domain,
#     enhanced with AI integration for more comprehensive analysis.
    
#     The system uses:
#     - A reactive agent architecture with perception, reasoning, and action components
#     - Best-first search algorithm for diagnosis identification
#     - A knowledge base with conditions, symptoms, and their relationships
#     - AI integration for enhanced analysis and second opinions
#     """)

# if __name__ == "__main__":
#     main()








"""
Medical Diagnostic Agent with Integrated Claude Chatbot.

This module provides a complete Streamlit interface including:
- Symptom selection and diagnosis
- PDF report generation
- Bookmark/save functionality
- Claude AI chatbot for discussing results
"""

import streamlit as st
import json
import os
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from diagnostic_agent import DiagnosticAgent
import time
from datetime import datetime, timedelta
import uuid
import base64
from io import BytesIO
import re
import pickle
from fpdf import FPDF
import requests

# Page configuration
def configure_page():
    """Configure the Streamlit page settings."""
    st.set_page_config(
        page_title="Medical Diagnostic Agent",
        page_icon="🏥",
        layout="wide",
        initial_sidebar_state="expanded"
    )

# Initialize the agent
@st.cache_resource
def get_agent():
    """Initialize and cache the diagnostic agent."""
    kb_path = "knowledge_base.json"
    return DiagnosticAgent(kb_path)

# Group symptoms by body system
def group_symptoms_by_system(symptoms):
    """Group symptoms by body system for better organization."""
    # Define body system categories
    body_systems = {
        "Respiratory": ["Cough", "Shortness of breath", "Wheezing", "Runny nose", "Sore throat"],
        "Digestive": ["Nausea", "Vomiting", "Diarrhea", "Abdominal pain", "Loss of appetite"],
        "Neurological": ["Headache", "Confusion", "Dizziness", "Loss of taste or smell"],
        "General": ["Fever", "Fatigue", "Muscle pain", "Joint pain", "Rash", "Chest pain"]
    }
    
    # Categorize symptoms
    categorized = {system: [] for system in body_systems}
    other = []
    
    for symptom_id, symptom_data in symptoms.items():
        symptom_name = symptom_data["name"]
        categorized_flag = False
        
        for system, system_symptoms in body_systems.items():
            if symptom_name in system_symptoms:
                categorized[system].append((symptom_id, symptom_name))
                categorized_flag = True
                break
                
        if not categorized_flag:
            other.append((symptom_id, symptom_name))
    
    # Add 'Other' category if needed
    if other:
        categorized["Other"] = other
        
    return categorized

# Generate color for confidence score
def get_confidence_color(score):
    """Return color based on confidence score."""
    if score >= 0.7:
        return "green"
    elif score >= 0.4:
        return "orange"
    else:
        return "red"

# Create confidence gauge chart
def create_confidence_gauge(score):
    """Create a gauge chart for the confidence score."""
    fig, ax = plt.subplots(figsize=(3, 2), subplot_kw={'projection': 'polar'})
    
    # Gauge settings
    theta = np.linspace(0, 180, 100) * np.pi / 180
    r = np.ones_like(theta)
    
    # Color sections
    ax.barh(0, 1, 0.6, theta[0], color='red', alpha=0.4)
    ax.barh(0, 1, 0.6, theta[33], color='orange', alpha=0.4)
    ax.barh(0, 1, 0.6, theta[66], color='green', alpha=0.4)
    
    # Needle
    needle_theta = score * 180 * np.pi / 180
    ax.plot([0, needle_theta], [0, 0.5], color='black', linewidth=2)
    
    # Clean up
    ax.set_yticks([])
    ax.set_xticks([])
    ax.set_ylim(0, 1)
    ax.set_title(f'Confidence: {score:.2f}', size=10)
    ax.spines['polar'].set_visible(False)
    
    return fig

# Create explanation visualization
def create_explanation_viz(diagnosis, agent):
    """Create a visualization of symptom matches for a diagnosis."""
    condition_id = diagnosis['condition_id']
    condition = agent.conditions[condition_id]
    
    # Get all symptoms for this condition
    all_condition_symptoms = [(s_id, agent.symptoms[s_id]['name'], weight) 
                             for s_id, weight in condition['symptoms'].items()]
    
    # Sort by weight descending
    all_condition_symptoms.sort(key=lambda x: x[2], reverse=True)
    
    # Prepare data for visualization
    symptom_names = [s[1] for s in all_condition_symptoms]
    weights = [s[2] for s in all_condition_symptoms]
    
    # Mark matched symptoms
    matched = [s[1] in diagnosis['matched_symptoms'] for s in all_condition_symptoms]
    colors = ['#2ecc71' if m else '#e74c3c' for m in matched]
    
    # Create horizontal bar chart
    fig, ax = plt.subplots(figsize=(8, max(3, len(symptom_names)*0.4)))
    bars = ax.barh(symptom_names, weights, color=colors)
    
    # Add legend
    from matplotlib.patches import Patch
    legend_elements = [
        Patch(facecolor='#2ecc71', label='Matched'),
        Patch(facecolor='#e74c3c', label='Not Present')
    ]
    ax.legend(handles=legend_elements, loc='upper right')
    
    # Add labels
    ax.set_title(f'Symptom Analysis for {condition["name"]}')
    ax.set_xlabel('Symptom Weight')
    
    # Improve appearance
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    return fig

# Create a human body map
def create_body_map():
    """Create a simple human body map with clickable regions."""
    # This is a placeholder HTML for a clickable body map
    body_map_html = """
    <style>
    .body-map {
        position: relative;
        width: 200px;
        height: 400px;
        margin: 0 auto;
        background-color: #f0f0f0;
        border-radius: 100px 100px 0 0;
    }
    .body-region {
        position: absolute;
        cursor: pointer;
        border: 1px solid #ddd;
        border-radius: 4px;
        text-align: center;
        font-size: 10px;
        color: #555;
    }
    .head {
        top: 20px;
        left: 75px;
        width: 50px;
        height: 50px;
        border-radius: 25px;
    }
    .chest {
        top: 80px;
        left: 50px;
        width: 100px;
        height: 80px;
    }
    .abdomen {
        top: 170px;
        left: 50px;
        width: 100px;
        height: 80px;
    }
    .limbs {
        top: 260px;
        left: 30px;
        width: 140px;
        height: 120px;
    }
    </style>
    
    <div class="body-map">
        <div class="body-region head" onclick="selectRegion('head')" title="Head & Neck">Head & Neck</div>
        <div class="body-region chest" onclick="selectRegion('chest')" title="Chest & Back">Chest & Back</div>
        <div class="body-region abdomen" onclick="selectRegion('abdomen')" title="Abdomen">Abdomen</div>
        <div class="body-region limbs" onclick="selectRegion('limbs')" title="Arms & Legs">Arms & Legs</div>
    </div>
    
    <script>
    function selectRegion(region) {
        // This would ideally communicate with Streamlit
        // For now, we'll just show an alert
        alert('Selected region: ' + region);
    }
    </script>
    """
    
    return body_map_html

# Generate PDF report using FPDF
def generate_pdf_report(patient_name, symptoms, results, agent, simplified_language):
    """Generate a printable report of the diagnosis using FPDF."""
    # Initialize PDF
    pdf = FPDF()
    pdf.add_page()
    
    # Set up fonts
    pdf.set_font("Arial", "B", 16)
    
    # Title
    pdf.cell(0, 10, "Medical Diagnostic Report", ln=True, align="C")
    pdf.ln(5)
    
    # Patient info
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, f"Patient: {patient_name if patient_name else 'Anonymous'}", ln=True)
    pdf.cell(0, 10, f"Date: {datetime.now().strftime('%B %d, %Y')}", ln=True)
    pdf.ln(5)
    
    # Disclaimer
    pdf.set_font("Arial", "I", 10)
    pdf.multi_cell(0, 5, "Educational Prototype - Not for Clinical Use")
    pdf.ln(5)
    
    # Symptoms section
    pdf.set_font("Arial", "B", 12)
    pdf.cell(0, 10, "Reported Symptoms:", ln=True)
    pdf.set_font("Arial", "", 12)
    
    for symptom in symptoms:
        pdf.cell(0, 8, f"• {symptom}", ln=True)
    
    pdf.cell(0, 8, f"Symptom onset: {results.get('symptom_onset', 'Not specified')}", ln=True)
    pdf.ln(5)
    
    # Diagnoses section
    if results['diagnoses']:
        pdf.set_font("Arial", "B", 12)
        pdf.cell(0, 10, "Diagnostic Results:", ln=True)
        
        for i, diagnosis in enumerate(results['diagnoses']):
            pdf.set_font("Arial", "B", 12)
            pdf.cell(0, 10, f"{i+1}. {diagnosis['condition_name']} (Confidence: {diagnosis['confidence']:.2f})", ln=True)
            
            # Explanation
            pdf.set_font("Arial", "", 10)
            explanation_text = results['explanations'][diagnosis['condition_id']]
            if simplified_language:
                explanation_text = simplify_medical_terms(explanation_text)
            
            pdf.multi_cell(0, 5, explanation_text)
            pdf.ln(3)
            
            # Recommendations
            pdf.set_font("Arial", "B", 11)
            pdf.cell(0, 8, "Recommendations:", ln=True)
            pdf.set_font("Arial", "", 10)
            
            recommendations_text = results['recommendations'][diagnosis['condition_id']]
            if simplified_language:
                recommendations_text = simplify_medical_terms(recommendations_text)
                
            pdf.multi_cell(0, 5, recommendations_text)
            pdf.ln(5)
    else:
        pdf.set_font("Arial", "I", 12)
        pdf.cell(0, 10, "No diagnoses found based on the provided symptoms.", ln=True)
        pdf.cell(0, 10, "Please consult with a healthcare professional.", ln=True)
    
    # Disclaimer footer
    pdf.ln(10)
    pdf.set_font("Arial", "I", 8)
    pdf.multi_cell(0, 4, "DISCLAIMER: This report was generated by an educational prototype and should not replace professional medical advice. Always consult with a healthcare provider for proper diagnosis and treatment.")
    
    # Return PDF as bytes
    return pdf.output(dest='S').encode('latin1')

# Create download link for PDF
def get_pdf_download_link(pdf_bytes, filename="medical_diagnosis_report.pdf"):
    """Generate a link to download the PDF file."""
    b64 = base64.b64encode(pdf_bytes).decode()
    href = f'<a href="data:application/pdf;base64,{b64}" download="{filename}" target="_blank">Download PDF Report</a>'
    return href

# Save bookmarks to file
def save_bookmarks(bookmarks):
    """Save bookmarks to a file."""
    try:
        with open('bookmarks.pkl', 'wb') as f:
            pickle.dump(bookmarks, f)
        return True
    except Exception as e:
        st.error(f"Error saving bookmarks: {e}")
        return False

# Load bookmarks from file
def load_bookmarks():
    """Load bookmarks from a file."""
    try:
        if os.path.exists('bookmarks.pkl'):
            with open('bookmarks.pkl', 'rb') as f:
                return pickle.load(f)
        return {}
    except Exception as e:
        st.error(f"Error loading bookmarks: {e}")
        return {}

# Suggest related symptoms based on selected symptoms
def suggest_related_symptoms(selected_symptoms, agent):
    """Suggest related symptoms based on currently selected symptoms."""
    if not selected_symptoms:
        return []
    
    related_symptoms = []
    selected_conditions = []
    
    # Find conditions related to selected symptoms
    for symptom_name in selected_symptoms:
        for symptom_id, symptom_data in agent.symptoms.items():
            if symptom_data['name'].lower() == symptom_name.lower():
                # Find conditions that have this symptom
                for condition_id, condition in agent.conditions.items():
                    if symptom_id in condition['symptoms']:
                        selected_conditions.append(condition_id)
    
    # Find other symptoms from these conditions
    for condition_id in selected_conditions:
        condition = agent.conditions[condition_id]
        for symptom_id in condition['symptoms']:
            symptom_name = agent.symptoms[symptom_id]['name']
            if symptom_name not in selected_symptoms and symptom_name not in related_symptoms:
                related_symptoms.append(symptom_name)
    
    # Return top 5 related symptoms
    return related_symptoms[:5]

# Find related conditions
def find_related_conditions(condition_id, agent, max_conditions=3):
    """Find related conditions based on symptom overlap."""
    condition = agent.conditions[condition_id]
    condition_symptoms = set(condition['symptoms'].keys())
    
    related = []
    for other_id, other_condition in agent.conditions.items():
        if other_id != condition_id:
            other_symptoms = set(other_condition['symptoms'].keys())
            overlap = len(condition_symptoms.intersection(other_symptoms))
            if overlap > 0:
                similarity = overlap / len(condition_symptoms.union(other_symptoms))
                related.append((other_id, other_condition['name'], similarity))
    
    # Sort by similarity and return top results
    related.sort(key=lambda x: x[2], reverse=True)
    return related[:max_conditions]

# Tooltip HTML
def tooltip(text, tooltip_text):
    """Create HTML for a text with tooltip."""
    return f"""
    <span class="tooltip">{text}
        <span class="tooltiptext">{tooltip_text}</span>
    </span>
    """

# Add tooltip CSS
def get_tooltip_css():
    """Return CSS for tooltips."""
    return """
    <style>
    .tooltip {
        position: relative;
        display: inline-block;
        border-bottom: 1px dotted #ccc;
        cursor: help;
    }
    
    .tooltip .tooltiptext {
        visibility: hidden;
        width: 200px;
        background-color: #555;
        color: #fff;
        text-align: center;
        border-radius: 6px;
        padding: 5px;
        position: absolute;
        z-index: 1;
        bottom: 125%;
        left: 50%;
        margin-left: -100px;
        opacity: 0;
        transition: opacity 0.3s;
    }
    
    .tooltip:hover .tooltiptext {
        visibility: visible;
        opacity: 0.9;
    }
    </style>
    """

# Check for contradictory symptoms
def check_contradictory_symptoms(symptoms, agent):
    """Check for contradictory symptom combinations."""
    contradictory_pairs = [
        ("Loss of appetite", "Increased appetite"),
        ("Fever", "Hypothermia"),
        ("Diarrhea", "Constipation"),
        ("Insomnia", "Excessive sleepiness")
    ]
    
    for pair in contradictory_pairs:
        if pair[0] in symptoms and pair[1] in symptoms:
            return f"{pair[0]} and {pair[1]} are contradictory symptoms."
    
    return None

# Simplify medical terminology with more robust implementation
def simplify_medical_terms(text):
    """Replace complex medical terms with simpler alternatives."""
    simplifications = {
        "myocardial infarction": "heart attack",
        "cerebrovascular accident": "stroke",
        "dyspnea": "shortness of breath",
        "pyrexia": "fever",
        "emesis": "vomiting",
        "syncope": "fainting",
        "edema": "swelling",
        "myalgia": "muscle pain",
        "cephalgia": "headache",
        "arthralgia": "joint pain",
        "pruritus": "itching",
        "erythema": "redness of skin",
        "lethargy": "tiredness",
        "vertigo": "dizziness",
        "anorexia": "loss of appetite",
        "dysphagia": "difficulty swallowing",
        "tachycardia": "rapid heart rate",
        "bradycardia": "slow heart rate",
        "hypertension": "high blood pressure",
        "hypotension": "low blood pressure",
        "upper respiratory": "nose and throat",
        "respiratory tract": "breathing system",
        "gastrointestinal": "stomach and intestines",
        "inflammation": "swelling",
        "condition": "health problem",
        "diagnoses": "findings",
        "diagnosis": "finding",
        "prevalence": "frequency",
        "symptoms": "signs",
        "consultation": "visit",
        "primary": "main",
        "practitioner": "doctor",
        "medication": "medicine",
        "prescribed": "ordered",
        "therapeutic": "treatment",
        "diagnostic": "testing",
        "assessment": "check-up",
        "physician": "doctor"
    }
    
    # Case-insensitive replacement with word boundary check
    for med_term, simple_term in simplifications.items():
        # Use regex with word boundaries for more precise replacement
        pattern = re.compile(r'\b' + re.escape(med_term) + r'\b', re.IGNORECASE)
        text = pattern.sub(simple_term, text)
    
    return text

# NEW: Get Claude AI response for chatbot
def get_claude_response(messages, api_key):
    """Get a response from Claude API."""
    headers = {
        "x-api-key": api_key,
        "content-type": "application/json",
        "anthropic-version": "2023-06-01"
    }
    
    data = {
        "model": "claude-3-haiku-20240307",
        "max_tokens": 500,
        "messages": messages
    }
    
    try:
        response = requests.post(
            "https://api.anthropic.com/v1/messages",
            headers=headers,
            json=data
        )
        if response.status_code == 200:
            return response.json()['content'][0]['text']
        else:
            return f"Error: {response.status_code} - {response.text}"
    except Exception as e:
        return f"Error connecting to Claude API: {str(e)}"

# NEW: Add chat interface for interacting with Claude
def add_chat_interface(selected_symptoms, results, agent):
    """Add a chat interface for discussing symptoms and results with Claude."""
    st.markdown("---")
    st.subheader("💬 Medical Advisor Chat")
    st.write("Chat with our AI medical advisor about your symptoms and results")
    
    # Initialize chat history in session state
    if "messages" not in st.session_state:
        st.session_state.messages = []
        
    # Display chat history
    for message in st.session_state.messages:
        with st.chat_message(message["role"]):
            st.write(message["content"])
    
    # Initial context when results are available and chat is empty
    if results and len(st.session_state.messages) == 0:
        # Create system message with context about symptoms and results
        diagnoses = [d['condition_name'] for d in results['diagnoses']] if results.get('diagnoses') else []
        symptom_list = ", ".join(selected_symptoms)
        
        context = f"""
        Patient symptoms: {symptom_list}
        Symptom onset: {results.get('symptom_onset', 'Not specified')}
        Diagnoses: {', '.join(diagnoses) if diagnoses else 'None'}
        
        You are a helpful medical advisor chatbot. You can discuss the patient's symptoms and 
        possible conditions, but always remind them that this is not a substitute for professional 
        medical advice. Be compassionate but factual. Don't make definitive diagnoses.
        Focus on discussing the symptoms, potential causes, and general recommendations.
        """
        
        # Add the system message (not visible to user)
        if "system_message" not in st.session_state:
            st.session_state.system_message = {"role": "system", "content": context}
    
    # Handle user input
    if prompt := st.chat_input("Ask about your symptoms or diagnosis..."):
        # Add user message to chat
        st.session_state.messages.append({"role": "user", "content": prompt})
        with st.chat_message("user"):
            st.write(prompt)
            
        # Get API key from secrets or ask user
        claude_api_key = st.secrets.get("ANTHROPIC_API_KEY", None)
        if not claude_api_key:
            if "claude_api_key" not in st.session_state:
                claude_api_key = st.text_input("Enter your Claude API key:", type="password")
                if claude_api_key:
                    st.session_state.claude_api_key = claude_api_key
            else:
                claude_api_key = st.session_state.claude_api_key
        
        # If we have the API key, get response from Claude
        if claude_api_key:
            with st.chat_message("assistant"):
                with st.spinner("Thinking..."):
                    # Prepare messages for API (include system message)
                    api_messages = [st.session_state.system_message] if "system_message" in st.session_state else []
                    # Add user messages (excluding system message)
                    api_messages.extend(st.session_state.messages)
                    
                    response = get_claude_response(api_messages, claude_api_key)
                    st.write(response)
                    
            # Add assistant response to chat history
            st.session_state.messages.append({"role": "assistant", "content": response})
        else:
            st.error("Please provide a Claude API key to chat with the medical advisor")

# Initialize session state
def init_session_state():
    """Initialize session state variables."""
    if 'bookmarks' not in st.session_state:
        st.session_state.bookmarks = load_bookmarks()
    
    if 'fade_in' not in st.session_state:
        st.session_state.fade_in = False
    
    if 'language_simplified' not in st.session_state:
        st.session_state.language_simplified = False
        
    if 'selected_symptoms' not in st.session_state:
        st.session_state.selected_symptoms = []
        
    if 'symptom_onset' not in st.session_state:
        st.session_state.symptom_onset = "Today"
    
    if 'claude_api_key' not in st.session_state:
        st.session_state.claude_api_key = ""
        
    if 'messages' not in st.session_state:
        st.session_state.messages = []

"""
Functions to implement a floating chatbot in the bottom right corner.
Add these to your streamlit_interface.py file.
"""

# Floating chatbot implementation
"""
Fixed floating chatbot implementation.
Replace the previous floating chatbot functions with these updated ones.
"""

# Floating chatbot implementation with improved event handling
def add_floating_chatbot_css():
    """Add CSS for floating chatbot."""
    return """
    <style>
    /* Floating chat button */
    #chat-button {
        position: fixed;
        bottom: 20px;
        right: 20px;
        width: 60px;
        height: 60px;
        border-radius: 50%;
        background-color: #2e86de;
        color: white;
        display: flex;
        justify-content: center;
        align-items: center;
        font-size: 24px;
        cursor: pointer;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        z-index: 9999;
        border: none;
    }
    
    /* Chat container */
    #chat-container {
        position: fixed;
        bottom: 90px;
        right: 20px;
        width: 350px;
        height: 500px;
        background-color: white;
        border-radius: 10px;
        box-shadow: 0 4px 12px rgba(0,0,0,0.2);
        display: none;
        flex-direction: column;
        z-index: 9999;
        overflow: hidden;
    }
    
    /* Chat header */
    .chat-header {
        background-color: #2e86de;
        color: white;
        padding: 10px 15px;
        display: flex;
        justify-content: space-between;
        align-items: center;
    }
    
    .chat-header h3 {
        margin: 0;
        font-size: 16px;
    }
    
    #close-chat {
        background: none;
        border: none;
        color: white;
        font-size: 18px;
        cursor: pointer;
    }
    
    /* Chat messages */
    #chat-messages {
        flex: 1;
        padding: 15px;
        overflow-y: auto;
        background-color: #f9f9f9;
    }
    
    .message {
        margin-bottom: 10px;
        max-width: 80%;
        padding: 10px;
        border-radius: 10px;
    }
    
    .user-message {
        background-color: #e9f5ff;
        margin-left: auto;
        border-bottom-right-radius: 0;
        color: #333;
    }
    
    .bot-message {
        background-color: #f1f1f1;
        margin-right: auto;
        border-bottom-left-radius: 0;
        color: #333;
    }
    
    /* Chat input */
    .chat-input-container {
        padding: 10px;
        border-top: 1px solid #ddd;
        display: flex;
        background-color: white;
    }
    
    #chat-input {
        flex: 1;
        padding: 8px 12px;
        border: 1px solid #ddd;
        border-radius: 20px;
        outline: none;
    }
    
    #send-button {
        background-color: #2e86de;
        color: white;
        border: none;
        border-radius: 50%;
        width: 36px;
        height: 36px;
        margin-left: 8px;
        cursor: pointer;
        display: flex;
        justify-content: center;
        align-items: center;
    }
    
    /* Show the chat container when active */
    #chat-container.active {
        display: flex !important;
    }
    
    /* Typing indicator */
    #typing-indicator {
        display: flex;
        padding: 10px;
        align-items: center;
    }
    
    #typing-indicator span {
        height: 8px;
        width: 8px;
        background-color: #aaa;
        border-radius: 50%;
        margin: 0 2px;
        display: inline-block;
        animation: typing 1s infinite ease-in-out;
    }
    
    #typing-indicator span:nth-child(2) {
        animation-delay: 0.2s;
    }
    
    #typing-indicator span:nth-child(3) {
        animation-delay: 0.4s;
    }
    
    @keyframes typing {
        0% { transform: translateY(0px); }
        50% { transform: translateY(-5px); }
        100% { transform: translateY(0px); }
    }
    </style>
    """

def add_floating_chatbot_html():
    """Add HTML for floating chatbot."""
    return """
    <div id="chat-button">
        💬
    </div>
    
    <div id="chat-container">
        <div class="chat-header">
            <h3>Medical Advisor</h3>
            <button id="close-chat">×</button>
        </div>
        <div id="chat-messages">
            <div class="message bot-message">
                Hello! I'm your medical advisor. How can I help you understand your symptoms or diagnosis?
            </div>
        </div>
        <div id="typing-indicator" style="display: none;">
            <span></span>
            <span></span>
            <span></span>
        </div>
        <div class="chat-input-container">
            <input type="text" id="chat-input" placeholder="Type your message...">
            <button id="send-button">➤</button>
        </div>
    </div>
    """

def add_chatbot_javascript(selected_symptoms=None, diagnoses=None):
    """Add JavaScript for floating chatbot with Claude integration."""
    
    # Create context information for Claude
    context = "The patient has no symptoms or diagnosis yet."
    if selected_symptoms and diagnoses:
        symptoms_str = ", ".join(selected_symptoms)
        diagnoses_str = ", ".join([d['condition_name'] for d in diagnoses]) if diagnoses else "No clear diagnosis"
        context = f"The patient has reported the following symptoms: {symptoms_str}. The diagnostic system suggests: {diagnoses_str}."
    
    return f"""
    <script>
    // Initialize chatbot functionality when the DOM is fully loaded
    document.addEventListener('DOMContentLoaded', function() {{
        console.log('DOM fully loaded, initializing chatbot');
        initChatbot();
    }});
    
    // Main chatbot initialization function
    function initChatbot() {{
        console.log('Initializing chatbot');
        const chatButton = document.getElementById('chat-button');
        const chatContainer = document.getElementById('chat-container');
        const closeChat = document.getElementById('close-chat');
        const chatMessages = document.getElementById('chat-messages');
        const chatInput = document.getElementById('chat-input');
        const sendButton = document.getElementById('send-button');
        const typingIndicator = document.getElementById('typing-indicator');
        
        // Patient context for the AI
        const patientContext = `{context}`;
        
        console.log('Setting up event listeners');
        
        // Toggle chat window when chat button is clicked
        if (chatButton) {{
            chatButton.addEventListener('click', function(e) {{
                console.log('Chat button clicked');
                e.preventDefault();
                if (chatContainer) {{
                    chatContainer.classList.toggle('active');
                    console.log('Chat container toggled, is active:', chatContainer.classList.contains('active'));
                }} else {{
                    console.error('Chat container not found');
                }}
            }});
        }} else {{
            console.error('Chat button not found');
        }}
        
        // Close chat window when close button is clicked
        if (closeChat) {{
            closeChat.addEventListener('click', function(e) {{
                console.log('Close button clicked');
                e.preventDefault();
                if (chatContainer) {{
                    chatContainer.classList.remove('active');
                }}
            }});
        }}
        
        // Send message function
        function sendMessage() {{
            const message = chatInput.value.trim();
            if (message) {{
                console.log('Sending message:', message);
                
                // Add user message to chat
                const userMessageDiv = document.createElement('div');
                userMessageDiv.classList.add('message', 'user-message');
                userMessageDiv.textContent = message;
                chatMessages.appendChild(userMessageDiv);
                
                // Clear input
                chatInput.value = '';
                
                // Scroll to bottom
                chatMessages.scrollTop = chatMessages.scrollHeight;
                
                // Show typing indicator
                typingIndicator.style.display = 'flex';
                
                // Get Claude response
                getClaudeResponse(message, patientContext)
                    .then(response => {{
                        console.log('Received AI response');
                        
                        // Hide typing indicator
                        typingIndicator.style.display = 'none';
                        
                        // Add bot message to chat
                        const botMessageDiv = document.createElement('div');
                        botMessageDiv.classList.add('message', 'bot-message');
                        botMessageDiv.textContent = response;
                        chatMessages.appendChild(botMessageDiv);
                        
                        // Scroll to bottom
                        chatMessages.scrollTop = chatMessages.scrollHeight;
                    }})
                    .catch(error => {{
                        console.error('Error getting response:', error);
                        
                        // Hide typing indicator
                        typingIndicator.style.display = 'none';
                        
                        // Add error message
                        const errorMessageDiv = document.createElement('div');
                        errorMessageDiv.classList.add('message', 'bot-message');
                        errorMessageDiv.textContent = "I'm having trouble responding right now. Please try again later.";
                        chatMessages.appendChild(errorMessageDiv);
                        
                        // Scroll to bottom
                        chatMessages.scrollTop = chatMessages.scrollHeight;
                    }});
            }}
        }}
        
        // Send message on button click
        if (sendButton) {{
            sendButton.addEventListener('click', function() {{
                console.log('Send button clicked');
                sendMessage();
            }});
        }}
        
        // Send message on Enter key
        if (chatInput) {{
            chatInput.addEventListener('keypress', function(e) {{
                if (e.key === 'Enter') {{
                    console.log('Enter key pressed');
                    sendMessage();
                }}
            }});
        }}
        
        console.log('Chatbot initialization complete');
    }}
    
    // Claude API integration
    async function getClaudeResponse(message, context) {{
        console.log('Getting Claude response for message:', message);
        
        // Get the Claude API key from session storage or ask for it
        let apiKey = sessionStorage.getItem('claude_api_key');
        
        if (!apiKey) {{
            console.log('No API key found, prompting user');
            apiKey = prompt("Please enter your Claude API key to continue:", "");
            if (apiKey) {{
                sessionStorage.setItem('claude_api_key', apiKey);
            }} else {{
                return "I need an API key to provide assistance. Please click the chat button again and enter your Claude API key.";
            }}
        }}
        
        try {{
            console.log('Sending request to Claude API');
            const response = await fetch('https://api.anthropic.com/v1/messages', {{
                method: 'POST',
                headers: {{
                    'Content-Type': 'application/json',
                    'x-api-key': apiKey,
                    'anthropic-version': '2023-06-01'
                }},
                body: JSON.stringify({{
                    model: 'claude-3-haiku-20240307',
                    max_tokens: 500,
                    messages: [
                        {{
                            role: 'system',
                            content: `You are a helpful medical advisor chatbot. ${context} 
                                      You can discuss symptoms and possible conditions, but always remind 
                                      users this is not a substitute for professional medical advice. 
                                      Be compassionate but factual. Give concise, helpful responses.`
                        }},
                        {{
                            role: 'user',
                            content: message
                        }}
                    ]
                }})
            }});
            
            console.log('Response received from API');
            const data = await response.json();
            if (data.error) {{
                console.error('Claude API error:', data.error);
                return "I encountered an error when trying to respond. Please try again or refresh the page.";
            }}
            return data.content[0].text;
        }} catch (error) {{
            console.error('Error calling Claude API:', error);
            return "I'm having trouble connecting to my reasoning capabilities. Please check your internet connection and try again.";
        }}
    }}
    
    // Initialize immediately as a fallback
    if (document.readyState === 'complete') {{
        console.log('Document already ready, initializing immediately');
        initChatbot();
    }}
    </script>
    """

def add_floating_chatbot(selected_symptoms=None, diagnoses=None):
    """Add a floating chatbot to the page."""
    css = add_floating_chatbot_css()
    html = add_floating_chatbot_html()
    js = add_chatbot_javascript(selected_symptoms, diagnoses)
    
    st.markdown(css + html + js, unsafe_allow_html=True)

# Main function to run the Streamlit interface
# This is just the main() function with the floating chatbot integrated
# Add this to your streamlit_interface.py after adding the floating chatbot functions

def main():
    """Run the enhanced Streamlit interface for the Medical Diagnostic Agent."""
    # Initialize session state
    init_session_state()
    
    # Configure the page
    configure_page()
    
    # Insert tooltip CSS
    st.markdown(get_tooltip_css(), unsafe_allow_html=True)
    
    # Add fade-in animation CSS
    st.markdown("""
    <style>
    @keyframes fadein {
        from { opacity: 0; }
        to   { opacity: 1; }
    }
    
    .fade-in {
        animation: fadein 1s;
    }
    </style>
    """, unsafe_allow_html=True)
    
    # Get the agent
    agent = get_agent()
    
    # Sidebar settings
    st.sidebar.title("Settings")
    
    # Dark mode toggle
    dark_mode = st.sidebar.checkbox("Dark Mode", value=False)
    
    # Simplified language toggle
    simplified_language = st.sidebar.checkbox("Simplified Medical Terms", value=st.session_state.language_simplified,
                                            help="Use simpler language instead of medical terminology")
    st.session_state.language_simplified = simplified_language
    
    # Add bookmark section to sidebar
    st.sidebar.markdown("---")
    st.sidebar.subheader("Saved Diagnoses")
    
    if st.session_state.bookmarks:
        for bookmark_id, bookmark in st.session_state.bookmarks.items():
            if st.sidebar.button(f"{bookmark['date']} - {bookmark['primary_diagnosis']}",
                               key=f"bookmark_{bookmark_id}"):
                # Load this bookmark
                st.session_state.selected_symptoms = bookmark['symptoms']
                st.session_state.symptom_onset = bookmark['symptom_onset']
                st.experimental_rerun()
    else:
        st.sidebar.write("No saved diagnoses yet.")
    
    if dark_mode:
        # Add dark theme CSS
        st.markdown("""
        <style>
        .stApp {
            background-color: #1E1E1E;
            color: #FFFFFF;
        }
        .stButton>button {
            background-color: #4e4e4e;
            color: white;
        }
        .stExpander {
            background-color: #2d2d2d;
        }
        </style>
        """, unsafe_allow_html=True)
    
    # Title and description
    st.title("Medical Diagnostic Agent System")
    
    # Create tooltip for educational purpose
    edu_tooltip = tooltip(
        "This intelligent agent uses a best-first search algorithm to suggest possible diagnoses based on reported symptoms.",
        "This is an educational prototype and should not replace professional medical advice."
    )
    
    st.markdown(f"""
    {edu_tooltip} Please select your symptoms from the list below.
    
    **Note: This is a prototype for educational purposes only and is not a substitute for professional medical advice.**
    """, unsafe_allow_html=True)
    
    # Create layout with columns for better organization
    col1, col2 = st.columns([1, 2])
    
    with col1:
        st.subheader("Select Your Symptoms")
        
        # Add symptom search
        search_query = st.text_input("Search symptoms:", "")
        
        # Group symptoms by body system
        categorized_symptoms = group_symptoms_by_system(agent.symptoms)
        
        # Show body map toggle
        show_body_map = st.checkbox("Show body map", value=False)
        
        if show_body_map:
            st.components.v1.html(create_body_map(), height=450)
        
        # Create symptom selection with categories
        selected_symptoms = []
        
        # Display symptoms with categorization and search filtering
        for system, symptoms in categorized_symptoms.items():
            if symptoms:  # Only show categories with symptoms
                with st.expander(f"{system} Symptoms", expanded=True):
                    for symptom_id, symptom_name in symptoms:
                        # Filter based on search query
                        if search_query.lower() in symptom_name.lower() or not search_query:
                            # Use session state to maintain selections
                            key = f"symptom_{symptom_id}"
                            if key not in st.session_state:
                                st.session_state[key] = symptom_name in st.session_state.selected_symptoms
                            
                            if st.checkbox(symptom_name, key=key):
                                selected_symptoms.append(symptom_name)
        
        # Update session state with current selections
        st.session_state.selected_symptoms = selected_symptoms
        
        # Add symptom timeline
        st.subheader("Symptom Timeline")
        
        # Get symptom onset time
        onset_options = ["Today", "Yesterday", "2-3 days ago", "This week", "Last week", "This month", "Over a month ago"]
        symptom_onset = st.selectbox("When did symptoms begin?", onset_options, 
                                   index=onset_options.index(st.session_state.symptom_onset))
        
        # Update session state
        st.session_state.symptom_onset = symptom_onset
        
        # Add a slider for diagnoses
        max_diagnoses = st.slider(
            "Maximum number of diagnoses to show:",
            min_value=1,
            max_value=5,
            value=3
        )
        
        # Show suggested related symptoms
        if selected_symptoms:
            related_symptoms = suggest_related_symptoms(selected_symptoms, agent)
            if related_symptoms:
                st.markdown("#### You might also consider:")
                for symptom in related_symptoms:
                    if symptom not in selected_symptoms:
                        if st.button(f"+ {symptom}", key=f"add_{symptom}"):
                            # Add this symptom
                            st.session_state.selected_symptoms.append(symptom)
                            st.experimental_rerun()
        
        # Check for contradictory symptoms
        contradiction = check_contradictory_symptoms(selected_symptoms, agent)
        if contradiction:
            st.warning(contradiction)
        
        # Add a diagnose button
        diagnose_button = st.button("Get Diagnosis", use_container_width=True)
    
    # Display results in the second column
    with col2:
        # Store results for report generation
        results = None
        
        if diagnose_button and selected_symptoms:
            # Use fade-in animation
            st.session_state.fade_in = True
            
            # Set fade-in class if animation is enabled
            fade_class = "fade-in" if st.session_state.fade_in else ""
            
            st.markdown(f'<div class="{fade_class}">', unsafe_allow_html=True)
            
            st.subheader("Diagnostic Results")
            
            # Process the symptoms
            agent.perceive(selected_symptoms)
            
            # Get diagnoses
            results = agent.act(max_diagnoses)
            
            # Add symptom timeline to results
            results['symptom_onset'] = symptom_onset
            
            if not results['diagnoses']:
                st.warning("Not enough information to make a diagnosis. Please provide more symptoms.")
            else:
                # Create bar chart for all diagnoses
                diagnosis_names = [d['condition_name'] for d in results['diagnoses']]
                confidence_scores = [d['confidence'] for d in results['diagnoses']]
                
                # Create DataFrame for the chart
                df = pd.DataFrame({
                    'Condition': diagnosis_names,
                    'Confidence': confidence_scores
                })
                
                # Create confidence score visualization
                st.subheader("Confidence Comparison")
                fig, ax = plt.subplots(figsize=(10, 5))
                bars = ax.barh(df['Condition'], df['Confidence'], color=[get_confidence_color(score) for score in df['Confidence']])
                ax.set_xlim(0, 1)
                ax.set_xlabel('Confidence Score')
                ax.set_title('Diagnosis Confidence Comparison')
                
                # Add value labels to the bars
                for i, v in enumerate(df['Confidence']):
                    ax.text(v + 0.01, i, f'{v:.2f}', va='center')
                
                st.pyplot(fig)
                
                # Display each diagnosis with improved visuals
                for i, diagnosis in enumerate(results['diagnoses']):
                    confidence_color = get_confidence_color(diagnosis['confidence'])
                    
                    # Create an expander with colored header based on confidence
                    with st.expander(
                        f"{i+1}. {diagnosis['condition_name']} - Confidence: {diagnosis['confidence']:.2f}",
                        expanded=(i == 0)  # Expand only the first result by default
                    ):
                        # Create two columns for explanation and visualization
                        exp_col1, exp_col2 = st.columns([3, 2])
                        
                        with exp_col1:
                            st.markdown("### Explanation")
                            
                            # Apply simplified language if enabled
                            explanation_text = results['explanations'][diagnosis['condition_id']]
                            if simplified_language:
                                explanation_text = simplify_medical_terms(explanation_text)
                            
                            st.markdown(explanation_text)
                            
                            st.markdown("### Recommendations")
                            
                            # Apply simplified language if enabled
                            recommendations_text = results['recommendations'][diagnosis['condition_id']]
                            if simplified_language:
                                recommendations_text = simplify_medical_terms(recommendations_text)
                                
                            st.markdown(recommendations_text)
                        
                        with exp_col2:
                            # Add confidence gauge
                            st.markdown("#### Confidence Score")
                            gauge_fig = create_confidence_gauge(diagnosis['confidence'])
                            st.pyplot(gauge_fig)
                            
                            # Add symptom match visualization
                            st.markdown("#### Symptom Analysis")
                            explanation_fig = create_explanation_viz(diagnosis, agent)
                            st.pyplot(explanation_fig)
                            
                            # Add related conditions section
                            st.markdown("### Related Conditions")
                            related_conditions = find_related_conditions(diagnosis['condition_id'], agent)
                            
                            for rel_id, rel_name, similarity in related_conditions:
                                similarity_pct = int(similarity * 100)
                                st.markdown(f"- {rel_name} ({similarity_pct}% symptom overlap)")
                
                # Add bookmark and report generation features
                st.markdown("---")
                report_col1, report_col2 = st.columns(2)
                
                with report_col1:
                    # Bookmark feature
                    if st.button("Save This Diagnosis"):
                        # Generate unique ID
                        bookmark_id = str(uuid.uuid4())
                        
                        # Create bookmark
                        st.session_state.bookmarks[bookmark_id] = {
                            'date': datetime.now().strftime("%Y-%m-%d"),
                            'symptoms': selected_symptoms,
                            'symptom_onset': symptom_onset,
                            'primary_diagnosis': results['diagnoses'][0]['condition_name'] if results['diagnoses'] else "No diagnosis"
                        }
                        
                        # Save bookmarks to file
                        if save_bookmarks(st.session_state.bookmarks):
                            st.success("Diagnosis saved! You can access it from the sidebar.")
                        else:
                            st.error("Failed to save diagnosis. Please try again.")
                
                with report_col2:
                    # Report generation
                    patient_name = st.text_input("Patient name for report (optional):", "")
                    
                    if st.button("Generate Printable Report"):
                        try:
                            # Generate PDF report
                            with st.spinner("Generating PDF report..."):
                                pdf_bytes = generate_pdf_report(
                                    patient_name, 
                                    selected_symptoms, 
                                    results, 
                                    agent, 
                                    simplified_language
                                )
                                
                                # Create download link
                                st.markdown(
                                    get_pdf_download_link(pdf_bytes), 
                                    unsafe_allow_html=True
                                )
                        except Exception as e:
                            st.error(f"Error generating report: {str(e)}")
                
                # Add a disclaimer
                st.markdown("""
                ---
                **Disclaimer:** This is an educational prototype. The diagnoses provided are based on a simplified model
                and should not be used for actual medical decisions. Always consult with a healthcare professional for
                proper diagnosis and treatment.
                """)
            
            # Close fade-in div
            st.markdown('</div>', unsafe_allow_html=True)
            
        elif diagnose_button:
            st.warning("Please select at least one symptom.")
        else:
            st.info("Select symptoms and click 'Get Diagnosis' to receive possible diagnoses.")
            
            # Show improved information about the agent
            st.markdown("""
            ### How This Works
            
            This diagnostic agent uses a best-first search algorithm to navigate through a knowledge base of medical conditions and their associated symptoms. The search prioritizes conditions that most closely match your reported symptoms, considering factors such as:
            """)
            
            # Use bullet points with tooltips for better readability
            st.markdown(f"""
            - {tooltip("Symptom-Condition Association", "The strength of relationship between symptoms and conditions based on medical knowledge")}
            - {tooltip("Primary Symptoms", "Key symptoms that are strongly indicative of specific conditions")}
            - {tooltip("Condition Prevalence", "How common different conditions are in the general population")}
            """, unsafe_allow_html=True)
            
            st.markdown("""
            ### Understanding Confidence Scores
            
            The confidence score is calculated using the following formula:
            
            `Confidence = 0.7 * (MatchedWeight / TotalWeight) + 0.3 * (PrimarySymptomMatch / TotalPrimarySymptoms)`
            
            This balances the breadth of symptom matching (70%) with the presence of primary symptoms (30%) to provide a more nuanced assessment of diagnostic likelihood.
            """)
            
            # Add information about the chat feature
            st.markdown("""
            ### Medical Advisor Chat
            
            Need to discuss your symptoms or diagnosis? Click the chat button in the bottom right corner to talk with our AI medical advisor.
            
            The advisor can help you:
            - Understand your symptoms better
            - Learn more about potential conditions
            - Know when to seek professional medical care
            - Get general health guidance
            """)
            
            # Add feature explanations
            st.markdown("""
            ### Features
            
            - **Symptom Timeline**: Indicate when your symptoms began to help with diagnosis
            - **Bookmarking**: Save your symptom sets and diagnoses for future reference
            - **Printable Report**: Generate a PDF report of your diagnosis to share with healthcare providers
            - **Related Symptoms**: Get suggestions for related symptoms you might be experiencing
            - **Simplified Language**: Toggle between medical terminology and simpler language
            - **Medical Advisor Chat**: Discuss your symptoms with our AI assistant (bottom right)
            """)
    
    # Add information about the project at the bottom
    st.markdown("""
    ---
    ### About This Project
    
    This Medical Diagnostic Agent System was developed as a final project for ITEC 781: Artificial Intelligence and Informatics I. 
    It demonstrates the application of intelligent agent architecture and search algorithms in the healthcare domain,
    enhanced with AI chatbot capabilities for more interactive patient guidance.
    
    The system uses:
    - A reactive agent architecture with perception, reasoning, and action components
    - Best-first search algorithm for diagnosis identification
    - A knowledge base with conditions, symptoms, and their relationships
    - Claude AI integration for interactive medical guidance
    """)
    
    # Add the floating chatbot
    if 'results' in locals() and results and 'diagnoses' in results:
        add_floating_chatbot(selected_symptoms, results['diagnoses'])
    else:
        add_floating_chatbot()
if __name__ == "__main__":
    main()