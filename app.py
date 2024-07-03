from flask import Flask, render_template, request, redirect, url_for
import sqlite3

app = Flask(__name__)

# BUSCA AS INFORMAÇÕES NO BANCO DE DADOS
def show_All():
    conn = sqlite3.connect('produtos.db')
    cur = conn.cursor()
    all_date = cur.execute('SELECT * FROM produtos;').fetchall()
    return all_date

#  ADICIONA UM NOVO ITEM
def add(name):
    conn = sqlite3.connect('produtos.db')
    
    with conn:
        sql = f'''INSERT INTO produtos (name) VALUES ('{name}')'''
        cur = conn.cursor()
        cur.execute(sql)
        conn.commit()
        return cur.lastrowid
    
# ROTA INICIAL, RETORNA TODOS OS DADOS NA TEBELA
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        name = request.form['name_product']
        add(name)
        return redirect(url_for('index'))
    return render_template("index.html", dados=show_All())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)