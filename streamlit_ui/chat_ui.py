import streamlit as st
import requests
from datetime import datetime

st.title("🗓️ Appointment Booking Agent")

user_input = st.chat_input("How can I help you today?")
if user_input:
    st.chat_message("user").write(user_input)

    # Modify this to dynamically parse the time from user_input later
    request_payload = {
        "user_name": "User",
        "time": "2025-06-26T15:00:00"
    }

    try:
        response = requests.post(
            "https://tailor-talk-booking-agent.onrender.com/check_availability/",
            json=request_payload
        )

        # Debug output to diagnose response content
        st.write("Status code:", response.status_code)
        st.write("Raw response text:", response.text)

        # Try to parse JSON safely
        try:
            data = response.json()
            st.write("Parsed JSON:", data)
            slots = data.get("available_slots", [])
        except Exception as json_error:
            st.error(f"⚠️ Failed to parse JSON: {json_error}")
            st.stop()

        # Display available slots
        if slots:
            formatted = "\n".join(
                f"• {datetime.fromisoformat(slot).strftime('%d %B %Y at %I:%M %p')}"
                for slot in slots
            )
            st.chat_message("assistant").markdown(f"✅ Here are the available slots:\n{formatted}")
        else:
            st.chat_message("assistant").markdown("❌ No available slots at that time.")

    except requests.exceptions.RequestException as e:
        st.error(f"🚫 Request failed: {e}")



