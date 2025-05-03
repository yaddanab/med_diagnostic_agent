# med_diagnostic_agent

## Overview

The Medical Diagnostic Agent System is an AI-powered tool that helps diagnose medical conditions based on patient-reported symptoms. The system uses a best-first search algorithm to navigate through a knowledge base of symptoms and conditions, providing potential diagnoses with confidence levels and explanations.


## Features

### Core Features
- **Symptom-Based Diagnosis**: Select your symptoms from a comprehensive list
- **Intelligent Search**: Uses a best-first search algorithm to find the most likely diagnoses
- **Confidence Scoring**: Each diagnosis comes with a confidence score
- **Detailed Explanations**: Understand why a diagnosis is suggested
- **Treatment Recommendations**: Basic guidance for each condition

### Enhanced UI Features
1. **Color-coded confidence scores**: Visual indicators show diagnosis reliability at a glance
2. **Symptom categories**: Symptoms organized by body systems for easier selection
3. **Symptom search**: Quickly find specific symptoms with the search box
4. **Interactive body map**: Visual interface to select affected body regions
5. **Results visualization**: Bar charts and gauges showing confidence scores
6. **Responsive design**: Works well on desktop and mobile devices
7. **Explanation visualization**: Visual representation of symptom matches
8. **Dark mode option**: Toggle between light and dark themes

## Try It Live

You can try the live demo here: 

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Setup

1. Clone the repository:
```bash
git clone https://github.com/your-username/medical-diagnostic-agent.git
cd medical-diagnostic-agent
```

2. Install the required dependencies:
```bash
pip install -r requirements.txt
```

3. Run the application:
```bash
streamlit run app.py
```


## How It Works

The Medical Diagnostic Agent follows a reactive agent architecture with three components:

1. **Perception**: Processes user-reported symptoms
2. **Reasoning**: Uses best-first search to identify potential diagnoses
3. **Action**: Returns diagnoses with explanations and recommendations

The agent calculates confidence scores for each diagnosis based on:
- Matched symptom weights (70% of score)
- Presence of primary symptoms (30% of score)

The formula is:
```
Confidence = 0.7 * (MatchedWeight / TotalWeight) + 0.3 * (PrimarySymptomMatch / TotalPrimarySymptoms)
```

## Using the Enhanced Interface

### Selecting Symptoms
- Use the categorized symptom panels to find symptoms by body system
- Type in the search box to quickly find specific symptoms
- Toggle the body map to select symptoms by body region

### Viewing Results
- See a comparative bar chart of all potential diagnoses
- Examine each diagnosis with color-coded confidence indicators
- View symptom match visualizations for each condition
- Read detailed explanations and recommendations

### Customizing Your Experience
- Toggle dark mode for reduced eye strain in low-light environments
- Adjust the number of diagnoses shown with the slider
- Expand/collapse specific diagnosis details as needed

## Project Structure

```
medical-diagnostic-agent/
├── app.py                      # Main application entry point
├── diagnostic_agent.py         # Core agent implementation
├── knowledge_base_data.py      # Knowledge base as Python dictionary
├── sample_knowledge_base.json  # Sample knowledge base template
├── streamlit_interface.py      # Enhanced Streamlit UI implementation
├── styles.css                  # Custom CSS styles
├── test_agent.py               # Test script for the agent
├── requirements.txt            # Project dependencies
├── README.md                   # Project documentation
└── LICENSE                     # MIT License file
```

## Limitations

- This is an educational prototype and should not be used for actual medical decisions
- The knowledge base is limited to 10 common conditions and 20 symptoms
- No consideration of symptom duration, severity, or progression
- Always consult with a healthcare professional for proper diagnosis and treatment

## Future Development

- Expand the knowledge base with more conditions and symptoms
- Add symptom duration and progression tracking
- Implement machine learning for improved accuracy
- Develop mobile application versions
- Add multilingual support
- Incorporate electronic health record integration

## License

This project is licensed under the MIT License

## Acknowledgments

- This project was developed as part of ITEC 781: Artificial Intelligence and Informatics I
