from flask import Flask, request, jsonify
from flask_cors import CORS
import openai
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Initialize Flask app
app = Flask(__name__)
CORS(app)  # Allow frontend to communicate with backend

# OpenAI API Key will be loaded from environment variables
openai.api_key = os.getenv("OPENAI_API_KEY")

@app.route('/', methods=['GET'])
def home():
    return """
    <html>
        <head>
            <title>What Are We Eating Today?</title>
        </head>
        <body style="font-family: Arial, sans-serif; text-align: center; margin: 50px;">
            <h1>Welcome to 'What Are We Eating Today?'</h1>
            <p>Your AI-powered cooking assistant.</p>
        </body>
    </html>
    """

if __name__ == '__main__':
    app.run(debug=True)