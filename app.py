from flask import Flask, request, render_template
from flask_debugtoolbar import DebugToolbarExtension
from stories import story1, story2, story3, stories

app = Flask(__name__)

app.config['SECRET_KEY'] = 'secretkey'

debug = DebugToolbarExtension(app)

@app.route('/')
def home_page():
    return render_template('home.html', stories=stories)

@app.route('/create')
def create_page():
    story_title = request.args['story_title']
    story = stories[story_title]
    return render_template('create.html', questions=story.prompts, story_title=story_title)

@app.route('/story')
def show_story():
    answers = {}
    story_title = request.args['story_title']
    story = stories[story_title]
    for question in story.prompts:
        answers[question] = request.args[question]
    story_text = story.generate(answers)
    return render_template('story.html', story_text=story_text, story_title=story_title)