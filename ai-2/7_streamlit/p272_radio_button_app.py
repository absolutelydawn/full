import streamlit as st
import pandas as pd

st.title("스트림릿의 라디오 박스 사용 예")

radio1_options = ['10', '20', '30', '40']
radio1_selected = st.radio('(5 X 5 +5)은 얼마인가요?', radio1_options)
st.write('***선택한 답*** : ', radio1_selected)

radio2_options = ['마라톤', '축구', '수영', '승마']
radio2_selected = st.radio('당신의 좋아하는 운동은?', radio2_options, index=2, horizontal=True)
st.write('***선택한 답*** : ', radio2_selected)