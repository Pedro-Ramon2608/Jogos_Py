from app import app
from flask import render_template, url_for, request
from random import choice

@app.route("/", methods=["GET", "POST"])
def jogos_py():
    return render_template("index.html")

@app.route("/jogo-ppt", methods=["GET", "POST"])
def ped_pap_tes():
    escolha_usuario = None
    escolha_computador = None
    resultado = None

    # Recebe os dados enviados pelo usuário
    if request.method == "POST":
        escolha_usuario = request.form.get("escolha") # 'pedra', 'papel' ou 'tesoura'

    # Opções do computador
    opcoes = ["pedra", "papel", "tesoura"]
    escolha_computador = choice(opcoes) # Computador escolhe uma das opções

    # Verificação da lógica de vencedor e perdedor
    if escolha_computador == escolha_usuario:
        resultado = "Empate!"

    elif escolha_usuario != escolha_computador:

        if escolha_usuario == "pedra":
            if escolha_computador == "papel":
                resultado = "Computador Ganhou!"
            elif escolha_computador == "tesoura":
                resultado = "Você Ganhou!!!"

        elif escolha_usuario == "papel":
            if escolha_computador == "pedra":
                resultado = "Você Ganhou!!!"
            elif escolha_computador == "tesoura":
                resultado = "Computador Ganhou!"

        elif escolha_usuario == "tesoura":
            if escolha_computador == "pedra":
                resultado = "Computador Ganhou!"
            elif escolha_computador == "papel":
                resultado = "Você Ganhou!!!"

    return render_template("ped_pap_tes.html", usuario=escolha_usuario, computador=escolha_computador, resultado=resultado)

@app.route("/jogo:advinhenumero", methods=["GET", "POST"])
def adivinhe_num():
    return render_template("adivinhe_num.html")