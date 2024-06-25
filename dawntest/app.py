import streamlit as st
import requests
import time
from datetime import datetime
import pytz

# 한국 시간대 설정
KST = pytz.timezone('Asia/Seoul')

st.title("Sensor Control Dashboard")

sensor_values = []
gyro_values = []

# 스타일 추가
sensor_box_style = """
    <style>
    .sensor-box {
        border: 2px solid #dcdcdc;
        padding: 10px;
        background-color: #f0fff0;
        border-radius: 5px;
        width: 90%;
        height: 200px;
        overflow-y: auto;
        margin: auto;
        margin-top: 20px;
    }
    </style>
"""

gyro_box_style = """
    <style>
    .gyro-box {
        border: 2px solid #dcdcdc;
        padding: 10px;
        background-color: #f0f8ff;
        border-radius: 5px;
        width: 90%;
        height: 200px;
        overflow-y: auto;
        margin: auto;
        margin-top: 20px;
    }
    </style>
"""

st.markdown(sensor_box_style, unsafe_allow_html=True)
st.markdown(gyro_box_style, unsafe_allow_html=True)

col1, col2 = st.columns(2)

status_placeholder = st.empty()

def update_status(new_status):
    global status_placeholder
    response = requests.post(f"http://localhost:8000/status?status={new_status}")
    if response.status_code == 200:
        status_placeholder.success(f"LED turned {new_status}")
    else:
        status_placeholder.error("Failed to update LED status")

with col1:
    if st.button("Turn LED ON"):
        update_status("on")

with col2:
    if st.button("Turn LED OFF"):
        update_status("off")

sensor_values_placeholder = col1.empty()
gyro_values_placeholder = col2.empty()

def display_sensor_values():
    sensor_values_str = "<div class='sensor-box'>" + "<br>".join([f"{time}: {v}" for time, v in sensor_values]) + "</div>"
    sensor_values_placeholder.markdown(sensor_values_str, unsafe_allow_html=True)

def display_gyro_values():
    gyro_values_str = "<div class='gyro-box'>" + "<br>".join([f"{time}: {v}" for time, v in gyro_values]) + "</div>"
    gyro_values_placeholder.markdown(gyro_values_str, unsafe_allow_html=True)

while True:
    response = requests.get("http://localhost:8000/value")
    data = response.json()
    sensor_value = data["value"]

    # 현재 시간을 한국 시간으로 변환
    current_time = datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S')

    if len(sensor_values) >= 10:
        sensor_values.pop(0)
    sensor_values.append((current_time, sensor_value))

    display_sensor_values()

    response = requests.get("http://localhost:8000/gyro")
    data = response.json()
    gyro_data_str = f"AcX={data['AcX']}, AcY={data['AcY']}, AcZ={data['AcZ']}, Tmp={data['Tmp']}, GyX={data['GyX']}, GyY={data['GyY']}, GyZ={data['GyZ']}"

    if len(gyro_values) >= 10:
        gyro_values.pop(0)
    gyro_values.append((current_time, gyro_data_str))

    display_gyro_values()

    time.sleep(1)
