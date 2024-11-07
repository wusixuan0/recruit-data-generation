import json

CONFIG = {
  "locations": {
    "cities": [
      "Toronto",
      "Vancouver",
      "Montreal",
      "Ottawa",
      "Waterloo"
    ],
    "remote_policies": [
      "Remote",
      "Hybrid",
      "Onsite"
    ]
  },

  "job_roles": {
    "Data Science": {
      "titles": [
        "Data Scientist",
        "Machine Learning Engineer",
        "Data Analyst",
        "AI Research Scientist"
      ],
      "skillsets": ["data_analysis", "machine_learning", "data_visualization"]
    },
    "Software Engineering": {
      "titles": [
        "Software Engineer",
        "Full Stack Developer",
        "Backend Developer",
        "Frontend Developer"
      ],
      "skillsets": ["backend", "frontend", "devops"]
    },
    "Business Analytics": {
      "titles": [
        "Business Analyst",
        "Business Intelligence Analyst",
        "Product Analyst",
        "Analytics Consultant"
      ],
      "skillsets": ["business_analysis", "data_analysis"]
    }
  },

  "skillsets": {
    "data_analysis": [
      "Python",
      "SQL",
      "Pandas",
      "Excel",
      "Tableau",
      "Power BI"
    ],
    "machine_learning": [
      "TensorFlow",
      "PyTorch",
      "Scikit-learn",
      "Machine Learning",
      "Deep Learning",
      "NLP"
    ],
    "data_visualization": [
      "Tableau",
      "Power BI",
      "D3.js",
      "Matplotlib",
      "Seaborn"
    ],
    "backend": [
      "Python",
      "Java",
      "Node.js",
      "SQL",
      "MongoDB",
      "AWS"
    ],
    "frontend": [
      "JavaScript",
      "React",
      "HTML",
      "CSS",
      "TypeScript",
      "Angular"
    ],
    "devops": [
      "Docker",
      "Kubernetes",
      "Jenkins",
      "AWS",
      "CI/CD",
      "Linux"
    ],
    "business_analysis": [
      "SQL",
      "Excel",
      "Requirement Analysis",
      "Agile",
      "JIRA",
      "Process Mapping"
    ]
  },

  "department_types": {
    'Technology': ['Data Science', 'Software Engineering', 'DevOps', 'Cloud Infrastructure', 'AI Research'],
    'Finance': ['Financial Analysis', 'Risk Management', 'Trading Technology'],
    'Marketing': ['Digital Marketing', 'Marketing Analytics', 'CRM']
  },

  "company_departments": {
    "DNA Team, RBC": {
      "roles": ["Data Scientist", "Machine Learning Engineer"],
      "skillsets": ["data_analysis", "machine_learning"],
      "department_type": "Technology",
      "department_role": "Data Analytics",
    },
    "Advanced Analytics Team, Manulife": {
      "roles": ["Data Scientist", "Data Analyst"],
      "skillsets": ["data_analysis", "business_analysis"],
      "department_type": "Business Analytics"
    },
    "Digital Technology, TD": {
      "roles": ["Software Engineer", "Full Stack Developer"],
      "skillsets": ["backend", "frontend"],
      "department_type": "Technology"
    },
    "AI Research Lab, Vector Institute": {
      "roles": ["AI Research Scientist", "Machine Learning Engineer"],
      "skillsets": ["machine_learning", "data_analysis"],
      "department_type": "Research"
    }
  },
  "companies":{
    'banks': ['RBC', 'TD', 'BMO', 'CIBC', 'Scotiabank'],
    'tech': ['Shopify', 'Amazon', 'Microsoft', 'Google'],
    'insurance': ['Manulife', 'Sun Life', 'Canada Life']
  },

  'candidate_status_keywords': ["Active", "Passive", "Not open to interview"],

  'interest_levels': {
      "Active": ["Actively interviewing", "Open to offers", "Very interested","Exploring opportunities",],
      "Passive": ["Not actively looking","Casually looking","Somewhat interested"],
      "Not open to interview": ["Not interested", "Offered", "Sourced", "Interviewed"],
  }
}

filename = "config.json"

with open(filename, 'w') as f:
    json.dump(CONFIG, f)