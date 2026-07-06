from app.models.rep_pokemon_cards import select_cards, select_card_id
from pprint import pprint

def lista_cards():
    return select_cards()

def detalhes_card(card_id):
    return select_card_id(card_id)