import random
from datetime import datetime, timedelta
from dateutil.relativedelta import relativedelta
from faker import Faker
from typing import Dict, List, Any
from config.config import CONFIG
from config.other_config import OTHER_CONFIG
from generators.candidate_generator import CandidateGenerator
from generators.company_generator import CompanyDataGenerator
from generators.job_generator import JobDataGenerator

fake = Faker()

class RecruitingSimulator:
    def __init__(self, start_date: datetime = None):
        self.current_date = start_date or datetime.now()
        self.job_categories = CONFIG["role_categories"]
        
        # Monthly generation parameters
        self.new_jobs_per_month = CONFIG["new_jobs_per_month"]
        self.new_candidates_per_month = CONFIG["new_candidates_per_month"]        
        
        # Initialize data stores
        self.departments = []
        self.jobs = []
        self.candidates = []
        self.contact_history = []
        self.apply_history = []

        # ID counters
        self.next_contact_id = 0
        self.next_apply_id = 0
    
    def generate_dataset(self, number_of_months: int) -> Dict[str, List[Dict[str, Any]]]:
        self._set_start_date(number_of_months)
        """Generate complete recruiting dataset over specified months"""
        # 1. Initial Setup
        self._generate_initial_candidates()
        self._generate_departments_for_categories()
        self._generate_initial_jobs()
        
        # 2. Monthly Cycles
        for _ in range(number_of_months - 1):  # -1 because we already generated initial month
            self._simulate_month()
        
        # 3. Finalize dataset
        self._finalize_statuses()
        
        return {
            'candidates': self.candidates,
            'departments': self.departments,
            'jobs': self.jobs,
            'contact_history': self.contact_history,
            'apply_history': self.apply_history
        }
    
    def _set_start_date(self, number_of_months: int):
        self.current_date = self.current_date - relativedelta(months=number_of_months)
    
    def _generate_departments_for_categories(self):
        for category in self.job_categories:
            self.departments.extend(CompanyDataGenerator().generate_dept_for_category(category, 15))
            
    def _generate_department(self):
        category = random.choice(self.job_categories)
        self.departments.extend(CompanyDataGenerator().generate_dept_for_category(category, 1))

    def _generate_initial_jobs(self):
        """Generate initial job openings"""
        for department in self.departments:
            jobs = JobDataGenerator().generate_jobs_for_dept(
                department=department,
                count=1,
                posting_date=self.current_date.isoformat(),
            )
            self.jobs.extend(jobs)

    def _generate_initial_candidates(self):
        """Generate initial candidate pool"""
        for category in self.job_categories:
            self._generate_candidates_for_category(category, self.new_candidates_per_month[category] * 2)
    
    def _generate_candidates_for_category(self, category: str, count: int):
        """Generate specified number of candidates for a category"""
        self.candidates.extend(CandidateGenerator().generate_candidates_for_category(category, count, self.current_date.isoformat()))
    
    def _simulate_month(self):
        """Simulate one month of recruiting activities"""
        # 1. Move to next month
        self.current_date += timedelta(days=30)
        
        # 2. Generate new data
        self._generate_department()

        for category in self.job_categories:
            # Add new jobs
            job_count = self.new_jobs_per_month[category]
            
            new_jobs = JobDataGenerator().generate_jobs_for_category(
                category=category,
                departments=self.departments,
                count=job_count,
                posting_date=self.current_date.isoformat(),
            )

            self.jobs.extend(new_jobs)
            # Add new candidates
            self._generate_candidates_for_category(category, self.new_candidates_per_month[category])
        
        # 3. Generate recruiter activities
        self._generate_recruiter_activities()
        
        # 4. Close old jobs
        self._close_old_jobs()
    
    def _generate_recruiter_activities(self):
        """Generate recruiter outreach and applications"""
        active_jobs = [j for j in self.jobs if j['status'] == 'Open']
        
        for job in active_jobs:
            # Find matching candidates
            matching_candidates = self._find_matching_candidates(job)
            
            # reach out to candidates
            candidates_to_contact = random.sample(
                matching_candidates,
                min(random.randint(2, 3), len(matching_candidates))
            )
            
            # Generate contact and application history
            for candidate in candidates_to_contact:
                self._generate_outreach_sequence(job, candidate)
    
    def _find_matching_candidates(self, job: Dict) -> List[Dict]:
        """Find candidates matching job criteria"""
        return [
            c for c in self.candidates
            if (c['role_category'] == job['category'] and
                c['location'] == job['location'] and
                c['YOE'] >= job['minimal_years_of_experience'] and
                c['status'] in ['Active', 'Passive'])
        ]
    
    def _generate_outreach_sequence(self, job: Dict, candidate: Dict):
        """Generate outreach sequence for a candidate"""
        # Initial outreach
        contact_date = datetime.fromisoformat(job['posting_date']) + timedelta(days=random.randint(1, 7))
        candidate_status = candidate['status']
        interest_level = random.choice(OTHER_CONFIG['interest_levels'][candidate_status])
        follow_up_needed = random.choice([True, False]) if candidate_status == "Active" else False
        
        self.contact_history.append({
            'id': self.next_contact_id,
            'candidate_id': candidate['id'],
            'contact_date': contact_date.isoformat(),
            'contact_method': random.choice(['email', 'phone']),
            'data_source': random.choice(["email", "zendesk", "manual notes"]),
            'interest_level': interest_level,
            'follow_up_needed': follow_up_needed,
            'job_id': job['id']
        })
        self.next_contact_id += 1
        
        # Generate application (60% for active, 20% for passive)
        if (random.random() < 0.6 and candidate_status.lower() == "active") or (random.random() < 0.2 and candidate_status.lower() == "passive"):
            apply_date = contact_date + timedelta(days=random.randint(1, 3))
            status = random.choices(
                ["successful", "rejected"],
                weights=[20, 80]
            )[0]
            additional_notes = random.choices(OTHER_CONFIG["application_note"][status])

            self.apply_history.append({
                'id': self.next_apply_id,
                'candidate_id': candidate['id'],
                'job_position_id': job['id'],
                'apply_date': apply_date.isoformat(),
                'status': status,
                'referral_source': 'Recruiter',
                'apply_method': random.choice([
                    "LinkedIn Easy Apply", "Company Website",
                    "Email Application", "Internal Referral System",
                    "Recruiter Submit"]),
                'additional_notes': additional_notes,
            })
            self.next_apply_id += 1

    def _close_old_jobs(self):
        """Close jobs from previous months"""
        current_month = self.current_date.replace(day=1)
        
        for job in self.jobs:
            job_date = datetime.fromisoformat(job['posting_date']).replace(day=1)
            if job_date < current_month:
                job['status'] = random.choice(['Closed', 'Filled'])

    def _finalize_statuses(self):
        """Finalize application statuses for closed jobs"""
        for application in self.apply_history:
            job = next(j for j in self.jobs if j['id'] == application['job_position_id'])
            if job['status'] == 'Closed':
                application['status'] = random.choices(
                    ['rejected', 'hired'],
                    weights=[60, 40]
                )[0]
                if application['status'] == 'hired':
                    for candidate in self.candidates:
                        if candidate['id'] == application['candidate_id']:
                            candidate['status'] = 'Not open to interview'
                            break
