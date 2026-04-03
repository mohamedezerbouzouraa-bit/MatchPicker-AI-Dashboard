from flask import Flask, request, jsonify
from flask_cors import CORS
import google.genai as genai

app = Flask(__name__)
CORS(app)

API_KEY = "ttttttttttttttt"
client = genai.Client(api_key=API_KEY)

@app.route("/chat", methods=["POST"])
def chat():
    data = request.json
    user_input = data.get("message", "")

    if not user_input:
        return jsonify({"reply": "I didn't catch that."}), 400

    try:
        # 1.5-flash is highly stable for free tier keys
        response = client.models.generate_content(
            model="gemini-1.5-flash", 
            contents=user_input
        )
        return jsonify({"reply": response.text})
    except Exception as e:
        print(f"Error: {e}")
        return jsonify({"reply": "API Error. Check if your key is valid in the terminal."}), 500

@app.route("/")
def index():
    return "Football Chatbot Server is Live!"

if __name__ == "__main__":
    app.run(host='127.0.0.1', port=5000, debug=True)
