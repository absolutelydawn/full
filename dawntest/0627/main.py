from fastapi import FastAPI, HTTPException, Request
from pydantic import BaseModel
from typing import Optional
import pandas as pd
import logging

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
    logger.debug(f"Received gyro data: {gyro_data}")  # 로그 추가
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

# 로깅 설정
logging.basicConfig(level=logging.DEBUG)
logger = logging.getLogger(__name__)

try:
    # JSON 파일을 읽어 DataFrame으로 변환
    df = pd.read_json('light_intensity_data.json')
    df['datetime'] = pd.to_datetime(df['datetime'])  # datetime 컬럼을 datetime 형식으로 변환
    logger.debug("JSON data loaded successfully.")
except Exception as e:
    logger.exception("Failed to load JSON data.")
    raise

@app.get("/light_intensity/{date}")
def read_light_intensity(date: str):
    logger.debug(f"Received request for date: {date}")
    try:
        # 날짜 형식 맞추기
        selected_date = pd.to_datetime(date)
        logger.debug(f"Parsed date: {selected_date}")
        
        # 해당 날짜의 데이터 필터링
        day_data = df[df['datetime'].dt.date == selected_date.date()]
        
        if day_data.empty:
            logger.error(f"No data found for date: {selected_date}")
            raise HTTPException(status_code=404, detail="Data not found for the given date.")
        
        logger.debug(f"Data for date {selected_date}: {day_data}")
        return day_data.to_dict(orient='records')
    
    except Exception as e:
        logger.exception("An error occurred while processing the request.")
        raise HTTPException(status_code=500, detail=str(e))

# FastAPI 서버 실행
if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)
