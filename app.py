from flask import Flask, render_template
app = Flask(__name__)
@app.route('/')
def index():
    return render_template('main.html', title = "nothing")

if  __name__ == "__main__":
    app.run(port = 8080)
