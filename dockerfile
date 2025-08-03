# Use Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy your code
COPY . .

# Run the Python app
CMD ["python", "app.py"]
