# Knowledge base data for the Medical Diagnostic Agent

knowledge_base = {
  "symptoms": {
    "s001": {
      "name": "Fever",
      "description": "Elevated body temperature above 37.5°C (99.5°F)",
      "severity": 0.6
    },
    "s002": {
      "name": "Cough",
      "description": "Reflex action to clear the airways",
      "severity": 0.5
    },
    "s003": {
      "name": "Fatigue",
      "description": "Extreme tiredness or lack of energy",
      "severity": 0.4
    },
    "s004": {
      "name": "Shortness of breath",
      "description": "Difficulty breathing or feeling breathless",
      "severity": 0.8
    },
    "s005": {
      "name": "Sore throat",
      "description": "Pain or irritation in the throat",
      "severity": 0.4
    },
    "s006": {
      "name": "Runny nose",
      "description": "Excessive nasal discharge",
      "severity": 0.3
    },
    "s007": {
      "name": "Headache",
      "description": "Pain in the head region",
      "severity": 0.5
    },
    "s008": {
      "name": "Muscle pain",
      "description": "Pain or aches in muscles",
      "severity": 0.4
    },
    "s009": {
      "name": "Chest pain",
      "description": "Pain or discomfort in the chest area",
      "severity": 0.9
    },
    "s010": {
      "name": "Loss of taste or smell",
      "description": "Inability to taste or smell properly",
      "severity": 0.6
    },
    "s011": {
      "name": "Nausea",
      "description": "Feeling of sickness with an inclination to vomit",
      "severity": 0.5
    },
    "s012": {
      "name": "Vomiting",
      "description": "Forceful expulsion of stomach contents through the mouth",
      "severity": 0.7
    },
    "s013": {
      "name": "Diarrhea",
      "description": "Loose, watery stool",
      "severity": 0.6
    },
    "s014": {
      "name": "Rash",
      "description": "Area of reddened, irritated, or swollen skin",
      "severity": 0.5
    },
    "s015": {
      "name": "Joint pain",
      "description": "Pain or discomfort in joints",
      "severity": 0.5
    },
    "s016": {
      "name": "Confusion",
      "description": "Difficulty thinking clearly or understanding",
      "severity": 0.8
    },
    "s017": {
      "name": "Dizziness",
      "description": "Feeling lightheaded or unsteady",
      "severity": 0.6
    },
    "s018": {
      "name": "Wheezing",
      "description": "Breathing with a whistling or rattling sound",
      "severity": 0.7
    },
    "s019": {
      "name": "Abdominal pain",
      "description": "Pain in the region between the chest and pelvis",
      "severity": 0.6
    },
    "s020": {
      "name": "Loss of appetite",
      "description": "Reduced desire to eat",
      "severity": 0.4
    }
  },
  "conditions": {
    "c001": {
      "name": "Common Cold",
      "description": "A viral infection of the upper respiratory tract, primarily the nose and throat.",
      "prevalence": 0.2,
      "primary_symptoms": ["s002", "s005", "s006"],
      "symptoms": {
        "s002": 0.9, 
        "s003": 0.6, 
        "s005": 0.8, 
        "s006": 0.9, 
        "s007": 0.7
      },
      "recommendations": "Rest, stay hydrated, and take over-the-counter cold medications if needed. If symptoms worsen or persist beyond 10 days, consult a healthcare provider."
    },
    "c002": {
      "name": "Influenza (Flu)",
      "description": "A contagious respiratory illness caused by influenza viruses that infect the nose, throat, and lungs.",
      "prevalence": 0.1,
      "primary_symptoms": ["s001", "s002", "s003", "s008"],
      "symptoms": {
        "s001": 0.9, 
        "s002": 0.8, 
        "s003": 0.9, 
        "s007": 0.8, 
        "s008": 0.8, 
        "s020": 0.7
      },
      "recommendations": "Rest, stay hydrated, and take fever reducers if needed. Antiviral medications may be prescribed if diagnosed early. Seek medical attention if symptoms are severe or you're at high risk for complications."
    },
    "c003": {
      "name": "COVID-19",
      "description": "A respiratory illness caused by the SARS-CoV-2 virus, ranging from mild to severe.",
      "prevalence": 0.08,
      "primary_symptoms": ["s001", "s002", "s004", "s010"],
      "symptoms": {
        "s001": 0.8, 
        "s002": 0.8, 
        "s003": 0.8, 
        "s004": 0.6, 
        "s005": 0.5, 
        "s007": 0.6, 
        "s008": 0.6, 
        "s010": 0.7, 
        "s013": 0.4
      },
      "recommendations": "Isolate yourself, monitor symptoms, and contact healthcare providers. Seek emergency care for severe symptoms like persistent chest pain or difficulty breathing."
    },
    "c004": {
      "name": "Pneumonia",
      "description": "An infection that inflames the air sacs in one or both lungs, which may fill with fluid.",
      "prevalence": 0.03,
      "primary_symptoms": ["s001", "s002", "s004", "s009"],
      "symptoms": {
        "s001": 0.9, 
        "s002": 0.9, 
        "s003": 0.8, 
        "s004": 0.9, 
        "s009": 0.7, 
        "s018": 0.6
      },
      "recommendations": "Seek medical attention immediately. Pneumonia requires proper diagnosis and treatment, which may include antibiotics, breathing treatments, or hospitalization depending on severity."
    },
    "c005": {
      "name": "Bronchitis",
      "description": "Inflammation of the lining of the bronchial tubes, which carry air to and from the lungs.",
      "prevalence": 0.05,
      "primary_symptoms": ["s002", "s004", "s018"],
      "symptoms": {
        "s001": 0.4, 
        "s002": 0.9, 
        "s003": 0.7, 
        "s004": 0.7, 
        "s018": 0.8
      },
      "recommendations": "Rest, stay hydrated, and use a humidifier. Over-the-counter medications may help relieve symptoms. If symptoms persist or worsen, consult a healthcare provider."
    },
    "c006": {
      "name": "Gastroenteritis",
      "description": "Inflammation of the stomach and intestines, typically resulting from a viral or bacterial infection.",
      "prevalence": 0.07,
      "primary_symptoms": ["s011", "s012", "s013"],
      "symptoms": {
        "s001": 0.4, 
        "s003": 0.7, 
        "s011": 0.9, 
        "s012": 0.8, 
        "s013": 0.9, 
        "s019": 0.8, 
        "s020": 0.7
      },
      "recommendations": "Stay hydrated, rest, and eat bland foods when appetite returns. Seek medical attention if you're unable to keep fluids down, have bloody stool, or symptoms persist more than a few days."
    },
    "c007": {
      "name": "Migraine",
      "description": "A headache of varying intensity, often accompanied by nausea and sensitivity to light and sound.",
      "prevalence": 0.12,
      "primary_symptoms": ["s007", "s011", "s017"],
      "symptoms": {
        "s007": 0.9, 
        "s011": 0.7, 
        "s017": 0.6
      },
      "recommendations": "Rest in a quiet, dark room. Over-the-counter pain relievers may help. If migraines are frequent or severe, consult a healthcare provider for preventive treatments."
    },
    "c008": {
      "name": "Allergic Rhinitis",
      "description": "Inflammation of the nasal passages caused by an allergic reaction.",
      "prevalence": 0.15,
      "primary_symptoms": ["s005", "s006", "s007"],
      "symptoms": {
        "s005": 0.6, 
        "s006": 0.9, 
        "s007": 0.5, 
        "s018": 0.4
      },
      "recommendations": "Avoid allergens if possible. Over-the-counter antihistamines, decongestants, or nasal sprays may provide relief. For persistent allergies, consult an allergist."
    },
    "c009": {
      "name": "Asthma",
      "description": "A condition in which airways narrow and swell and produce extra mucus, making breathing difficult.",
      "prevalence": 0.08,
      "primary_symptoms": ["s004", "s018"],
      "symptoms": {
        "s002": 0.7, 
        "s004": 0.9, 
        "s018": 0.9
      },
      "recommendations": "Use prescribed inhalers as directed. Avoid triggers and maintain an asthma action plan. Seek emergency care for severe attacks that don't respond to rescue inhalers."
    },
    "c010": {
      "name": "Acute Sinusitis",
      "description": "Inflammation of the sinuses, usually due to infection.",
      "prevalence": 0.09,
      "primary_symptoms": ["s002", "s005", "s006", "s007"],
      "symptoms": {
        "s002": 0.6, 
        "s005": 0.7, 
        "s006": 0.8, 
        "s007": 0.8
      },
      "recommendations": "Use saline nasal sprays, apply warm compresses, and take over-the-counter pain relievers. If symptoms persist more than 10 days or are severe, consult a healthcare provider."
    }
  }
}