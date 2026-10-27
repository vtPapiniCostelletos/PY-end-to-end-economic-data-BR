FROM apache/airflow:3.3.1-python3.14

###  With .VENV
#--------------------
#WORKDIR /app

#COPY pyproject.toml uv.lock ./

#RUN uv lock
#RUN uv sync
#--------------------
COPY requirements.txt .
RUN pip install -r requirements.txt