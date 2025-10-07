from fastapi import FastAPI, WebSocket, WebSocketDisconnect
from pydantic import BaseModel
from typing import List, Optional

app = FastAPI()

class DigitalTwinState(BaseModel):
    temperature: Optional[float] = None
    pressure: Optional[float] = None
    status: Optional[str] = "offline"

state = DigitalTwinState()

class ConnectionManager:
    def __init__(self):
        self.active_connections: List[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)

manager = ConnectionManager()

@app.get("/state", response_model=DigitalTwinState)
def get_state():
    return state

@app.post("/state", response_model=DigitalTwinState)
async def update_state(new_state: DigitalTwinState):
    global state
    state = new_state
    await manager.broadcast(state.json())
    return state

@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await manager.connect(websocket)
    try:
        while True:
            data = await websocket.receive_text()
            # Not doing anything with received data for now
    except WebSocketDisconnect:
        manager.disconnect(websocket)
