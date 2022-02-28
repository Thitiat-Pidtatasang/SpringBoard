from flask import Flask, renfer_template, request
from flask_debugtoolbar import DebugToolBarExtension
from stories import story

app = Flask(__name__)
app.config['SECRET_KEY'] = "secret"

debug = DebugToolBarExtension(app)



@app.route('/')
def ask_question():
    prompts = story.prompts

    return render_template("questions.html" prompts = prompts)


@app.route("/story")
def show_story():
    text = story.generate(request.args)

    return render_template("story.html", text = text)

