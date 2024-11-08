import random
from datetime import datetime, timedelta
from faker import Faker
from config.other_config import OTHER_CONFIG
fake = Faker()

class ContactDataGenerator:
    def __init__(self):
      self.current_date = datetime.now()

    def generate_contact_history(self, candidate_id, candidate_status):
        """Generate contact history for a candidate."""
        history = []
        contact_methods = ["email", "phone", "Zendesk"]

        if candidate_status == "Active":
            num_contacts = random.randint(2,5)
        elif candidate_status == "Active":
            num_contacts = random.randint(1,2)
        else:
            num_contacts = 1
        for _ in range(num_contacts):
            contact_date = self.current_date - timedelta(days=random.randint(1, 180))
            interest_level = random.choice(OTHER_CONFIG['interest_levels'][candidate_status])
            follow_up_needed = random.choice([True, False]) if candidate_status == "Active" else False

            history.append({
                'id': fake.uuid4(),
                'candidate_id': candidate_id,
                'contact_date': contact_date.isoformat(),
                'contact_method': random.choice(contact_methods),
                'contact_source': "Zendesk" if random.random() > 0.7 else "Email",
                'interest_level': interest_level,
                'follow_up_needed': follow_up_needed,
                'contact_priority': random.choice(["High", "Medium", "Low"]),
            })
        return history

    def generate_data(self, candidates):

        # Generate contact histories
        contact_histories = []

        for candidate in candidates:
            candidate_id = candidate['id']
            candidate_status = candidate['status']
            contact_histories.extend(self.generate_contact_history(candidate_id, candidate_status))

        return contact_histories
