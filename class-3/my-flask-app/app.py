import os
from flask import Flask, render_template

app = Flask(__name__)

color = os.environ.get('APP_COLOR', 'blue')  # Default to 'blue' if APP_COLOR is not set

@app.route("/")
def main():
    print(color)
    return render_template( color=color)

if __name__ == "__main__":
    app.run()

