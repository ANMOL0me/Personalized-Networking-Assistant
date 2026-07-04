import streamlit as st
import requests
import json
from pathlib import Path
import sys

# Add root project directory to Python path
sys.path.append(str(Path(__file__).resolve().parent.parent))

from app.services import feedback_logger

# ----------------------------
# Railway Backend URL
# ----------------------------
BASE_URL = "https://personalized-networking-assistant-production-265c.up.railway.app"

st.set_page_config(
    page_title="Personalized Networking Assistant",
    page_icon="🤝",
    layout="wide"
)


st.title("🤝 Personalized Networking Assistant")
st.error("VERSION 2 - DEBUG MODE")
st.write("Generate conversation starters for networking events.")

# ============================================================
# Generate Conversation Starters
# ============================================================

st.subheader("Generate Conversation Starters")

event_description = st.text_area(
    "Event Description",
    placeholder="Example: AI Conference in Bangalore"
)

user_interests = st.text_input(
    "Your Interests",
    placeholder="Python, Machine Learning"
)

if st.button("Generate Conversation Starters"):

    if not event_description or not user_interests:
        st.warning("Please enter both Event Description and Interests.")

    else:

        payload = {
            "description": event_description,
            "interests": [
                x.strip()
                for x in user_interests.split(",")
                if x.strip()
            ]
        }

        try:

            response = requests.post(
                f"{BASE_URL}/conversation/generate-conversation",
                json=payload,
                timeout=120
            )

            st.write("### Debug Information")
            st.write("Status Code:", response.status_code)
            st.write("Response:")
            st.code(response.text)

            response.raise_for_status()

            data = response.json()

            st.session_state["topics"] = data.get("topics", [])
            st.session_state["suggestions"] = data.get("suggestions", [])

        except requests.exceptions.HTTPError as e:
            st.error("HTTP Error")
            st.exception(e)

        except requests.exceptions.ConnectionError as e:
            st.error("Could not connect to Railway backend.")
            st.exception(e)

        except requests.exceptions.Timeout as e:
            st.error("Backend timed out.")
            st.exception(e)

        except Exception as e:
            st.error("Unexpected Error")
            st.exception(e)

# ============================================================
# Display Results
# ============================================================

if "topics" in st.session_state:

    st.success("Conversation generated successfully!")

    st.subheader("Extracted Topics")

    for topic in st.session_state["topics"]:
        st.write("•", topic)

    st.subheader("Conversation Starters")

    for i, suggestion in enumerate(st.session_state["suggestions"]):

        st.markdown(f"**{i+1}. {suggestion}**")

        col1, col2 = st.columns(2)

        with col1:
            if st.button("👍", key=f"like_{i}"):

                feedback_logger.log_feedback(
                    suggestion,
                    "like"
                )

                st.success("Feedback saved.")

        with col2:
            if st.button("👎", key=f"dislike_{i}"):

                feedback_logger.log_feedback(
                    suggestion,
                    "dislike"
                )

                st.info("Feedback saved.")

# ============================================================
# Fact Check
# ============================================================

st.divider()

st.subheader("Fact Check")

query = st.text_input(
    "Topic",
    placeholder="Artificial Intelligence"
)

if st.button("Fact Check"):

    if query:

        try:

            response = requests.post(
                f"{BASE_URL}/conversation/fact-check",
                json={"query": query},
                timeout=120
            )

            st.write("Status:", response.status_code)
            st.code(response.text)

            response.raise_for_status()

            data = response.json()

            st.success(data["summary"])

        except Exception as e:
            st.exception(e)

# ============================================================
# Conversation History
# ============================================================

st.divider()

st.subheader("Conversation History")

history_file = Path("history.json")

if st.button("Show History"):

    if history_file.exists():

        history = json.loads(history_file.read_text())

        for item in reversed(history[-5:]):

            st.markdown(f"### {item['timestamp']}")
            st.write("Event:", item["description"])
            st.write("Interests:", ", ".join(item["interests"]))
            st.write("Topics:", ", ".join(item["topics"]))

            st.write("Suggestions")

            for s in item["suggestions"]:
                st.write("-", s)

            st.divider()

    else:
        st.info("No history found.")

# ============================================================
# Feedback History
# ============================================================

st.divider()

st.subheader("Feedback History")

feedback_file = Path("feedback.json")

if st.button("Show Feedback"):

    if feedback_file.exists():

        feedback = json.loads(feedback_file.read_text())

        for item in reversed(feedback[-10:]):

            icon = "👍" if item["feedback"] == "like" else "👎"

            st.write(
                f"{icon} {item['suggestion']}"
            )

            st.caption(item["timestamp"])

    else:
        st.info("No feedback available.")
