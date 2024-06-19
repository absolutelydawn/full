import openai
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

def answer_from_given_info(question_info, prompt):
    user_content = f"{prompt} 다음 내용을 바탕으로 질문에 답해 줘. {question_info}"

    message = [
        { "role": "user", "content": user_content }
    ]

    response = openai.ChatCompletion.create(
        model = "get-3.5-turbo",
        messages = message,
        max_tokens = 500,
        stop = ["."],
        temperature = 0.2,
    )

    return response['choices'][0]['message']['content']

    question_info = text_info
    prompt = "허준이 교수가 받은 상은 무엇인가요?"
    print(prompt)
    response = answer_from_given_info(question_info, prompt)
    print(response)
    print('-' * 70)