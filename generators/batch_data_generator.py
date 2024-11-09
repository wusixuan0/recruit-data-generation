import random
from datetime import datetime, timedelta
from faker import Faker
from typing import List, Dict, Any

fake = Faker()

class RecruiterMatchingGenerator:
    def __init__(self):
        self.current_date = datetime.now()
        self.talent_pool = []
        
    def generate_complete_dataset(
        self,
        num_departments: int = 2,
        jobs_per_dept: int = 3,
        talent_pool_size: int = 50
    ) -> Dict[str, List[Dict[str, Any]]]:
        """Generate a complete dataset with recruiter-initiated matching flow"""
        
        # 1. Generate departments (focused on Data Analytics)
        departments = self._generate_departments(num_departments)
        
        # 2. Generate job openings
        jobs = self._generate_jobs(departments, jobs_per_dept)
        
        # 3. Generate talent pool
        self.talent_pool = self._generate_talent_pool(talent_pool_size)
        
        # 4. Generate recruiter outreach and applications
        contact_history = []
        apply_history = []
        
        # For each job, generate outreach sequence
        for job in jobs:
            job_contacts, job_applications = self._generate_job_matching_sequence(job)
            contact_history.extend(job_contacts)
            apply_history.extend(job_applications)
        
        return {
            'departments': departments,
            'jobs': jobs,
            'candidates': self.talent_pool,
            'contact_history': contact_history,
            'apply_history': apply_history
        }
    
    def _generate_departments(self, num_departments: int) -> List[Dict[str, Any]]:
        """Generate Data Analytics departments"""
        departments = []
        companies = ['RBC', 'TD', 'BMO', 'CIBC', 'Scotiabank']
        
        for i in range(num_departments):
            company = random.choice(companies)
            departments.append({
                'id': i,
                'company_department_name': f"Data Analytics, {company}",
                'department_type': "Data Analytics",
                'location': random.choice(['Toronto', 'Vancouver', 'Montreal']),
                'department_size': random.randint(5, 30)
            })
        
        return departments
    
    def _generate_jobs(self, departments: List[Dict], jobs_per_dept: int) -> List[Dict[str, Any]]:
        """Generate jobs under Data Analytics departments"""
        jobs = []
        job_id = 0
        analytics_titles = [
            "Data Analyst",
            "Business Intelligence Analyst",
            "Data Science Analyst",
            "Analytics Consultant"
        ]
        
        for dept in departments:
            for _ in range(jobs_per_dept):
                yoe_min = random.randint(0, 3)
                posting_date = self.current_date - timedelta(days=random.randint(1, 60))
                
                jobs.append({
                    'id': job_id,
                    'company_department_id': dept['id'],
                    'department_name': dept['company_department_name'],
                    'job_title': random.choice(analytics_titles),
                    'minimal_years_of_experience': yoe_min,
                    'preferred_years_of_experience': yoe_min + random.randint(2, 3),
                    'location': dept['location'],
                    'status': random.choice(['Posted', 'Active']),
                    'posting_date': posting_date.isoformat()
                })
                job_id += 1
        
        return jobs
    
    def _generate_talent_pool(self, pool_size: int) -> List[Dict[str, Any]]:
        """Generate pool of Data Analytics candidates"""
        candidates = []
        
        for i in range(pool_size):
            yoe = random.randint(0, 8)
            candidates.append({
                'id': i,
                'full_name': fake.name(),
                'role_category': "Data Analytics",
                'location': random.choice(['Toronto', 'Vancouver', 'Montreal']),
                'YOE': yoe,
                'status': random.choice(["Active", "Passive", "Not open to interview"]),
                'updated_at': (self.current_date - timedelta(days=random.randint(1, 90))).isoformat()
            })
            
        return candidates
    
    def _find_matching_candidates(self, job: Dict[str, Any], num_candidates: int = 8) -> List[Dict[str, Any]]:
        """Find suitable candidates for a job based on criteria"""
        matching_candidates = []
        
        for candidate in self.talent_pool:
            if (
                candidate['YOE'] >= job['minimal_years_of_experience'] and
                candidate['status'] != "Not open to interview" and
                candidate['location'] == job['location']
            ):
                matching_candidates.append(candidate)
        
        # Return random sample of matching candidates
        return random.sample(
            matching_candidates,
            min(num_candidates, len(matching_candidates))
        )
    
    def _generate_job_matching_sequence(
        self,
        job: Dict[str, Any]
    ) -> tuple[List[Dict[str, Any]], List[Dict[str, Any]]]:
        """Generate complete outreach and application sequence for a job"""
        contact_history = []
        apply_history = []
        contact_id = 0
        application_id = 0
        
        # Find matching candidates
        matching_candidates = self._find_matching_candidates(job)
        
        # Generate initial outreach for each matching candidate
        posting_date = datetime.fromisoformat(job['posting_date'])
        
        for candidate in matching_candidates:
            # Initial outreach date (1-7 days after posting)
            outreach_date = posting_date + timedelta(days=random.randint(1, 7))
            
            # Initial recruiter outreach
            contact_history.append({
                'id': contact_id,
                'candidate_id': candidate['id'],
                'contact_date': outreach_date.isoformat(),
                'contact_method': random.choice(['email', 'phone']),
                'contact_source': 'Recruiter',
                'interest_level': None,  # Initially unknown
                'follow_up_needed': True,
                'contact_priority': 'High',
                'job_id': job['id']  # Link to specific job
            })
            contact_id += 1
            
            # Simulate candidate response (2-5 days after outreach)
            if random.random() < 0.7:  # 70% response rate
                response_date = outreach_date + timedelta(days=random.randint(2, 5))
                interest_level = random.choice(['High', 'Medium', 'Low', 'Not Interested'])
                
                # Record candidate response
                contact_history.append({
                    'id': contact_id,
                    'candidate_id': candidate['id'],
                    'contact_date': response_date.isoformat(),
                    'contact_method': random.choice(['email', 'phone']),
                    'contact_source': 'Candidate',
                    'interest_level': interest_level,
                    'follow_up_needed': interest_level in ['High', 'Medium'],
                    'contact_priority': 'Medium',
                    'job_id': job['id']
                })
                contact_id += 1
                
                # Generate application if interested
                if interest_level in ['High', 'Medium']:
                    apply_date = response_date + timedelta(days=random.randint(1, 3))
                    
                    apply_history.append({
                        'id': application_id,
                        'candidate_id': candidate['id'],
                        'job_position_id': job['id'],
                        'apply_date': apply_date.isoformat(),
                        'status': 'pending',
                        'referral_source': 'Recruiter',
                        'apply_method': random.choice([
                            'Company Website',
                            'Email Application'
                        ])
                    })
                    application_id += 1
        
        return contact_history, apply_history

if __name__ == "__main__":
    # Example usage
    generator = RecruiterMatchingGenerator()
    dataset = generator.generate_complete_dataset(
        num_departments=2,
        jobs_per_dept=3,
        talent_pool_size=50
    )
    
    # Print some statistics
    print(f"Generated:")
    print(f"- {len(dataset['departments'])} departments")
    print(f"- {len(dataset['jobs'])} jobs")
    print(f"- {len(dataset['candidates'])} candidates")
    print(f"- {len(dataset['contact_history'])} contact records")
    print(f"- {len(dataset['apply_history'])} applications")