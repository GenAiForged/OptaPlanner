# Digital Twin for Manufacturing with PINN-based Optimization

This project is a starter kit for a digital twin in a manufacturing use-case. It includes a FastAPI backend with a Physics-Informed Neural Network (PINN) for optimization, a simulator, a frontend dashboard, and a Docker setup to run everything.

## Components

### Backend

A FastAPI application that serves as the core of the digital twin.
- **REST API:** Exposes endpoints to get and update the twin's state. It also includes an endpoint to trigger the PINN-based optimization.
- **WebSocket:** Pushes live telemetry data to connected clients (like the frontend).
- **PINN Model:** A simple Physics-Informed Neural Network (PINN) implemented with PyTorch. This model serves as a proof-of-concept for incorporating physical constraints into an optimization process.

### Simulator

A Python script that mimics sensor data.
- **`main.py`:** Publishes telemetry data (temperature, pressure) to an MQTT broker.
- **`mqtt_bridge.py`:** Subscribes to the MQTT topic and forwards the data to the backend's REST API.

### Frontend

A simple HTML dashboard.
- **`index.html`:** Displays live telemetry data using Chart.js and provides a button to run the PINN optimization and view the results.

### Docker Setup

- **`Dockerfile`:** Each service (`backend`, `simulator`) has its own Dockerfile.
- **`docker-compose.yml`:** Orchestrates the deployment of all services, including an MQTT broker (Eclipse Mosquitto) and a web server (Nginx) for the frontend.

## How to Run

1. **Install Docker and Docker Compose.**
2. **Clone this repository.**
3. **Run the application:**
   ```bash
   docker compose up --build
   ```
4. **Access the components:**
   - **Frontend Dashboard:** http://localhost:8080
   - **Backend API:** http://localhost:8000/docs

## Physics-Informed Neural Network (PINN)

The PINN included in this project is a simple proof-of-concept to demonstrate how physical constraints can be incorporated into a neural network model. It solves a simple ordinary differential equation (ODE), `dy/dx = -y`, with the boundary condition `y(0) = 1`.

In a real-world manufacturing scenario, this PINN could be extended to model more complex physical phenomena, such as:
- **Material Flow:** Optimizing the layout of a factory floor to minimize the distance materials travel.
- **Machine Dynamics:** Predicting the wear and tear on a machine based on its operational parameters.

## Project Structure
```
.
├── backend
│   ├── Dockerfile
│   ├── main.py
│   ├── pinn_model.py
│   └── requirements.txt
├── docker-compose.yml
├── frontend
│   ├── index.html
│   └── nginx.conf
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
- Implementing more complex digital twin models and PINNs.
- Integrating with other industrial protocols (e.g., OPC-UA).
- Adding machine learning models for predictive maintenance.
- Deploying to Kubernetes for a production environment.