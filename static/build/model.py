import sqlite3
from sqlite3 import Error

# CRIA CONEXÃO COM O BANCO DE DADOS
def conecta_db():
  conn = None
  
  try:
    conn = sqlite3.connect("produtos.db")
  except Error as e:
    print(e)
  
  return conn


# BUSCA AS INFORMAÇÕES NO BANCO DE DADOS
def show_All():
    conn = conecta_db()
    cur = conn.cursor()
    all_date = cur.execute('SELECT * FROM produtos;').fetchall()
    return all_date

#  ADICIONA UM NOVO ITEM
def add(name):
    conn = conecta_db()
    
    with conn:
        sql = f'''INSERT INTO produtos (name) VALUES ('{name}')'''
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return cur.lastrowid
    
# ALTERA UM PRODUTO
def alter_item(id, name):
    conn = conecta_db()
    with conn:
        sql = f'''UPDATE produtos SET name='{name}' WHERE id='{id}' '''
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

# DELETA UM PRODUTO
def delete_item(id):
    conn = conecta_db()
    
    with conn:
        sql = f'''DELETE FROM produtos WHERE id='{id}'  '''
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()