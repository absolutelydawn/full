from youtube_transcript_api import YouTubeTranscriptApi
from youtube_transcript_api.formatters import TextFormatter
import textwrap

def get_video_id(video_url):
    video_id = video_url.split("v=")[1][:11]

    return video_id

video_url = "https://www.youtube.com/watch?v=pSJrML-TTmI"
video_id = get_video_id(video_url)

transcript = YouTubeTranscriptApi.get_transcript(video_id, languages=['ko'])

text_formatter = TextFormatter()
text_formatted = text_formatter.format_transcript(transcript)
text_info = text_formatted.replace('\n', " ")

shorten_text_info = textwrap.shorten(text_info, width=150, placeholder=' [...이하 생략...]')
print(shorten_text_info, end='\n')