import whisper
import pyttsx3
import sounddevice as sd
import scipy.io.wavfile as wav
import tempfile

# Initialize Whisper model (small = fast, base = default, medium/large = slow+accurate)
model = whisper.load_model("base")

# 1. Record voice input (5 seconds)
def record_voice(duration=5, samplerate=16000):
    print("🎙️ Listening... Speak now!")
    audio = sd.rec(int(duration * samplerate), samplerate=samplerate, channels=1)
    sd.wait()
    return audio, samplerate

# 2. Convert to text using Whisper
def transcribe_audio(audio, samplerate):
    with tempfile.NamedTemporaryFile(suffix=".wav", delete=False) as f:
        wav.write(f.name, samplerate, audio)
        result = model.transcribe(f.name)
        return result["text"]

# 3. Speak response
def speak_text(text):
    engine = pyttsx3.init()
    engine.setProperty('rate', 160)  # slower = more natural
    engine.say(text)
    engine.runAndWait()
