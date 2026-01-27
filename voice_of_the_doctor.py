# if you dont use pipenv uncomment the following:
# from dotenv import load_dotenv
# load_dotenv()

import os
from gtts import gTTS
import elevenlabs
from elevenlabs.client import ElevenLabs

# ==============================
# ENV
# ==============================
ELEVENLABS_API_KEY = os.environ.get("ELEVEN_API_KEY")

# ==============================
# gTTS (Fallback / Free TTS)
# ==============================
def text_to_speech_with_gtts(input_text, output_filepath="gtts_output.mp3"):
    """
    Convert text to speech using gTTS and return audio file path (Gradio-safe)
    """
    tts = gTTS(
        text=input_text,
        lang="en",
        slow=False
    )
    tts.save(output_filepath)
    return output_filepath


# ==============================
# ElevenLabs (Premium TTS)
# ==============================
def text_to_speech_with_elevenlabs(input_text, output_filepath="elevenlabs_output.mp3"):
    """
    Convert text to speech using ElevenLabs and return audio file path (Gradio-safe)
    """
    if not ELEVENLABS_API_KEY:
        raise ValueError("ELEVEN_API_KEY not found in environment variables")

    client = ElevenLabs(api_key=ELEVENLABS_API_KEY)

    audio = client.generate(
        text=input_text,
        voice="Aria",
        output_format="mp3_22050_32",
        model="eleven_turbo_v2"
    )

    elevenlabs.save(audio, output_filepath)
    return output_filepath


# ==============================
# Optional local test (NOT for Gradio)
# ==============================
if __name__ == "__main__":
    test_text = "Hello, this is a test of the AI doctor's voice."
    text_to_speech_with_gtts(test_text, "test_gtts.mp3")
    # text_to_speech_with_elevenlabs(test_text, "test_elevenlabs.mp3")
