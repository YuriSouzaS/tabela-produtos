import sqlite3
from sqlite3 import Error

# CRIAR CONEXÃO COM O BANCO DE DADOS
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

#  ADICIONAR UM ELEMENTO
def add_item(name):
    conn = conecta_db()
    
    with conn:
        sql = f'''INSERT INTO produtos (name) VALUES ('{name}')'''
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return cur.lastrowid
    
# ALTERAR UM ELEMENTO
def alter_item(name, id):
    conn = conecta_db()
    
    with conn:
        sql = f'''UPDATE produtos SET name='{name}' WHERE id='{id}'; '''
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()

# DELETA UM ELEMENTO
def delete_item(id):
    conn = conecta_db()
    
    with conn:
        sql = f'''DELETE FROM produtos WHERE id='{id}'  '''
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()