import whisper

def transcribe_audio(audio_path):
    model = whisper.load_model("base")  # you can use tiny/base/small
    result = model.transcribe(audio_path)
    return result["text"]