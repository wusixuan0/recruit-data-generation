import random
from datetime import datetime, timedelta
from faker import Faker
from utils.get_skills_for_role import get_skills_for_role
from generators.description_generator import DescriptionGenerator
from config.config import CONFIG
from config.other_config import OTHER_CONFIG
import uuid
fake = Faker()

class JobDataGenerator:
    def __init__(self):
        self.current_date = datetime.now()

    def generate_job_fields(self, department_id, title, category, location, company_dept_name, posting_date):
        required_skills = get_skills_for_role(category)
        yoe_min = random.randint(3, 5)
        parts = company_dept_name.split(",")
        company_name = parts[1].strip()
        dept_name = parts[0].strip()

        job_description = DescriptionGenerator().generate_job_description(
            job_title=title,
            category=category,
            company_name=company_name,
            department=dept_name,
        )
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
            'job_description': job_description,
            'posting_date': posting_date,
        }

    def generate_job_for_dept(self, department, posting_date):
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
            company_dept_name=department['company_department_name'],
            posting_date=posting_date,
        )

    def generate_jobs_for_dept(self, department, count, posting_date):
        # Generate jobs based on departments
        jobs = []
        for _ in range(count):
            job = self.generate_job_for_dept(department, posting_date)
            jobs.append(job)

        return jobs
    
    def generate_jobs_for_category(self, category, departments, count, posting_date):
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
                company_dept_name=dept['company_department_name'],
                posting_date=posting_date,
            )
            jobs.append(job)
        return jobs