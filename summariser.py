import os
import google.generativeai as genai
import video_info
from dotenv import load_dotenv
load_dotenv()

api_key=os.getenv("GEMINI_API_KEY")
genai.configure(api_key=api_key)

def abstractive_summarization(transcript_text, max_len, temperature):
    prompt=f"You are Youtube transcript summarizer. Summarize the given transcript text within {max_len} words. The transcript text is:\n{transcript_text} "
    model=genai.GenerativeModel("gemini-1.5-flash")
    try:
        response=model.generate_content(
                prompt,
                generation_config = genai.GenerationConfig(
                        temperature = temperature
                )
            )
        return response.text
    except Exception as e:
        raise e

def summarise(video_id, max_len=150, temperature=0.2):
    try:
        transcript_text = video_info.get_video_transcript(video_id)
    except:
        return "No subtitles available for this video"

    summary = abstractive_summarization(transcript_text, max_len, temperature)

    return (summary, transcript_text)