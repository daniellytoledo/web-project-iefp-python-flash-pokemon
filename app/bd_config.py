import pymysql
import os
from dotenv import load_dotenv

load_dotenv()

def conectar_pymysql():
    return pymysql.connect(
        host=os.getenv("DB_HOST"),
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        database=os.getenv("DB_NAME"),
        autocommit=False,
        cursorclass=pymysql.cursors.DictCursor
    )

def teste ():
    sql = "SELECT * FROM tbl_cards"
    conexao = conectar_pymysql()
    cursor = conexao.cursor()
    cursor.execute(sql)

    resultado = cursor.fetchall()

    return resultado

if __name__ == "__main__":
    print(teste())