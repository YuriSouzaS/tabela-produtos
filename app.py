from flask import Flask, render_template, request, redirect, url_for
from static.build.model import * # type: ignore

app = Flask(__name__)

# ROTA INICIAL, RETORNA TODOS OS DADOS NA TEBELA
@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == 'POST':
        name = request.form['name_product']
        add(name)
        return redirect(url_for('index'))
    return render_template("index.html", dados=show_All())


@app.route("/update/<string:id>", methods=["GET", "POST"])
def alter(id):
    alter_item(id)
    return redirect(url_for('index'))


@app.route("/delete/<string:id>", methods=["GET", "POST"])
def delete(id):
    delete_item(id)
    return redirect(url_for('index'))
    
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3000)