from flask import Flask, render_template
from flask_sock import Sock
import openai
import asyncio
import azure.cognitiveservices.speech as speechsdk

app = Flask(__name__)  # Create a Flask application
sock = Sock(app)  # Add WebSocket functionality to the Flask app

# -------------------- Azure OpenAI API Configuration --------------------

openai.api_type = "azure"
openai.api_key = "YOUR_AZURE_OPENAI_API_KEY"
openai.api_base = "YOUR_AZURE_OPENAI_API_BASE"
openai.api_version = "2023-03-15-preview"

# -------------------- Azure Speech API Configuration --------------------

SPEECH_KEY = "YOUR_AZURE_SPEECH_API_KEY"
SPEECH_REGION = "YOUR_AZURE_SPEECH_REGION"

# -------------------- Define Web Application Routes --------------------

# Route for the main page of the application
@app.route("/")
def index():
    return render_template("chatbot.html")

# -------------------- Function to Query Azure OpenAI API --------------------

# This function sends a prompt to the Azure OpenAI API and retrieves a response
async def query_azure_openai(prompt):
    try:
        response = openai.ChatCompletion.create(
            engine="gpt-35-turbo",
            messages=[
                {"role": "system", "content": "You are a helpful assistant and reply in German."},
                {"role": "user", "content": prompt}
            ]
        )
        return response["choices"][0]["message"]["content"].strip()
    except Exception as e:
        return f"Error: {e}"

# -------------------- WebSocket Route for Speech Recording --------------------

# This function is used to receive and process speech data via WebSockets
@sock.route("/ws/recording")
def websocket_route(ws):
    ws.send("Recording started...")

    while True:
        data = ws.receive()
        if not data:
            break
        if "stop recording" in data.lower():
            ws.send("Recording stopped.")
            break
        ai_response = asyncio.run(query_azure_openai(data))
        ws.send(f"Response: {ai_response} Can I assist you further?")

# -------------------- Start the Application --------------------

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
