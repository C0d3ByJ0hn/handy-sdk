from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import requests
from handy_sdk import HandyAPI

app = FastAPI()

class ConnectionRequest(BaseModel):
    connection_key: str

class VelocityRequest(ConnectionRequest):
    velocity: int

class SlideRangeRequest(ConnectionRequest):
    min_value: int
    max_value: int

@app.post("/set_hamp_mode")
async def set_hamp_mode(request: ConnectionRequest):
    handy = HandyAPI(request.connection_key)
    try:
        handy.set_hamp_mode()
        return {"status": "Hamp mode set successfully."}
    except requests.HTTPError as err:
        raise HTTPException(status_code=500, detail=f"HTTP error occurred: {err}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

@app.post("/start_hamp")
async def start_hamp(request: ConnectionRequest):
    handy = HandyAPI(request.connection_key)
    try:
        handy.start_hamp()
        return {"status": "Hamp started successfully."}
    except requests.HTTPError as err:
        raise HTTPException(status_code=500, detail=f"HTTP error occurred: {err}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

@app.post("/stop_hamp")
async def stop_hamp(request: ConnectionRequest):
    handy = HandyAPI(request.connection_key)
    try:
        handy.stop_hamp()
        return {"status": "Hamp stopped successfully."}
    except requests.HTTPError as err:
        raise HTTPException(status_code=500, detail=f"HTTP error occurred: {err}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

@app.post("/set_hamp_velocity")
async def set_hamp_velocity(request: VelocityRequest):
    handy = HandyAPI(request.connection_key)
    try:
        handy.set_hamp_velocity(velocity=request.velocity)
        return {"status": f"Hamp velocity set to {request.velocity}."}
    except requests.HTTPError as err:
        raise HTTPException(status_code=500, detail=f"HTTP error occurred: {err}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

@app.post("/set_hamp_slide")
async def set_hamp_slide(request: SlideRangeRequest):
    handy = HandyAPI(request.connection_key)
    try:
        handy.set_hamp_slide(min_value=request.min_value, max_value=request.max_value)
        return {"status": f"Hamp slide range set from {request.min_value} to {request.max_value}."}
    except requests.HTTPError as err:
        raise HTTPException(status_code=500, detail=f"HTTP error occurred: {err}")
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"An error occurred: {e}")

