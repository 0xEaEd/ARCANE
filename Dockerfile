# Dockerfile for Django Application

# Use the official Python image from the Docker Hub
FROM python:3.9

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set the working directory in the container
WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /app
COPY . .

# Command to run the application
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]