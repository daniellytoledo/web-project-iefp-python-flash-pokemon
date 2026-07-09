import os
from werkzeug.utils import secure_filename
from flask import Blueprint, render_template, request, redirect, url_for, flash
from app.services.srv_pokemon_cards import lista_cards, detalhes_card, lista_tipos, adicionar_pokemon, atualizar_card

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
        nome = request.form.get("fnome")
        tipo = request.form.get("ftipo")
        desc = request.form.get("fdesc")

        arquivo_imagem = request.files.get("fimg")
        nome_imagem = None

        if arquivo_imagem and arquivo_imagem.filename != "":
            nome_imagem = secure_filename(arquivo_imagem.filename)
            caminho_pasta = os.path.join("app", "static", "imgs", "pokemon")
            caminho_completo = os.path.join(caminho_pasta, nome_imagem)
            arquivo_imagem.save(caminho_completo)

        pokemon_novo = adicionar_pokemon(nome, tipo, desc, nome_imagem)

        return redirect(url_for('pokemon_cards.homepage'))

    tipos = lista_tipos()
    return render_template("adicionar.html", tipos=tipos)

@pokemon_cards.route("/atualizar/<int:card_id>", methods=["GET", "POST"])
def atualizar(card_id):
    if request.method == "POST":
        nome = request.form.get("fnome")
        tipo = request.form.get("ftipo")
        desc = request.form.get("fdesc")

        atualizar_card(card_id, nome, tipo, desc)
        return redirect(url_for('pokemon_cards.detalhes', card_id=card_id))
    
    dados = detalhes_card(card_id)
    tipos = lista_tipos()
    return render_template("atualizar.html", dados=dados, tipos=tipos)