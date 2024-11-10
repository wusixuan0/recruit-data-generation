OTHER_CONFIG = {
  "locations":   {
    "cities": ["Toronto", "Vancouver", "Montreal", "Ottawa", "Waterloo"],
    "remote_policies": ["Remote", "Hybrid", "Onsite"]
  },
  # candidate_status is keys from interest_levels
  "candidate_status_keywords": ["Active", "Passive", "Not open to interview"],
  "interest_levels":   {
    "Active": ["Actively interviewing", "Open to offers", "Very interested", "Exploring opportunities"],
    "Passive": ["Not actively looking", "Casually looking", "Somewhat interested"],
    "Not open to interview": ["Not interested", "Offered", "Sourced", "Interviewed"]
  },
  "application_note": {
    "successful": ["Great fit for the role", "Strong technical background", "Good communication skills"],
    "rejected": [ "Looking for candidates with more years of experience",
    "Found candidates with more relevant experience",
    "Position requires more years of experience",
    "Position filled by another candidate",
    "Found candidates with better role alignment",
    "Moving forward with other candidates"],
  },
  "job_status": ['Active', 'Closed', 'Filled', 'On Hold', 'Pending', 'Cancelled'],
}
# dept_specialization is equivalent to job category (keys in job_roles)
COMPANY_CONFIG = {
  "company_departments":   {
    "DNA Team, RBC":     {
      "roles": ["Data Scientist", "Machine Learning Engineer"],
      "skillsets": ["data_analysis", "machine_learning"],
      "department_type": "Technology",
      "dept_specialization": "Data Analytics"
    },
    "Advanced Analytics Team, Manulife":     {
      "roles": ["Data Scientist", "Data Analyst"],
      "skillsets": ["data_analysis", "business_analysis"],
      "department_type": "Technology",
      "dept_specialization": "Data Analytics"
    },
    "Digital Technology, TD":     {
      "roles": ["Software Engineer", "Full Stack Developer"],
      "skillsets": ["backend", "frontend"],
      "department_type": "Technology",
      "dept_specialization": "Software Engineering"
    },
    "AI Research Lab, Vector Institute":     {
      "roles": ["AI Research Scientist", "Machine Learning Engineer"],
      "skillsets": ["machine_learning", "data_analysis"],
      "department_type": "Technology",
      "dept_specialization": "Data Science"
    }
  },
# grouped by industry  
  "companies":   {
    "banks": ["RBC", "TD", "BMO", "CIBC", "Scotiabank"],
    "tech": ["Shopify", "Amazon", "Microsoft", "Google"],
    "insurance": ["Manulife", "Sun Life", "Canada Life"]
  },
}