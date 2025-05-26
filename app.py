import streamlit as st
import pandas as pd
import datetime

st.set_page_config(page_title="30-Day Cybersecurity Sprint Dashboard", layout="wide")

# Title
st.title("🔐 30-Day Cybersecurity Sprint Tracker")
st.markdown("""
Welcome to your 30-day cybersecurity journey! This dashboard helps you track progress across:
- Google Cybersecurity Certificate 🎓
- TryHackMe Labs 🧪
- CompTIA Security+ Exam Prep 📚
- Job Applications 💼
""")

# Initialize session state if needed
if 'progress' not in st.session_state:
    st.session_state.progress = [False] * 30
    st.session_state.notes = ["" for _ in range(30)]
    st.session_state.time_spent = [0 for _ in range(30)]

# Progress bar
completed_days = sum(st.session_state.progress)
st.progress(completed_days / 30.0)
st.success(f"You've completed {completed_days} out of 30 days! ({completed_days * 100 // 30}%)")

# Define plan for 30 days
@st.cache_data
def load_plan():
    plan = []
    google_cert_modules = [
        "Foundations of Cybersecurity",
        "Play It Safe: Manage Security Risks",
        "Connect and Protect: Networks",
        "Tools of the Trade: Linux and SQL",
        "Assets, Threats, and Vulnerabilities",
        "Sound the Alarm: Detection and Response",
        "Automate Cybersecurity Tasks",
        "Put It to Work: Final Project"
    ]
    for day in range(1, 31):
        module_index = min((day - 1) // 4, len(google_cert_modules) - 1)
        day_plan = {
            "Day": f"Day {day}",
            "Google Cert": f"Finish part of: {google_cert_modules[module_index]}",
            "TryHackMe": (
                "Room: Introduction to Cyber Security" if day <= 5 else
                "Room: Pre-Security" if day <= 10 else
                "Room: Cyber Defence" if day <= 20 else
                "Room: Blue Team Labs"
            ),
            "Security+": (
                "Threats & Attacks" if day <= 5 else
                "Risk Mgmt" if day <= 10 else
                "Architecture & Design" if day <= 15 else
                "Identity & Access" if day <= 20 else
                "Cryptography & PKI" if day <= 25 else
                "Practice Questions"
            ),
            "Jobs": (
                "Update resume" if day == 1 else
                "Apply to 1 job" if day % 2 == 0 else
                "Research companies / roles"
            )
        }
        plan.append(day_plan)
    return pd.DataFrame(plan)

plan_df = load_plan()

# Timer helper
def timer_input(day_index):
    with st.expander("⏱ Track Time Spent"):
        minutes = st.slider("How many minutes did you study today?", 0, 120, 0, key=f"time_{day_index}")
        if st.button("Submit Time", key=f"submit_{day_index}"):
            st.session_state.time_spent[day_index] = minutes
            st.success(f"Recorded {minutes} minutes of study.")

# Tabs for each day
selected_day = st.selectbox("Select a Day to Update", [f"Day {i+1}" for i in range(30)])
day_index = int(selected_day.split(" ")[1]) - 1

# Show tasks
day_tasks = plan_df.iloc[day_index]
st.subheader(f"🗓 {day_tasks['Day']}")
st.markdown(f"**Google Cybersecurity Certificate Task:** {day_tasks['Google Cert']}")
st.markdown(f"**TryHackMe Lab Task:** {day_tasks['TryHackMe']}")
st.markdown(f"**Security+ Study Task:** {day_tasks['Security+']}")
st.markdown(f"**Job Search Task:** {day_tasks['Jobs']}")

# Daily completion checkbox
if st.checkbox("Mark this day as complete ✅", value=st.session_state.progress[day_index]):
    st.session_state.progress[day_index] = True
else:
    st.session_state.progress[day_index] = False

# Time tracking
timer_input(day_index)

# Notes section
note = st.text_area("📝 Your notes or reflections for today:", value=st.session_state.notes[day_index])
if st.button("Save Notes", key=f"note_{day_index}"):
    st.session_state.notes[day_index] = note
    st.success("Notes saved successfully!")

# Motivation section
st.markdown("---")
if completed_days >= 15:
    st.balloons()
    st.info("🚀 You're over halfway through your sprint! Keep going!")
elif completed_days >= 10:
    st.info("👏 You've completed 1/3rd of your sprint! Stay consistent.")
else:
    st.info("💡 Every day counts. Small steps lead to big wins.")

# Footer
st.markdown("---")
st.caption("Created with ❤️ for aspiring cybersecurity professionals.")
