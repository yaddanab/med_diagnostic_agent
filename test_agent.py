"""
Test module for the Medical Diagnostic Agent.

This script tests the functionality of the diagnostic agent with different
symptom combinations to verify correct operation.
"""

import json
import os
from diagnostic_agent import DiagnosticAgent

def setup_test_environment():
    """Set up the test environment with the knowledge base."""
    # Ensure the knowledge base file exists
    kb_path = "knowledge_base.json"
    
    if not os.path.exists(kb_path):
        # If knowledge_base.json doesn't exist, create it from the sample
        sample_kb_path = "sample_knowledge_base.json"
        
        # Check if the sample file exists
        if os.path.exists(sample_kb_path):
            with open(sample_kb_path, 'r') as source:
                kb_data = json.load(source)
                
            with open(kb_path, 'w') as target:
                json.dump(kb_data, target, indent=2)
        else:
            print(f"Error: {sample_kb_path} not found. Please create it first.")
            return None
    
    return kb_path

def test_common_cold():
    """Test the agent with common cold symptoms."""
    print("\n=== Testing Common Cold Symptoms ===")
    
    # Initialize agent
    kb_path = setup_test_environment()
    agent = DiagnosticAgent(kb_path)
    
    # Test symptoms for common cold
    symptoms = ["Cough", "Sore throat", "Runny nose"]
    print(f"Symptoms: {', '.join(symptoms)}")
    
    # Process symptoms and get diagnoses
    agent.perceive(symptoms)
    results = agent.act(3)
    
    # Print results
    if results['diagnoses']:
        print("\nDiagnoses:")
        for i, diagnosis in enumerate(results['diagnoses']):
            print(f"{i+1}. {diagnosis['condition_name']} (Confidence: {diagnosis['confidence']:.2f})")
    else:
        print("No diagnoses found.")

def test_covid19():
    """Test the agent with COVID-19 symptoms."""
    print("\n=== Testing COVID-19 Symptoms ===")
    
    # Initialize agent
    kb_path = setup_test_environment()
    agent = DiagnosticAgent(kb_path)
    
    # Test symptoms for COVID-19
    symptoms = ["Fever", "Cough", "Shortness of breath", "Loss of taste or smell"]
    print(f"Symptoms: {', '.join(symptoms)}")
    
    # Process symptoms and get diagnoses
    agent.perceive(symptoms)
    results = agent.act(3)
    
    # Print results
    if results['diagnoses']:
        print("\nDiagnoses:")
        for i, diagnosis in enumerate(results['diagnoses']):
            print(f"{i+1}. {diagnosis['condition_name']} (Confidence: {diagnosis['confidence']:.2f})")
            
        # Print full explanation for the top diagnosis
        top_diagnosis = results['diagnoses'][0]
        print(f"\nExplanation for top diagnosis ({top_diagnosis['condition_name']}):")
        print(results['explanations'][top_diagnosis['condition_id']])
    else:
        print("No diagnoses found.")

def test_gastroenteritis():
    """Test the agent with gastroenteritis symptoms."""
    print("\n=== Testing Gastroenteritis Symptoms ===")
    
    # Initialize agent
    kb_path = setup_test_environment()
    agent = DiagnosticAgent(kb_path)
    
    # Test symptoms for gastroenteritis
    symptoms = ["Nausea", "Vomiting", "Diarrhea", "Abdominal pain"]
    print(f"Symptoms: {', '.join(symptoms)}")
    
    # Process symptoms and get diagnoses
    agent.perceive(symptoms)
    results = agent.act(3)
    
    # Print results
    if results['diagnoses']:
        print("\nDiagnoses:")
        for i, diagnosis in enumerate(results['diagnoses']):
            print(f"{i+1}. {diagnosis['condition_name']} (Confidence: {diagnosis['confidence']:.2f})")
    else:
        print("No diagnoses found.")

def test_ambiguous_symptoms():
    """Test the agent with ambiguous symptoms that could match multiple conditions."""
    print("\n=== Testing Ambiguous Symptoms ===")
    
    # Initialize agent
    kb_path = setup_test_environment()
    agent = DiagnosticAgent(kb_path)
    
    # Test ambiguous symptoms
    symptoms = ["Fever", "Cough", "Fatigue"]
    print(f"Symptoms: {', '.join(symptoms)}")
    
    # Process symptoms and get diagnoses
    agent.perceive(symptoms)
    results = agent.act(5)  # Show top 5 to see the spread
    
    # Print results
    if results['diagnoses']:
        print("\nDiagnoses:")
        for i, diagnosis in enumerate(results['diagnoses']):
            print(f"{i+1}. {diagnosis['condition_name']} (Confidence: {diagnosis['confidence']:.2f})")
    else:
        print("No diagnoses found.")

def run_all_tests():
    """Run all test cases."""
    print("=== Running Diagnostic Agent Tests ===")
    
    test_common_cold()
    test_covid19()
    test_gastroenteritis()
    test_ambiguous_symptoms()
    
    print("\n=== All Tests Completed ===")

if __name__ == "__main__":
    run_all_tests()