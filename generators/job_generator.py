import json
import random
from datetime import datetime, timedelta
from faker import Faker
from utils.get_skills_for_role import get_skills_for_role
from config.config import CONFIG
from config.other_config import OTHER_CONFIG
import uuid
fake = Faker()

class JobDataGenerator:
    def __init__(self):
        self.current_date = datetime.now()

    def generate_job(self, department):
        """Generate a job position aligned with department"""
        dept_specialization = department['dept_specialization']
        
        if 'roles' in department:
            role = random.choice(department['roles'])
        else:
            role = random.choice(CONFIG['job_roles'][dept_specialization]['titles'])

        required_skills = get_skills_for_role(dept_specialization)
        yoe_min = random.randint(3, 5)

        status = random.choice(['Active', 'Closed', 'Filled'])

        return {
            'id': str(uuid.uuid4()),
            'company_department_id': department['id'],
            'job_title': role,
            'required_skills': json.dumps(required_skills),
            'minimal_years_of_experience': yoe_min,
            'preferred_years_of_experience': yoe_min + random.randint(0, 3),
            'location': department['location'],  # Use department location
            'category': dept_specialization,
            'remote_policy': random.choice(OTHER_CONFIG['locations']['remote_policies']),
            'status': status,
            'posting_date': (self.current_date - timedelta(days=random.randint(1, 90))).isoformat()
        }

    def generate_job_for_dept(self, department, count):
        # Generate jobs based on departments
        jobs = []
        for _ in range(count):
            jobs.append(self.generate_job(department))

        return jobs