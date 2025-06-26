
# import streamlit as st
# import requests

# st.title("🗓️ Appointment Booking Agent")

# user_input = st.chat_input("How can I help you today?")
# if user_input:
#     st.write("You said:", user_input)
#     response = requests.post("http://localhost:8000/check_availability/", json={
#         "user_name": "User",
#         "time": "2025-06-26T15:00:00"
#     })
#     st.write("Response:", response.json())



import streamlit as st
import requests
from datetime import datetime

st.title("🗓️ Appointment Booking Agent")

user_input = st.chat_input("How can I help you today?")
if user_input:
    st.chat_message("user").write(user_input)

    # Send POST request to FastAPI backend
    response = requests.post("http://localhost:8000/check_availability/", json={
        "user_name": "User",
        "time": "2025-06-26T15:00:00"
    })

    slots = response.json().get("available_slots", [])

    # ✅ Format response instead of showing raw JSON
    if slots:
        formatted = "\n".join(
            f"• {datetime.fromisoformat(slot).strftime('%d %B %Y at %I:%M %p')}" for slot in slots
        )
        st.chat_message("assistant").markdown(f"✅ Here are the available slots:\n{formatted}")
    else:
        st.chat_message("assistant").markdown("❌ No available slots at that time.")
