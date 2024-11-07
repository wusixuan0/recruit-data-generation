import random
import json
from datetime import datetime
from faker import Faker
from generators.helpers import get_skills_for_role
from config.load_config import load_config
CONFIG = load_config()
fake = Faker()

class CandidateGenerator:
    def __init__(self):
        self.current_date = datetime.now()

    def generate_work_experience(self, role_category, yoe):
        """Generate structured work experience based on role category"""
        num_positions = min(yoe // 2 + 1, 4)  # Reasonable number of positions based on YOE
        positions = []

        available_titles = CONFIG['job_roles'][role_category]['titles']
        remaining_years = yoe

        for _ in range(num_positions):
            duration = min(random.randint(1, 3), remaining_years)
            remaining_years -= duration

            positions.append({
                'title': random.choice(available_titles),
                'company': fake.company(),
                'duration': f"{duration} years",
                'skills': get_skills_for_role(role_category, 3),
            })

        return positions
    def generate_candidate(self, id):
        """Generate a single candidate with structured matching fields"""
        # Select a random role category and its details
        role_category = random.choice(list(CONFIG['job_roles'].keys()))
        yoe = random.randint(0, 15)
        is_structured = random.random() > 0.3  # 70% clean data, 30% messy

        # Generate core matching fields
        skills = get_skills_for_role(role_category)
        work_experience = self.generate_work_experience(role_category, yoe)

        # Generate location preference
        location_type = random.choice(['city', 'remote'])
        if location_type == 'city':
            location = random.choice(CONFIG['locations']['cities'])
        else:
            location = random.choice(CONFIG['locations']['remote_policies'])

        status = random.choice(CONFIG['candidate_status_keywords'])

        return {
            'id': id,
            'full_name': fake.name(),
            'location': location,
            'work_experience': (
                json.dumps(work_experience)
                if is_structured
                else f"Previously worked as {work_experience[-1]['title']} at {work_experience[-1]['company']}"
            ),
            'YOE': yoe,
            'skills': (
                json.dumps(skills)
                if is_structured
                else ', '.join(skills)
            ),
            'status': status,
            'updated_at': self.current_date.isoformat()
        }
    def generate_data(self, num_candidates=500):
        return [self.generate_candidate(i) for i in range(num_candidates)]