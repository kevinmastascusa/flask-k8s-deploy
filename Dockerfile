FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
COPY app.py .
COPY generate_model.py .

RUN pip install --no-cache-dir -r requirements.txt
RUN python generate_model.py

EXPOSE 5000

CMD ["python", "app.py"]
