FROM python:3.12-slim

WORKDIR /app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt

RUN chmod +x start.sh

EXPOSE 8000
EXPOSE 8501

CMD ["./start.sh"]
<<<<<<< HEAD:dockerfile


=======
>>>>>>> 027e40baec6c3f6b57e61c3fc28af5233b68323b:Dockerfile
