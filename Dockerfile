#using the official Python 3.11 image as the base
FROM python:3.11

#settingthe working directory inside the container
WORKDIR /app

#copying the requirements.txt file into the container
COPY requirements.txt .

#installing all Python dependencies listed in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

#copying all files from the current directory into the container
COPY . .

#giving execution permission to wait-for-it.sh so it can be run
RUN chmod +x wait-for-it.sh

#final command: wait for Postgres to be ready, then run etl.py
CMD ["./wait-for-it.sh", "postgres:5432", "--", "python", "etl.py"]






# # Base image
# FROM python:3.11-slim

# # Set work directory
# WORKDIR /app

# # Copy requirements and install
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# # Copy ETL script and data directory
# COPY etl.py .
# COPY data/ ./data/

# # Default command to run ETL script
# CMD ["python", "etl.py"]




# # Use an official Python image as a base
# FROM python:3.9-slim

# # Set the working directory inside the container
# WORKDIR /app

# # Install the necessary Python dependencies
# COPY requirements.txt .
# RUN pip install -r requirements.txt

# # Copy the scripts and data directories
# COPY ./scripts /scripts
# COPY ./data /data

# # Run the ETL script
# CMD ["python", "/scripts/data-ingest.py"]
