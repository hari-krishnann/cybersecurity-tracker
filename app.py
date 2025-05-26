import streamlit as st
from datetime import date, timedelta
import json
import time
import os

# --- Configuration ---
SPRINT_START_DATE = date(2025, 5, 26) # May 26th, 2025
TOTAL_SPRINT_DAYS = 60 # Extended to 60 days
DATA_FILE = 'sprint_data.json'

# --- Helper Functions for Data Persistence ---
def load_data():
    """Loads sprint data from a JSON file."""
    if os.path.exists(DATA_FILE):
        with open(DATA_FILE, 'r') as f:
            return json.load(f)
    return {
        'tasks': {},
        'notes': {},
        'timer_data': {},
        'total_tryhackme_rooms': 0,
        'total_tryhackme_points': 0
    }

def save_data(data):
    """Saves sprint data to a JSON file."""
    with open(DATA_FILE, 'w') as f:
        json.dump(data, f, indent=4)

# --- Initialize Session State and Load Data ---
if 'sprint_data' not in st.session_state:
    st.session_state.sprint_data = load_data()

# --- Daily Task Definitions (Highly Condensed for 1 hour/day) ---
# Each day's tasks are designed to fit within roughly 1 hour.
# Google Cert: ~25-30 minutes
# Security+: ~15-20 minutes
# TryHackMe: ~10-15 minutes
# Job applications/Networking: Integrated less frequently, or as quick check-ins.

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
            {"desc": "Job Search: Update LinkedIn profile summary", "type": "Job Search"}
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
            {"desc": "Google Cert: Foundations of Cybersecurity (Course 1) - Week 2, Module 2 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 7-8) - Threats, Attacks, Vulnerabilities", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Network Fundamentals (Part 2)", "type": "TryHackMe"},
        ]
    },
    5: {
        "date": SPRINT_START_DATE + timedelta(days=4),
        "tasks": [
            {"desc": "Google Cert: Foundations of Cybersecurity (Course 1) - Week 3, Module 1 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Review Domain 1 concepts & practice questions", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Linux Fundamentals Part 1 (Part 1)", "type": "TryHackMe"},
            {"desc": "Job Search: Identify 1-2 target companies/roles", "type": "Job Search"}
        ]
    },
    6: {
        "date": SPRINT_START_DATE + timedelta(days=5),
        "tasks": [
            {"desc": "Google Cert: Foundations of Cybersecurity (Course 1) - Week 3, Module 2 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 9-10) - Architecture & Design", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Linux Fundamentals Part 1 (Part 2)", "type": "TryHackMe"},
        ]
    },
    7: {
        "date": SPRINT_START_DATE + timedelta(days=6),
        "tasks": [
            {"desc": "Google Cert: Foundations of Cybersecurity (Course 1) - Week 4, Module 1 (Video/Reading) (Aim to finish Course 1)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 11-12) - Architecture & Design", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Windows Fundamentals 1 (Part 1)", "type": "TryHackMe"},
            {"desc": "Weekly Review: Catch-up on any missed tasks", "type": "Review"}
        ]
    },
    # Week 2: Deep Dive & Practical Application (Days 8-14)
    8: {
        "date": SPRINT_START_DATE + timedelta(days=7),
        "tasks": [
            {"desc": "Google Cert: Play It Safe: Manage Security Risks (Course 2) - Week 1, Module 1 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 13-14) - Architecture & Design", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Windows Fundamentals 1 (Part 2)", "type": "TryHackMe"},
            {"desc": "Job Search: Apply to 1 entry-level job (quick apply)", "type": "Job Search"}
        ]
    },
    9: {
        "date": SPRINT_START_DATE + timedelta(days=8),
        "tasks": [
            {"desc": "Google Cert: Play It Safe: Manage Security Risks (Course 2) - Week 1, Module 2 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 15-16) - Architecture & Design", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Linux Fundamentals Part 2 (Part 1)", "type": "TryHackMe"},
        ]
    },
    10: {
        "date": SPRINT_START_DATE + timedelta(days=9),
        "tasks": [
            {"desc": "Google Cert: Play It Safe: Manage Security Risks (Course 2) - Week 2, Module 1 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Review Domain 2 concepts & practice questions", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Linux Fundamentals Part 2 (Part 2)", "type": "TryHackMe"},
        ]
    },
    11: {
        "date": SPRINT_START_DATE + timedelta(days=10),
        "tasks": [
            {"desc": "Google Cert: Play It Safe: Manage Security Risks (Course 2) - Week 2, Module 2 (Video/Reading) (Aim to finish Course 2)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 17-18) - Implementation", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Windows Fundamentals 2 (Part 1)", "type": "TryHackMe"},
        ]
    },
    12: {
        "date": SPRINT_START_DATE + timedelta(days=11),
        "tasks": [
            {"desc": "Google Cert: Protect Company Assets: Data, Devices, and Vulnerabilities (Course 3) - Week 1, Module 1 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 19-20) - Implementation", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Windows Fundamentals 2 (Part 2)", "type": "TryHackMe"},
            {"desc": "Job Search: Quick LinkedIn networking (1 connection)", "type": "Job Search"}
        ]
    },
    13: {
        "date": SPRINT_START_DATE + timedelta(days=12),
        "tasks": [
            {"desc": "Google Cert: Protect Company Assets: Data, Devices, and Vulnerabilities (Course 3) - Week 1, Module 2 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 21-22) - Implementation", "type": "Security+"},
            {"desc": "TryHackMe: Intro to Cyber Defense (Part 1)", "type": "TryHackMe"},
        ]
    },
    14: {
        "date": SPRINT_START_DATE + timedelta(days=13),
        "tasks": [
            {"desc": "Google Cert: Protect Company Assets: Data, Devices, and Vulnerabilities (Course 3) - Week 2, Module 1 (Video/Reading) (Aim to finish Course 3)", "type": "Google Cert"},
            {"desc": "Security+: Review Domain 3 concepts & practice questions", "type": "Security+"},
            {"desc": "TryHackMe: Intro to Cyber Defense (Part 2)", "type": "TryHackMe"},
            {"desc": "Weekly Review: Catch-up on any missed tasks", "type": "Review"}
        ]
    },
    # Week 3: Incident Response & Governance (Days 15-21)
    15: {
        "date": SPRINT_START_DATE + timedelta(days=14),
        "tasks": [
            {"desc": "Google Cert: Become a Cybersecurity Analyst (Course 4) - Week 1, Module 1 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 23-24) - Operations & Incident Response", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Blue Team (Part 1)", "type": "TryHackMe"},
            {"desc": "Job Search: Apply to 1 entry-level job (quick apply)", "type": "Job Search"}
        ]
    },
    16: {
        "date": SPRINT_START_DATE + timedelta(days=15),
        "tasks": [
            {"desc": "Google Cert: Become a Cybersecurity Analyst (Course 4) - Week 1, Module 2 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 25-26) - Operations & Incident Response", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Blue Team (Part 2)", "type": "TryHackMe"},
        ]
    },
    17: {
        "date": SPRINT_START_DATE + timedelta(days=16),
        "tasks": [
            {"desc": "Google Cert: Become a Cybersecurity Analyst (Course 4) - Week 2, Module 1 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 27-28) - Operations & Incident Response", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating Windows (Part 1)", "type": "TryHackMe"},
        ]
    },
    18: {
        "date": SPRINT_START_DATE + timedelta(days=17),
        "tasks": [
            {"desc": "Google Cert: Become a Cybersecurity Analyst (Course 4) - Week 2, Module 2 (Video/Reading) (Aim to finish Course 4)", "type": "Google Cert"},
            {"desc": "Security+: Review Domain 4 concepts & practice questions", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating Windows (Part 2)", "type": "TryHackMe"},
            {"desc": "Job Search: Research visa sponsorship policies (quick check)", "type": "Job Search"}
        ]
    },
    19: {
        "date": SPRINT_START_DATE + timedelta(days=18),
        "tasks": [
            {"desc": "Google Cert: Put It to the Test: Blue Team Practices (Course 5) - Week 1, Module 1 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 29-30) - Governance, Risk, Compliance", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating Linux (Part 1)", "type": "TryHackMe"},
        ]
    },
    20: {
        "date": SPRINT_START_DATE + timedelta(days=19),
        "tasks": [
            {"desc": "Google Cert: Put It to the Test: Blue Team Practices (Course 5) - Week 1, Module 2 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 31-32) - Governance, Risk, Compliance", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating Linux (Part 2)", "type": "TryHackMe"},
        ]
    },
    21: {
        "date": SPRINT_START_DATE + timedelta(days=20),
        "tasks": [
            {"desc": "Google Cert: Put It to the Test: Blue Team Practices (Course 5) - Week 2, Module 1 (Video/Reading) (Aim to finish Course 5)", "type": "Google Cert"},
            {"desc": "Security+: Review Domain 5 concepts & practice questions", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating with Splunk (Part 1)", "type": "TryHackMe"},
            {"desc": "Weekly Review: Catch-up on any missed tasks", "type": "Review"}
        ]
    },
    # Week 4: Certification Finalization & Job Search Acceleration (Days 22-28)
    22: {
        "date": SPRINT_START_DATE + timedelta(days=21),
        "tasks": [
            {"desc": "Google Cert: Respond to Threats and Defend Systems (Course 6) - Week 1, Module 1 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 33-34) - General Review/Deep Dive", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating with Splunk (Part 2)", "type": "TryHackMe"},
            {"desc": "Job Search: Apply to 1 entry-level job (quick apply)", "type": "Job Search"}
        ]
    },
    23: {
        "date": SPRINT_START_DATE + timedelta(days=22),
        "tasks": [
            {"desc": "Google Cert: Respond to Threats and Defend Systems (Course 6) - Week 1, Module 2 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 35-36) - General Review/Deep Dive", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating with Splunk (Part 3)", "type": "TryHackMe"},
        ]
    },
    24: {
        "date": SPRINT_START_DATE + timedelta(days=23),
        "tasks": [
            {"desc": "Google Cert: Respond to Threats and Defend Systems (Course 6) - Week 2, Module 1 (Video/Reading) (Aim to finish Course 6)", "type": "Google Cert"},
            {"desc": "Security+: Take a short practice quiz (all domains)", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating with Splunk (Part 4)", "type": "TryHackMe"},
        ]
    },
    25: {
        "date": SPRINT_START_DATE + timedelta(days=24),
        "tasks": [
            {"desc": "Google Cert: Automate Cybersecurity Tasks with Python (Course 7) - Week 1, Module 1 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Review weakest areas from practice quiz", "type": "Security+"},
            {"desc": "TryHackMe: Explore a new tool or concept (e.g., Nmap basics)", "type": "TryHackMe"},
            {"desc": "Job Search: Tailor resume/cover letter for 1 specific role", "type": "Job Search"}
        ]
    },
    26: {
        "date": SPRINT_START_DATE + timedelta(days=25),
        "tasks": [
            {"desc": "Google Cert: Automate Cybersecurity Tasks with Python (Course 7) - Week 1, Module 2 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Quick review of all Security+ domains (key concepts)", "type": "Security+"},
            {"desc": "TryHackMe: Complete a new room or a CTF challenge (easy level)", "type": "TryHackMe"},
        ]
    },
    27: {
        "date": SPRINT_START_DATE + timedelta(days=26),
        "tasks": [
            {"desc": "Google Cert: Automate Cybersecurity Tasks with Python (Course 7) - Week 2, Module 1 (Video/Reading) (Aim to finish Course 7)", "type": "Google Cert"},
            {"desc": "Security+: Final review of acronyms and port numbers", "type": "Security+"},
            {"desc": "TryHackMe: Revisit a foundational room to solidify knowledge", "type": "TryHackMe"},
            {"desc": "Job Search: Apply to 1 more entry-level job", "type": "Job Search"}
        ]
    },
    28: {
        "date": SPRINT_START_DATE + timedelta(days=27),
        "tasks": [
            {"desc": "Google Cert: Capstone: Apply Your Skills with a Cybersecurity Project (Course 8) - Week 1, Module 1 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Practice performance-based questions (PBQs) concepts", "type": "Security+"},
            {"desc": "TryHackMe: Explore a room related to your weakest Security+ domain", "type": "TryHackMe"},
        ]
    },
    # Week 5: Capstone & Deeper Dives (Days 29-35)
    29: {
        "date": SPRINT_START_DATE + timedelta(days=28),
        "tasks": [
            {"desc": "Google Cert: Capstone: Apply Your Skills with a Cybersecurity Project (Course 8) - Week 1, Module 2 (Video/Reading)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 37-38) - General Review/Deep Dive", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating with Splunk (Part 5)", "type": "TryHackMe"},
            {"desc": "Job Search: Quick LinkedIn networking (1 connection)", "type": "Job Search"}
        ]
    },
    30: {
        "date": SPRINT_START_DATE + timedelta(days=29),
        "tasks": [
            {"desc": "Google Cert: Capstone: Apply Your Skills with a Cybersecurity Project (Course 8) - Week 2, Module 1 (Video/Reading) (Aim to finish Course 8 & Google Cert!)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 39-40) - General Review/Deep Dive", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating with Splunk (Part 6)", "type": "TryHackMe"},
        ]
    },
    31: {
        "date": SPRINT_START_DATE + timedelta(days=30),
        "tasks": [
            {"desc": "Google Cert: Review all Google Cert material for final understanding", "type": "Google Cert"},
            {"desc": "Security+: Take a full practice exam (if available, or compile questions)", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating with Splunk (Part 7)", "type": "TryHackMe"},
        ]
    },
    32: {
        "date": SPRINT_START_DATE + timedelta(days=31),
        "tasks": [
            {"desc": "Google Cert: Consolidate notes and key concepts from all courses", "type": "Google Cert"},
            {"desc": "Security+: Review practice exam results, identify weakest domain", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating with Splunk (Part 8)", "type": "TryHackMe"},
            {"desc": "Job Search: Apply to 1 entry-level job", "type": "Job Search"}
        ]
    },
    33: {
        "date": SPRINT_START_DATE + timedelta(days=32),
        "tasks": [
            {"desc": "Google Cert: Prepare for any final assessments or project submissions", "type": "Google Cert"},
            {"desc": "Security+: Deep dive into weakest Security+ domain", "type": "Security+"},
            {"desc": "TryHackMe: Complete a room on a topic you enjoyed most", "type": "TryHackMe"},
        ]
    },
    34: {
        "date": SPRINT_START_DATE + timedelta(days=33),
        "tasks": [
            {"desc": "Google Cert: Celebrate Google Cert completion! 🎉", "type": "Google Cert"},
            {"desc": "Security+: Review all Security+ domains (skim/re-watch weak areas)", "type": "Security+"},
            {"desc": "TryHackMe: Complete a new room from 'Cyber Defense' or 'Security Engineer' path", "type": "TryHackMe"},
        ]
    },
    35: {
        "date": SPRINT_START_DATE + timedelta(days=34),
        "tasks": [
            {"desc": "Sprint Review: Summarize key learnings from Google Cert & Security+", "type": "Review"},
            {"desc": "Security+: Practice PBQs concepts again", "type": "Security+"},
            {"desc": "TryHackMe: Document your favorite TryHackMe rooms/learnings for LinkedIn", "type": "TryHackMe"},
            {"desc": "Weekly Review: Catch-up on any missed tasks", "type": "Review"}
        ]
    },
    # Week 6: Refinement & Job Search Focus (Days 36-42)
    36: {
        "date": SPRINT_START_DATE + timedelta(days=35),
        "tasks": [
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 41-42) - General Review/Deep Dive", "type": "Security+"},
            {"desc": "TryHackMe: Explore a room related to a Security+ domain you find challenging", "type": "TryHackMe"},
            {"desc": "Job Search: Tailor resume/cover letter for 1 specific role", "type": "Job Search"},
        ]
    },
    37: {
        "date": SPRINT_START_DATE + timedelta(days=36),
        "tasks": [
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 43-44) - General Review/Deep Dive", "type": "Security+"},
            {"desc": "TryHackMe: Complete a new room on a topic you want to showcase on LinkedIn", "type": "TryHackMe"},
        ]
    },
    38: {
        "date": SPRINT_START_DATE + timedelta(days=37),
        "tasks": [
            {"desc": "Security+: Take another short practice quiz (mixed domains)", "type": "Security+"},
            {"desc": "TryHackMe: Re-do a room you completed earlier to reinforce understanding", "type": "TryHackMe"},
            {"desc": "Job Search: Apply to 1 entry-level job", "type": "Job Search"}
        ]
    },
    39: {
        "date": SPRINT_START_DATE + timedelta(days=38),
        "tasks": [
            {"desc": "Security+: Review quiz results, focus on weak areas", "type": "Security+"},
            {"desc": "TryHackMe: Explore a new tool or concept (e.g., Wireshark basics)", "type": "TryHackMe"},
        ]
    },
    40: {
        "date": SPRINT_START_DATE + timedelta(days=39),
        "tasks": [
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 45-46) - General Review/Deep Dive", "type": "Security+"},
            {"desc": "TryHackMe: Complete a new room (e.g., from 'Red Team Fundamentals' for exposure)", "type": "TryHackMe"},
            {"desc": "Job Search: Quick LinkedIn networking (1 connection)", "type": "Job Search"}
        ]
    },
    41: {
        "date": SPRINT_START_DATE + timedelta(days=40),
        "tasks": [
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 47-48) - General Review/Deep Dive", "type": "Security+"},
            {"desc": "TryHackMe: Work on a small CTF challenge or a more advanced room (if time allows)", "type": "TryHackMe"},
        ]
    },
    42: {
        "date": SPRINT_START_DATE + timedelta(days=41),
        "tasks": [
            {"desc": "Security+: Final review of all Security+ domains (quick skim)", "type": "Security+"},
            {"desc": "TryHackMe: Review your TryHackMe profile, identify rooms to highlight on LinkedIn", "type": "TryHackMe"},
            {"desc": "Weekly Review: Catch-up on any missed tasks", "type": "Review"}
        ]
    },
    # Week 7: Security+ Prep & Job Application Push (Days 43-49)
    43: {
        "date": SPRINT_START_DATE + timedelta(days=42),
        "tasks": [
            {"desc": "Security+: Take a full-length practice exam (if available)", "type": "Security+"},
            {"desc": "Job Search: Apply to 2 entry-level jobs", "type": "Job Search"},
        ]
    },
    44: {
        "date": SPRINT_START_DATE + timedelta(days=43),
        "tasks": [
            {"desc": "Security+: Review practice exam results in detail, focus on weakest areas", "type": "Security+"},
            {"desc": "TryHackMe: Complete a room that directly relates to a job description you're interested in", "type": "TryHackMe"},
        ]
    },
    45: {
        "date": SPRINT_START_DATE + timedelta(days=44),
        "tasks": [
            {"desc": "Security+: Focus on PBQs and scenario-based questions", "type": "Security+"},
            {"desc": "Job Search: Tailor resume/cover letter for another specific role", "type": "Job Search"},
        ]
    },
    46: {
        "date": SPRINT_START_DATE + timedelta(days=45),
        "tasks": [
            {"desc": "Security+: Quick review of all acronyms, port numbers, and common tools", "type": "Security+"},
            {"desc": "TryHackMe: Revisit a challenging room for mastery", "type": "TryHackMe"},
        ]
    },
    47: {
        "date": SPRINT_START_DATE + timedelta(days=46),
        "tasks": [
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 49-50) - Last minute review", "type": "Security+"},
            {"desc": "Job Search: Apply to 2 entry-level jobs", "type": "Job Search"},
        ]
    },
    48: {
        "date": SPRINT_START_DATE + timedelta(days=47),
        "tasks": [
            {"desc": "Security+: Final quick review of key concepts across all domains", "type": "Security+"},
            {"desc": "TryHackMe: Select 2-3 rooms to feature prominently on LinkedIn", "type": "TryHackMe"},
        ]
    },
    49: {
        "date": SPRINT_START_DATE + timedelta(days=48),
        "tasks": [
            {"desc": "Security+: Mentally prepare for the exam, light review only", "type": "Security+"},
            {"desc": "Job Search: Update LinkedIn 'Skills' section with new certs/TryHackMe rooms", "type": "Job Search"},
            {"desc": "Weekly Review: Catch-up on any missed tasks", "type": "Review"}
        ]
    },
    # Week 8: Final Sprint & Future Planning (Days 50-56)
    50: {
        "date": SPRINT_START_DATE + timedelta(days=49),
        "tasks": [
            {"desc": "Job Search: Apply to 2 entry-level jobs (aggressive push)", "type": "Job Search"},
            {"desc": "TryHackMe: Complete one final room you enjoy and can explain well", "type": "TryHackMe"},
            {"desc": "Future Planning: Research next steps for Security+ exam scheduling", "type": "Future Planning"},
        ]
    },
    51: {
        "date": SPRINT_START_DATE + timedelta(days=50),
        "tasks": [
            {"desc": "Job Search: Tailor resume/cover letter for 1 more specific role", "type": "Job Search"},
            {"desc": "Networking: Send personalized connection requests to 2-3 professionals on LinkedIn", "type": "Job Search"},
        ]
    },
    52: {
        "date": SPRINT_START_DATE + timedelta(days=51),
        "tasks": [
            {"desc": "Job Search: Apply to 2 entry-level jobs", "type": "Job Search"},
            {"desc": "TryHackMe: Review your TryHackMe profile and identify key achievements for interviews", "type": "TryHackMe"},
        ]
    },
    53: {
        "date": SPRINT_START_DATE + timedelta(days=52),
        "tasks": [
            {"desc": "Job Search: Research common cybersecurity interview questions", "type": "Job Search"},
            {"desc": "Networking: Follow up with previous connections or mentors", "type": "Job Search"},
        ]
    },
    54: {
        "date": SPRINT_START_DATE + timedelta(days=53),
        "tasks": [
            {"desc": "Job Search: Apply to 2 entry-level jobs", "type": "Job Search"},
            {"desc": "TryHackMe: Practice explaining a TryHackMe lab solution verbally", "type": "TryHackMe"},
        ]
    },
    55: {
        "date": SPRINT_START_DATE + timedelta(days=54),
        "tasks": [
            {"desc": "Job Search: Update resume/LinkedIn with all new certifications and skills", "type": "Job Search"},
            {"desc": "Future Planning: Research advanced certifications or specializations", "type": "Future Planning"},
        ]
    },
    56: {
        "date": SPRINT_START_DATE + timedelta(days=55),
        "tasks": [
            {"desc": "Job Search: Apply to 2 entry-level jobs", "type": "Job Search"},
            {"desc": "Sprint Retrospective: What went well, what to improve?", "type": "Review"},
            {"desc": "Weekly Review: Catch-up on any missed tasks", "type": "Review"}
        ]
    },
    # Final Days: Consolidation & Celebration (Days 57-60)
    57: {
        "date": SPRINT_START_DATE + timedelta(days=56),
        "tasks": [
            {"desc": "Job Search: Final check for new relevant job postings", "type": "Job Search"},
            {"desc": "Networking: Send thank you notes/follow-ups to any connections made", "type": "Job Search"},
        ]
    },
    58: {
        "date": SPRINT_START_DATE + timedelta(days=57),
        "tasks": [
            {"desc": "Job Search: Review all applications sent and plan follow-up strategy", "type": "Job Search"},
            {"desc": "Future Planning: Set goals for the next 30-60 days of learning", "type": "Future Planning"},
        ]
    },
    59: {
        "date": SPRINT_START_DATE + timedelta(days=58),
        "tasks": [
            {"desc": "Sprint Summary: Document key achievements and quantifiable progress (e.g., TryHackMe rooms/points)", "type": "Review"},
            {"desc": "Prepare for Security+ exam within the next 1-2 weeks (post-sprint)", "type": "Security+"},
        ]
    },
    60: {
        "date": SPRINT_START_DATE + timedelta(days=59),
        "tasks": [
            {"desc": "Celebrate your 60-day sprint achievement! 🎉🚀", "type": "Motivation"},
            {"desc": "Update LinkedIn with Google Cert and TryHackMe progress", "type": "Job Search"},
            {"desc": "Take a well-deserved break!", "type": "Motivation"}
        ]
    },
}

# Ensure all tasks are initialized in sprint_data if not present
for day, day_info in daily_tasks_template.items():
    day_str = str(day)
    if day_str not in st.session_state.sprint_data['tasks']:
        st.session_state.sprint_data['tasks'][day_str] = [
            {'desc': task['desc'], 'type': task['type'], 'completed': False}
            for task in day_info['tasks']
        ]
    if day_str not in st.session_state.sprint_data['notes']:
        st.session_state.sprint_data['notes'][day_str] = ""
    if day_str not in st.session_state.sprint_data['timer_data']:
        st.session_state.sprint_data['timer_data'][day_str] = {'start_time': None, 'elapsed_time': 0}

# --- Streamlit App Layout ---
st.set_page_config(layout="wide", page_title="Cybersecurity 60-Day Sprint Dashboard")

st.title("🛡️ Cybersecurity 60-Day Sprint Dashboard")
st.markdown("---")

# Calculate current day of sprint
today = date.today()
current_sprint_day = (today - SPRINT_START_DATE).days + 1

if current_sprint_day < 1:
    st.info(f"Your sprint officially starts on {SPRINT_START_DATE.strftime('%B %d, %Y')}. You can select Day 1 below to get started!")
    current_sprint_day = 1 # Default to Day 1
elif current_sprint_day > TOTAL_SPRINT_DAYS:
    st.success(f"🎉 Congratulations! You've completed your 60-day sprint! 🎉")
    st.balloons()
    current_sprint_day = TOTAL_SPRINT_DAYS # Default to the last day

# Day selection dropdown
selected_day_option = st.selectbox(
    "Select Day:",
    options=[f"Day {d}" for d in range(1, TOTAL_SPRINT_DAYS + 1)],
    index=min(current_sprint_day - 1, TOTAL_SPRINT_DAYS - 1), # Set default to current sprint day, max out at last day
    key="day_selector"
)
selected_day_num = int(selected_day_option.split(" ")[1])
selected_day_str = str(selected_day_num)

st.header(f"{selected_day_option}: {daily_tasks_template[selected_day_num]['date'].strftime('%B %d, %Y')}")

# --- Overall Progress Bar ---
total_tasks_count = sum(len(st.session_state.sprint_data['tasks'][str(day)]) for day in range(1, TOTAL_SPRINT_DAYS + 1))
completed_tasks_count = 0
for day_str in st.session_state.sprint_data['tasks']:
    for task in st.session_state.sprint_data['tasks'][day_str]:
        if task['completed']:
            completed_tasks_count += 1

progress_percentage = (completed_tasks_count / total_tasks_count) * 100 if total_tasks_count > 0 else 0
st.progress(progress_percentage / 100, text=f"Overall Sprint Progress: {progress_percentage:.1f}%")

# Motivation messages
if progress_percentage < 25:
    st.info("Keep going! Every small step adds up. You've got this! 💪")
elif 25 <= progress_percentage < 50:
    st.warning("You're building great momentum. Stay focused! ⚡")
elif 50 <= progress_percentage < 75:
    st.success("Over halfway! You're crushing it! Push through to the finish line! 🚀")
else:
    st.balloons()
    st.success("Almost there! The finish line is in sight. You're doing amazing! ✨")

st.markdown("---")

# --- Display Content for Selected Day ---
day_info = daily_tasks_template[selected_day_num]
    
# Ensure selected day's data is initialized
if selected_day_str not in st.session_state.sprint_data['tasks']:
    st.session_state.sprint_data['tasks'][selected_day_str] = [
        {'desc': task['desc'], 'type': task['type'], 'completed': False}
        for task in day_info['tasks']
    ]
if selected_day_str not in st.session_state.sprint_data['notes']:
    st.session_state.sprint_data['notes'][selected_day_str] = ""
if selected_day_str not in st.session_state.sprint_data['timer_data']:
    st.session_state.sprint_data['timer_data'][selected_day_str] = {'start_time': None, 'elapsed_time': 0}

st.subheader("Tasks:")
        
# Display tasks for the selected day
for i, task in enumerate(st.session_state.sprint_data['tasks'][selected_day_str]):
    # Use a unique key for each checkbox to ensure persistence
    checkbox_key = f"day_{selected_day_str}_task_{i}"
            
    # Create a column layout for task type and checkbox
    col_type, col_task = st.columns([0.2, 0.8])
    with col_type:
        st.markdown(f"**`{task['type']}`**")
    with col_task:
        checked = st.checkbox(
            task['desc'], 
            value=task['completed'], 
            key=checkbox_key
        )
        if checked != task['completed']:
            st.session_state.sprint_data['tasks'][selected_day_str][i]['completed'] = checked
            save_data(st.session_state.sprint_data)
            st.rerun() # Rerun to update progress bar immediately

st.markdown("---")
st.subheader("Timer (for focused work sessions):")
        
# Timer functionality for the selected day
timer_data = st.session_state.sprint_data['timer_data'][selected_day_str]
        
col_start, col_stop = st.columns(2)
        
with col_start:
    if st.button("Start Timer", key=f"start_timer_{selected_day_str}"):
        timer_data['start_time'] = time.time()
        save_data(st.session_state.sprint_data)
        st.toast("Timer started!")
        
with col_stop:
    if st.button("Stop Timer", key=f"stop_timer_{selected_day_str}"):
        if timer_data['start_time'] is not None:
            elapsed = time.time() - timer_data['start_time']
            timer_data['elapsed_time'] += elapsed
            timer_data['start_time'] = None # Reset start time
            save_data(st.session_state.sprint_data)
            st.toast(f"Timer stopped! Added {elapsed:.0f} seconds.")
        else:
            st.warning("Timer not started yet.")
        
# Display elapsed time for the day
total_seconds = timer_data['elapsed_time']
hours = int(total_seconds // 3600)
minutes = int((total_seconds % 3600) // 60)
seconds = int(total_seconds % 60)
st.info(f"Time spent today: {hours:02d}h {minutes:02d}m {seconds:02d}s")

st.markdown("---")
st.subheader("Daily Notes:")
        
# Notes section for the day
current_notes = st.session_state.sprint_data['notes'][selected_day_str]
new_notes = st.text_area(
    "Add your reflections, challenges, or key learnings here:",
    value=current_notes,
    height=150,
    key=f"notes_day_{selected_day_str}"
)
if new_notes != current_notes:
    st.session_state.sprint_data['notes'][selected_day_str] = new_notes
    save_data(st.session_state.sprint_data)
    st.toast("Notes saved!")

st.markdown("---")
st.subheader("TryHackMe Quantifiable Progress:")

# TryHackMe progress tracking
col_rooms, col_points = st.columns(2)

with col_rooms:
    current_rooms = st.session_state.sprint_data['total_tryhackme_rooms']
    new_rooms = st.number_input(
        "Total TryHackMe Rooms Completed:",
        min_value=0,
        value=current_rooms,
        step=1,
        key="total_tryhackme_rooms_input"
    )
    if new_rooms != current_rooms:
        st.session_state.sprint_data['total_tryhackme_rooms'] = new_rooms
        save_data(st.session_state.sprint_data)
        st.toast("TryHackMe rooms updated!")

with col_points:
    current_points = st.session_state.sprint_data['total_tryhackme_points']
    new_points = st.number_input(
        "Total TryHackMe Points Gained:",
        min_value=0,
        value=current_points,
        step=10,
        key="total_tryhackme_points_input"
    )
    if new_points != current_points:
        st.session_state.sprint_data['total_tryhackme_points'] = new_points
        save_data(st.session_state.sprint_data)
        st.toast("TryHackMe points updated!")

st.markdown("---")
st.info(f"""
**Important Notes for Your 1-Hour Daily 60-Day Sprint:**
* **Consistency is Key:** With only 1 hour per day, consistent effort is paramount. Missing days will significantly impact your progress.
* **Prioritization:** This schedule is designed to give you a strong foundation and demonstrable progress.
    * **Google Cybersecurity Certificate:** The plan aims for you to finish this certificate by the end of the 60 days. Focus on understanding the core concepts and completing the labs/quizzes.
    * **CompTIA Security+:** You will cover a significant portion of the Security+ material, especially the foundational domains, using Professor Messer's videos. The goal is to be *ready to give* the exam shortly after the sprint, not necessarily to pass it within the 60 days, as a full 100% readiness might require more dedicated study time.
    * **TryHackMe:** The plan includes completing the "Pre-Security" path, "Intro to Cyber Defense," and making substantial progress in the "SOC Level 1" path. This will give you quantifiable achievements to update on your LinkedIn profile.
    * **Job Applications:** Job search activities are integrated regularly. Remember to tailor your resume and cover letter for each application.
* **Resource Links:**
    * **Google Cybersecurity Certificate (Coursera):** [https://www.coursera.org/professional-certificates/google-cybersecurity](https://www.coursera.org/professional-certificates/google-cybersecurity)
    * **Professor Messer (YouTube):** [https://www.youtube.com/@professormesser](https://www.youtube.com/@professormesser) (Search for "Security+ SY0-601" or "Security+ SY0-701" playlists)
    * **TryHackMe:** [https://tryhackme.com/](https://tryhackme.com/)
    * **Job Boards:**
        * Indeed: [https://www.indeed.com/](https://www.indeed.com/)
        * LinkedIn Jobs: [https://www.linkedin.com/jobs/](https://www.linkedin.com/jobs/)
        * Glassdoor: [https://www.glassdoor.com/jobs/](https://www.glassdoor.com/jobs/)
        * CyberSN: [https://www.cybersn.com/](https://www.cybersn.com/)
        * Monster: [https://www.monster.com/](https://www.monster.com/)
        * ZipRecruiter: [https://www.ziprecruiter.com/](https://www.ziprecruiter.com/)
    * **Networking:** Leverage LinkedIn for professional connections. Consider searching for cybersecurity communities on platforms like Discord (e.g., "The Many Hats Club" or other infosec communities).
    * **General Cybersecurity Resources (for deeper dives/reference):**
        * OWASP Top Ten: [https://owasp.org/www-project-top-10/](https://owasp.org/www-project-top-10/)
        * CVE Database: [https://cve.mitre.org/](https://cve.mitre.org/)
        * NIST Cybersecurity Frameworks: [https://www.nist.gov/cyberframework](https://www.nist.gov/cyberframework)
* **Flexibility:** If you fall behind on a task, don't get discouraged. Use the "Weekly Review" days to catch up, or simply adjust the next day's tasks. The goal is continuous progress, not perfection.
""")
