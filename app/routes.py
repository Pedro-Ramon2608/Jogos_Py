from app import app
from flask import render_template, url_for, request, session, redirect
from app.logica_jogos import rodar_ppt, rodar_adivinhe_num
from app.auxiliares import listaPalavras
from random import randint, choice


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

@app.route("/jogo-forca", methods=["GET", "POST"])
def jogo_da_forca():
    resultado = None
    # Recebe escolha da categoria
    if request.method == "POST":
        categoria = request.form.get("categoria") # anime, filme, serie, desenho, jogo, comida, fruta
        
        # Escolha da lista de palavras de acordo com a categoria
        lista = listaPalavras(categoria)

        # Escolha da palavra dentre as opções da lista
        palavra = choice(lista)

        # Redireciona para a página do jogo já com a categoria e a palavra
        return redirect(url_for("jogar_forca"))

    return render_template("forca.html")

@app.route("/jogo-forca/jogar", methods=["GET", "POST"])
def jogar_forca():
    return render_template("jogar_forca.html")