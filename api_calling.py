from google import genai
from dotenv import load_dotenv
import os
import io
from gtts import gTTS
#loading environment variable
load_dotenv()
my_api_key=os.getenv("Gemini_Api_Key")

#initialize client

client=genai.Client(api_key=my_api_key)

#note genartor function

def note_generator(images):
    prompt="""summarize the picture in note formate at max 100 words,
              make sure markdown to differntiate diffarent section"""
    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images,prompt]
    )

    return response.text

#audio

def audio_transcript(text):
    speach=gTTS(text,lang='en',slow=False)
    audio_buffer=io.BytesIO()
    speach.write_to_fp(audio_buffer)
    return audio_buffer

#qiuz

def quiz_generator(images,difficulty):
    prompt=f"Create 3 quiz and last solve the answer {difficulty}.make sure markdown to differntiate diffarent section"
    response=client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images,prompt]
    )

    return response.text
