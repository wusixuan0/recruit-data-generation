import random
import json
from datetime import datetime
from faker import Faker
from utils.get_skills_for_role import get_skills_for_role
from config.config import CONFIG
from config.other_config import OTHER_CONFIG
import uuid
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
    
    def generate_candidate(self, role_category):
        """Generate a single candidate with structured matching fields"""
        yoe = random.randint(0, 15)
        is_structured = random.random() > 0.3  # 70% clean data, 30% messy

        # Generate core matching fields
        skills = get_skills_for_role(role_category)
        work_experience = self.generate_work_experience(role_category, yoe)

        # Generate location preference
        location = random.choice(OTHER_CONFIG['locations']['cities'])
        location_type = random.random() > 0.5
        location_preference = location if location_type else 'remote'

        status = random.choice(OTHER_CONFIG['candidate_status_keywords'])

        return {
            'id': str(uuid.uuid4()),
            'full_name': fake.name(),
            'location': location,
            'location_preference': location_preference,
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
            'role_category': role_category,
            'status': status,
            'updated_at': self.current_date.isoformat()
        }
    
    def generate_candidates_for_category(self, role_category, count):
        return [self.generate_candidate(role_category) for _ in range(count)]