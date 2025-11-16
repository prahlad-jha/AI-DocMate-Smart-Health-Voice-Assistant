# Deployment Guide

## Deploying to Hugging Face Spaces

### Step 1: Create a Hugging Face Account
1. Go to https://huggingface.co
2. Sign up or log in to your account

### Step 2: Create a New Space
1. Click on your profile → "New Space"
2. Name: `ai-doctor-assistant`
3. License: `apache-2.0`
4. Space SDK: `Docker`
5. Create Space

### Step 3: Connect GitHub Repository
1. In your Space, go to "Settings"
2. Click "Link a Repository"
3. Select your GitHub repository: `AI-DocMate-Smart-Health-Voice-Assistant`
4. The Space will auto-sync

### Step 4: Add Secrets
1. In Space Settings → "Repository secrets"
2. Add: `GROQ_API_KEY` = your actual Groq API key

### Step 5: The app will auto-deploy!

## Docker Deployment (Local)

```bash
docker build -t ai-doctor-assistant .
docker run -p 7860:7860 -e GROQ_API_KEY=your_key_here ai-doctor-assistant
```

## Local Development

```bash
# Clone repo
git clone https://github.com/prahlad-jha/AI-DocMate-Smart-Health-Voice-Assistant.git
cd AI-DocMate-Smart-Health-Voice-Assistant

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create .env file
cp .env.example .env
# Edit .env and add GROQ_API_KEY

# Run the app
python gradio_121app.py
```

Visit: http://localhost:7860

## File Structure Overview

```
├── gradio_121app.py          # Main Gradio application (entry point)
├── brain_of_the_doctor.py    # LLM image analysis logic
├── voice_of_the_patient.py   # Speech-to-text (STT)
├── voice_of_the_doctor.py    # Text-to-speech (TTS)
├── requirements.txt          # Python dependencies
├── Dockerfile               # Docker container config
├── .dockerignore            # Docker ignore rules
├── .gitignore              # Git ignore rules
├── .env.example            # Environment template
└── README.md               # Main documentation
```

## What's Ignored from Git

❌ `.env` - Contains API keys (use `.env.example` as template)
❌ `*.mp3` - Generated audio files
❌ `*.wav` - Generated audio files
❌ `__pycache__/` - Python cache
❌ `.gradio/` - Gradio cache
❌ `.venv/` - Virtual environment
❌ `.idea/` - IDE settings
❌ `.vscode/` - IDE settings

✅ All `.py` files
✅ `requirements.txt`
✅ `Dockerfile`
✅ `README.md`
✅ Configuration files

## Troubleshooting

### Missing GROQ_API_KEY
- Ensure `.env` file exists with valid GROQ_API_KEY
- For Hugging Face Spaces, add it in Repository Secrets

### Audio Processing Issues
- Ensure ffmpeg is installed: `apt-get install ffmpeg`
- On Windows: Download ffmpeg from https://ffmpeg.org/download.html

### Import Errors
- Run: `pip install -r requirements.txt`
- Ensure virtual environment is activated

## Next Steps

1. ✅ Push to GitHub
2. ✅ Create Hugging Face Space
3. ✅ Add Secrets
4. ✅ Space auto-deploys!

## Support

For issues, check:
- GitHub Issues: https://github.com/prahlad-jha/AI-DocMate-Smart-Health-Voice-Assistant/issues
- Groq Docs: https://console.groq.com/docs
- Gradio Docs: https://www.gradio.app
