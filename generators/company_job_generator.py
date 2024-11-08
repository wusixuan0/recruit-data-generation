import json
import random
from datetime import datetime, timedelta
from faker import Faker
from utils.get_skills_for_role import get_skills_for_role
from config.config import CONFIG
from config.other_config import COMPANY_CONFIG, OTHER_CONFIG
fake = Faker()

class CompanyJobDataGenerator:
    def __init__(self):
        self.current_date = datetime.now()

    def generate_department(self, id):
        """Generate a company department using both predefined and dynamic names"""
        use_predefined = random.random() < 0.1

        if use_predefined and COMPANY_CONFIG.get('company_departments'):
            # Use predefined department name
            dept_name = random.choice(list(COMPANY_CONFIG['company_departments'].keys()))
            dept_info = COMPANY_CONFIG['company_departments'][dept_name]
            dept_type = dept_info['department_type']
            dept_specialization = dept_info['dept_specialization']
        else:
            # Generate dynamic department name
            dept_type = random.choice(list(CONFIG['department_types'].keys()))
            
            use_predefined_companies = random.random() < 0.5
            
            if use_predefined_companies:
                industry = random.choice(list(COMPANY_CONFIG['companies'].keys()))
                company = random.choice(COMPANY_CONFIG['companies'][industry])
            else:
                company = fake.company()

            department_types = random.choice(list(CONFIG['department_types'].keys()))
            dept_specialization = random.choice(CONFIG['department_types'][department_types])
            dept_name = f"{dept_specialization} Team, {company}"

        department = {
            'id': id,
            'company_department_name': dept_name,
            'department_type': dept_type,
            'dept_specialization': dept_specialization,
            'location': random.choice(OTHER_CONFIG['locations']['cities']),
            'department_size': random.randint(5, 50),
        }

        # Add role mapping based on department type
        department['roles'] = CONFIG['job_roles'][dept_specialization]['titles']

        return department

    def generate_job(self, id, department):
        """Generate a job position aligned with department"""
        # Use department info directly instead of looking up
        dept_specialization = department['dept_specialization']
        
        if 'roles' in department:
            role = random.choice(department['roles'])
        else:
            role = random.choice(CONFIG['job_roles'][dept_specialization]['titles'])

        required_skills = get_skills_for_role(dept_specialization)
        yoe_min = random.randint(0, 5)

        status = random.choice(['Active', 'Closed', 'Filled'])

        return {
            'id': id,
            'company_department_id': department['id'],
            'job_title': role,
            'required_skills': json.dumps(required_skills),
            'minimal_years_of_experience': yoe_min,
            'preferred_years_of_experience': yoe_min + random.randint(2, 5),
            'location': department['location'],  # Use department location
            'remote_policy': random.choice(OTHER_CONFIG['locations']['remote_policies']),
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
