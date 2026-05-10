import os
import sys
from pathlib import Path

import streamlit as st
from dotenv import load_dotenv

# Add parent directory to path
sys.path.insert(0, str(Path(__file__).parent.parent))

from data.json_store import load_data, save_data, get_data_as_string
from services.chatbot_service import AppointmentChatBot

def show_chatbot_page():
    load_dotenv()

    st.title("AI Appointment Assistant")
    st.write("Ask questions about appointment data.")

    api_key = os.getenv("OPENAI_API_KEY")

    if not api_key:
        st.error("OPENAI_API_KEY was not found. Check your .env file.")
        st.stop()

    appointments_context = get_data_as_string("appointments.json")
    bot = AppointmentChatBot(api_key, appointments_context)

    if "chat_messages" not in st.session_state:
        st.session_state["chat_messages"] = []

        logs = load_data("chat_logs.json")

        for log in logs:
            st.session_state["chat_messages"].append({
                "role": "user",
                "content": log["user_message"]
            })
            st.session_state["chat_messages"].append({
                "role": "assistant",
                "content": log["assistant_message"]
            })

        if len(st.session_state["chat_messages"]) == 0:
            st.session_state["chat_messages"].append({
                "role": "assistant",
                "content": "Hi! Ask me a question about your appointments."
            })

    for msg in st.session_state["chat_messages"]:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    user_input = st.chat_input("Type your question...")

    if user_input:
        st.session_state["chat_messages"].append({
            "role": "user",
            "content": user_input
        })

        with st.chat_message("user"):
            st.markdown(user_input)

        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                response_text = bot.get_ai_response(
                    st.session_state["chat_messages"]
                )
                st.markdown(response_text)

        st.session_state["chat_messages"].append({
            "role": "assistant",
            "content": response_text
        })

        logs = load_data("chat_logs.json")
        logs.append({
            "user_message": user_input,
            "assistant_message": response_text
        })
        save_data("chat_logs.json", logs)