FROM python:3.10

WORKDIR /app

RUN apt-get update \
    && apt-get install -y libgl1-mesa-glx \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8080

# Run the command to start the development server
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8080"]
