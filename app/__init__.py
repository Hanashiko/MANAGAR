from flask import Flask, render_template
from .config import Config
from app.extensions import db
def create_app(config_class=Config):
    app = Flask(__name__)
    app.config.from_object(config_class)
    db.init_app(app)
    from app.main import bp as main_bp
    app.register_blueprint(main_bp)
    from app.chooseClass import bp as posts_bp
    app.register_blueprint(posts_bp, url_prefix='/chooseClass')
    @app.route('/test/')
    def test_page():
        return render_template("test.html")
    
    return app
