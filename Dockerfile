
# Stage 1: build environment
FROM python:3.12-slim AS base

# Set workdir
WORKDIR /app

# Install deps
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app
COPY app ./app
COPY templates ./templates
COPY db ./db
COPY init_db.py ./init_db.py

# Expose port
EXPOSE 8080

# Initialize database at container start if not exists, then run
CMD ["/bin/sh", "-c", "python init_db.py && python -m flask --app app.app run --host=0.0.0.0 --port=8080"]
