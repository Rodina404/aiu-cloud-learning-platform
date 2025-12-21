from flask import Flask
app = Flask(__name__)

@app.route("/health")
def health():
    return "OK", 200

@app.route("/api/quiz")
def quiz():
    return {"question": "What is 2+2?", "answer": 4}

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
