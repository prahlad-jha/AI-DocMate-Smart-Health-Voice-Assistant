# 🧠 AI Doctor Assistant with Vision & Voice  
A smart AI-powered healthcare assistant that combines **vision analysis**, **voice interaction**, and **LLM-based medical reasoning**. Built using **Gradio** for an intuitive web interface and powered by **Groq AI models**.

🚀 **Live Demo (Hugging Face Space):**  
🔗 [https://huggingface.co/spaces/YOUR-SPACE-LINK ](https://huggingface.co/spaces/PRAhlad9818/ai-doctor) 


---

## 🌟 Features

- 🎙 **Speech-to-Text**  
  Converts patient speech into text using **Groq Whisper (whisper-large-v3)**.

- 🩺 **Vision Diagnosis**  
  Upload medical images (skin, X-rays, reports) for AI-based analysis using  
  **llama-3.2-90b-vision-preview**.

- 🤖 **AI Doctor Response**  
  Provides medical insights using Groq LLMs with reasoning capability.

- 🔊 **Text-to-Speech**  
  Doctor's response is converted to audio using **gTTS**.

- 🖥 **Interactive Web UI**  
  Built with **Gradio**, accessible on web or Hugging Face Spaces.

---

## 🏗 Tech Stack

### **AI & Models**
- Groq Whisper (STT)
- Groq Llama Vision (Image + Text)
- Mixtral fallback model

### **Frameworks**
- Gradio  
- Python 3.11+

### **Libraries**
- Pillow (Image Processing)  
- SpeechRecognition, PyAudio  
- gTTS, Pydub  
- pygame  

---

## 🔧 Installation & Setup

### ▶ Prerequisites
- Python **3.11+**
- Groq API Key → https://console.groq.com
- FFmpeg installed and added to PATH

---

### 1️⃣ Clone Repository
```bash
git clone https://github.com/prahlad-jha/AI-DocMate-Smart-Health-Voice-Assistant.git
cd AI-DocMate-Smart-Health-Voice-Assistant


