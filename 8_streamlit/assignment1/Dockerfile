FROM python:3.9-slim

WORKDIR /code
 
COPY /requirements.txt /code/requirements.txt

RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    git \
    && rm -rf /var/lib/apt/lists/*

RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

COPY /counter.py /code/counter.py

EXPOSE 8501

HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health

ENTRYPOINT ["streamlit", "run", "counter.py", "--server.port=8501", "--server.address=0.0.0.0"]