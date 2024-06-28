import streamlit as st
import requests
from datetime import datetime
import pytz
import pandas as pd
import matplotlib.pyplot as plt

# 한국 시간대 설정
KST = pytz.timezone('Asia/Seoul')

st.title("Sensor Control Dashboard")

# 초기화
if 'sensor_values' not in st.session_state:
    st.session_state.sensor_values = []
if 'gyro_values' not in st.session_state:
    st.session_state.gyro_values = []
if 'page' not in st.session_state:
    st.session_state.page = 'sensor_data'  # 기본 페이지 설정

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

# 센서 및 자이로 값 표시를 위한 빈 공간
sensor_values_placeholder = st.empty()
gyro_values_placeholder = st.empty()

def display_sensor_values():
    sensor_values_str = "<div class='sensor-box'>" + "<br>".join([f"{time}: {v}" for time, v in st.session_state.sensor_values]) + "</div>"
    sensor_values_placeholder.markdown(sensor_values_str, unsafe_allow_html=True)

def display_gyro_values():
    gyro_values_str = "<div class='gyro-box'>" + "<br>".join([f"{time}: {v}" for time, v in st.session_state.gyro_values]) + "</div>"
    gyro_values_placeholder.markdown(gyro_values_str, unsafe_allow_html=True)

def update_data():
    response = requests.get("http://localhost:8000/value")
    data = response.json()
    sensor_value = data["value"]

    # 현재 시간을 한국 시간으로 변환
    current_time = datetime.now(KST).strftime('%Y-%m-%d %H:%M:%S')

    if len(st.session_state.sensor_values) >= 10:
        st.session_state.sensor_values.pop(0)
    st.session_state.sensor_values.append((current_time, sensor_value))

    display_sensor_values()

    response = requests.get("http://localhost:8000/gyro")
    data = response.json()
    gyro_data_str = f"AcX={data.get('AcX', 'N/A')}, AcY={data.get('AcY', 'N/A')}, AcZ={data.get('AcZ', 'N/A')}, Tmp={data.get('Tmp', 'N/A')}, GyX={data.get('GyX', 'N/A')}, GyY={data.get('GyY', 'N/A')}, GyZ={data.get('GyZ', 'N/A')}"

    if len(st.session_state.gyro_values) >= 10:
        st.session_state.gyro_values.pop(0)
    st.session_state.gyro_values.append((current_time, gyro_data_str))

    display_gyro_values()

# 페이지 전환 로직
def load_page(page_name):
    st.session_state.page = page_name
    st.experimental_rerun()

st.sidebar.title("👁️Sauron Dashboard")
if st.sidebar.button("Sensor Data"):
    load_page("sensor_data")

if st.sidebar.button("Light Intensity Data"):
    load_page("light_intensity_data")

# 페이지 로드
if st.session_state.page == "sensor_data":
    update_data()
elif st.session_state.page == "light_intensity_data":
    st.subheader("Light Intensity Data")

    # 날짜 선택 위젯
    selected_date = st.date_input("Select a date", key="date_input")

    if selected_date:
        st.session_state.selected_date = selected_date

    if 'selected_date' in st.session_state:
        selected_date = st.session_state.selected_date
        # FastAPI 서버에서 데이터 가져오기
        url = f"http://localhost:8000/light_intensity/{selected_date}"
        response = requests.get(url)

        if response.status_code == 200:
            data = response.json()
            df = pd.DataFrame(data)

            st.write(f"Light intensity data for {selected_date}")

            # 꺾은선 그래프 그리기
            fig, ax = plt.subplots()
            ax.plot(pd.to_datetime(df['datetime']), df['light_intensity'], marker='o')
            ax.set_xlabel('Time')
            ax.set_ylabel('Light Intensity')
            ax.set_title(f'Light Intensity on {selected_date}')
            st.pyplot(fig)
        else:
            st.error("No data found for the selected date.")
