import streamlit as st
from datetime import date, timedelta
import json
import time
import os

# --- Configuration ---
SPRINT_START_DATE = date(2025, 5, 26) # May 26th, 2025 - Adjust this to your actual start date!
TOTAL_SPRINT_DAYS = 60
JOB_APPLICATIONS_PER_WEEK_TARGET = 25
TOTAL_SPRINT_WEEKS = TOTAL_SPRINT_DAYS / 7
DATA_FILE = 'sprint_data.json'

# --- Helper Functions for Data Persistence ---
def load_data():
    """Loads sprint data from a JSON file, ensuring all keys are present."""
    # Define the default structure with all expected keys and their initial values
    data = {
        'tasks': {},
        'notes': {},
        'timer_data': {},
        'jobs_applied_daily': {}, # Ensure this key is always initialized as a dictionary
        'tryhackme_rooms_completed': 0,
        'tryhackme_points_gained': 0
    }
    
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                loaded_data = json.load(f)
                # Update the default structure with any loaded data.
                # This ensures existing data is kept, but missing keys are added with defaults.
                data.update(loaded_data)
                
                # Explicitly ensure nested dictionaries are indeed dictionaries,
                # in case a corrupted or malformed file changed their type.
                if not isinstance(data.get('tasks'), dict):
                    data['tasks'] = {}
                if not isinstance(data.get('notes'), dict):
                    data['notes'] = {}
                if not isinstance(data.get('timer_data'), dict):
                    data['timer_data'] = {}
                if not isinstance(data.get('jobs_applied_daily'), dict):
                    data['jobs_applied_daily'] = {}

        except json.JSONDecodeError:
            # Handle cases where the JSON file is corrupted or malformed
            st.error("Error loading data file. It might be corrupted. Starting with fresh data.")
            # Optionally, remove the corrupted file so it doesn't cause issues on next run
            if os.path.exists(DATA_FILE):
                os.remove(DATA_FILE)
        except Exception as e:
            # Catch any other unexpected errors during file loading
            st.error(f"An unexpected error occurred while loading data: {e}. Starting with fresh data.")
            if os.path.exists(DATA_FILE):
                os.remove(DATA_FILE)
    return data

def save_data(data):
    """Saves sprint data to a JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# --- Initialize Session State and Load Data ---
if 'sprint_data' not in st.session_state:
    st.session_state.sprint_data = load_data()

# --- Daily Task Definitions (Highly Condensed for 1 hour/day & 25 jobs/week) ---
daily_tasks_template = {
    # Week 1: Foundations & Initial Momentum (Days 1-7)
    1: {
        "date": SPRINT_START_DATE,
        "tasks": [
            {"desc": "Google Cert: Foundations of Cybersecurity (Course 1) - Week 1, Module 1 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 1-2) - Threats, Attacks, Vulnerabilities", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Intro to Cyber Security (Part 1)", "type": "TryHackMe"},
        ]
    },
    2: {
        "date": SPRINT_START_DATE + timedelta(days=1),
        "tasks": [
            {"desc": "Google Cert: Foundations of Cybersecurity (Course 1) - Week 1, Module 2 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 3-4) - Threats, Attacks, Vulnerabilities", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Intro to Cyber Security (Part 2)", "type": "TryHackMe"},
        ]
    },
    3: {
        "date": SPRINT_START_DATE + timedelta(days=2),
        "tasks": [
            {"desc": "Google Cert: Foundations of Cybersecurity (Course 1) - Week 2, Module 1 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 5-6) - Threats, Attacks, Vulnerabilities", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Network Fundamentals (Part 1)", "type": "TryHackMe"},
        ]
    },
    4: {
        "date": SPRINT_START_DATE + timedelta(days=3),
        "tasks": [
            {"desc": "Google Cert: Foundations of Cybersecurity (Course 1) - Week 2, Module 2 (Video/Reading) (Aim to finish C1)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 7-8) - Threats, Attacks, Vulnerabilities", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Network Fundamentals (Part 2)", "type": "TryHackMe"},
        ]
    },
    5: {
        "date": SPRINT_START_DATE + timedelta(days=4),
        "tasks": [
            {"desc": "Google Cert: Play It Safe: Manage Security Risks (Course 2) - Week 1, Module 1 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Review Domain 1 concepts & practice questions", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Linux Fundamentals Part 1 (Part 1)", "type": "TryHackMe"},
        ]
    },
    6: {
        "date": SPRINT_START_DATE + timedelta(days=5),
        "tasks": [
            {"desc": "Google Cert: Play It Safe: Manage Security Risks (Course 2) - Week 1, Module 2 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 9-10) - Architecture & Design", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Linux Fundamentals Part 1 (Part 2)", "type": "TryHackMe"},
        ]
    },
    7: {
        "date": SPRINT_START_DATE + timedelta(days=6),
        "tasks": [
            {"desc": "Google Cert: Play It Safe: Manage Security Risks (Course 2) - Week 2, Module 1 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 11-12) - Architecture & Design", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Windows Fundamentals 1 (Part 1)", "type": "TryHackMe"},
            {"desc": "Weekly Review: Catch-up on any missed tasks", "type": "Review"}
        ]
    },
    # Week 2: Deep Dive & Practical Application (Days 8-14)
    8: {
        "date": SPRINT_START_DATE + timedelta(days=7),
        "tasks": [
            {"desc": "Google Cert: Play It Safe: Manage Security Risks (Course 2) - Week 2, Module 2 (Video/Reading) (Aim to finish C2)", "type": "Google Cert"},
            {"desc": "Security+: Review Domain 2 concepts & practice questions", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Windows Fundamentals 1 (Part 2)", "type": "TryHackMe"},
        ]
    },
    9: {
        "date": SPRINT_START_DATE + timedelta(days=8),
        "tasks": [
            {"desc": "Google Cert: Protect Company Assets: Data, Devices, and Vulnerabilities (Course 3) - Week 1, Module 1 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 13-14) - Implementation", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Linux Fundamentals Part 2 (Part 1)", "type": "TryHackMe"},
        ]
    },
    10: {
        "date": SPRINT_START_DATE + timedelta(days=9),
        "tasks": [
            {"desc": "Google Cert: Protect Company Assets: Data, Devices, and Vulnerabilities (Course 3) - Week 1, Module 2 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 15-16) - Implementation", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Linux Fundamentals Part 2 (Part 2)", "type": "TryHackMe"},
        ]
    },
    11: {
        "date": SPRINT_START_DATE + timedelta(days=10),
        "tasks": [
            {"desc": "Google Cert: Protect Company Assets: Data, Devices, and Vulnerabilities (Course 3) - Week 2, Module 1 (Video/Reading) (Aim to finish C3)", "type": "Google Cert"},
            {"desc": "Security+: Review Domain 3 concepts & practice questions", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Windows Fundamentals 2 (Part 1)", "type": "TryHackMe"},
        ]
    },
    12: {
        "date": SPRINT_START_DATE + timedelta(days=11),
        "tasks": [
            {"desc": "Google Cert: Become a Cybersecurity Analyst (Course 4) - Week 1, Module 1 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 17-18) - Operations & Incident Response", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Windows Fundamentals 2 (Part 2)", "type": "TryHackMe"},
        ]
    },
    13: {
        "date": SPRINT_START_DATE + timedelta(days=12),
        "tasks": [
            {"desc": "Google Cert: Become a Cybersecurity Analyst (Course 4) - Week 1, Module 2 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 19-20) - Operations & Incident Response", "type": "Security+"},
            {"desc": "TryHackMe: Intro to Cyber Defense (Part 1)", "type": "TryHackMe"},
        ]
    },
    14: {
        "date": SPRINT_START_DATE + timedelta(days=13),
        "tasks": [
            {"desc": "Google Cert: Become a Cybersecurity Analyst (Course 4) - Week 2, Module 1 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Review Domain 4 concepts & practice questions", "type": "Security+"},
            {"desc": "TryHackMe: Intro to Cyber Defense (Part 2)", "type": "TryHackMe"},
            {"desc": "Weekly Review: Catch-up on any missed tasks", "type": "Review"}
        ]
    },
    # Week 3: Incident Response & Governance (Days 15-21)
    15: {
        "date": SPRINT_START_DATE + timedelta(days=14),
        "tasks": [
            {"desc": "Google Cert: Become a Cybersecurity Analyst (Course 4) - Week 2, Module 2 (Video/Reading) (Aim to finish C4)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 21-22) - Governance, Risk, Compliance", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Blue Team (Part 1)", "type": "TryHackMe"},
        ]
    },
    16: {
        "date": SPRINT_START_DATE + timedelta(days=15),
        "tasks": [
            {"desc": "Google Cert: Put It to the Test: Blue Team Practices (Course 5) - Week 1, Module 1 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Review Domain 5 concepts & practice questions", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Blue Team (Part 2)", "type": "TryHackMe"},
        ]
    },
    17: {
        "date": SPRINT_START_DATE + timedelta(days=16),
        "tasks": [
            {"desc": "Google Cert: Put It to the Test: Blue Team Practices (Course 5) - Week 1, Module 2 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Take a short practice quiz (all domains)", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating Windows (Part 1)", "type": "TryHackMe"},
        ]
    },
    18: {
        "date": SPRINT_START_DATE + timedelta(days=17),
        "tasks": [
            {"desc": "Google Cert: Put It to the Test: Blue Team Practices (Course 5) - Week 2, Module 1 (Video/Reading) (Aim to finish C5)", "type": "Google Cert"},
            {"desc": "Security+: Review weakest areas from practice quiz", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating Windows (Part 2)", "type": "TryHackMe"},
        ]
    },
    19: {
        "date": SPRINT_START_DATE + timedelta(days=18),
        "tasks": [
            {"desc": "Google Cert: Respond to Threats and Defend Systems (Course 6) - Week 1, Module 1 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 23-24) - General Review/Deep Dive", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating Linux (Part 1)", "type": "TryHackMe"},
        ]
    },
    20: {
        "date": SPRINT_START_DATE + timedelta(days=19),
        "tasks": [
            {"desc": "Google Cert: Respond to Threats and Defend Systems (Course 6) - Week 1, Module 2 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 25-26) - General Review/Deep Dive", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating Linux (Part 2)", "type": "TryHackMe"},
        ]
    },
    21: {
        "date": SPRINT_START_DATE + timedelta(days=20),
        "tasks": [
            {"desc": "Google Cert: Respond to Threats and Defend Systems (Course 6) - Week 2, Module 1 (Video/Reading) (Aim to finish C6)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 27-28) - General Review/Deep Dive", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating with Splunk (Part 1)", "type": "TryHackMe"},
            {"desc": "Weekly Review: Catch-up on any missed tasks", "type": "Review"}
        ]
    },
    # Week 4: Certification Finalization & Job Search Acceleration (Days 22-28)
    22: {
        "date": SPRINT_START_DATE + timedelta(days=21),
        "tasks": [
            {"desc": "Google Cert: Automate Cybersecurity Tasks with Python (Course 7) - Week 1, Module 1 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 29-30) - General Review/Deep Dive", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating with Splunk (Part 2)", "type": "TryHackMe"},
        ]
    },
    23: {
        "date": SPRINT_START_DATE + timedelta(days=22),
        "tasks": [
            {"desc": "Google Cert: Automate Cybersecurity Tasks with Python (Course 7) - Week 1, Module 2 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 31-32) - General Review/Deep Dive", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating with Splunk (Part 3)", "type": "TryHackMe"},
        ]
    },
    24: {
        "date": SPRINT_START_DATE + timedelta(days=23),
        "tasks": [
            {"desc": "Google Cert: Automate Cybersecurity Tasks with Python (Course 7) - Week 2, Module 1 (Video/Reading) (Aim to finish C7)", "type": "Google Cert"},
            {"desc": "Security+: Take a full-length practice exam (if available)", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating with Splunk (Part 4)", "type": "TryHackMe"},
        ]
    },
    25: {
        "date": SPRINT_START_DATE + timedelta(days=24),
        "tasks": [
            {"desc": "Google Cert: Capstone: Apply Your Skills with a Cybersecurity Project (Course 8) - Week 1, Module 1 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Focus on weakest areas from practice exam", "type": "Security+"},
            {"desc": "TryHackMe: Explore a new tool or concept (e.g., Nmap basics)", "type": "TryHackMe"},
        ]
    },
    26: {
        "date": SPRINT_START_DATE + timedelta(days=25),
        "tasks": [
            {"desc": "Google Cert: Capstone: Apply Your Skills with a Cybersecurity Project (Course 8) - Week 1, Module 2 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Quick review of all acronyms, port numbers, and common tools", "type": "Security+"},
            {"desc": "TryHackMe: Complete a new room or a CTF challenge (easy level)", "type": "TryHackMe"},
        ]
    },
    27: {
        "date": SPRINT_START_DATE + timedelta(days=26),
        "tasks": [
            {"desc": "Google Cert: Capstone: Apply Your Skills with a Cybersecurity Project (Course 8) - Week 2, Module 1 (Video/Reading) (Aim to finish C8 & Google Cert!)", "type": "Google Cert"},
            {"desc": "Security+: Practice performance-based questions (PBQs) concepts", "type": "Security+"},
            {"desc": "TryHackMe: Revisit a foundational room to solidify knowledge", "type": "TryHackMe"},
        ]
    },
    28: {
        "date": SPRINT_START_DATE + timedelta(days=27),
        "tasks": [
            {"desc": "Google Cert: Final review for Google Cert concepts", "type": "Google Cert"},
            {"desc": "Security+: Final quick review of key concepts across all domains", "type": "Security+"},
            {"desc": "TryHackMe: Explore a room related to your weakest Security+ domain", "type": "TryHackMe"},
            {"desc": "Weekly Review: Catch-up on any missed tasks", "type": "Review"}
        ]
    },
    # Week 5: Security+ Consolidation & Job Application Push (Days 29-35)
    29: {
        "date": SPRINT_START_DATE + timedelta(days=28),
        "tasks": [
            {"desc": "Security+: Mentally prepare for the exam, light review only", "type": "Security+"},
            {"desc": "TryHackMe: Complete one final room you enjoy and can explain well", "type": "TryHackMe"},
            {"desc": "Job Search: Research visa sponsorship policies (if applicable)", "type": "Job Search"},
        ]
    },
    30: {
        "date": SPRINT_START_DATE + timedelta(days=29),
        "tasks": [
            {"desc": "Security+: Review all acronyms, port numbers, and common tools", "type": "Security+"},
            {"desc": "TryHackMe: Document your favorite TryHackMe rooms/learnings for LinkedIn", "type": "TryHackMe"},
            {"desc": "Networking: Send 1-2 LinkedIn connection requests to cybersecurity professionals", "type": "Job Search"},
        ]
    },
    31: {
        "date": SPRINT_START_DATE + timedelta(days=30),
        "tasks": [
            {"desc": "Security+: Take another full-length practice exam", "type": "Security+"},
            {"desc": "TryHackMe: Begin 'Cyber Security 101' path (if not already done)", "type": "TryHackMe"},
            {"desc": "Job Search: Review common cybersecurity interview questions", "type": "Job Search"},
        ]
    },
    32: {
        "date": SPRINT_START_DATE + timedelta(days=31),
        "tasks": [
            {"desc": "Security+: Focus on weakest areas from practice exam results", "type": "Security+"},
            {"desc": "TryHackMe: Continue 'Cyber Security 101' path", "type": "TryHackMe"},
            {"desc": "Job Search: Tailor resume/cover letter for 1 specific role", "type": "Job Search"},
        ]
    },
    33: {
        "date": SPRINT_START_DATE + timedelta(days=32),
        "tasks": [
            {"desc": "Security+: Final intensive review of all domains", "type": "Security+"},
            {"desc": "TryHackMe: Continue 'Cyber Security 101' path", "type": "TryHackMe"},
            {"desc": "Job Search: Update LinkedIn profile with Google Cert & TryHackMe progress", "type": "Job Search"},
        ]
    },
    34: {
        "date": SPRINT_START_DATE + timedelta(days=33),
        "tasks": [
            {"desc": "Security+: Light review before the exam (if scheduling soon)", "type": "Security+"},
            {"desc": "TryHackMe: Continue 'Cyber Security 101' path", "type": "TryHackMe"},
            {"desc": "Job Search: Actively search for roles on multiple job boards", "type": "Job Search"},
        ]
    },
    35: {
        "date": SPRINT_START_DATE + timedelta(days=34),
        "tasks": [
            {"desc": "Security+: Prepare for Security+ exam within the next 1-2 weeks (post-sprint)", "type": "Security+"},
            {"desc": "TryHackMe: Begin 'Security Engineer' path", "type": "TryHackMe"},
            {"desc": "Job Search: Identify 1-2 target companies for direct applications", "type": "Job Search"},
            {"desc": "Weekly Review: Catch-up on any missed tasks", "type": "Review"}
        ]
    },
    # Week 6: Continued Learning & Job Search Focus (Days 36-42)
    36: {
        "date": SPRINT_START_DATE + timedelta(days=35),
        "tasks": [
            {"desc": "TryHackMe: Continue 'Security Engineer' path", "type": "TryHackMe"},
            {"desc": "Job Search: Tailor resume/cover letter for a specific job", "type": "Job Search"},
            {"desc": "Networking: Follow up on any previous connections", "type": "Job Search"},
        ]
    },
    37: {
        "date": SPRINT_START_DATE + timedelta(days=36),
        "tasks": [
            {"desc": "TryHackMe: Explore another room from 'Cyber Security 101' or 'SOC Level 1'", "type": "TryHackMe"},
            {"desc": "Job Search: Actively search for roles on multiple job boards", "type": "Job Search"},
        ]
    },
    38: {
        "date": SPRINT_START_DATE + timedelta(days=37),
        "tasks": [
            {"desc": "TryHackMe: Begin a new path (e.g., 'CompTIA Pentest+ Prep' if interested)", "type": "TryHackMe"},
            {"desc": "Job Search: Update LinkedIn profile with any new skills/rooms completed", "type": "Job Search"},
        ]
    },
    39: {
        "date": SPRINT_START_DATE + timedelta(days=38),
        "tasks": [
            {"desc": "TryHackMe: Continue new path/explore more rooms", "type": "TryHackMe"},
            {"desc": "Job Search: Research common cybersecurity interview questions (technical focus)", "type": "Job Search"},
        ]
    },
    40: {
        "date": SPRINT_START_DATE + timedelta(days=39),
        "tasks": [
            {"desc": "TryHackMe: Focus on a specific tool (e.g., Wireshark basics, Metasploit intro)", "type": "TryHackMe"},
            {"desc": "Job Search: Identify 1-2 more target companies for direct applications", "type": "Job Search"},
            {"desc": "Networking: Send 1-2 more LinkedIn connection requests", "type": "Job Search"},
        ]
    },
    41: {
        "date": SPRINT_START_DATE + timedelta(days=40),
        "tasks": [
            {"desc": "TryHackMe: Complete a relevant CTF or challenge room (easy/medium)", "type": "TryHackMe"},
            {"desc": "Job Search: Actively search for roles on multiple job boards", "type": "Job Search"},
        ]
    },
    42: {
        "date": SPRINT_START_DATE + timedelta(days=41),
        "tasks": [
            {"desc": "TryHackMe: Review favorite rooms/concepts and summarize key takeaways", "type": "TryHackMe"},
            {"desc": "Job Search: Review all applications sent and plan follow-up strategy", "type": "Job Search"},
            {"desc": "Weekly Review: Catch-up on any missed tasks", "type": "Review"}
        ]
    },
    # Week 7: Advanced Concepts & Application Refinement (Days 43-49)
    43: {
        "date": SPRINT_START_DATE + timedelta(days=42),
        "tasks": [
            {"desc": "Explore a new cybersecurity topic (e.g., cloud security fundamentals, reverse engineering basics)", "type": "Other Learning"},
            {"desc": "Job Search: Tailor resume/cover letter for another specific job", "type": "Job Search"},
        ]
    },
    44: {
        "date": SPRINT_START_DATE + timedelta(days=43),
        "tasks": [
            {"desc": "Research advanced cybersecurity certifications (e.g., CySA+, GSEC)", "type": "Future Planning"},
            {"desc": "Job Search: Actively search for roles on multiple job boards", "type": "Job Search"},
        ]
    },
    45: {
        "date": SPRINT_START_DATE + timedelta(days=44),
        "tasks": [
            {"desc": "Participate in an online cybersecurity webinar or workshop", "type": "Other Learning"},
            {"desc": "Job Search: Update LinkedIn profile with any new learning/certifications", "type": "Job Search"},
        ]
    },
    46: {
        "date": SPRINT_START_DATE + timedelta(days=45),
        "tasks": [
            {"desc": "Read a cybersecurity blog or article on a recent threat", "type": "Other Learning"},
            {"desc": "Job Search: Research companies known for hiring entry-level cyber talent", "type": "Job Search"},
            {"desc": "Networking: Send 1-2 more LinkedIn connection requests", "type": "Job Search"},
        ]
    },
    47: {
        "date": SPRINT_START_DATE + timedelta(days=46),
        "tasks": [
            {"desc": "Explore a new open-source cybersecurity tool (e.g., OSINT tools)", "type": "Other Learning"},
            {"desc": "Job Search: Prepare for potential interview questions (behavioral)", "type": "Job Search"},
        ]
    },
    48: {
        "date": SPRINT_START_DATE + timedelta(days=47),
        "tasks": [
            {"desc": "Review notes from Google Cert or Security+ for areas needing reinforcement", "type": "Review"},
            {"desc": "Job Search: Actively search for roles on multiple job boards", "type": "Job Search"},
        ]
    },
    49: {
        "date": SPRINT_START_DATE + timedelta(days=48),
        "tasks": [
            {"desc": "Summarize key learnings from the past week's exploration", "type": "Review"},
            {"desc": "Job Search: Review all applications sent and plan follow-up strategy", "type": "Job Search"},
            {"desc": "Weekly Review: Catch-up on any missed tasks", "type": "Review"}
        ]
    },
    # Week 8: Final Sprint & Future Planning (Days 50-56)
    50: {
        "date": SPRINT_START_DATE + timedelta(days=49),
        "tasks": [
            {"desc": "Job Search: Final check for new relevant job postings", "type": "Job Search"},
            {"desc": "Networking: Send thank you notes/follow-ups to any connections made", "type": "Job Search"},
        ]
    },
    51: {
        "date": SPRINT_START_DATE + timedelta(days=50),
        "tasks": [
            {"desc": "Job Search: Review all applications sent and plan follow-up strategy", "type": "Job Search"},
            {"desc": "Future Planning: Set goals for the next 30-60 days of learning", "type": "Future Planning"},
        ]
    },
    52: {
        "date": SPRINT_START_DATE + timedelta(days=51),
        "tasks": [
            {"desc": "Prepare for Security+ exam within the next 1-2 weeks (post-sprint)", "type": "Security+"},
            {"desc": "Job Search: Update resume/LinkedIn with all new certifications and skills", "type": "Job Search"},
        ]
    },
    53: {
        "date": SPRINT_START_DATE + timedelta(days=52),
        "tasks": [
            {"desc": "Sprint Retrospective: What went well, what to improve?", "type": "Review"},
            {"desc": "Job Search: Research common cybersecurity interview questions (behavioral & technical)", "type": "Job Search"},
        ]
    },
    54: {
        "date": SPRINT_START_DATE + timedelta(days=53),
        "tasks": [
            {"desc": "Review your daily notes and highlight key insights or challenges faced", "type": "Review"},
            {"desc": "Job Search: Mock interview practice (even with yourself!)", "type": "Job Search"},
        ]
    },
    55: {
        "date": SPRINT_START_DATE + timedelta(days=54),
        "tasks": [
            {"desc": "Consolidate all learning resources for future reference", "type": "Review"},
            {"desc": "Job Search: Actively search for roles on multiple job boards", "type": "Job Search"},
            {"desc": "Networking: Plan ongoing networking activities for post-sprint", "type": "Job Search"},
        ]
    },
    56: {
        "date": SPRINT_START_DATE + timedelta(days=55),
        "tasks": [
            {"desc": "Final review of your career launch strategy", "type": "Review"},
            {"desc": "Job Search: Send any last applications or follow-ups for the sprint", "type": "Job Search"},
            {"desc": "Weekly Review: Catch-up on any missed tasks", "type": "Review"}
        ]
    },
    # Final Days: Consolidation & Celebration (Days 57-60)
    57: {
        "date": SPRINT_START_DATE + timedelta(days=56),
        "tasks": [
            {"desc": "Review all completed TryHackMe rooms and concepts", "type": "TryHackMe"},
            {"desc": "Job Search: Prepare for potential interviews next week", "type": "Job Search"},
        ]
    },
    58: {
        "date": SPRINT_START_DATE + timedelta(days=57),
        "tasks": [
            {"desc": "Review all completed Google Cert modules", "type": "Google Cert"},
            {"desc": "Job Search: Continue applying to relevant positions if needed", "type": "Job Search"},
        ]
    },
    59: {
        "date": SPRINT_START_DATE + timedelta(days=58),
        "tasks": [
            {"desc": "Review all Security+ domains for areas of strength and weakness", "type": "Security+"},
            {"desc": "Job Search: Update your professional network on your sprint completion", "type": "Job Search"},
        ]
    },
    60: {
        "date": SPRINT_START_DATE + timedelta(days=59),
        "tasks": [
            {"desc": "🎉 CELEBRATE! You've completed an incredible 60-day sprint!", "type": "Motivation"},
            {"desc": "Update LinkedIn with your Google Cert and TryHackMe progress", "type": "Job Search"},
            {"desc": "Take a well-deserved break and recharge!", "type": "Motivation"}
        ]
    },
}

# --- Initialize or update sprint_data for new features ---
# This loop now relies on the robust load_data() to ensure top-level keys exist.
for day, day_info in daily_tasks_template.items():
    day_str = str(day)
    # Ensure nested structures for each day are initialized if they don't exist
    st.session_state.sprint_data['tasks'].setdefault(day_str, [
        {'desc': task['desc'], 'type': task['type'], 'completed': False}
        for task in day_info['tasks']
    ])
    st.session_state.sprint_data['notes'].setdefault(day_str, "")
    st.session_state.sprint_data['timer_data'].setdefault(day_str, {'start_time': None, 'elapsed_time': 0})
    st.session_state.sprint_data['jobs_applied_daily'].setdefault(day_str, 0)


# --- Streamlit App Layout ---
st.set_page_config(layout="wide", page_title="Cybersecurity 60-Day Sprint Dashboard 🚀")

st.markdown("""
    <style>
    .big-font {
        font-size:30px !important;
        font-weight: bold;
    }
    .medium-font {
        font-size:20px !important;
    }
    .stProgress > div > div > div > div {
        background-color: #6a0dad; /* A nice purple */
    }
    .stButton>button {
        background-color: #4CAF50; /* Green */
        color: white;
        padding: 10px 24px;
        border-radius: 8px;
        border: none;
        cursor: pointer;
        font-size: 16px;
    }
    .stButton>button:hover {
        background-color: #45a049;
    }
    </style>
    """, unsafe_allow_html=True)

st.title("🚀 Your Cybersecurity 60-Day Sprint Dashboard 🚀")
st.markdown("---")

# --- Calculate Current Day ---
today = date.today()
current_sprint_day = (today - SPRINT_START_DATE).days + 1

if current_sprint_day < 1:
    st.info(f"✨ Your intensive sprint officially kicks off on **{SPRINT_START_DATE.strftime('%B %d, %Y')}**! Let's get ready! ✨")
    current_sprint_day = 1
elif current_sprint_day > TOTAL_SPRINT_DAYS:
    st.balloons()
    st.success(f"🎉 **CONGRATULATIONS! You've successfully completed your {TOTAL_SPRINT_DAYS}-day sprint!** 🎉")
    st.markdown("<p class='big-font' style='text-align: center; color: #4CAF50;'>You've crushed it! What an achievement! 💪</p>", unsafe_allow_html=True)
    current_sprint_day = TOTAL_SPRINT_DAYS

# --- Day Selection ---
selected_day_col1, selected_day_col2 = st.columns([0.7, 0.3])
with selected_day_col1:
    selected_day_option = st.selectbox(
        "### 🗓️ Select Your Sprint Day:",
        options=[f"Day {d}" for d in range(1, TOTAL_SPRINT_DAYS + 1)],
        index=min(current_sprint_day - 1, TOTAL_SPRINT_DAYS - 1),
        key="day_selector"
    )
selected_day_num = int(selected_day_option.split(" ")[1])
selected_day_str = str(selected_day_num)

with selected_day_col2:
    st.markdown(f"<p class='big-font' style='text-align: center; margin-top: 20px;'>Day {selected_day_num} of {TOTAL_SPRINT_DAYS}</p>", unsafe_allow_html=True)
    st.markdown(f"<p style='text-align: center; font-size: 18px;'>{daily_tasks_template[selected_day_num]['date'].strftime('%B %d, %Y')}</p>", unsafe_allow_html=True)

st.markdown("---")

# --- Overall Sprint Progress ---
total_tasks_count = sum(len(daily_tasks_template[day]['tasks']) for day in range(1, TOTAL_SPRINT_DAYS + 1))
completed_tasks_count = 0
for day_str_key in st.session_state.sprint_data['tasks']:
    for task_obj in st.session_state.sprint_data['tasks'][day_str_key]:
        if task_obj['completed']:
            completed_tasks_count += 1

overall_progress_percentage = (completed_tasks_count / total_tasks_count) * 100 if total_tasks_count > 0 else 0
st.markdown(f"### 📈 Overall Sprint Progress: {overall_progress_percentage:.1f}%")
st.progress(overall_progress_percentage / 100, text=f"**You're making great strides!**")

if overall_progress_percentage < 25:
    st.info("Keep that momentum going! Every single task moves you closer to your goal. 💪")
elif 25 <= overall_progress_percentage < 50:
    st.warning("Halfway to the finish line! You're building an incredible foundation. Stay consistent! ⚡")
elif 50 <= overall_progress_percentage < 75:
    st.success("Over the peak! The end is in sight. Push through these crucial days! 🚀")
else:
    st.success("Final stretch! You're a cybersecurity force of nature. Finish strong! ✨")

st.markdown("---")

# --- Categorized Progress Bars ---
st.subheader("📊 Progress by Pillar:")

# Calculate progress for each category
category_progress = {
    "Google Cert": {"completed": 0, "total": 0},
    "Security+": {"completed": 0, "total": 0},
    "TryHackMe": {"completed": 0, "total": 0},
    "Job Search Task": {"completed": 0, "total": 0}, # For Job Search tasks within daily plan
    "Other Learning": {"completed": 0, "total": 0},
    "Review": {"completed": 0, "total": 0},
    "Future Planning": {"completed": 0, "total": 0},
    "Motivation": {"completed": 0, "total": 0},
}

for day_str_key in st.session_state.sprint_data['tasks']:
    for task_obj in st.session_state.sprint_data['tasks'][day_str_key]:
        task_type = task_obj['type']
        if task_type in category_progress:
            category_progress[task_type]["total"] += 1
            if task_obj['completed']:
                category_progress[task_type]["completed"] += 1

# Display categorized progress
progress_cols = st.columns(4)

categories_to_display = ["Google Cert", "Security+", "TryHackMe"] # Focus on core three

for i, category in enumerate(categories_to_display):
    with progress_cols[i % 4]:
        completed = category_progress[category]["completed"]
        total = category_progress[category]["total"]
        percent = (completed / total) * 100 if total > 0 else 0
        st.markdown(f"**{category}:** {percent:.1f}%")
        st.progress(percent / 100)

# Job Applications specific progress
total_jobs_applied_overall = sum(st.session_state.sprint_data['jobs_applied_daily'].values())
job_application_target_overall = JOB_APPLICATIONS_PER_WEEK_TARGET * TOTAL_SPRINT_WEEKS
job_app_percent = (total_jobs_applied_overall / job_application_target_overall) * 100 if job_application_target_overall > 0 else 0

with progress_cols[len(categories_to_display) % 4]: # Place in next available column
    st.markdown(f"**Job Applications:** {job_app_percent:.1f}%")
    st.progress(job_app_percent / 100)

st.markdown("---")

# --- Daily Task Management ---
st.header("📝 Daily Tasks & Check-offs:")
st.markdown(f"<p class='medium-font'>Here are your focus tasks for <b>{selected_day_option}</b>. Check them off as you complete them!</p>", unsafe_allow_html=True)
        
# Display tasks for the selected day
for i, task in enumerate(st.session_state.sprint_data['tasks'][selected_day_str]):
    checkbox_key = f"day_{selected_day_str}_task_{i}"
    
    task_col1, task_col2 = st.columns([0.15, 0.85]) # Adjust column width for type and description
    with task_col1:
        st.markdown(f"<span style='font-weight: bold; color: #4B0082;'>{task['type']}</span>", unsafe_allow_html=True)
    with task_col2:
        checked = st.checkbox(
            task['desc'], 
            value=task['completed'], 
            key=checkbox_key
        )
        if checked != task['completed']:
            st.session_state.sprint_data['tasks'][selected_day_str][i]['completed'] = checked
            save_data(st.session_state.sprint_data)
            st.rerun()

st.markdown("---")

# --- Job Application Tracker ---
st.header("💼 Job Application Tracker:")

# Input for jobs applied today
current_jobs_applied_today = st.session_state.sprint_data['jobs_applied_daily'].get(selected_day_str, 0)
new_jobs_applied_today = st.number_input(
    f"🚀 Jobs Applied Today ({selected_day_option}):",
    min_value=0,
    value=current_jobs_applied_today,
    step=1,
    key=f"jobs_applied_today_{selected_day_str}"
)
if new_jobs_applied_today != current_jobs_applied_today:
    st.session_state.sprint_data['jobs_applied_daily'][selected_day_str] = new_jobs_applied_today
    save_data(st.session_state.sprint_data)
    st.toast("Daily job applications updated!")

# Calculate jobs applied this week
current_week_num = (selected_day_num - 1) // 7
jobs_this_week = 0
for d in range(current_week_num * 7 + 1, min((current_week_num + 1) * 7 + 1, TOTAL_SPRINT_DAYS + 1)):
    jobs_this_week += st.session_state.sprint_data['jobs_applied_daily'].get(str(d), 0)

# Display weekly and overall totals
job_tracker_col1, job_tracker_col2 = st.columns(2)
with job_tracker_col1:
    st.markdown(f"<p class='medium-font'>🎯 <b>Jobs Applied This Week:</b> <span style='font-size: 24px; font-weight: bold; color: #8A2BE2;'>{jobs_this_week}</span> / {JOB_APPLICATIONS_PER_WEEK_TARGET}</p>", unsafe_allow_html=True)
    if jobs_this_week >= JOB_APPLICATIONS_PER_WEEK_TARGET:
        st.success("🎉 You've hit your weekly job application goal! Fantastic!")
    else:
        st.info(f"Keep pushing! You need {JOB_APPLICATIONS_PER_WEEK_TARGET - jobs_this_week} more applications this week.")
with job_tracker_col2:
    st.markdown(f"<p class='medium-font'>🌐 <b>Total Jobs Applied Overall:</b> <span style='font-size: 24px; font-weight: bold; color: #8A2BE2;'>{total_jobs_applied_overall}</span></p>", unsafe_allow_html=True)
    st.caption(f"Aiming for ~{JOB_APPLICATIONS_PER_WEEK_TARGET * TOTAL_SPRINT_WEEKS} by end of sprint.")

st.markdown("---")

# --- Timer for Focused Work Sessions ---
st.header("⏰ Focus Timer:")
st.markdown("<p class='medium-font'>Use this to track your dedicated study time for <b>{selected_day_option}</b>.</p>", unsafe_allow_html=True)

timer_data = st.session_state.sprint_data['timer_data'][selected_day_str]
        
timer_col1, timer_col2, timer_col3 = st.columns([0.3, 0.3, 0.4])
        
with timer_col1:
    if st.button("▶️ Start Timer", key=f"start_timer_{selected_day_str}"):
        timer_data['start_time'] = time.time()
        save_data(st.session_state.sprint_data)
        st.toast("Timer started! Focus up! ⚡")
        
with timer_col2:
    if st.button("⏹️ Stop Timer", key=f"stop_timer_{selected_day_str}"):
        if timer_data['start_time'] is not None:
            elapsed = time.time() - timer_data['start_time']
            timer_data['elapsed_time'] += elapsed
            timer_data['start_time'] = None # Reset start time
            save_data(st.session_state.sprint_data)
            st.toast(f"Timer stopped! Added {elapsed:.0f} seconds to your session.")
        else:
            st.warning("Timer not active. Press 'Start Timer' first.")

with timer_col3:
    total_seconds = timer_data['elapsed_time']
    hours = int(total_seconds // 3600)
    minutes = int((total_seconds % 3600) // 60)
    seconds = int(total_seconds % 60)
    st.markdown(f"<p class='medium-font'>Total Focus Time: <b>{hours:02d}h {minutes:02d}m {seconds:02d}s</b></p>", unsafe_allow_html=True)

st.markdown("---")

# --- Daily Notes & Reflections ---
st.header("✍️ Daily Notes & Reflections:")
st.markdown("<p class='medium-font'>Jot down your key learnings, challenges, or thoughts for <b>{selected_day_option}</b>.</p>", unsafe_allow_html=True)
        
current_notes = st.session_state.sprint_data['notes'][selected_day_str]
new_notes = st.text_area(
    "What did you learn today? What challenges did you face?",
    value=current_notes,
    height=200,
    key=f"notes_day_{selected_day_str}"
)
if new_notes != current_notes:
    st.session_state.sprint_data['notes'][selected_day_str] = new_notes
    save_data(st.session_state.sprint_data)
    st.toast("Notes saved successfully! 📝")

st.markdown("---")

# --- TryHackMe Quantifiable Progress ---
st.header("🎮 TryHackMe Progress:")
st.markdown("<p class='medium-font'>Keep track of your hands-on achievements on TryHackMe!</p>", unsafe_allow_html=True)

thm_col1, thm_col2 = st.columns(2)

with thm_col1:
    current_rooms = st.session_state.sprint_data['tryhackme_rooms_completed']
    new_rooms = st.number_input(
        "Total TryHackMe Rooms Completed:",
        min_value=0,
        value=current_rooms,
        step=1,
        key="total_tryhackme_rooms_input"
    )
    if new_rooms != current_rooms:
        st.session_state.sprint_data['tryhackme_rooms_completed'] = new_rooms
        save_data(st.session_state.sprint_data)
        st.toast("TryHackMe rooms updated!")

with thm_col2:
    current_points = st.session_state.sprint_data['tryhackme_points_gained']
    new_points = st.number_input(
        "Total TryHackMe Points Gained:",
        min_value=0,
        value=current_points,
        step=10,
        key="total_tryhackme_points_input"
    )
    if new_points != current_points:
        st.session_state.sprint_data['tryhackme_points_gained'] = new_points
        save_data(st.session_state.sprint_data)
        st.toast("TryHackMe points updated!")

st.markdown("---")

# --- Important Notes & Resources ---
st.header("💡 Important Notes & Key Resources:")
<p class='medium-font'>**Your 60-Day Sprint is INTENSE!**</p>
<p>This schedule is incredibly ambitious. Achieving **{JOB_APPLICATIONS_PER_WEEK_TARGET} job applications per week** (averaging 3-4 per day) within a **1-hour daily limit**, while also making progress on certifications and hands-on labs, will demand **unwavering focus, discipline, and efficiency**.</p>
<p><b>🔑 Key Strategies for Success:</b></p>
<ul>
    <li><b>Job Application Efficiency:</b> Have polished resume/cover letter templates ready. Utilize quick-apply features. Focus on roles requiring minimal customization initially. On high-target days, job search will be the primary focus.</li>
    <li><b>Condensed Learning:</b>
        <ul>
            <li><b>Google Cert:</b> Prioritize videos and quizzes. You may need to skim some readings or rely on official summaries.</li>
            <li><b>Security+:</b> Focus on Professor Messer's core videos for each domain. Defer extensive practice questions to review days or post-sprint.</li>
            <li><b>TryHackMe:</b> Select shorter, high-impact rooms or specific modules that directly reinforce cert concepts or provide demonstrable skills for your profile.</li>
        </ul>
    </li>
    <li><b>Consistency over Perfection:</b> If you miss a task or an application target, don't get discouraged. Adjust and keep moving forward. Every small step counts!</li>
</ul>
<p class='medium-font'><b>🔗 Essential Resource Links:</b></p>
<ul>
    <li><b>Google Cybersecurity Certificate (Coursera):</b> <a href="https://www.coursera.org/professional-certificates/google-cybersecurity" target="_blank">Link</a></li>
    <li><b>Professor Messer (YouTube):</b> <a href="https://www.youtube.com/@professormesser" target="_blank">Search his channel for "Security+ SY0-601" or "SY0-701" playlists</a></li>
    <li><b>TryHackMe:</b> <a href="https://tryhackme.com/" target="_blank">Link</a></li>
    <li><b>Top Job Boards:</b> Indeed, LinkedIn Jobs, Glassdoor, CyberSN, Monster, ZipRecruiter</li>
    <li><b>Networking:</b> LinkedIn is crucial. Explore cybersecurity communities on Discord (e.g., "The Many Hats Club").</li>
    <li><b>General Cybersecurity Resources (for deeper dives):</b> OWASP Top Ten, CVE Database, NIST Cybersecurity Frameworks.</li>
</ul>
<p class='medium-font'><b>🧘‍♂️ Remember Self-Care:</b> This is an intensive sprint. Prioritize rest, healthy eating, and short breaks to avoid burnout and maintain peak performance.</p>
""", unsafe_allow_html=True)

st.markdown("---")

# --- Data Reset Button ---
st.header("🗑️ Reset All Data:")
st.warning("🚨 This will permanently delete ALL your tracked progress (tasks, notes, timer, job apps, TryHackMe data). This cannot be undone!")
if st.button("Permanently Delete All Data", key="reset_all_data_button"):
    st.session_state.sprint_data = {
        'tasks': {},
        'notes': {},
        'timer_data': {},
        'jobs_applied_daily': {},
        'tryhackme_rooms_completed': 0,
        'tryhackme_points_gained': 0
    }
    save_data(st.session_state.sprint_data)
    st.toast("All sprint data has been reset! Starting fresh...")
    st.rerun() # Rerun to reflect the cleared data

st.markdown("---")
st.markdown("<p style='text-align: center; color: gray;'>Designed to empower your cybersecurity career launch. Good luck!</p>", unsafe_allow_html=True)

