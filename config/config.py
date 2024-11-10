CONFIG = {
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
  },
  "role_categories": ["Data Science", "Software Engineering", "Business Analytics"],
          
  # Monthly generation parameters
  "new_jobs_per_month": {
      "Business Analytics": 3,
      "Data Science": 1,
      "Software Engineering": 5
  },
  "new_candidates_per_month": {
      "Business Analytics": 8,
      "Data Science": 5,
      "Software Engineering": 8
  },
  # job_roles is a dictionary with keys as job categories/department specializations and values as a dictionary with titles and skillsets
  "job_roles":   {
    "Data Science":     {
      "titles": ["Data Scientist", "Machine Learning Engineer", "Data Analyst", "AI Research Scientist"],
      "skillsets": ["data_analysis", "machine_learning", "data_visualization"]
    },
    "Software Engineering":     {
      "titles": ["Software Engineer", "Full Stack Developer", "Backend Developer", "Frontend Developer"],
      "skillsets": ["backend", "frontend", "devops"]
    },
    "Business Analytics":     {
      "titles": ["Business Analyst", "Business Intelligence Analyst", "Product Analyst", "Analytics Consultant"],
      "skillsets": ["business_analysis", "data_analysis"]
    }
  },
  "skillsets":   {
    "data_analysis": ["Python", "SQL", "Pandas", "Excel", "Tableau", "Power BI"],
    "machine_learning": ["TensorFlow", "PyTorch", "Scikit-learn", "Machine Learning", "Deep Learning", "NLP"],
    "data_visualization": ["Tableau", "Power BI", "D3.js", "Matplotlib", "Seaborn"],
    "backend": ["Python", "Java", "Node.js", "SQL", "MongoDB", "AWS"],
    "frontend": ["JavaScript", "React", "HTML", "CSS", "TypeScript", "Angular"],
    "devops": ["Docker", "Kubernetes", "Jenkins", "AWS", "CI/CD", "Linux"],
    "business_analysis": ["SQL", "Excel", "Requirement Analysis", "Agile", "JIRA", "Process Mapping"]
  },
  # department_types is a dictionary with keys as department types and values as a list of department specializations
  "department_types":   {
    "Technology": ["Data Science", "Software Engineering", "Business Analytics"],
  },
}
