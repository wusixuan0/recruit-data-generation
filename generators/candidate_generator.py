import random
import json
from datetime import datetime
from faker import Faker
from utils.get_skills_for_role import get_skills_for_role
from generators.description_generator import DescriptionGenerator
from config.other_config import OTHER_CONFIG
import uuid
fake = Faker()

class CandidateGenerator:
    def __init__(self):
        self.current_date = datetime.now()

    def generate_candidate(self, role_category, created_at):
        """Generate a single candidate with structured matching fields"""
        yoe = random.randint(0, 15)
        is_structured = random.random() > 0.3  # 70% clean data, 30% messy

        # Generate core matching fields
        skills = get_skills_for_role(role_category)

        work_experience = DescriptionGenerator().generate_work_experience(
            category=role_category,
            yoe=yoe,
        )

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
            'work_experience': work_experience,
            'YOE': yoe,
            'skills': (
                json.dumps(skills)
                if is_structured
                else ', '.join(skills)
            ),
            'role_category': role_category,
            'status': status,
            'created_at': created_at,
        }
    
    def generate_candidates_for_category(self, role_category, count, created_at):
        return [self.generate_candidate(role_category, created_at) for _ in range(count)]