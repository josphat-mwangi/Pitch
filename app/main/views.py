from flask import render_template
from flask_login import login_required
from ..models import User,Pitch,Comment,Upvotes,Downvotes
from . import main

# Views
@main.route('/')
def index():

    '''
    View root page function that returns the index page and its data
    '''
    title = 'Welcome to Pitch'
    return render_template('index.html',title=title)
