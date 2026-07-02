# !/bin/bash

# Start FastAPI in the background
uvicorn app.main:app --host 0.0.0.0 --port 8000 &

# Start Streamlit
streamlit run frontend/streamlit_app.py \
  --server.port=$PORT \
  --server.address=0.0.0.0
 export API_URL=http://localhost:8000
