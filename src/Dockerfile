FROM python:3.12-slim

# Install dependencies and clean up in a single RUN step to reduce layers
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
        build-essential \
        libpq-dev \
        python3-dev \
        python3-pip \
        python3-setuptools \
        python3-wheel \
        python3-cffi \
        shared-mime-info \
        iputils-ping \
        curl && \
    pip install --no-cache-dir --upgrade pip && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy only the requirements first to leverage Docker cache
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application code
COPY . .

# Set PYTHONPATH environment variable
ENV PYTHONPATH "${PYTHONPATH}:/app/src"

# Expose port 8080
EXPOSE 8080

# Install the package in editable mode
RUN pip install --no-cache-dir --editable .

# Command to run the application
CMD ["gunicorn", "--bind", "0.0.0.0:8080", "src.app.app:create_app()"]
