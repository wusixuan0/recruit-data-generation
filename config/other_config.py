OTHER_CONFIG = {
  "locations":   {
    "cities": ["Toronto", "Vancouver", "Montreal", "Ottawa", "Waterloo"],
    "remote_policies": ["Remote", "Hybrid", "Onsite"]
  },
  "candidate_status_keywords": ["Active", "Passive", "Not open to interview"],
  "interest_levels":   {
    "Active": ["Actively interviewing", "Open to offers", "Very interested", "Exploring opportunities"],
    "Passive": ["Not actively looking", "Casually looking", "Somewhat interested"],
    "Not open to interview": ["Not interested", "Offered", "Sourced", "Interviewed"]
  }
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