import random
from faker import Faker
from config.config import CONFIG
from config.description_config import DESCRIPTION_CONFIG
from utils.get_skills_for_role import get_skills_for_role

fake = Faker()

class DescriptionGenerator:
    def __init__(self):
        self.intro_templates = DESCRIPTION_CONFIG["intro_templates"]
        self.responsibility_templates = DESCRIPTION_CONFIG["responsibility_templates"]
        self.target_phrases = DESCRIPTION_CONFIG["target_phrases"]
        self.action_phrases = DESCRIPTION_CONFIG["action_phrases"]
        self.experience_templates = DESCRIPTION_CONFIG["experience_templates"]

        self.metrics = [str(x) for x in range(10, 96, 5)]  # Generate metrics like 10%, 15%, etc.
        self.team_sizes = ["2", "3", "4", "5", "6", "8", "10"]

    def generate_job_description(self, job_title, category, company_name, department):
        """Generate a complete job description"""
        if category not in self.responsibility_templates:
            category = random.choice(list(self.responsibility_templates.keys()))

        # Generate intro
        intro = random.choice(self.intro_templates).format(
            company_name=company_name,
            department=department,
            job_title=job_title
        )

        # Generate 3-5 responsibilities
        num_responsibilities = random.randint(3, 5)
        responsibilities = []
        used_targets = set()
        
        for _ in range(num_responsibilities):
            template = random.choice(self.responsibility_templates[category])
            action = random.choice(self.action_phrases[category])
            
            # Ensure unique targets
            available_targets = [t for t in self.target_phrases[category] if t not in used_targets]
            if not available_targets:
                used_targets.clear()
                available_targets = self.target_phrases[category]
            
            target = random.choice(available_targets)
            used_targets.add(target)
            
            responsibility = template.format(action=action, target=target)
            responsibilities.append(responsibility)

        # Combine all parts
        description = f"{intro}\n\nKey Responsibilities:\n" + \
                     "\n".join(f"• {r}" for r in responsibilities)
        
        return description

    def generate_work_experience(self, category, yoe):
        """Generate work experiences for a candidate"""
        if category not in self.experience_templates:
            category = random.choice(list(self.experience_templates.keys()))

        experiences = []
        used_targets = set()
        num_experiences=min(yoe // 2 + 1, 4)
        available_titles = CONFIG['job_roles'][category]['titles']
        remaining_years = yoe
        
        for _ in range(num_experiences):
            duration = min(random.randint(1, 3), remaining_years)
            remaining_years -= duration
            
            # Generate 2-3 achievements per experience
            achievements = []
            for _ in range(random.randint(2, 3)):
                template = random.choice(self.experience_templates[category])
                action = random.choice(self.action_phrases[category])
                
                # Ensure unique targets
                available_targets = [t for t in self.target_phrases[category] if t not in used_targets]
                if not available_targets:
                    used_targets.clear()
                    available_targets = self.target_phrases[category]
                
                target = random.choice(available_targets)
                used_targets.add(target)
                
                achievement = template.format(
                    action=action,
                    target=target,
                    team_size=random.choice(self.team_sizes),
                    metric=random.choice(self.metrics)
                )
                achievements.append(achievement)

            experience = {
                "title": random.choice(available_titles),
                "company": fake.company(),
                "duration": duration,
                "achievements": achievements,
                'skills': get_skills_for_role(category, 3),
            }
            experiences.append(experience)

        return experiences