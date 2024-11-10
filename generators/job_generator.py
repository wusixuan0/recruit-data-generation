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

    def generate_job_fields(self, department_id, title, category, location, posting_date):
        required_skills = get_skills_for_role(category)
        yoe_min = random.randint(3, 5)

        return {
            'id': str(uuid.uuid4()),
            'company_department_id': department_id,
            'job_title': title,
            'required_skills': required_skills,
            'minimal_years_of_experience': yoe_min,
            'preferred_years_of_experience': yoe_min + random.randint(0, 3),
            'location': location,
            'category': category,
            'remote_policy': random.choice(OTHER_CONFIG['locations']['remote_policies']),
            'status': 'Open',
            'posting_date': posting_date,
        }

    def generate_job_for_dept(self, department):
        """Generate a job position aligned with department"""
        dept_specialization = department['dept_specialization']
        
        if 'roles' in department:
            role = random.choice(department['roles'])
        else:
            role = random.choice(CONFIG['job_roles'][dept_specialization]['titles'])

        return self.generate_job_fields(
            department_id=department['id'],
            title=role,
            category=dept_specialization,
            location=department['location'],
            posting_date=(self.current_date - timedelta(days=random.randint(1, 90))).isoformat()
        )

    def generate_jobs_for_dept(self, department, count):
        # Generate jobs based on departments
        jobs = []
        for _ in range(count):
            job = self.generate_job_for_dept(department)
            jobs.append(job)

        return jobs
    
    def generate_jobs_for_category(self, category, departments, count, current_date):
        """Generate specified number of jobs for a category"""
        # Get departments for this category
        category_departments = [d for d in departments if d['dept_specialization'] == category]
        
        jobs = []
        for _ in range(count):
            dept = random.choice(category_departments)
            
            job = self.generate_job_fields(
                department_id=dept['id'],
                title=random.choice(CONFIG['job_roles'][category]['titles']),
                category=category,
                location=dept['location'],
                posting_date=current_date.isoformat(),
            )
            jobs.append(job)
        return jobs