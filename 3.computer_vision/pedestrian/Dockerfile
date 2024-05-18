FROM python:3.11-slim

ENV PORT 8000

RUN apt-get update && apt-get install ffmpeg libsm6 libxext6  -y

# install pytorch CPU
RUN pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/cpu

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt
COPY src src

CMD uvicorn src.app:app --host 0.0.0.0 --port ${PORT}