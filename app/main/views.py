from flask import render_template

from . import main
from .. import db

@main.route('/', methods=['GET'])
def index():
    return render_template('main/index.html')
