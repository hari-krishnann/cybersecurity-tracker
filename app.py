import streamlit as st
import pandas as pd

# Set up page
st.set_page_config(page_title="Cybersecurity Sprint Dashboard", layout="wide")

st.title("🔐 30-Day Cybersecurity Sprint Tracker")
st.markdown("""
Track your progress toward:
- Google Cybersecurity Certificate 🎓
- TryHackMe Labs 🧪
- CompTIA Security+ Exam Prep 📚
""")

# Initialize session state
if "progress" not in st.session_state:
    st.session_state.progress = [False] * 30
    st.session_state.notes = [""] * 30
    st.session_state.time_spent = [0] * 30

# Progress Bar
completed = sum(st.session_state.progress)
st.progress(completed / 30.0)
st.success(f"You've completed {completed}/30 days! ({(completed / 30) * 100:.1f}%)")

# Daily plan
def get_daily_plan():
    plan = []
    for i in range(30):
        plan.append({
            "Day": f"Day {i+1}",
            "Google Cert": f"Finish Lesson {(i)//3 + 1} on Coursera",
            "TryHackMe": (
                "Introduction to Cyber Security" if i < 5 else
                "Pre-Security" if i < 10 else
                "Cyber Defence" if i < 20 else
                "Blue Team Labs"
            ),
            "Security+": (
                "Threats & Attacks" if i < 5 else
                "Risk Management" if i < 10 else
                "Architecture & Design" if i < 15 else
                "Identity & Access Management" if i < 20 else
                "Cryptography & PKI" if i < 25 else
                "Review & Practice Tests"
            )
        })
    return pd.DataFrame(plan)

plan_df = get_daily_plan()

# Select Day
selected_day = st.selectbox("Select a Day", [f"Day {i+1}" for i in range(30)])
day_index = int(selected_day.split()[1]) - 1

# Show tasks
st.subheader(f"📅 {selected_day}")
st.markdown(f"**Google Cybersecurity Certificate Task:** {plan_df.iloc[day_index]['Google Cert']}")
st.markdown(f"**TryHackMe Task:** {plan_df.iloc[day_index]['TryHackMe']}")
st.markdown(f"**Security+ Topic:** {plan_df.iloc[day_index]['Security+']}")

# Task completion checkbox
st.session_state.progress[day_index] = st.checkbox(
    "Mark as Complete ✅", value=st.session_state.progress[day_index])

# Time tracking
with st.expander("⏱ Time Spent Tracker"):
    minutes = st.slider("How many minutes did you study today?", 0, 120, st.session_state.time_spent[day_index])
    if st.button("Save Time", key=f"time_{day_index}"):
        st.session_state.time_spent[day_index] = minutes
        st.success(f"{minutes} minutes saved!")

# Notes
note_input = st.text_area("📝 Your notes or thoughts for today:", value=st.session_state.notes[day_index])
if st.button("Save Notes", key=f"note_{day_index}"):
    st.session_state.notes[day_index] = note_input
    st.success("Note saved!")

# Motivation Section
st.markdown("---")
if completed >= 15:
    st.balloons()
    st.info("🚀 You're over halfway through. Keep pushing!")
elif completed >= 10:
    st.info("🎯 You've hit one-third milestone. Stay consistent!")
else:
    st.info("💡 Keep going—every small step adds up!")

# Footer
st.markdown("---")
st.caption("Made with ❤️ for cybersecurity warriors. Stay sharp, stay secure.")
