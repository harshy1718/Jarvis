# Jarvis AI - Voice-Activated Assistant

A voice-activated AI assistant built using Python. Jarvis can execute voice commands, control apps, play songs, provide news updates, and fetch answers using the Groq API.

## Features
- **Voice Command Processing**: Takes voice inputs and processes them using speech recognition.
- **App Control**: Opens applications based on voice commands.
- **Music Playback**: Plays songs from local storage or online services.
- **News Updates**: Provides current news using APIs.
- **Groq API Integration**: Fetches answers from Groq AI for various queries.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/jarvis-ai.git
   cd jarvis-ai
   ```

2. Create a virtual environment (if not already done):
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

1. Run the application:
   ```bash
   python jarvis.py
   ```

2. Speak to Jarvis by activating the microphone, and issue commands such as:
   - "Open Chrome"
   - "Play music"
   - "What's the news today?"
   - "What is the weather like?"

## Requirements
- Python 3.x
- `speechrecognition`
- `pyttsx3` (for text-to-speech)
- `groq` (for API integration)
- Other dependencies listed in `requirements.txt`

## License
This project is licensed under the MIT License.

---

Let me know if you'd like any changes or additions!
