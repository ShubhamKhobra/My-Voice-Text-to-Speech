import streamlit as st
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
from elevenlabs.play import play
import os
import io

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

st.title("Text to Speech App")

text = st.text_area("Enter text to convert to speech:")

if st.button("Convert to Speech"):
    if text:
        audio = elevenlabs.text_to_speech.convert(
            text=text,
            voice_id="JBFqnCBsd6RMkjVDRZzb",
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )

        # audio_bytes = io.BytesIO(audio)
        # play(audio)

         # Join chunks into one byte string
        audio_data = b"".join(audio)

        # Wrap in buffer
        audio_bytes = io.BytesIO(audio_data)

        st.audio(audio_bytes, format='audio/mp3', autoplay=True)
    
    else:
        st.warning("Please enter some text.")