from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from config import Config

db = SQLAlchemy()
migrate = Migrate()

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    db.init_app(app)
    migrate.init_app(app, db)

    from .routes.clientes import clientes_bp
    from .routes.agendamentos import agendamentos_bp

    app.register_blueprint(clientes_bp, url_prefix='/clientes')
    app.register_blueprint(agendamentos_bp, url_prefix='/agendamentos')

    @app.route('/')
    def index():
        return render_template('index.html')
    return app