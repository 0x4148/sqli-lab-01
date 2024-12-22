# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . /app

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Install MySQL client
RUN apt-get update && \
    apt-get install -y default-mysql-client

# Expose port
EXPOSE 8070

# Run the application
CMD ["python", "app.py"]
