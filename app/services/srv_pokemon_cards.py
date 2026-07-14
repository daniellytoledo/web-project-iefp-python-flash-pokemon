from app.models.rep_pokemon_cards import select_cards, select_card_id, select_types, insert_into_cards, update_card, delete_card, select_pesquisa
from pprint import pprint

def lista_cards():
    return select_cards()

def detalhes_card(card_id):
    return select_card_id(card_id)

def lista_tipos():
    return select_types()

def adicionar_pokemon(nome, tipo, desc, img):
    return insert_into_cards(nome, tipo, desc, img)

def atualizar_card(card_id, nome, tipo, desc):
    return update_card(card_id, nome, tipo, desc)

def eliminar_card(id):
    return delete_card(id)

def pesquisa_card(texto):
    dados = select_pesquisa(texto)
    lista_final = []
    for card in dados:
        dadosPesquisados = {
            "id": card['id_c'],
            "nome": card['name_c'],
            "desc": desc_resumo_pesq(card['desc_c'], texto)
        }
        lista_final.append(dadosPesquisados)
    return (texto, lista_final)

def desc_resumo_pesq(desc, pesq):
    desc_1 = desc.lower()
    pesq_1 = pesq.lower()

    tamanho = len(desc)
    tamanho_pesq = len(pesq)

    posicao = desc_1.find(pesq_1)

    # se não encontrar a pesquisa
    if posicao == -1:
        return desc[:220] + ("..." if len(desc) > 220 else "")
    
    str_sem_negrito = desc[posicao:posicao + tamanho_pesq]

    qnts_car = 110
    inicio   = 0 if posicao < qnts_car else posicao - qnts_car

    reticencias_inicio = "..." if posicao > qnts_car else ""
    reticencias_final  = "..." if posicao < (tamanho - qnts_car) else ""

    resumo   = desc[inicio:inicio + qnts_car * 2]
    resposta = reticencias_inicio + resumo + reticencias_final

    # substituição ignorando maiúsculas/minúsculas
    import re
    substituto = f"<strong>{str_sem_negrito}</strong>"
    resposta = re.sub(
        re.escape(pesq),
        substituto,
        resposta,
        flags=re.IGNORECASE
    )

    return resposta

