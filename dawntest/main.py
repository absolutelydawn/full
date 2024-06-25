from fastapi import FastAPI, Request
from pydantic import BaseModel
from typing import Optional

app = FastAPI()

class SensorData(BaseModel):
    value: int

class GyroData(BaseModel):
    AcX: int
    AcY: int
    AcZ: int
    Tmp: float
    GyX: int
    GyY: int
    GyZ: int

sensor_value = 0
gyro_data = {}
led_status = "off"

@app.post("/update")
async def update_sensor(data: SensorData):
    global sensor_value
    sensor_value = data.value
    return {"status": "success"}

@app.post("/gyro")
async def update_gyro(data: GyroData):
    global gyro_data
    gyro_data = data.dict()
    return {"status": "success"}

@app.get("/value")
async def get_sensor_value():
    return {"value": sensor_value}

@app.get("/gyro")
async def get_gyro_data():
    return gyro_data

@app.post("/status")
async def update_status(status: Optional[str] = None):
    global led_status
    if status:
        led_status = status
    return {"led_status": led_status}

@app.get("/status")
async def get_status():
    return {"led_status": led_status}
