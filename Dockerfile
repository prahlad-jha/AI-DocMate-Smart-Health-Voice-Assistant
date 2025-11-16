FROM python:3.11-slim

# Install system deps needed for audio/image processing
RUN apt-get update && apt-get install -y --no-install-recommends \
    ffmpeg \
    libsndfile1 \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy and install python deps
COPY requirements.txt /app/requirements.txt
RUN python -m pip install --upgrade pip setuptools wheel
RUN pip install -r /app/requirements.txt

# Copy app files
COPY . /app

ENV PORT=7860
EXPOSE 7860

CMD ["python", "gradio_121app.py"]
