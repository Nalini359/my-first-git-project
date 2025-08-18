from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Hello from Jenkins Python job!</h1>
    <p>Jenkins pipeline automation is working perfectly!</p>
    <p>Learning basics of DevOps</p>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
print("Hello from Jenkins Python job!")
print("Jenkins pipeline automation is working perfectly!")
print("Learning basics of devops")



