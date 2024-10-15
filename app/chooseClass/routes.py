from flask import render_template
from app.chooseClass import bp
from app.extensions import db
from app.models.chooseClass import ChooseClass

@bp.route('/')
def index():
    chooseClass = ChooseClass.query.all()
    return render_template('chooseClass/index.html', chooseClass=chooseClass)

@bp.route('/chooseClass/')
def categories():
    return render_template('chooseClass/categories.html')