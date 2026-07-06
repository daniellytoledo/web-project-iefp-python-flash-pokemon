from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.srv_pokemon_cards import lista_cards, detalhes_card

pokemon_cards = Blueprint('pokemon_cards', __name__)

@pokemon_cards.route("/")
def homepage():
    dados = lista_cards()
    return render_template("home.html", lista_pokemon=dados)

@pokemon_cards.route("/<int:card_id>")
def detalhes(card_id):
    dados = detalhes_card(card_id)
    return render_template("detalhes.html", dados=dados)

@pokemon_cards.route("/adicionar", methods=["GET", "POST"])
def add_card():
    if request.method == "POST":
        card = request.form.get("fcard")
        desc = request.form.get("fdesc")
        tipo = request.form.get("ftipo")
    
    # elif request.method == "GET":
       # lista_tipos =    criar um serviço com os tipos, criar um template com as opções 
       # return render_template("adicionar.html", tipos=lista_tipos)
