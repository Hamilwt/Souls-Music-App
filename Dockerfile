# Start with an official Python base image
FROM python:3.12-slim

# Set the working directory inside the container
WORKDIR /app

# Copy the requirements file first to leverage Docker cache
COPY requirements.txt .

# Install the Python libraries
RUN pip install -r requirements.txt

# Copy the rest of the application code into the container
# This will copy app.py, the templates folder, and the static folder
COPY . .

# Tell Docker the container listens on port 5000
EXPOSE 5000

# The command to run when the container starts
CMD ["python", "app.py"]