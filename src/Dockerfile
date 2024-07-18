FROM python:3.12-slim

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    libpq-dev

# Set the working directory
WORKDIR /app

# Copy requirements first to leverage Docker cache
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application
COPY . .

# Install the application
RUN pip install --no-cache-dir -e .

# Set environment variable for Python path
ENV PYTHONPATH=/app

# Command to run the application
CMD ["gunicorn", "main:app", "--bind", "0.0.0.0:8080"]