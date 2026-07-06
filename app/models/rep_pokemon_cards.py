from app.bd_config import conectar_pymysql
from pprint import pprint

def select_cards():
    conexao = conectar_pymysql()
    cursor  = conexao.cursor()

    sql = "SELECT * from pokemon_cards"
    cursor.execute(sql)
    resultado = cursor.fetchall()

    return(resultado)

if __name__ == "__main__":
    pprint(select_cards())