import json
from generators.candidate_generator import CandidateGenerator
from generators.company_job_generator import CompanyJobDataGenerator
from generators.contact_history_generator import ContactDataGenerator
from generators.apply_history_generator import ApplyHistoryGenerator

candidates = CandidateGenerator().generate_data(num_candidates=1)

# with open("candidates.json", 'w') as f:
#     json.dump(candidates, f, indent=2)

company_data = CompanyJobDataGenerator().generate_data(num_departments=2, num_jobs=2)
jobs = company_data['jobs']

# with open("jobs.json", 'w') as f:
#     json.dump(jobs, f, indent=2)
# with open("departments.json", 'w') as f:
#     json.dump(company_data['departments'], f, indent=2)

# contact_history = ContactDataGenerator().generate_data(candidates)
# with open("contact_history.json", 'w') as f:
#     json.dump(contact_history, f, indent=2)

apply_history = ApplyHistoryGenerator().generate_apply_history(candidates, jobs, num_applications=1)
with open("apply_history.json", 'w') as f:
    json.dump(apply_history, f, indent=2)
