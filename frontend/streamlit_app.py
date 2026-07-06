import streamlit as st
import requests
import json
from pathlib import Path
import sys

# Add project root
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.services import feedback_logger

# Railway Backend URL
BASE_URL = "https://personalized-networking-assistant-production.up.railway.app"

# ---------------------------------------------------
# PAGE TITLE
# ---------------------------------------------------

st.set_page_config(
    page_title="Personalized Networking Assistant",
    page_icon="🤝",
    layout="centered"
)

st.title("🤝 Personalized Networking Assistant")
st.write(
    "Generate personalized conversation starters for networking events."
)

# ---------------------------------------------------
# INPUT
# ---------------------------------------------------

with st.container(border=True):

    event_description = st.text_area(
        "What's the event about?",
        placeholder="Example: A startup networking event for AI founders"
    )

    user_interests = st.text_input(
        "Your interests (comma-separated)",
        placeholder="AI, Cricket, Music, Startups"
    )

    generate_clicked = st.button(
        "Generate Conversation Starters",
        use_container_width=True
    )

# ---------------------------------------------------
# GENERATE CONVERSATIONS
# ---------------------------------------------------

if generate_clicked:

    if event_description and user_interests:

        payload = {
            "description": event_description,
            "interests": [
                interest.strip()
                for interest in user_interests.split(",")
            ]
        }

        try:

            response = requests.post(
                f"{BASE_URL}/conversation/generate-conversation",
                json=payload,
                timeout=60
            )

            if response.status_code == 200:

                data = response.json()

                st.session_state["topics"] = data["topics"]
                st.session_state["suggestions"] = data["suggestions"]

            else:

                st.error(f"Status Code: {response.status_code}")
                st.code(response.text)

        except requests.exceptions.RequestException as e:

            st.error(f"Connection Error:\n{e}")

    else:

        st.warning("Please enter both an event description and your interests.")

# ---------------------------------------------------
# RESULTS
# ---------------------------------------------------

if "suggestions" in st.session_state:

    st.markdown("---")
    st.subheader("💬 Conversation Starters")

    for i, suggestion in enumerate(st.session_state["suggestions"]):

        with st.container(border=True):

            st.write(suggestion)

            col1, col2 = st.columns(2)

            with col1:

                if st.button("👍", key=f"like_{i}"):

                    feedback_logger.log_feedback(
                        suggestion,
                        "like"
                    )

                    st.success("Thanks for the feedback!")

            with col2:

                if st.button("👎", key=f"dislike_{i}"):

                    feedback_logger.log_feedback(
                        suggestion,
                        "dislike"
                    )

                    st.info("Feedback recorded.")

# ---------------------------------------------------
# FACT CHECK
# ---------------------------------------------------

st.markdown("---")
st.subheader("🔍 Quick Fact Check")

query = st.text_input(
    "Enter a topic",
    placeholder="Artificial Intelligence"
)

if st.button("Fact Check"):

    if query:

        try:

            response = requests.post(
                f"{BASE_URL}/conversation/fact-check",
                json={"query": query},
                timeout=60
            )

            if response.status_code == 200:

                st.success(response.json()["summary"])

            else:

                st.error(f"Status Code: {response.status_code}")
                st.code(response.text)

        except requests.exceptions.RequestException as e:

            st.error(f"Connection Error:\n{e}")

# ---------------------------------------------------
# HISTORY
# ---------------------------------------------------

st.markdown("---")
st.subheader("📜 Previous Conversations")

if st.button("Show History"):

    history_path = Path("history.json")

    if history_path.exists():

        with open(history_path, "r") as f:

            history = json.load(f)

        for item in reversed(history[-5:]):

            with st.container(border=True):

                st.markdown(f"**{item['timestamp']}**")
                st.write("**Event:**", item["description"])
                st.write("**Interests:**", ", ".join(item["interests"]))
                st.write("**Topics:**", ", ".join(item["topics"]))

                st.write("**Suggestions:**")

                for suggestion in item["suggestions"]:

                    st.markdown(f"- {suggestion}")

    else:

        st.info("No history found.")

# ---------------------------------------------------
# FEEDBACK
# ---------------------------------------------------

st.markdown("---")
st.subheader("📝 Feedback History")

feedback_path = Path("feedback.json")

if st.button("Show Feedback"):

    if feedback_path.exists():

        with open(feedback_path, "r") as f:

            feedback = json.load(f)

        for item in reversed(feedback[-10:]):

            icon = "👍" if item["feedback"] == "like" else "👎"

            with st.container(border=True):

                st.markdown(f"{icon} **{item['suggestion']}**")
                st.caption(item["timestamp"])

    else:

        st.info("No feedback available.")