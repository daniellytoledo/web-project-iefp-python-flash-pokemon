"""
Script para criar um utilizador com senha criptografada.
Rodar uma única vez pelo terminal:

    python -m app.scripts.criar_utilizador

(ajuste o caminho do import abaixo conforme a localização
real deste arquivo dentro do seu projeto)
"""

from app.models.rep_utilizadores import insert_utilizador
from werkzeug.security import generate_password_hash


def criar_utilizador(nome, senha_texto_puro, nivel):
    hash_senha = generate_password_hash(senha_texto_puro)
    sucesso = insert_utilizador(nome, hash_senha, nivel)

    if sucesso:
        print(f"Utilizador '{nome}' criado com sucesso!")
    else:
        print(f"Erro ao criar o utilizador '{nome}'.")


if __name__ == "__main__":
    # Ajuste nome, senha e nível conforme necessário
    criar_utilizador("danielly", "Tic9e10.", 1)