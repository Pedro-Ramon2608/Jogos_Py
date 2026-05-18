from app import app
from flask import render_template, url_for, request
from app.logica_jogos import rodar_ppt, rodar_adivinhe_num


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
        resposta_usuario = request.form.get("escolha") # 'pedra', 'papel' ou 'tesoura'

        # Chamada da função do pedra, papel e tesoura, do arquivo logica_jogos.py
        escolha_usuario, escolha_computador, resultado = rodar_ppt(resposta_usuario) 

    return render_template("ped_pap_tes.html", usuario=escolha_usuario, computador=escolha_computador, resultado=resultado)


@app.route("/jogo:advinhenumero", methods=["GET", "POST"])
def adivinhe_num():
    resultado = None
    escolha_usuario = None

    if request.method == "POST":
        numero_usuario = request.form.get("numero") # Número escolhido pelo usuário

        # Chamada da função do adivinhe o número, do arquivo logica_jogos.py
        escolha_usuario, resultado = rodar_adivinhe_num(numero_usuario)
        
    return render_template("adivinhe_num.html", usuario=escolha_usuario, resultado=resultado)