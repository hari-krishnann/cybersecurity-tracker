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
    """Loads sprint data from a JSON file and ensures all necessary keys are present for backward compatibility."""
    loaded_data = {}
    if os.path.exists(DATA_FILE):
        try:
            with open(DATA_FILE, 'r') as f:
                loaded_data = json.load(f)
        except json.JSONDecodeError:
            st.error("Error decoding sprint_data.json. Starting with fresh data.")
            # loaded_data remains empty, so default values will be used
        except Exception as e:
            st.error(f"An unexpected error occurred while loading data: {e}. Starting with fresh data.")
            # loaded_data remains empty

    # Define the default structure and ensure all keys exist in loaded_data
    # This handles cases where old JSON files might be missing new keys
    if 'tasks' not in loaded_data:
        loaded_data['tasks'] = {}
    if 'notes' not in loaded_data:
        loaded_data['notes'] = {}
    if 'timer_data' not in loaded_data:
        loaded_data['timer_data'] = {}
    if 'jobs_applied_daily' not in loaded_data:
        loaded_data['jobs_applied_daily'] = {}
    if 'tryhackme_rooms_completed' not in loaded_data:
        loaded_data['tryhackme_rooms_completed'] = 0
    if 'tryhackme_points_gained' not in loaded_data:
        loaded_data['tryhackme_points_gained'] = 0

    return loaded_data

# --- Initialize Session State and Load Data ---
if 'sprint_data' not in st.session_state:
    st.session_state.sprint_data = load_data()

# This loop ensures that for each day in the template, the nested dictionaries
# (tasks, notes, timer_data, jobs_applied_daily) are correctly initialized
# within the loaded/default sprint_data.
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
    if day_str not in st.session_state.sprint_data['jobs_applied_daily']:
        st.session_state.sprint_data['jobs_applied_daily'][day_str] = 0


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
st.info(f"""
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

