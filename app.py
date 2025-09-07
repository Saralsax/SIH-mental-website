from flask import Flask, request, jsonify, render_template
import subprocess

app = Flask(__name__)

def query_ollama(prompt):
    """Send prompt to Ollama and return response."""
    try:
        result = subprocess.run(
            ["ollama", "run", "llama3.2", prompt],
            capture_output=True,
            text=True
        )
        return result.stdout.strip()
    except Exception as e:
        return f"Error connecting to Ollama: {e}"

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_message = request.json.get("message", "")
    if not user_message:
        return jsonify({"reply": "Please say something."})
    bot_reply = query_ollama(user_message)
    return jsonify({"reply": bot_reply})

if __name__ == "__main__":
    app.run(debug=True)
