from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story


app = Flask(__name__)
app.config['SECRET_KEY'] = 'sam123'
debug = DebugToolbarExtension(app)
    
@app.route('/')
def home():
    ques = story.prompts

    return render_template("index.html", ques=ques)

@app.route('/story')
def story_final():

    user_input = story.generate(request.args)

    return render_template("story.html", user_input=user_input)