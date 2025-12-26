import os
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello():
    return 'Hello, World from Flask in Docker!'

if __name__ == "__main__":
    # Allow Flask to auto-reload in dev mode if needed
    app.run(host="0.0.0.0", port=int(os.environ.get("PORT", 5000)), debug=True)

