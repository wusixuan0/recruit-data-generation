import random
from config.config import CONFIG

def get_skills_for_role(role_category, num_skills=5):
    """Get relevant skills based on role category and its required skillsets"""
    role_info = CONFIG['job_roles'][role_category]
    all_relevant_skills = []

    # Collect all skills from required skillsets
    for skillset in role_info['skillsets']:
        all_relevant_skills.extend(CONFIG['skillsets'][skillset])

    # Remove duplicates and sample
    unique_skills = list(set(all_relevant_skills))
    return random.sample(unique_skills, min(num_skills, len(unique_skills)))