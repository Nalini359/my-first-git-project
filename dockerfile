# Use official Python image as base
FROM python:3.9-slim

# Set working directory inside the container
WORKDIR /app

# Copy current directory contents into the container
COPY . .

# Run the app when container starts
CMD ["python", "app.py"]
