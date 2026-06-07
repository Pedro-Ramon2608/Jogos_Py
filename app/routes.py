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
    # Recebe escolha da categoria
    if request.method == "POST":
        categoria = request.form.get("categoria") # anime, filme, serie, desenho, jogo, comida, fruta
        
        # Escolha a lista de palavras de acordo com a categoria
        lista = listaPalavras(categoria)

        # Escolha da palavra secreta dentre as opções da lista
        palavra_secreta = choice(lista)

        # Salvamento de tudo que o jogo precisa dentro de session
        session["forca_categoria"] = categoria
        session["forca_palavra"] = palavra_secreta
        session["forca_letras_chutadas"] = [] # Guarda palavras que o usuário ja chutou
        session["forca_tentativas_restantes"] = 6

        # Redireciona para a página do jogo já com a categoria e a palavra
        return redirect(url_for("jogar_forca"))

    return render_template("forca.html")

@app.route("/jogo-forca/jogar", methods=["GET", "POST"])
def jogar_forca():
    # Se o usuário acessar a rota sem escolher a categoria, ele volta
    if "forca_categoria" not in session:
        return redirect(url_for("jogo_da_forca"))
    
    # Recupera os dados da session
    categoria = session["forca_categoria"]
    palavra = session["forca_palavra"]
    letras_chutadas = session["forca_letras_chutadas"]
    tentativas = session["forca_tentativas_restantes"]

    # Recebe as letras 
    if request.method == "POST":
        letra = request.form.get("letra")

    return render_template("jogar_forca.html")