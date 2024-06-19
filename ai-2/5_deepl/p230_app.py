import yt_dlp
from pathlib import Path

def get_youtube_video_info(video_url):
    ydl_opts = {
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(video_url, download=False)
        video_id = video_info['id']
        title = video_info['title']
        upload_date = video_info['upload_date']
        channel = video_info['channel']
        duration = video_info['duration_string']

    return video_id, title, upload_date, channel, duration

def remove_invalid_char_for_filename(input_str):
    invalid_characters = '<>:"/\|?*'

    for char in invalid_characters:
        input_str = input_str.replace(char, '_')

    while input_str.endswith('.'):
        input_str = input_str[:-1]

    return input_str

def download_youtube_video(video_url, folder, filename=None):
    _, title, _, _, _ = get_youtube_video_info(video_url)
    filename_no_ext = remove_invalid_char_for_filename(title)

    if filename == None:
        download_file = f"{filename_no_ext}.mp4"
    else:
        download_file = filename

    outtmpl_str = f'{folder}/{download_file}'

    download_path = Path(outtmpl_str)

    ydl_opts = {
        'format': 'best',
        'outtmpl': outtmpl_str,
        'noplaylist': True,
        'quiet': True,
        'no_warnings': True
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        video_info = ydl.extract_info(video_url, download=True)
        title = video_info.get('title', None)

    return title, download_path

video_url = 'https://www.youtube.com/watch?v=pSJrML-TTmI'
download_folder = './data'
video_title, download_path = download_youtube_video(video_url, download_folder)

print("- 유튜브 제목 : ", video_title)
print("- 다운로드한 파일명 : ", download_path.name)

video_url = 'https://www.youtube.com/watch?v=Ks-_Mh1QhMc'
download_folder = './data'
video_title, download_path = download_youtube_video(video_url, download_folder)

print("- 유튜브 제목 : ", video_title)
print("- 다운로드한 파일명 : ", download_path.name)
