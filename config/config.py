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
      "Business Analytics": 15,
      "Data Science": 15,
      "Software Engineering": 40,
      "Data Analytics": 15, 
      "DevOps": 1, 
      "Cloud Infrastructure": 1, 
      "AI Research":1,
      "Financial Analysis": 10,
  },
  "new_candidates_per_month": {
      "Business Analytics": 15,
      "Data Science": 15,
      "Software Engineering": 30,
      "Data Analytics": 15, 
      "DevOps": 1, 
      "Cloud Infrastructure": 1, 
      "AI Research": 1,
      "Financial Analysis": 10,
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
    },
    "Data Analytics":     {
      "titles": ["Data Analyst", "Data Engineer", "Data Architect", "Database Administrator"],
      "skillsets": ["data_analysis", "data_mining", "data_modeling"]
    },
    "DevOps":     {
      "titles": ["DevOps Engineer", "Site Reliability Engineer", "Cloud Engineer", "Build and Release Engineer"],
      "skillsets": ["devops", "cloud_computing", "automation"]
    },
    "Cloud Infrastructure":     {
      "titles": ["Cloud Architect", "Cloud Engineer", "Cloud Security Engineer", "Network Engineer"],
      "skillsets": ["cloud_computing", "networking", "security", "infrastructure_as_code"]
    },
    "AI Research":     {
      "titles": ["AI Research Scientist", "Machine Learning Researcher", "Deep Learning Researcher", "NLP Researcher"],
      "skillsets": ["machine_learning", "deep_learning", "natural_language_processing", "computer_vision"]
    },
    "Financial Analysis":     {
      "titles": ["Financial Analyst", "Investment Analyst", "Portfolio Manager", "Budget Analyst"],
      "skillsets": ["financial_analysis", "investment_analysis", "portfolio_management", "forecasting"]
    },
  },
  "skillsets":   {
    "data_analysis": ["Python", "SQL", "Pandas", "Excel", "Tableau", "Power BI"],
    "machine_learning": ["TensorFlow", "PyTorch", "Scikit-learn", "Machine Learning", "Deep Learning", "NLP"],
    "data_visualization": ["Tableau", "Power BI", "D3.js", "Matplotlib", "Seaborn"],
    "backend": ["Python", "Java", "Node.js", "SQL", "MongoDB", "AWS"],
    "frontend": ["JavaScript", "React", "HTML", "CSS", "TypeScript", "Angular"],
    "devops": ["Docker", "Kubernetes", "Jenkins", "AWS", "CI/CD", "Linux"],
    "business_analysis": ["SQL", "Excel", "Requirement Analysis", "Agile", "JIRA", "Process Mapping"],
    "data_mining": ["Data Mining Techniques", "Statistical Modeling", "Data Warehousing", "ETL Processes"],
    "data_modeling": ["Data Modeling Techniques", "Database Design", "SQL", "NoSQL"],
    "devops": ["Docker", "Kubernetes", "Jenkins", "AWS", "CI/CD", "Linux", "Git"],
    "business_analysis": ["SQL", "Excel", "Requirement Analysis", "Agile", "JIRA", "Process Mapping"],
    "data_mining": ["Data Mining Techniques", "Statistical Modeling", "Data Warehousing", "ETL Processes"],
    "data_modeling": ["Data Modeling Techniques", "Database Design", "SQL", "NoSQL"],
    "cloud_computing": ["AWS", "Azure", "GCP", "Cloud Security", "Serverless Computing"],
    "automation": ["Scripting Languages (Python, Bash)", "Automation Tools (Ansible, Chef, Puppet)", "CI/CD Pipelines"],
    "networking": ["Network Protocols (TCP/IP, DNS)", "Network Security", "Cloud Networking", "Network Management"],
    "security": ["Security Protocols", "Encryption", "Vulnerability Management", "Threat Detection"],
    "infrastructure_as_code": ["Terraform", "CloudFormation", "Ansible", "Configuration Management"],
    "deep_learning": ["Deep Learning Frameworks", "Neural Networks", "Computer Vision", "Natural Language Processing"],
    "natural_language_processing": ["NLP Techniques", "Text Mining", "Sentiment Analysis", "Machine Translation"],
    "computer_vision": ["Computer Vision Techniques", "Image Recognition", "Object Detection", "Image Processing"],
    "accounting": ["Accounting Principles (GAAP)", "Financial Reporting", "Auditing Standards", "Tax Laws"],
    "financial_reporting": ["Financial Statement Analysis", "Reporting Software", "Data Visualization"],
    "auditing": ["Auditing Standards", "Risk Assessment", "Internal Controls"],
    "taxation": ["Tax Laws", "Tax Preparation Software", "Tax Planning"],
    "financial_analysis": ["Financial Modeling", "Valuation Techniques", "Data Analysis", "Forecasting"],
    "investment_analysis": ["Investment Strategies", "Portfolio Management", "Risk Management", "Financial Modeling"],
    "portfolio_management": ["Portfolio Optimization", "Risk Management", "Asset Allocation", "Performance Measurement"],
    "forecasting": ["Trend Analysis", "Regression Analysis", "Time Series Analysis", "Predictive Modeling"],
  },
  # department_types is a dictionary with keys as department types and values as a list of department specializations
  "department_types":   {
    "Technology": ["Data Science", "Software Engineering", "Business Analytics", "Data Analytics", "DevOps", "Cloud Infrastructure", "AI Research"],
    "Finance": ["Financial Analysis"],
  },
}
