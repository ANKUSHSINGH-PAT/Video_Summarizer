from fastapi import FastAPI
from langserve import add_routes
from app.main_pipeline.summarize import summarize
from app.main_pipeline.transcribe import transcribe
from app.main_pipeline.extract_audio import extract_audio

from langchain.runnables.base import Runnable

class SummarizeVideo(Runnable):
    """Custom Runnable that performs the pipeline."""
    def invoke(self, video_file: str, **kwargs) -> str:
        audio_file = "/tmp/audio.wav"
        extract_audio(video_file, audio_file)
        transcript = transcribe(audio_file)
        summary = summarize(transcript)
        return summary

app = FastAPI()

add_routes(app, SummarizeVideo(), path="/summarize")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host='0.0.0.0', port=8000)
