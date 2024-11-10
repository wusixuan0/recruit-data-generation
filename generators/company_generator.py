import random
from datetime import datetime
from faker import Faker
from config.config import CONFIG
from config.other_config import COMPANY_CONFIG, OTHER_CONFIG
import uuid
fake = Faker()

class CompanyDataGenerator:
    def __init__(self):
        self.current_date = datetime.now()

    def generate_department(self, dept_specialization):
        """Generate a company department using both predefined and dynamic names"""
        use_predefined_companies = random.random() < 0.5
        
        if use_predefined_companies:
            industry = random.choice(list(COMPANY_CONFIG['companies'].keys()))
            company = random.choice(COMPANY_CONFIG['companies'][industry])
        else:
            company = fake.company()
        
        dept_name = f"{dept_specialization} Team, {company}"

        department = {
            'id': str(uuid.uuid4()),
            'company_department_name': dept_name,
            # 'department_type': dept_type,
            'dept_specialization': dept_specialization,
            'location': random.choice(OTHER_CONFIG['locations']['cities']),
            'department_size': random.randint(5, 50),
        }

        # Add role mapping based on department type
        department['roles'] = CONFIG['job_roles'][dept_specialization]['titles']

        return department

    def generate_dept_for_category(self, category, count):
        return [self.generate_department(category) for _ in range(count)]