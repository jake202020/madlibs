from flask import Flask, render_template, request
from stories import story
from flask_debugtoolbar import DebugToolbarExtension

app = Flask(__name__)

app.config['SECRET_KEY'] = "chickenzarecool21837"
debug = DebugToolbarExtension(app)

@app.route('/')
def get_answers():
    """Generate and show form asking user for words"""

    prompts = story.prompts
    return render_template('ans_questions.html', prompts=prompts)

@app.route('/story')
def make_story():
    """Show resulting madlib"""
    
    result = story.generate(request.args)
    return render_template('story.html', story=result)