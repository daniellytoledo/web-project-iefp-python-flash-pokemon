from flask import Flask
import os

def criar_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = os.environ.get('SK', 'dev-inseguro')

    from app.routes.rt_pokemon_cards import pokemon_cards

    app.register_blueprint(pokemon_cards)

    return app