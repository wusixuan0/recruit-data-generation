import argparse
from generators.candidate_generator import CandidateGenerator
from generators.company_job_generator import CompanyJobDataGenerator
from generators.contact_history_generator import ContactDataGenerator
from generators.apply_history_generator import ApplyHistoryGenerator
from utils.custom_print import custom_print
from utils.file_utils import save_json
from config.config import CONFIG
from generators.batch_data_generator import RecruitingSimulator

def main(args):
    if args.batch:
        dataset = RecruitingSimulator().generate_dataset(number_of_months=6)
        
        print(f"Generated dataset over 6 months:")
        print(f"Departments: {len(dataset['departments'])}")
        print(f"Jobs: {len(dataset['jobs'])}")
        print(f"Candidates: {len(dataset['candidates'])}")
        print(f"Contacts: {len(dataset['contact_history'])}")
        print(f"Applications: {len(dataset['apply_history'])}")

        departments = dataset['departments']
        jobs = dataset['jobs']
        candidates = dataset['candidates']
        apply_history = dataset['apply_history']

        print("\nExample Department:")
        custom_print(departments[0])

        print("\nExample Job:")
        custom_print(jobs[0])

        print("\nExample Candidate:")
        custom_print(candidates[0])

        print("\nExample Application:")
        custom_print(apply_history[0])
    if args.print:
        custom_print()
        print()

    if args.generate_candidates:
        candidates = CandidateGenerator().generate_data(num_candidates=args.num_candidates)
        save_json(candidates, "candidates.json")

    if args.generate_jobs:
        company_data = CompanyJobDataGenerator().generate_data(num_departments=1, num_jobs=1)
        jobs = company_data['jobs']
        save_json(company_data['jobs'], "jobs.json")
        save_json(company_data['departments'], "departments.json")

    if args.generate_contact_history:
        candidates = CandidateGenerator().generate_data(num_candidates=1)
        contact_history = ContactDataGenerator().generate_data(candidates)
        save_json(contact_history, "contact_history.json")

    if args.generate_apply_history:
        # Example Batch: "Data Analytics" Jobs & Candidates
        # 1. Generate 20 Data Analytics jobs
        # 2. Generate 50 candidates in Data Analytics
        # 3. Generate apply_history within this batch
        # (role_category in candidate == dept_specialization in job)
        for role_category in CONFIG['role_categories']:
            candidates = CandidateGenerator().generate_data(num_candidates=50, role_category=role_category)
            company_data = CompanyJobDataGenerator().generate_data(num_departments=10, num_jobs=20, dept_specialization=role_category)
            jobs = company_data['jobs']

            apply_history = ApplyHistoryGenerator().generate_apply_history(candidates, jobs, num_applications=args.num_applications)
            save_json(apply_history, "apply_history.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate data for various tables.")
    parser.add_argument('--batch', action='store_true')
    parser.add_argument('--print', action='store_true', help="print pre-defined job data")
    parser.add_argument('--generate-candidates', action='store_true', help="Generate candidate data")
    parser.add_argument('--generate-jobs', action='store_true', help="Generate job and department data")
    parser.add_argument('--generate-contact-history', action='store_true', help="Generate contact history data")
    parser.add_argument('--generate-apply-history', action='store_true', help="Generate apply history data")
    parser.add_argument('--num-candidates', type=int, default=1, help="Number of candidates to generate")
    parser.add_argument('--num-departments', type=int, default=2, help="Number of departments to generate for jobs")
    parser.add_argument('--num-jobs', type=int, default=2, help="Number of jobs to generate per department")
    parser.add_argument('--num-applications', type=int, default=1, help="Number of job applications to generate")

    args = parser.parse_args()
    main(args)
