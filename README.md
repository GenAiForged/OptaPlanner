# Digital Twin for Manufacturing

This project is a starter kit for a digital twin in a manufacturing use-case. It includes a FastAPI backend, a simulator, a frontend dashboard, and a Docker setup to run everything.

## Components

### Backend

A FastAPI application that serves as the core of the digital twin.
- **REST API:** Exposes endpoints to get and update the twin's state.
- **WebSocket:** Pushes live telemetry data to connected clients (like the frontend).

### Simulator

A Python script that mimics sensor data.
- **`main.py`:** Publishes telemetry data (temperature, pressure) to an MQTT broker.
- **`mqtt_bridge.py`:** Subscribes to the MQTT topic and forwards the data to the backend's REST API.

### Frontend

A simple HTML dashboard.
- **`index.html`:** Displays live telemetry data using Chart.js, connected to the backend's WebSocket.

### Docker Setup

- **`Dockerfile`:** Each service (`backend`, `simulator`) has its own Dockerfile.
- **`docker-compose.yml`:** Orchestrates the deployment of all services, including an MQTT broker (Eclipse Mosquitto) and a web server (Nginx) for the frontend.

## How to Run

1. **Install Docker and Docker Compose.**
2. **Clone this repository.**
3. **Run the application:**
   ```bash
   docker-compose up --build
   ```
4. **Access the components:**
   - **Frontend Dashboard:** http://localhost:8080
   - **Backend API:** http://localhost:8000/docs

## Project Structure
```
.
├── backend
│   ├── Dockerfile
│   ├── main.py
│   └── requirements.txt
├── docker-compose.yml
├── frontend
│   └── index.html
├── README.md
└── simulator
    ├── Dockerfile
    ├── main.py
    ├── mqtt_bridge.py
    └── requirements.txt
```

## Extending the Project

This is a minimal setup. You can extend it by:
- Adding a database (e.g., Redis, InfluxDB) for persistent storage.
- Implementing more complex digital twin models.
- Integrating with other industrial protocols (e.g., OPC-UA).
- Adding machine learning models for predictive maintenance.
- Deploying to Kubernetes for a production environment.
