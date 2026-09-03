from flask import Flask

app = Flask(__name__)


@app.route("/")
def home():
    return """
    <h1>Study Task Tracker</h1>
    <p>Organize your assignments and stay on schedule.</p>
    """


if __name__ == "__main__":
    app.run(debug=True)