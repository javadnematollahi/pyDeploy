FROM python:3.10.13-bullseye

# 
WORKDIR /code

# 
COPY /requirements.txt /code/requirements.txt

RUN apt-get update && apt-get install -y libpq-dev build-essential
# 
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# 
COPY /app /code/app

# 
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "80", "--reload"]