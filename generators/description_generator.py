import random
from faker import Faker
from config.config import CONFIG
from utils.get_skills_for_role import get_skills_for_role

fake = Faker()

class DescriptionGenerator:
    def __init__(self):
        # Template components for job descriptions
        self.intro_templates = [
            "Join {company_name}'s {department} team as a {job_title}.",
            "We are seeking an experienced {job_title} to join our growing {department} team.",
            "{company_name} is looking for a talented {job_title} to drive innovation in our {department} division.",
            "Exciting opportunity for a {job_title} to make an impact in our {department} organization."
        ]
        
        self.responsibility_templates = {
            "Data Science": [
                "Build and optimize machine learning models to {action} {target}",
                "Analyze complex datasets to {action} {target}",
                "Collaborate with stakeholders to {action} {target}",
                "Develop and maintain data pipelines for {target}",
                "Create and deploy ML models for {target}",
                "Conduct statistical analysis to {action} {target}"
            ],
            "Software Engineering": [
                "Design and implement scalable solutions for {target}",
                "Write clean, maintainable code for {target}",
                "Debug and optimize {target}",
                "Collaborate with cross-functional teams on {target}",
                "Develop and maintain RESTful APIs for {target}",
                "Implement automated testing frameworks for {target}"
            ]
        }
        
        self.target_phrases = {
            "Data Science": [
                "business intelligence dashboards",
                "customer segmentation models",
                "prediction algorithms",
                "data warehousing solutions",
                "automated reporting systems",
                "real-time analytics platforms"
            ],
            "Software Engineering": [
                "high-traffic web applications",
                "distributed systems",
                "cloud infrastructure",
                "microservices architecture",
                "backend services",
                "user-facing features"
            ]
        }
        
        self.action_phrases = {
            "Data Science": [
                "derive insights from",
                "improve efficiency of",
                "automate analysis of",
                "optimize performance of",
                "enhance accuracy of",
                "streamline processing of"
            ],
            "Software Engineering": [
                "enhance scalability of",
                "improve reliability of",
                "optimize performance of",
                "maintain and upgrade",
                "implement new features for",
                "modernize and refactor"
            ]
        }

        # Template components for work experience
        self.experience_templates = {
            "Data Science": [
                "Led {team_size} person team in developing {target}",
                "Implemented machine learning solutions that {action} {target}",
                "Collaborated with stakeholders to {action} {target}",
                "Spearheaded development of {target}",
                "Achieved {metric}% improvement in {target}"
            ],
            "Software Engineering": [
                "Developed and maintained {target}",
                "Architected and implemented {target}",
                "Led technical initiatives to {action} {target}",
                "Reduced {metric}% in system latency for {target}",
                "Mentored junior developers while working on {target}"
            ]
        }

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