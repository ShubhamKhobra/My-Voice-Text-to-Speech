import streamlit as st
from dotenv import load_dotenv
from elevenlabs.client import ElevenLabs
import os
import io

load_dotenv()

elevenlabs = ElevenLabs(
  api_key=os.getenv("ELEVENLABS_API_KEY"),
)

voice_id = os.getenv("VOICE_ID")

st.title("Text to Speech App")

text = st.text_area("Enter text to convert to speech:")

if st.button("Convert to Speech"):
    if text:
        audio = elevenlabs.text_to_speech.convert(
            text=text,
            voice_id=voice_id,
            model_id="eleven_multilingual_v2",
            output_format="mp3_44100_128",
        )

        # Combine the list of byte chunks into a single byte string
        audio_data = b"".join(audio)

        # Create a BytesIO object from the byte string
        audio_bytes = io.BytesIO(audio_data)

        st.audio(audio_bytes, format='audio/mp3', autoplay=True)
    
    else:
        st.warning("Please enter some text.")