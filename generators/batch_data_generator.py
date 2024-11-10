import random
from datetime import datetime, timedelta
from faker import Faker
from typing import Dict, List, Any
from config.config import CONFIG
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

        self._generate_job_for_dept = JobDataGenerator().generate_job_for_dept
        
        # ID counters
        self.next_contact_id = 0
        self.next_apply_id = 0
    
    def generate_dataset(self, number_of_months: int) -> Dict[str, List[Dict[str, Any]]]:
        """Generate complete recruiting dataset over specified months"""
        # 1. Initial Setup
        self._generate_initial_candidates()
        self._generate_departments()
        self._generate_initial_jobs()
        
        # 2. Monthly Cycles
        # for _ in range(number_of_months - 1):  # -1 because we already generated initial month
        #     self._simulate_month()
        
        # # 3. Finalize dataset
        # self._finalize_statuses()
        
        return {
            'candidates': self.candidates,
            'departments': self.departments,
            'jobs': self.jobs,
        #     'contact_history': self.contact_history,
        #     'apply_history': self.apply_history
        }
    
    def _generate_departments(self):
        for category in self.job_categories:
            self.departments.extend(CompanyDataGenerator().generate_dept_for_category(category, 15))
      
    def _generate_initial_jobs(self):
        """Generate initial job openings"""
        for department in self.departments:
            self.jobs.extend(self._generate_job_for_dept(department, self.new_jobs_per_month[department['dept_specialization']]))

    def _generate_initial_candidates(self):
        """Generate initial candidate pool"""
        for category in self.job_categories:
            self._generate_candidates_for_category(category, self.new_candidates_per_month[category] * 2)
    
    def _generate_candidates_for_category(self, category: str, count: int):
        """Generate specified number of candidates for a category"""
        self.candidates.extend(CandidateGenerator().generate_candidates_for_category(category, count))
    
    def _generate_jobs_for_category(self, category: str, count: int):
        """Generate specified number of jobs for a category"""
        # Get departments for this category
        category_departments = [d for d in self.departments if d['dept_specialization'] == category]
        
        for _ in range(count):
            dept = random.choice(category_departments)
            yoe_min = random.randint(0, 5)
            
            self.jobs.append({
                'id': self.next_job_id,
                'company_department_id': dept['id'],
                'department_name': dept['company_department_name'],
                'job_title': self._get_job_title(category),
                'minimal_years_of_experience': yoe_min,
                'preferred_years_of_experience': yoe_min + random.randint(2, 3),
                'location': dept['location'],
                'status': 'Open',
                'posting_date': self.current_date.isoformat(),
                'category': category
            })
            self.next_job_id += 1
    
    def _get_job_title(self, category: str) -> str:
        """Get random job title based on category"""
        titles = {
            'Data Analytics': [
                'Data Analyst', 'Business Intelligence Analyst',
                'Data Science Analyst', 'Analytics Consultant'
            ],
            'Software Engineering': [
                'Software Engineer', 'Full Stack Developer',
                'Backend Engineer', 'Frontend Developer'
            ]
        }
        return random.choice(titles[category])
    
    def _simulate_month(self):
        """Simulate one month of recruiting activities"""
        # 1. Move to next month
        self.current_date += timedelta(days=30)
        
        # 2. Generate new data
        for category in self.job_categories:
            # Add new jobs
            self._generate_jobs_for_category(category, self.new_jobs_per_month[category])
            
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
            
            # Generate outreach for 5-8 candidates
            candidates_to_contact = random.sample(
                matching_candidates,
                min(random.randint(5, 8), len(matching_candidates))
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
        
        self.contact_history.append({
            'id': self.next_contact_id,
            'candidate_id': candidate['id'],
            'contact_date': contact_date.isoformat(),
            'contact_method': random.choice(['email', 'phone']),
            'contact_source': 'Recruiter', # email, zendesk, and manual notes.
            'interest_level': None,
            'follow_up_needed': True,
            'job_id': job['id']
        })
        self.next_contact_id += 1
        
        # Simulate response (70% response rate)
        if random.random() < 0.7:
            response_date = contact_date + timedelta(days=random.randint(2, 5))
            interest_level = random.choice(['High', 'Medium', 'Low', 'Not Interested'])
            
            self.contact_history.append({
                'id': self.next_contact_id,
                'candidate_id': candidate['id'],
                'contact_date': response_date.isoformat(),
                'contact_method': random.choice(['email', 'phone']),
                'contact_source': 'Candidate',
                'interest_level': interest_level,
                'follow_up_needed': interest_level in ['High', 'Medium'],
                'job_id': job['id']
            })
            self.next_contact_id += 1
            
            # Generate application if interested
            if interest_level in ['High', 'Medium']:
                apply_date = response_date + timedelta(days=random.randint(1, 3))
                
                self.apply_history.append({
                    'id': self.next_apply_id,
                    'candidate_id': candidate['id'],
                    'job_position_id': job['id'],
                    'apply_date': apply_date.isoformat(),
                    'status': 'pending',
                    'referral_source': 'Recruiter',
                    'apply_method': random.choice(['Company Website', 'Email Application'])
                })
                self.next_apply_id += 1
    
    def _close_old_jobs(self):
        """Close jobs from previous months"""
        current_month = self.current_date.replace(day=1)
        
        for job in self.jobs:
            job_date = datetime.fromisoformat(job['posting_date']).replace(day=1)
            if job_date < current_month:
                job['status'] = 'Closed'
    
    def _finalize_statuses(self):
        """Finalize application statuses for closed jobs"""
        for application in self.apply_history:
            job = next(j for j in self.jobs if j['id'] == application['job_position_id'])
            if job['status'] == 'Closed':
                application['status'] = random.choices(
                    ['completed', 'rejected'],
                    weights=[80, 20]
                )[0]
