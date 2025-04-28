"""
Diagnostic Agent module for the Medical Diagnostic Agent System.

This module implements the core agent functionality including perception,
reasoning, and action components.
"""

import json
import heapq
import math
from typing import List, Dict, Tuple, Set, Any

class DiagnosticAgent:
    """
    An agent that diagnoses medical conditions based on reported symptoms.
    Uses a best-first search algorithm to navigate through symptom space.
    """
    
    def __init__(self, knowledge_base_path: str):
        """
        Initialize the diagnostic agent with a knowledge base.
        
        Args:
            knowledge_base_path: Path to the knowledge base JSON file
        """
        with open(knowledge_base_path, 'r') as file:
            self.knowledge_base = json.load(file)
            
        # Extract conditions and symptoms for quick lookup
        self.conditions = self.knowledge_base['conditions']
        self.symptoms = self.knowledge_base['symptoms']
        
        # Create symptom-to-condition mapping for efficient lookup
        self.symptom_to_conditions = {}
        for condition_id, condition in self.conditions.items():
            for symptom_id, weight in condition['symptoms'].items():
                if symptom_id not in self.symptom_to_conditions:
                    self.symptom_to_conditions[symptom_id] = []
                self.symptom_to_conditions[symptom_id].append((condition_id, weight))
                
    def normalize_symptoms(self, reported_symptoms: List[str]) -> List[str]:
        """
        Normalize user-reported symptoms to match knowledge base format.
        
        Args:
            reported_symptoms: List of symptom names as reported by user
            
        Returns:
            List of symptom IDs from the knowledge base
        """
        normalized_symptoms = []
        
        # Convert reported symptom names to symptom IDs
        for symptom_name in reported_symptoms:
            symptom_name_lower = symptom_name.lower()
            for symptom_id, symptom_data in self.symptoms.items():
                if symptom_name_lower == symptom_data['name'].lower():
                    normalized_symptoms.append(symptom_id)
                    break
                    
        return normalized_symptoms
    
    def perceive(self, reported_symptoms: List[str]) -> None:
        """
        Process and normalize symptom inputs from the user.
        
        Args:
            reported_symptoms: List of symptom names as reported by user
        """
        self.current_symptoms = self.normalize_symptoms(reported_symptoms)
    
    def best_first_search(self, max_diagnoses: int = 3) -> List[Dict[str, Any]]:
        """
        Implement best-first search to find the most likely diagnoses.
        
        Args:
            max_diagnoses: Maximum number of diagnoses to return
            
        Returns:
            List of diagnosis dictionaries with condition ID and confidence score
        """
        # Initialize priority queue for search
        # Each entry is (negative score, condition_id)
        # We use negative score because heapq is a min-heap
        queue = []
        visited = set()
        
        # Initialize search with conditions related to reported symptoms
        condition_scores = {}
        
        for symptom_id in self.current_symptoms:
            if symptom_id in self.symptom_to_conditions:
                for condition_id, weight in self.symptom_to_conditions[symptom_id]:
                    if condition_id not in condition_scores:
                        condition_scores[condition_id] = 0
                    condition_scores[condition_id] += weight
        
        # Add conditions to the queue
        for condition_id, score in condition_scores.items():
            # Calculate heuristic based on condition prevalence and symptom match
            condition_prevalence = self.conditions[condition_id].get('prevalence', 0.01)
            heuristic = score * math.log(condition_prevalence + 0.01)
            heapq.heappush(queue, (-heuristic, condition_id))
            
        # Perform best-first search
        results = []
        while queue and len(results) < max_diagnoses:
            score, condition_id = heapq.heappop(queue)
            score = -score  # Convert back to positive
            
            if condition_id in visited:
                continue
                
            visited.add(condition_id)
            
            # Calculate confidence score (normalized)
            total_symptom_weight = sum(weight for symptom, weight in self.conditions[condition_id]['symptoms'].items())
            matched_weight = sum(self.conditions[condition_id]['symptoms'].get(symptom, 0) for symptom in self.current_symptoms)
            
            # Avoid division by zero
            if total_symptom_weight > 0:
                confidence = matched_weight / total_symptom_weight
            else:
                confidence = 0
                
            # Adjust confidence based on how many of the condition's primary symptoms are present
            primary_symptoms = self.conditions[condition_id].get('primary_symptoms', [])
            if primary_symptoms:
                primary_symptom_match = sum(1 for symptom in primary_symptoms if symptom in self.current_symptoms)
                primary_symptom_factor = primary_symptom_match / len(primary_symptoms)
                confidence = 0.7 * confidence + 0.3 * primary_symptom_factor
            
            results.append({
                'condition_id': condition_id,
                'condition_name': self.conditions[condition_id]['name'],
                'confidence': confidence,
                'matched_symptoms': [self.symptoms[s]['name'] for s in self.current_symptoms if s in self.conditions[condition_id]['symptoms']]
            })
            
        # Sort by confidence
        results.sort(key=lambda x: x['confidence'], reverse=True)
        return results
        
    def reason(self, max_diagnoses: int = 3) -> List[Dict[str, Any]]:
        """
        Use search algorithm to explore possible diagnoses.
        
        Args:
            max_diagnoses: Maximum number of diagnoses to return
            
        Returns:
            List of diagnoses with confidence scores
        """
        if not self.current_symptoms:
            return []
            
        return self.best_first_search(max_diagnoses)
    
    def generate_explanation(self, diagnosis: Dict[str, Any]) -> str:
        """
        Generate an explanation for a diagnosis.
        
        Args:
            diagnosis: Diagnosis dictionary from reason method
            
        Returns:
            String explanation of the reasoning
        """
        condition_id = diagnosis['condition_id']
        condition = self.conditions[condition_id]
        
        explanation = f"The diagnosis of {condition['name']} is based on the following:\n\n"
        
        # Explain matched symptoms
        explanation += "Matching symptoms:\n"
        for symptom_name in diagnosis['matched_symptoms']:
            explanation += f"- {symptom_name}\n"
            
        # Explain missing key symptoms if any
        missing_key_symptoms = []
        for symptom_id in condition.get('primary_symptoms', []):
            if symptom_id not in self.current_symptoms:
                missing_key_symptoms.append(self.symptoms[symptom_id]['name'])
                
        if missing_key_symptoms:
            explanation += "\nKey symptoms that would strengthen this diagnosis:\n"
            for symptom_name in missing_key_symptoms:
                explanation += f"- {symptom_name}\n"
                
        # Add information about condition
        if 'description' in condition:
            explanation += f"\nAbout {condition['name']}:\n{condition['description']}\n"
            
        return explanation
    
    def generate_recommendations(self, diagnosis: Dict[str, Any]) -> str:
        """
        Generate recommendations based on a diagnosis.
        
        Args:
            diagnosis: Diagnosis dictionary from reason method
            
        Returns:
            String recommendations
        """
        condition_id = diagnosis['condition_id']
        condition = self.conditions[condition_id]
        
        if 'recommendations' in condition:
            return condition['recommendations']
        else:
            return f"Please consult with a healthcare professional for a proper diagnosis and treatment of {condition['name']}."
    
    def act(self, max_diagnoses: int = 3) -> Dict[str, Any]:
        """
        Return diagnostic suggestions with explanations.
        
        Args:
            max_diagnoses: Maximum number of diagnoses to return
            
        Returns:
            Dictionary with diagnoses, explanations, and recommendations
        """
        diagnoses = self.reason(max_diagnoses)
        
        if not diagnoses:
            return {
                'diagnoses': [],
                'explanations': {},
                'recommendations': "Please provide more symptoms or consult with a healthcare professional."
            }
            
        explanations = {d['condition_id']: self.generate_explanation(d) for d in diagnoses}
        recommendations = {d['condition_id']: self.generate_recommendations(d) for d in diagnoses}
        
        return {
            'diagnoses': diagnoses,
            'explanations': explanations,
            'recommendations': recommendations
        }

# Example of how to use the agent
if __name__ == "__main__":
    # This is just an example, the knowledge base file should be created
    agent = DiagnosticAgent("knowledge_base.json")
    
    # Example symptoms
    reported_symptoms = ["fever", "cough", "fatigue"]
    
    # Process symptoms
    agent.perceive(reported_symptoms)
    
    # Get diagnoses and explanations
    results = agent.act()
    
    # Print results
    for diagnosis in results['diagnoses']:
        print(f"Condition: {diagnosis['condition_name']}")
        print(f"Confidence: {diagnosis['confidence']:.2f}")
        print("\nExplanation:")
        print(results['explanations'][diagnosis['condition_id']])
        print("\nRecommendations:")
        print(results['recommendations'][diagnosis['condition_id']])
        print("-" * 50)