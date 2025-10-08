from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import asyncio
import json
from backend.pinn_model import get_optimized_layout

app = FastAPI()

# In-memory storage for telemetry data
telemetry_data = {"temperature": 0, "pressure": 0}

@app.get("/")
def read_root():
    return {"message": "Digital Twin Backend"}

@app.post("/telemetry")
async def update_telemetry(data: dict):
    global telemetry_data
    telemetry_data.update(data)
    return {"message": "Telemetry data updated successfully"}

@app.get("/telemetry")
def get_telemetry():
    return telemetry_data

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    try:
        while True:
            await websocket.send_text(json.dumps(telemetry_data))
            await asyncio.sleep(1)
    except Exception as e:
        print(f"WebSocket error: {e}")
    finally:
        await websocket.close()

@app.post("/api/pinn/optimize")
async def run_pinn_optimization():
    """
    Endpoint to run the PINN optimization.
    """
    results = get_optimized_layout()
    return results