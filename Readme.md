For installation refer to [installation.txt]
 Personalized Networking Assistant
<div align="center">
 Personalized Networking Assistant

An AI-powered networking assistant built with FastAPI and Streamlit

Generate personalized conversation starters for networking events and instantly fact-check claims using AI.

</div>
 Overview

The Personalized Networking Assistant is an AI-based web application that helps users prepare for networking events by generating personalized conversation starters based on event descriptions and individual interests.

The application also includes a Quick Fact-Check feature that verifies claims or topics using an AI-powered backend.

The project follows a modern architecture:

Frontend: Streamlit
Backend: FastAPI
AI Models: Hugging Face Transformers
Communication: REST APIs
 Features
 Personalized Networking Assistant
Generate networking conversation starters
Understands event descriptions
Personalizes responses based on user interests
Easy-to-use Streamlit interface
 Quick Fact Check
Verify facts instantly
AI-powered claim analysis
Simple one-click interface
 REST API

FastAPI provides APIs for:

Analyze Event
Generate Conversation
Fact Check
🛠 Tech Stack
Technology	Purpose
Python	Programming Language
FastAPI	Backend API
Streamlit	Frontend
Hugging Face Transformers	NLP Models
Uvicorn	ASGI Server
Pydantic	Data Validation
 Project Structure
project/
│
├── backend/
│   ├── main.py
│   ├── models.py
│   ├── utils.py
│   └── requirements.txt
│
├── frontend/
│   ├── app.py
│   └── requirements.txt
│
├── README.md
└── .gitignore
⚙ Installation
1. Clone Repository
git clone https://github.com/yourusername/networking-assistant.git

cd networking-assistant
2. Create Virtual Environment

Windows

python -m venv venv

Activate

venv\Scripts\activate

Mac/Linux

python3 -m venv venv

source venv/bin/activate
3. Install Dependencies
pip install -r requirements.txt
▶ Running the Backend

Start FastAPI server

uvicorn main:app --reload

Backend runs at

http://127.0.0.1:8000

Swagger Documentation

http://127.0.0.1:8000/docs
▶ Running the Frontend

Open another terminal

streamlit run app.py

The application will open automatically in your browser.

Usually at

http://localhost:8501
 API Endpoints
Method	Endpoint	Description
POST	/analyze-event	Analyze event description
POST	/generate-conversation	Generate conversation starters
POST	/fact-check	Verify facts
GET	/	Root Endpoint
🖥 Application Screens
Main Interface
Enter Event Description
Enter Your Interests
Generate Conversation Starters
Quick Fact Check
FastAPI Swagger UI

Provides interactive API testing for all endpoints.

📷 Screenshots
Streamlit Frontend
<img src="Screenshot%202026-07-02%20225852(1).png" width="900">
FastAPI Swagger Documentation
<img src="Screenshot%202026-07-03%20004627.png" width="900">
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
 Author

Anmol Soni

AI & Data Science Enthusiast

 License

This project is intended for educational and learning purposes. Feel free to fork, modify, and enhance it.