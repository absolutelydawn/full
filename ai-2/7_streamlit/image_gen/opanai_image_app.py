import my_image_gen
import streamlit as st
import openai
import os
import requests
import textwrap
from datetime import datetime


# ----- 세션 초기화 ------
if 'image_caption' not in st.session_state:
    st.session_state['image_caption'] = ''


if 'shorten_text_for_image' not in st.session_state:
    st.session_state['shorten_text_for_image'] = ''


if 'image_urls' not in st.session_state:
    st.session_state['image_urls'] = ''


if 'images' not in st.session_state:
    st.session_state['images'] = ''


if 'download_file_names' not in st.session_state:
    st.session_state['download_file_names'] = ''


if 'download_buttons' not in st.session_state:
    st.session_state['download_buttons'] = ''


# ----- 이미지 생성을 위한 텍스트와 생성된 이미지를 화면에 표시하는 함수 ------
def display_results():
    shorten_text_for_image = st.session_state['shorten_text_for_image']
    imag_caption = st.session_state['image_caption']
    image_urls = st.session_state['image_urls']


    st.sidebar.write("[이미지 생성을 위한 텍스트]")
    st.sidebar.write(shorten_text_for_image)


    for k, image_url in enumerate(image_urls):
        st.image(image_url, caption=imag_caption)


        image_data = st.session_state['images'][k]
        download_file_name = st.session_state['download_file_names'][k]


        st.download_button(
            label="이미지 파일 다운로드",
            data=image_data,
            file_name=download_file_name,
            mime="image/png",
            key=k,
            on_click=download_button_callback
        )


# ----- callback 함수 ------
def download_button_callback():
    st.session_state['download_buttons'] = True


def button_callback():
    if radio_selected_lang == '한국어':
        translate_text = my_image_gen.translate_text_for_image(input_text)
    elif radio_selected_lang == '영어':
        translate_text = input_text


    if detail_description == 'Yes':
        resp = my_image_gen.generate_text_for_image(translate_text)
        text_for_image = resp
        image_caption = "상세 묘사를 추가해 생성한 이미지"
    elif detail_description == 'No':
        text_for_image = translate_text
        image_caption = "입력 내용으로 생성한 이미지"


    shorten_text_for_image = textwrap.shorten(text_for_image, 200, placeholder=' [...이하 생략...]')


    image_urls = my_image_gen.generate_image_from_text(text_for_image, image_num, image_size)


    images = []
    download_file_names = []


    for k, image_url in enumerate(image_urls):
        r = requests.get(image_url)
        image_data = r.content
        images.append(image_data)


        now_datetime = datetime.now().strftime("%Y%m%d_%H%M%S")
        download_file_name = f'gen_image_{k}_{now_datetime}.png'
        download_file_names.append(download_file_name)


    st.session_state['image_caption'] = image_caption
    st.session_state['shorten_text_for_image'] = shorten_text_for_image
    st.session_state['image_urls'] = image_urls
    st.session_state['images'] = images
    st.session_state['download_file_names'] = download_file_names


# ----- 사이드바 화면 구성 ------
st.sidebar.title('이미지 생성을 위한 설정')


input_text = st.sidebar.text_input('이미지 생성을 위한 설명을 입력하세요.', '빌딩이 보이는 호수가 있는 도시의 공원')


radio_selected_lang = st.sidebar.radio('입력 언어', ['한국어', '영어'], index=0, horizontal=True)


image_num_options = [1, 2, 3]
image_num = st.sidebar.radio('생성할 이미지 파일의 개수를 선택하세요.', image_num_options, index=0, horizontal=True)


image_size_options = ['256x256', '512x512', '1024x1024']
image_size = st.sidebar.radio('생성할 이미지 크기를 선택하세요.',image_size_options, index=1, horizontal=True)


detail_description = st.sidebar.radio('상세 묘사를 추가하시겠습니까?', ['Yes', 'No'], index=1, horizontal=True)


clicked = st.sidebar.button('이미지 생성', on_click=button_callback)


# ----- 메인 화면 구성 -----
st.title('OpenAI Image Generator')


if clicked or st.session_state['download_buttons'] == True:
    display_results()
