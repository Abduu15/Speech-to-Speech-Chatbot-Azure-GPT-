# Speech-to-Speech Chatbot

A web-based speech-to-speech chatbot that utilizes Azure's Speech-to-Text (STT), Text-to-Speech (TTS), and OpenAI's GPT model for intelligent conversation. The chatbot can be accessed locally or via the internet using ngrok.

## Features
- Converts spoken language to text using Azure Speech-to-Text.
- Processes the text input using OpenAI's GPT model to generate responses.
- Converts the generated responses back to speech using Azure Text-to-Speech.
- Can be used locally or deployed for online access.

## Prerequisites
Before running the chatbot, ensure you have:
- Python installed (preferably Python 3.8 or higher).
- A Microsoft Azure account with access to Speech Services and OpenAI API.
- Required dependencies installed via `pip install -r requirements.txt`.

## Installation
1. Clone this repository:
   ```sh
   git clone https://github.com/yourusername/speech-to-speech-chatbot.git
   cd speech-to-speech-chatbot
   ```
2. Install required dependencies:
   ```sh
   pip install -r requirements.txt
   ```
3. Add your Azure API keys:
   - In `app.py`, replace the placeholders with your Azure OpenAI and Speech API keys:
     ```python
     openai.api_key = "YOUR_AZURE_OPENAI_API_KEY"
     SPEECH_KEY = "YOUR_AZURE_SPEECH_API_KEY"
     ```
   - In `chatbot.html`, update the WebSocket URL with your ngrok link (if using online access):
     ```javascript
     socket = new WebSocket("wss://your-ngrok-url/ws/recording");
     ```

## Running the Chatbot
### Local Deployment
To run the chatbot locally, follow these steps:
1. Open your terminal and navigate to the project directory.
2. Start the Flask application:
   ```sh
   flask run
   ```
   or
   ```sh
   python app.py
   ```
4. Access the chatbot in your browser:
   ```
   http://127.0.0.1:5000/
   ```

### Online Deployment with ngrok
If you want to access the chatbot over the internet:
1. Download and install [ngrok](https://ngrok.com/download).
2. Start an HTTP tunnel for port 5000:
   ```sh
   ngrok http 5000
   ```
3. Copy the generated public URL and replace the WebSocket link in `chatbot.html`.

## Usage Notes
- Ensure AdBlockers and other blockers are disabled.
- Refresh the page if speech recognition or synthesis does not work.
- Do not use the chatbot in incognito mode, as microphone access may be restricted.

## Contribution & Attribution
If you use this code in your project, please give proper credit by mentioning my name and linking back to this repository. Contributions and improvements are always welcome!

## License
This project is open-source and available under the MIT License.

---

Feel free to contribute or report issues!

