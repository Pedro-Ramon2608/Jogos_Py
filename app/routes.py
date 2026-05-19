from app import app
from flask import render_template, url_for, request, session
from app.logica_jogos import rodar_ppt, rodar_adivinhe_num
from random import randint


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


@app.route("/jogo-advinhenumero", methods=["GET", "POST"])
def adivinhe_num():
    # Padrões de exibição
    resultado = None
    escolha_usuario = None

    # Se o número secreto ainda não existe na sessão, ele é criado agora
    if "numero_secreto" not in session:
        session["numero_secreto"] = randint(0, 100)

    # Pega o número fixo que está na sessão 
    escolha_computador = session["numero_secreto"]

    # Condição caso o método POST seja chamado
    if request.method == "POST":
        resposta_usuario = int(request.form.get("numero")) # Número escolhido pelo usuário

        # Chamada da função do adivinhe o número, do arquivo logica_jogos.py
        escolha_usuario, resultado = rodar_adivinhe_num(resposta_usuario, escolha_computador)

        # Se o usuário acertar, limpa a sessão para que no próximo carregamento se inicie um novo
        if resposta_usuario == escolha_computador:
            session.pop("numero_secreto", None)
        
    return render_template("adivinhe_num.html", usuario=escolha_usuario, resultado=resultado)