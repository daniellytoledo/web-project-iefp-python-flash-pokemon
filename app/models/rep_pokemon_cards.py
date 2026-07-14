from app.bd_config import conectar_pymysql
from pprint import pprint

def select_cards():
    conexao = conectar_pymysql()
    cursor  = conexao.cursor()

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
    cursor  = conexao.cursor()

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
    cursor  = conexao.cursor()

    sql = "SELECT id_t, name_t FROM tbl_types ORDER BY name_t"
    cursor.execute(sql)
    resultado = cursor.fetchall()

    cursor.close()
    conexao.close()

    return resultado

def insert_into_cards(nome, tipo, desc, img):
    conexao = conectar_pymysql()
    cursor  = conexao.cursor()

    sql = """
        INSERT INTO tbl_cards (name_c, id_t, desc_c, img_c)
        VALUES (%s, %s, %s, %s)
    """

    cursor.execute(sql, (nome, tipo, desc, img))
    conexao.commit() # commit explicito, senão os dados ficam pendentes na transação

    novo_id = cursor.lastrowid

    cursor.close()
    conexao.close()

    return novo_id

def update_card(card_id, nome, tipo, desc):
    conexao = conectar_pymysql()
    cursor  =  conexao.cursor()

    try:
        sql = "UPDATE tbl_cards SET name_c=%s, id_t=%s, desc_c=%s WHERE id_c=%s"
        cursor.execute(sql, (nome, tipo, desc, card_id))
        conexao.commit()
        return True
    except Exception as e:
        print(e)
        conexao.rollback()
        return False
    
    cursor.close()
    conexao.close()

def delete_card(id):
    conexao = conectar_pymysql()
    cursor  = conexao.cursor()

    try:
        sql    = "DELETE FROM tbl_cards WHERE id_c=%s"
        cursor.execute(sql, (id, ))
        conexao.commit()
        return True
    except Exception as e:
        print(e)
        conexao.rollback()
        return False
    
def select_pesquisa(str):
    conexao = conectar_pymysql()
    cursor  = conexao.cursor()

    pesquisa = "%"+str+"%"
    sql      = "SELECT * FROM tbl_cards WHERE name_c LIKE %s OR desc_c LIKE %s ORDER BY nome_c ASC";
    cursor.execute(sql, (pesquisa, pesquisa, pesquisa))
    resultado = cursor.fetchall()

    return (resultado)

if __name__ == "__main__":
    pprint(select_cards())