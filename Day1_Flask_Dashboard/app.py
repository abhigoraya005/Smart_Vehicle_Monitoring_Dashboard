from flask import Flask, render_template
import random

app = Flask(__name__)

@app.route('/')

def home():

    distance = random.randint(5, 100)

    if distance > 50:
        status = "SAFE"

    elif distance > 20:
        status = "WARNING"

    else:
        status = "DANGER"

    return render_template("index.html",
                           distance=distance,
                           status=status)

if __name__ == '__main__':
    app.run(debug=True)