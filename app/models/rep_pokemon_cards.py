from app.bd_config import conectar_pymysql
from pprint import pprint

def select_cards():
    conexao = conectar_pymysql()
    cursor = conexao.cursor()

    sql = """
        SELECT
            c.id_c,
            c.name_c,
            c.desc_c,
            c.hp_c,
            c.img_c,
            t.name_t
        FROM tbl_cards c
        INNER JOIN tbl_types t ON c.id_t = t.id_t
    """
    cursor.execute(sql)
    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultado


def select_card_id(card_id):
    conexao = conectar_pymysql()
    cursor = conexao.cursor()

    sql = """
        SELECT
            c.id_c,
            c.name_c,
            c.desc_c,
            c.hp_c,
            c.img_c,
            t.name_t
        FROM tbl_cards c
        INNER JOIN tbl_types t ON c.id_t = t.id_t
        WHERE c.id_c = %s
    """
    cursor.execute(sql, (card_id,))
    resultado = cursor.fetchone()

    cursor.close()
    conexao.close()

    return resultado

def select_types():
    conexao = conectar_pymysql()
    cursor = conexao.cursor()

    sql = "SELECT id_t, name_t FROM tbl_types ORDER BY name_t"
    cursor.execute(sql)
    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultado


if __name__ == "__main__":
    pprint(select_cards())