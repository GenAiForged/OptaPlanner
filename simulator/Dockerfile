# Use an official Python runtime as a parent image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container at /app
COPY simulator/requirements.txt .

# Install any needed packages specified in requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the simulator code into the container
COPY simulator/ ./simulator

# Run the mqtt_bridge.py when the container launches
# This bridge will connect to the MQTT broker and forward messages to the backend
CMD ["python", "simulator/mqtt_bridge.py"]