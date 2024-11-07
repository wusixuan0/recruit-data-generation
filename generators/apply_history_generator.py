import random
from datetime import datetime, timedelta

class ApplyHistoryGenerator:
    def __init__(self):
        self.current_date = datetime.now()
        self.referral_sources = [
            "Employee Referral", "LinkedIn", "Indeed",
            "University Career Fair", "Company Website",
            "Recruiter Outreach", "Professional Network"
        ]
        self.apply_methods = [
            "LinkedIn Easy Apply", "Company Website",
            "Email Application", "Internal Referral System",
            "Recruiter Submit"
        ]

    def check_yoe_match(self, candidate_yoe, job_min_yoe):
        """Simple YOE check - returns True if candidate meets minimum requirements"""
        return candidate_yoe >= job_min_yoe

    def generate_feedback(self, status, is_yoe_match, candidate_yoe, job_min_yoe):
        """Generate simple feedback based on status and YOE match"""
        if status == "successful":
            templates = [
                "Strong interview performance. Great cultural fit.",
                "Excellent technical assessment results.",
                "Team was impressed with experience and background.",
                "Strong alignment with role requirements."
            ]
        elif status == "rejected":
            if not is_yoe_match:
                templates = [
                    f"Looking for candidates with {job_min_yoe}+ years of experience",
                    "Found candidates with more relevant experience",
                    "Position requires more years of experience"
                ]
            else:
                templates = [
                    "Position filled by another candidate",
                    "Found candidates with better role alignment",
                    "Moving forward with other candidates"
                ]
        else:  # pending
            templates = [
                "Application under review",
                "Scheduling technical assessment",
                "Initial screening in progress",
                "Review in progress"
            ]

        return random.choice(templates)

    def determine_application_status(self, is_yoe_match, candidate_status):
        """Determine application status based on YOE match and candidate status"""
        if candidate_status == "Active":
            if is_yoe_match:
                probabilities = {"successful": 0.4, "rejected": 0.3, "pending": 0.3}
            else:
                probabilities = {"successful": 0.1, "rejected": 0.7, "pending": 0.2}
        else:  # Passive
            if is_yoe_match:
                probabilities = {"successful": 0.2, "rejected": 0.5, "pending": 0.3}
            else:
                probabilities = {"successful": 0.05, "rejected": 0.8, "pending": 0.15}

        return random.choices(
            list(probabilities.keys()),
            weights=list(probabilities.values())
        )[0]

    def generate_apply_date(self, job_posting_date, candidate_updated_at):
        """Generate a realistic apply date"""
        posting_date = datetime.fromisoformat(job_posting_date)
        candidate_date = datetime.fromisoformat(candidate_updated_at)

        earliest_date = max(posting_date, candidate_date)
        latest_date = self.current_date

        if earliest_date >= latest_date:
            return latest_date

        days_diff = (latest_date - earliest_date).days
        random_days = random.randint(0, max(0, days_diff))

        return earliest_date + timedelta(days=random_days)

    def generate_apply_history(self, candidates, jobs, num_applications=1000):
        """Generate apply history data with simple matching logic"""
        apply_history = []
        application_id = 0

        # Track applications per candidate
        candidate_application_counts = {candidate['id']: 0 for candidate in candidates}
        max_applications = {
            'Active': random.randint(5, 10),
            'Passive': random.randint(1, 3),
            'Not open to interview': 0
        }

        while len(apply_history) < num_applications:
            candidate = random.choice(candidates)
            job = random.choice(jobs)

            # Skip if job is not active/posted
            if job['status'] not in ['Posted', 'Active']:
                continue

            # Skip if candidate is not open to interviews
            if candidate['status'] == 'Not open to interview':
                continue

            # Check application limit for candidate
            if candidate_application_counts[candidate['id']] >= max_applications[candidate['status']]:
                continue

            # Simple YOE check
            is_yoe_match = self.check_yoe_match(
                candidate['YOE'],
                job['minimal_years_of_experience']
            )

            # Determine application status
            status = self.determine_application_status(is_yoe_match, candidate['status'])

            # Generate apply date
            apply_date = self.generate_apply_date(job['posting_date'], candidate['updated_at'])

            # Generate feedback
            feedback = self.generate_feedback(
                status,
                is_yoe_match,
                candidate['YOE'],
                job['minimal_years_of_experience']
            ) if status != "pending" else None

            application = {
                'id': application_id,
                'candidate_id': candidate['id'],
                'job_position_id': job['id'],
                'apply_date': apply_date.isoformat(),
                'status': status,
                'feedback': feedback,
                'referral_source': random.choice(self.referral_sources),
                'apply_method': random.choice(self.apply_methods)
            }

            apply_history.append(application)
            candidate_application_counts[candidate['id']] += 1
            application_id += 1

        return apply_history