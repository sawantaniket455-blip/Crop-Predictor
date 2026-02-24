from flask import Flask, render_template, request
import front  # or whichever file does prediction

app = Flask(__name__)

@app.route("/")
def home():
    return "Crop Predictor is running!"

if __name__ == "__main__":
    app.run()