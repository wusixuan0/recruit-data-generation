import argparse
from generators.candidate_generator import CandidateGenerator
from generators.company_job_generator import CompanyJobDataGenerator
from generators.contact_history_generator import ContactDataGenerator
from generators.apply_history_generator import ApplyHistoryGenerator
from utils.custom_print import custom_print
from utils.file_utils import save_json

def main(args):
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
        candidates = CandidateGenerator().generate_data(num_candidates=1)
        company_data = CompanyJobDataGenerator().generate_data(num_departments=2, num_jobs=2)
        jobs = company_data['jobs']
        apply_history = ApplyHistoryGenerator().generate_apply_history(candidates, jobs, num_applications=args.num_applications)
        save_json(apply_history, "apply_history.json")

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate data for various tables.")
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
