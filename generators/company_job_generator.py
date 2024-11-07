import json
import random
from datetime import datetime, timedelta
from faker import Faker
from generators.helpers import get_skills_for_role
from config.load_config import load_config
CONFIG = load_config()
fake = Faker()

class CompanyJobDataGenerator:
    def __init__(self):
        self.current_date = datetime.now()

    def generate_department(self, id):
        """Generate a company department using both predefined and dynamic names"""
        use_predefined = random.random() < 0.3  # 30% predefined, 70% dynamic

        if use_predefined and CONFIG.get('company_departments'):
            # Use predefined department name
            dept_name = random.choice(list(CONFIG['company_departments'].keys()))
            dept_info = CONFIG['company_departments'][dept_name]
            dept_type = dept_info['department_type']
        else:
            # Generate dynamic department name
            dept_type = random.choice(list(CONFIG['department_types'].keys()))
            company_category = random.choice(list(CONFIG['companies'].keys()))
            company = random.choice(CONFIG['companies'][company_category])
            dept_specialization = random.choice(CONFIG['department_types'][dept_type])
            dept_name = f"{dept_specialization} Team, {company}"

        department = {
            'id': id,
            'company_department_name': dept_name,
            'department_type': dept_type,
            'location': random.choice(CONFIG['locations']['cities']),
            'department_size': random.randint(5, 50),
        }

        # Add role mapping based on department type
        if dept_type == 'Technology':
            department['roles'] = CONFIG['job_roles']['Data Science']['titles'] + CONFIG['job_roles']['Software Engineering']['titles']
        elif dept_type == 'Finance':
            department['roles'] = CONFIG['job_roles']['Business Analytics']['titles']
        elif dept_type == 'Marketing':
            department['roles'] = CONFIG['job_roles']['Business Analytics']['titles']

        return department

    def generate_job(self, id, department):
        """Generate a job position aligned with department"""
        # Use department info directly instead of looking up
        role = random.choice(department['roles'])

        # Find role category
        role_category = next(
            category
            for category, info in CONFIG['job_roles'].items()
            if role in info['titles']
        )

        required_skills = get_skills_for_role(role_category)
        yoe_min = random.randint(0, 5)

        status = random.choice(['Draft', 'Posted', 'Active'])


        return {
            'id': id,
            'company_department_id': department['id'],
            'job_title': role,
            'required_skills': json.dumps(required_skills),
            'minimal_years_of_experience': yoe_min,
            'preferred_years_of_experience': yoe_min + random.randint(2, 5),
            'location': department['location'],  # Use department location
            'remote_policy': random.choice(CONFIG['locations']['remote_policies']),
            'status': status,
            'posting_date': (self.current_date - timedelta(days=random.randint(1, 90))).isoformat()
        }

    def generate_data(self, num_departments=50, num_jobs=600):
        """Generate complete dataset with proper relationships"""
        # Generate departments first
        departments = [self.generate_department(i) for i in range(num_departments)]

        # Generate jobs based on departments
        jobs = []
        for i in range(num_jobs):
            dept = random.choice(departments)
            # jobs.append(self.generate_job(i, dept['company_department_name']))
            jobs.append(self.generate_job(i, dept))  # Pass the full department object, not just its name

        return {
            'departments': departments,
            'jobs': jobs
        }
