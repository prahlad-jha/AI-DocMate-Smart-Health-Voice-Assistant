# AI Doctor with Vision and Voice

## Overview

AI Doctor with Vision and Voice is an AI-powered medical assistant capable of analyzing images and audio inputs to provide insightful medical feedback. This project integrates cutting-edge speech-to-text, image analysis, and text-to-speech technologies to create a seamless interactive experience for users. It is designed to assist in preliminary medical evaluations by leveraging advanced AI models.

## Features

### **1. Speech-to-Text (Voice Input Processing)**
- Converts user speech into text using the **GROQ API**.
- Supports various audio formats for input.
- Allows real-time or pre-recorded voice input.

### **2. Medical Image Analysis**
- Uses a pre-trained deep learning model to analyze medical images.
- Supports common medical imaging formats such as **X-rays, MRIs, CT scans, and ultrasound images**.
- Provides potential diagnoses and explanations based on input images.

### **3. Text-to-Speech (AI Doctor's Voice)**
- Converts AI-generated responses into speech using **Google Text-to-Speech (gTTS)**.
- Offers multi-language support.
- Provides an interactive experience by playing responses aloud.

### **4. User-Friendly Interface**
- Powered by **Gradio**, allowing easy interaction through a web-based interface.
- Drag-and-drop support for both audio and image uploads.
- Simple button-based interaction for non-technical users.

### **5. Secure API Integration**
- Uses API keys for secure communication with external services (**GROQ API, ElevenLabs, Google TTS**).
- Ensures privacy and data security.

### **6. Local & Cloud Deployment**
- Can be run locally on a personal computer or deployed to a cloud-based server.
- Compatible with **Docker** for containerized deployment.

## Requirements

- **Python 3.7+**
- **Gradio** (for UI interface)
- **GROQ API Key** (for speech-to-text processing)
- **ElevenLabs API Key** (for enhanced AI-generated speech output)
- **Google Text-to-Speech (gTTS)**
- **Pygame** (for playing generated speech audio)

## Installation

1. **Clone the Repository**:
    ```bash
    git clone https://github.com/your-username/your-repository.git
    cd your-repository
    ```

2. **Create a Virtual Environment**:
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows use `venv\Scripts\activate`
    ```

3. **Install the Required Packages**:
    ```bash
    pip install -r requirements.txt
    ```

4. **Set Up Environment Variables**:
    Create a `.env` file in the root directory and add your API keys:
    ```env
    GROQ_API_KEY=your_groq_api_key
    ELEVENLABS_API_KEY=your_elevenlabs_api_key
    ```

## Usage

1. **Run the Application**:
    ```bash
    python gradio_121app.py
    ```

2. **Access the Web Interface**:
    Open your web browser and navigate to `http://127.0.0.1:7861`.

3. **Interact with the AI Doctor**:
    - Upload an **audio file** or **record your voice**.
    - Upload a **medical image** for analysis.
    - Click `Submit` to receive AI-generated medical insights.
    - Listen to the AI doctor's spoken response.

## File Structure

```
├── gradio_121app.py        # Main application file for the Gradio interface
├── brain_of_the_doctor.py  # Functions for encoding and analyzing medical images
├── voice_of_the_patient.py # Functions for recording and transcribing audio using the GROQ API
├── voice_of_the_doctor.py  # Functions for converting text to speech with gTTS & ElevenLabs
├── requirements.txt        # List of dependencies
├── .env                    # Environment variables file (not shared publicly)
├── screenshots/            # Contains images for documentation
```
## Troubleshooting

- **Permission Denied Error**:
    - Ensure that no other program is using the file `final_output.mp3`.
    - Use Task Manager or Resource Monitor to close any conflicting processes.

- **API Key Errors**:
    - Double-check that your API keys are correctly set in the `.env` file.
    - Ensure you have an active subscription or access to the required APIs.

## Future Improvements

- **Multimodal AI**: Integration of advanced AI models like GPT-4 for better natural language understanding.
- **Enhanced Medical Knowledge**: Connecting to medical databases for more accurate and up-to-date diagnoses.
- **Mobile App Support**: Developing a mobile-friendly version of the AI Doctor.
- **Integration with Wearables**: Allowing health monitoring via smartwatches or fitness trackers.

## Contributing

Contributions are welcome! If you would like to contribute:
- Fork the repository
- Create a feature branch (`git checkout -b feature-name`)
- Commit your changes (`git commit -m "Added new feature"`)
- Push to the branch (`git push origin feature-name`)
- Open a **Pull Request**

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for more details.

## Acknowledgements

- [Gradio](https://gradio.app/) - Web UI for AI models
- [GROQ](https://groq.com/) - Speech-to-text processing
- [Google Text-to-Speech (gTTS)](https://gtts.readthedocs.io/en/latest/) - AI-powered voice generation
- [ElevenLabs](https://elevenlabs.io/) - High-quality text-to-speech engine

  ![Alt Text](https://github.com/krish38506/AI-DocMate-Smart-Health-Voice-Assistant/blob/main/ai-doc.png)

  Deployed: https://huggingface.co/spaces/anandjha38506/ai_docmate_smart_health_voice_assistant

  

