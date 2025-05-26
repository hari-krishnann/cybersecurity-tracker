import streamlit as st
from datetime import date, timedelta
import json
import time
import os

# --- Configuration ---
SPRINT_START_DATE = date(2025, 5, 26) # May 26th, 2025
TOTAL_SPRINT_DAYS = 30
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

# --- Daily Task Definitions (Highly Condensed for 2 hours/day) ---
# Each day's tasks are designed to fit within roughly 2 hours.
# Google Cert: ~1 hour
# Security+: ~30 minutes
# TryHackMe: ~30 minutes
# Job applications/Networking: Integrate into weekly review or assume brief check-ins.

daily_tasks_template = {
    # Week 1: Foundations & Initial Momentum (May 26 - June 1)
    1: {
        "date": SPRINT_START_DATE,
        "tasks": [
            {"desc": "Google Cert: Foundations of Cybersecurity (Course 1) - Week 1, Module 1", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 1-5) - Threats, Attacks, Vulnerabilities", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Intro to Cyber Security (Complete)", "type": "TryHackMe"},
            {"desc": "Job Search: Update LinkedIn profile summary", "type": "Job Search"}
        ]
    },
    2: {
        "date": SPRINT_START_DATE + timedelta(days=1),
        "tasks": [
            {"desc": "Google Cert: Foundations of Cybersecurity (Course 1) - Week 1, Module 2", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 6-10) - Threats, Attacks, Vulnerabilities", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Network Fundamentals (Complete)", "type": "TryHackMe"},
        ]
    },
    3: {
        "date": SPRINT_START_DATE + timedelta(days=2),
        "tasks": [
            {"desc": "Google Cert: Foundations of Cybersecurity (Course 1) - Week 2, Module 1", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 11-15) - Threats, Attacks, Vulnerabilities", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Linux Fundamentals Part 1 (Complete)", "type": "TryHackMe"},
        ]
    },
    4: {
        "date": SPRINT_START_DATE + timedelta(days=3),
        "tasks": [
            {"desc": "Google Cert: Foundations of Cybersecurity (Course 1) - Week 2, Module 2 (Aim to finish Course 1)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 16-20) - Threats, Attacks, Vulnerabilities", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Windows Fundamentals 1 (Complete)", "type": "TryHackMe"},
        ]
    },
    5: {
        "date": SPRINT_START_DATE + timedelta(days=4),
        "tasks": [
            {"desc": "Google Cert: Play It Safe: Manage Security Risks (Course 2) - Week 1, Module 1", "type": "Google Cert"},
            {"desc": "Security+: Review Domain 1 & practice questions", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Linux Fundamentals Part 2 (Complete)", "type": "TryHackMe"},
            {"desc": "Job Search: Identify 2-3 target companies/roles", "type": "Job Search"}
        ]
    },
    6: {
        "date": SPRINT_START_DATE + timedelta(days=5),
        "tasks": [
            {"desc": "Google Cert: Play It Safe: Manage Security Risks (Course 2) - Week 1, Module 2", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 21-25) - Architecture & Design", "type": "Security+"},
            {"desc": "TryHackMe: Pre-Security Path - Windows Fundamentals 2 (Complete)", "type": "TryHackMe"},
        ]
    },
    7: {
        "date": SPRINT_START_DATE + timedelta(days=6),
        "tasks": [
            {"desc": "Google Cert: Play It Safe: Manage Security Risks (Course 2) - Week 2, Module 1 (Aim to finish Course 2)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 26-30) - Architecture & Design", "type": "Security+"},
            {"desc": "TryHackMe: Intro to Cyber Defense (Complete)", "type": "TryHackMe"},
            {"desc": "Weekly Review: Catch-up on any missed tasks", "type": "Review"}
        ]
    },
    # Week 2: Deep Dive & Practical Application (June 2 - June 8)
    8: {
        "date": SPRINT_START_DATE + timedelta(days=7),
        "tasks": [
            {"desc": "Google Cert: Protect Company Assets: Data, Devices, and Vulnerabilities (Course 3) - Week 1, Module 1", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 31-35) - Implementation", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Blue Team (Part 1)", "type": "TryHackMe"},
            {"desc": "Job Search: Apply to 1 entry-level job", "type": "Job Search"}
        ]
    },
    9: {
        "date": SPRINT_START_DATE + timedelta(days=8),
        "tasks": [
            {"desc": "Google Cert: Protect Company Assets: Data, Devices, and Vulnerabilities (Course 3) - Week 1, Module 2", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 36-40) - Implementation", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Blue Team (Part 2)", "type": "TryHackMe"},
        ]
    },
    10: {
        "date": SPRINT_START_DATE + timedelta(days=9),
        "tasks": [
            {"desc": "Google Cert: Protect Company Assets: Data, Devices, and Vulnerabilities (Course 3) - Week 2, Module 1 (Aim to finish Course 3)", "type": "Google Cert"},
            {"desc": "Security+: Review Domain 2 & 3 & practice questions", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating Windows (Part 1)", "type": "TryHackMe"},
        ]
    },
    11: {
        "date": SPRINT_START_DATE + timedelta(days=10),
        "tasks": [
            {"desc": "Google Cert: Become a Cybersecurity Analyst (Course 4) - Week 1, Module 1", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 41-45) - Operations & Incident Response", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating Windows (Part 2)", "type": "TryHackMe"},
        ]
    },
    12: {
        "date": SPRINT_START_DATE + timedelta(days=11),
        "tasks": [
            {"desc": "Google Cert: Become a Cybersecurity Analyst (Course 4) - Week 1, Module 2", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 46-50) - Operations & Incident Response", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating Linux (Part 1)", "type": "TryHackMe"},
            {"desc": "Job Search: Network on LinkedIn (connect with 2-3 professionals)", "type": "Job Search"}
        ]
    },
    13: {
        "date": SPRINT_START_DATE + timedelta(days=12),
        "tasks": [
            {"desc": "Google Cert: Become a Cybersecurity Analyst (Course 4) - Week 2, Module 1 (Aim to finish Course 4)", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 51-55) - Governance, Risk, Compliance", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating Linux (Part 2)", "type": "TryHackMe"},
        ]
    },
    14: {
        "date": SPRINT_START_DATE + timedelta(days=13),
        "tasks": [
            {"desc": "Google Cert: Put It to the Test: Blue Team Practices (Course 5) - Week 1, Module 1", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 56-60) - Governance, Risk, Compliance", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating with Splunk (Part 1)", "type": "TryHackMe"},
            {"desc": "Weekly Review: Catch-up on any missed tasks", "type": "Review"}
        ]
    },
    # Week 3: Incident Response & Governance (June 9 - June 15)
    15: {
        "date": SPRINT_START_DATE + timedelta(days=14),
        "tasks": [
            {"desc": "Google Cert: Put It to the Test: Blue Team Practices (Course 5) - Week 1, Module 2", "type": "Google Cert"},
            {"desc": "Security+: Review all domains & take a short practice quiz", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating with Splunk (Part 2)", "type": "TryHackMe"},
            {"desc": "Job Search: Apply to 1 entry-level job", "type": "Job Search"}
        ]
    },
    16: {
        "date": SPRINT_START_DATE + timedelta(days=15),
        "tasks": [
            {"desc": "Google Cert: Put It to the Test: Blue Team Practices (Course 5) - Week 2, Module 1 (Aim to finish Course 5)", "type": "Google Cert"},
            {"desc": "Security+: Focus on weak areas identified from quiz/review", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating with Splunk (Part 3)", "type": "TryHackMe"},
        ]
    },
    17: {
        "date": SPRINT_START_DATE + timedelta(days=16),
        "tasks": [
            {"desc": "Google Cert: Respond to Threats and Defend Systems (Course 6) - Week 1, Module 1", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 61-65) - General Review/Deep Dive", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating with Splunk (Part 4)", "type": "TryHackMe"},
        ]
    },
    18: {
        "date": SPRINT_START_DATE + timedelta(days=17),
        "tasks": [
            {"desc": "Google Cert: Respond to Threats and Defend Systems (Course 6) - Week 1, Module 2", "type": "Google Cert"},
            {"desc": "Security+: Professor Messer SY0-601/701 (Videos 66-70) - General Review/Deep Dive", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating with Splunk (Part 5)", "type": "TryHackMe"},
            {"desc": "Job Search: Research visa sponsorship policies of potential employers", "type": "Job Search"}
        ]
    },
    19: {
        "date": SPRINT_START_DATE + timedelta(days=18),
        "tasks": [
            {"desc": "Google Cert: Respond to Threats and Defend Systems (Course 6) - Week 2, Module 1 (Aim to finish Course 6)", "type": "Google Cert"},
            {"desc": "Security+: Take a full practice exam (if available, or compile questions)", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating with Splunk (Part 6)", "type": "TryHackMe"},
        ]
    },
    20: {
        "date": SPRINT_START_DATE + timedelta(days=19),
        "tasks": [
            {"desc": "Google Cert: Automate Cybersecurity Tasks with Python (Course 7) - Week 1, Module 1", "type": "Google Cert"},
            {"desc": "Security+: Review practice exam results, identify weakest domain", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating with Splunk (Part 7)", "type": "TryHackMe"},
        ]
    },
    21: {
        "date": SPRINT_START_DATE + timedelta(days=20),
        "tasks": [
            {"desc": "Google Cert: Automate Cybersecurity Tasks with Python (Course 7) - Week 1, Module 2 (Aim to finish Course 7)", "type": "Google Cert"},
            {"desc": "Security+: Deep dive into weakest Security+ domain", "type": "Security+"},
            {"desc": "TryHackMe: SOC Level 1 Path - Investigating with Splunk (Part 8)", "type": "TryHackMe"},
            {"desc": "Weekly Review: Catch-up on any missed tasks", "type": "Review"}
        ]
    },
    # Week 4: Certification Finalization & Job Search Acceleration (June 16 - June 24)
    22: {
        "date": SPRINT_START_DATE + timedelta(days=21),
        "tasks": [
            {"desc": "Google Cert: Capstone: Apply Your Skills with a Cybersecurity Project (Course 8) - Week 1, Module 1", "type": "Google Cert"},
            {"desc": "Security+: Practice performance-based questions (PBQs) concepts", "type": "Security+"},
            {"desc": "TryHackMe: Explore a room related to your weakest Security+ domain", "type": "TryHackMe"},
            {"desc": "Job Search: Apply to 2 entry-level jobs", "type": "Job Search"}
        ]
    },
    23: {
        "date": SPRINT_START_DATE + timedelta(days=22),
        "tasks": [
            {"desc": "Google Cert: Capstone: Apply Your Skills with a Cybersecurity Project (Course 8) - Week 1, Module 2", "type": "Google Cert"},
            {"desc": "Security+: Final review of all Professor Messer videos (skim/re-watch weak areas)", "type": "Security+"},
            {"desc": "TryHackMe: Complete a new room from the 'Cyber Defense' or 'Security Engineer' path", "type": "TryHackMe"},
        ]
    },
    24: {
        "date": SPRINT_START_DATE + timedelta(days=23),
        "tasks": [
            {"desc": "Google Cert: Capstone: Apply Your Skills with a Cybersecurity Project (Course 8) - Week 2, Module 1 (Aim to finish Course 8 & Google Cert!)", "type": "Google Cert"},
            {"desc": "Security+: Take another full practice exam", "type": "Security+"},
            {"desc": "TryHackMe: Select a room you found challenging and re-do it for mastery", "type": "TryHackMe"},
        ]
    },
    25: {
        "date": SPRINT_START_DATE + timedelta(days=24),
        "tasks": [
            {"desc": "Google Cert: Review all Google Cert material for final understanding", "type": "Google Cert"},
            {"desc": "Security+: Review practice exam results & focus on last minute weak points", "type": "Security+"},
            {"desc": "TryHackMe: Complete a new room or a CTF challenge (easy level)", "type": "TryHackMe"},
            {"desc": "Job Search: Tailor resume/cover letter for specific roles", "type": "Job Search"}
        ]
    },
    26: {
        "date": SPRINT_START_DATE + timedelta(days=25),
        "tasks": [
            {"desc": "Google Cert: Consolidate notes and key concepts from all courses", "type": "Google Cert"},
            {"desc": "Security+: Quick review of all Security+ domains", "type": "Security+"},
            {"desc": "TryHackMe: Explore a new tool or concept (e.g., Nmap basics, Wireshark basics)", "type": "TryHackMe"},
        ]
    },
    27: {
        "date": SPRINT_START_DATE + timedelta(days=26),
        "tasks": [
            {"desc": "Google Cert: Prepare for any final assessments or project submissions", "type": "Google Cert"},
            {"desc": "Security+: Final review of acronyms and port numbers", "type": "Security+"},
            {"desc": "TryHackMe: Complete a room on a topic you enjoyed most", "type": "TryHackMe"},
            {"desc": "Job Search: Apply to 2 more entry-level jobs", "type": "Job Search"}
        ]
    },
    28: {
        "date": SPRINT_START_DATE + timedelta(days=27),
        "tasks": [
            {"desc": "Google Cert: Celebrate Google Cert completion! 🎉", "type": "Google Cert"},
            {"desc": "Security+: Take one last comprehensive practice exam (if time allows)", "type": "Security+"},
            {"desc": "TryHackMe: Revisit a foundational room to solidify knowledge", "type": "TryHackMe"},
        ]
    },
    29: {
        "date": SPRINT_START_DATE + timedelta(days=28),
        "tasks": [
            {"desc": "Sprint Review: Summarize key learnings from Google Cert & Security+", "type": "Review"},
            {"desc": "TryHackMe: Document your favorite TryHackMe rooms/learnings", "type": "TryHackMe"},
            {"desc": "Future Planning: Research next steps for Security+ exam & advanced studies", "type": "Future Planning"},
        ]
    },
    30: {
        "date": SPRINT_START_DATE + timedelta(days=29),
        "tasks": [
            {"desc": "Sprint Retrospective: What went well, what to improve?", "type": "Review"},
            {"desc": "Job Search: Update resume/LinkedIn with new certifications and skills", "type": "Job Search"},
            {"desc": "Networking: Send thank you notes/follow-ups to any connections made", "type": "Job Search"},
            {"desc": "Celebrate your 30-day sprint achievement! 🚀", "type": "Motivation"}
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
st.set_page_config(layout="wide", page_title="Cybersecurity 30-Day Sprint Dashboard")

st.title("🛡️ Cybersecurity 30-Day Sprint Dashboard")
st.markdown("---")

# Calculate current day of sprint
today = date.today()
current_sprint_day = (today - SPRINT_START_DATE).days + 1

if current_sprint_day < 1:
    st.info(f"Your sprint starts on {SPRINT_START_DATE.strftime('%B %d, %Y')}. Get ready!")
    current_sprint_day = 1 # Show Day 1 tasks even before sprint officially starts
elif current_sprint_day > TOTAL_SPRINT_DAYS:
    st.success(f"🎉 Congratulations! You've completed your 30-day sprint! 🎉")
    st.balloons()
    current_sprint_day = TOTAL_SPRINT_DAYS # Keep showing the last day's content

st.header(f"Day {current_sprint_day} of {TOTAL_SPRINT_DAYS} - {daily_tasks_template[current_sprint_day]['date'].strftime('%B %d, %Y')}")

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
    st.warning("Halfway there! You're building great momentum. Stay focused! ⚡")
elif 50 <= progress_percentage < 75:
    st.success("Over halfway! You're crushing it! Push through to the finish line! 🚀")
else:
    st.balloons()
    st.success("Almost there! The finish line is in sight. You're doing amazing! ✨")

st.markdown("---")

# --- Daily Sections (Expanders) ---
# Display current day first, then previous/future days in expanders
days_to_display = [current_sprint_day] + sorted(list(set(range(1, TOTAL_SPRINT_DAYS + 1)) - {current_sprint_day}))

for day_num in days_to_display:
    day_str = str(day_num)
    day_info = daily_tasks_template[day_num]
    
    # Check if the day exists in sprint_data, if not, initialize it
    if day_str not in st.session_state.sprint_data['tasks']:
        st.session_state.sprint_data['tasks'][day_str] = [
            {'desc': task['desc'], 'type': task['type'], 'completed': False}
            for task in day_info['tasks']
        ]
    if day_str not in st.session_state.sprint_data['notes']:
        st.session_state.sprint_data['notes'][day_str] = ""
    if day_str not in st.session_state.sprint_data['timer_data']:
        st.session_state.sprint_data['timer_data'][day_str] = {'start_time': None, 'elapsed_time': 0}

    with st.expander(f"Day {day_num}: {day_info['date'].strftime('%B %d, %Y')}"):
        st.subheader("Tasks:")
        
        # Display tasks for the day
        for i, task in enumerate(st.session_state.sprint_data['tasks'][day_str]):
            # Use a unique key for each checkbox to ensure persistence
            checkbox_key = f"day_{day_str}_task_{i}"
            
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
                    st.session_state.sprint_data['tasks'][day_str][i]['completed'] = checked
                    save_data(st.session_state.sprint_data)
                    st.rerun() # Rerun to update progress bar immediately

        st.markdown("---")
        st.subheader("Timer (for focused work sessions):")
        
        # Timer functionality for the current day
        timer_data = st.session_state.sprint_data['timer_data'][day_str]
        
        col_start, col_stop = st.columns(2)
        
        with col_start:
            if st.button("Start Timer", key=f"start_timer_{day_str}"):
                timer_data['start_time'] = time.time()
                save_data(st.session_state.sprint_data)
                st.toast("Timer started!")
        
        with col_stop:
            if st.button("Stop Timer", key=f"stop_timer_{day_str}"):
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
        current_notes = st.session_state.sprint_data['notes'][day_str]
        new_notes = st.text_area(
            "Add your reflections, challenges, or key learnings here:",
            value=current_notes,
            height=150,
            key=f"notes_day_{day_str}"
        )
        if new_notes != current_notes:
            st.session_state.sprint_data['notes'][day_str] = new_notes
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
st.info("""
**Important Notes for Your 2-Hour Daily Sprint:**
* **Intensity is Key:** This schedule is extremely ambitious for 2 hours/day. You will need to be highly focused and minimize distractions.
* **Prioritization:** The plan attempts to cover all areas. If you fall behind, prioritize Google Cert completion, then Security+ foundational concepts, and finally TryHackMe labs.
* **Security+ Resources:** Professor Messer's free YouTube course is highly recommended for SY0-601/SY0-701. You can find it by searching "Professor Messer Security+ SY0-601" or "SY0-701" on YouTube.
* **TryHackMe:** Focus on completing the specified rooms/paths to gain quantifiable progress. Don't get stuck too long on one room; move on if necessary and revisit later.
* **Job Search:** Daily job search tasks are minimal. Consider dedicating extra time on weekends for applications and networking, or integrate quick checks into your daily routine if you finish learning tasks early.
* **Flexibility:** Life happens! If you miss a day, try to catch up on the weekend or adjust the following days slightly. Consistency is more important than perfection.
""")
