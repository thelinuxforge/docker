# Use official Python image
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Copy application code
COPY app.py .

# Install Flask
RUN pip install flask

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "app.py"]
