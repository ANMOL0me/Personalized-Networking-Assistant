
=>Personalized Networking Assistant

An AI-powered networking assistant built with FastAPI and Streamlit

Generate personalized conversation starters for networking events and instantly fact-check claims using AI.

=>Overview

The Personalized Networking Assistant is an AI-based web application that helps users prepare for networking events by generating personalized conversation starters based on event descriptions and individual interests.

The application also includes a Quick Fact-Check feature that verifies claims or topics using an AI-powered backend.

The project follows a modern architecture:

-Frontend: Streamlit
-Backend: FastAPI
-AI Models: Hugging Face Transformers
-Communication: REST APIs

=>Features
-Personalized Networking Assistant
-Generate networking conversation starters
-Understands event descriptions
-Personalizes responses based on user interests
-Easy-to-use Streamlit interface
 -Quick Fact Check
-Verify facts instantly
-AI-powered claim analysis
-Simple one-click interface
 -REST API

>FastAPI provides APIs for:

-Analyze Event
-Generate Conversation
-Fact Check
-Tech Stack
-Technology	Purpose
-Python	Programming Language
-FastAPI	Backend API
-Streamlit	Frontend
-Hugging Face Transformers	NLP Models
-Uvicorn	ASGI Server
-Pydantic	Data Validation

=> Project Structure
```
networking-assistant/
├── app/
│   ├── models/
│   │   └── schemas.py          # Pydantic request/response models
│   ├── routers/
│   │   └── conversation.py     # FastAPI route handlers
│   ├── services/
│   │   ├── event_analyzer.py   # Zero-shot event theme extraction
│   │   ├── topic_generator.py  # GPT-2 conversation starter generation
│   │   ├── fact_checker.py     # External fact-check API integration
│   │   ├── history_logger.py   # Conversation history persistence
│   │   └── feedback_logger.py  # User feedback logging
│   ├── config.py               # Model names and API config
│   └── main.py                 # FastAPI app entry point
├── frontend/
│   └── streamlit_app.py        # Streamlit UI
├── tests/
│   ├── conftest.py
│   ├── test_event_analyzer.py
│   ├── test_fact_checker.py
│   ├── test_routes.py
│   └── test_topic_generator.py
├── requirements.txt
└── README.md
```
=>Installation = [installation.txt](https://github.com/ANMOL0me/Personalized-Networking-Assistant/blob/main/installation.txt)

=> Screenshots
Streamlit Frontend
<img src="Screenshot 2026-07-04 141719.png" width="900">
FastAPI Working and deployment on Railway
<img src="Screenshot 2026-07-04 141837.png" width="900">
FastAPI Swagger Documentation
<img src="Screenshot 2026-07-04 141850.png" width="900">
Installing Dependencies
<img src="Screenshot%202026-07-03%20004638.png" width="900">
Package Installation
<img src="Screenshot%202026-07-03%20004647.png" width="900">
 Future Improvements
User Authentication
Conversation History
Export Results as PDF
Multi-language Support
Speech-to-Text Input
Voice Assistant
OpenAI/Llama Integration
Cloud Deployment
Docker Support
 Requirements

Example

fastapi
uvicorn
streamlit
transformers
torch
pydantic
requests
Example Workflow
Launch FastAPI backend.
Launch Streamlit frontend.
Enter an event description.
Add your interests.
Click Generate Conversation Starters.
Review personalized networking suggestions.
Use Quick Fact Check to verify any claim.
 Future Deployment

The application can be deployed using:

Render (FastAPI)
Streamlit Community Cloud
Railway
Docker
AWS EC2
Azure App Service
=>Author
Anmol Soni
=>License
This project is intended for educational and learning purposes. Feel free to fork, modify, and enhance it.
