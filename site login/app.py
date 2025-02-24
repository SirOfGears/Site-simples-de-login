from flask import Flask, render_template, request

app = Flask(__name__)

nomes = ['2', '3', '4', '5']
senhas = ['0000', '1234', '5575', '1144']

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        nome = request.form['nome']
        if nome == "1":
            return "Acesso liberado e direto sem senha"
        else:
            senha = request.form['senha']
            if senha in senhas:
                return "Acesso liberado"
            else:
                return "Senha incorreta"
    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)
