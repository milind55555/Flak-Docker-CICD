from flask import Flask

app = Flask(__name__)

@app.route('/')
def home():
    return """
    <h1>Flask CI/CD Demo</h1>
    <h2>Application Deployed Successfully 🚀</h2>
    """

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
