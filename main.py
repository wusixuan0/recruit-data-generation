import argparse
from utils.custom_print import custom_print
from utils.file_utils import save_json
from generators.recruit_simulator import RecruitingSimulator

def main(args):
    if args.generate:
        number_of_months=6
        dataset = RecruitingSimulator().generate_dataset(number_of_months=number_of_months)
 
        departments = dataset['departments']
        jobs = dataset['jobs']
        candidates = dataset['candidates']
        contact_history = dataset['contact_history']
        apply_history = dataset['apply_history']
       
        print(f"Generated dataset over {number_of_months} months:")
        print(f"Candidates: {len(candidates)}")
        print(f"Departments: {len(departments)}")
        print(f"Jobs: {len(jobs)}")
        print(f"Contacts: {len(contact_history)}")
        print(f"Applications: {len(apply_history)}")

        # print("\nExample Department:")
        # custom_print(departments[0])

        # print("\nExample Job:")
        # custom_print(jobs[0])

        # print("\nExample Candidate:")

        # custom_print(candidates[0])
        # print("\nExample Contact:")
        # custom_print(contact_history[0])

        # print("\nExample Application:")
        # custom_print(apply_history[0])

        save_json(candidates, "candidates.json")
        save_json(departments, "company_departments.json")
        save_json(jobs, "jobs.json")
        save_json(contact_history, "contact_history.json")
        save_json(apply_history, "apply_history.json")
    
    if args.print:
        custom_print()
        print()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Generate data for 5 tables.")
    parser.add_argument('--generate', action='store_true')
    parser.add_argument('--print', action='store_true', help="print pre-defined job data")

    args = parser.parse_args()
    main(args)
