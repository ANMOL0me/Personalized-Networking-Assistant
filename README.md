# 🤝 Personalized Networking Assistant

An AI-powered networking assistant that generates personalized conversation starters for events based on your interests, powered by HuggingFace Transformers and FastAPI.

---

## 📁 Project Structure

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

---

## 🚀 Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/your-username/networking-assistant.git
cd networking-assistant
```

### 2. Create and activate a virtual environment

```bash
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate
```

### 3. Install dependencies

```bash
pip install -r requirements.txt
```

---

## ▶️ Running the App

### Start the FastAPI backend

```bash
uvicorn app.main:app --reload
```

The API will be available at `http://127.0.0.1:8000`.  
Interactive docs: `http://127.0.0.1:8000/docs`

### Start the Streamlit frontend

In a separate terminal:

```bash
cd frontend
streamlit run streamlit_app.py
```

The UI will open at `http://localhost:8501`.

---

## 🔌 API Endpoints

| Method | Endpoint | Description |
|--------|----------|-------------|
| `GET` | `/` | Health check / welcome message |
| `POST` | `/analyze-event` | Extract top themes from event description |
| `POST` | `/generate-conversation` | Generate personalized conversation starters |
| `POST` | `/fact-check` | Fact-check a topic via external API |

### Example request — Generate Conversation

```bash
curl -X POST "http://127.0.0.1:8000/generate-conversation" \
  -H "Content-Type: application/json" \
  -d '{"description": "AI in healthcare", "interests": ["ethics", "automation"]}'
```

---

## 🧪 Running Tests

```bash
pytest tests/
```

---

## 🛠️ Tech Stack

- **Backend:** FastAPI, Uvicorn
- **AI Models:** HuggingFace Transformers (BART zero-shot classification, GPT-2 text generation)
- **Frontend:** Streamlit
- **Testing:** Pytest, FastAPI TestClient
- **Data persistence:** JSON files (`history.json`, `feedback.json`)

---

## 📝 Notes

- On first run, HuggingFace models will be downloaded automatically (~1–2 GB).
- The fact-checker uses an external API (`FACT_CHECK_API` in `config.py`) — update this URL to point to a real fact-checking service.
- History and feedback are stored locally as JSON files in the project root.
