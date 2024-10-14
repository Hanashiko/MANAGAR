from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from enum import Enum as PyEnum

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///main.db'
db = SQLAlchemy(app)


@app.route('/')
def index():
    return render_template("index.html")


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
    app.run(debug=True)