from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return "Hello from Jenkins Python job!<br>Jenkins pipeline automation is working perfectly!<br>Learning basics of devops"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
