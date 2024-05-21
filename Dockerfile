# Use the official Python image from the Docker Hub
FROM python:3.9-slim

# Set the working directory
WORKDIR /LLM_Project

# Set the PYTHONPATH environment variable
ENV PYTHONPATH=/app

# Copy the requirements file to the working directory
COPY requirement.txt .

# Install the dependencies
RUN pip install --no-cache-dir -r requirement.txt

# Copy the entire application code
COPY . .

# Expose the port the app runs on
EXPOSE 8000

# Command to run the application
# CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
# Command to run the application
# CMD ["python", "main.py"]
CMD ["python", "-m", "main"]


