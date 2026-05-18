from random import choice, randint

def rodar_ppt(escolha_usuario):
    # Opções do computador
    opcoes = ["pedra", "papel", "tesoura"]
    escolha_computador = choice(opcoes) # Computador escolhe uma das opções

    # Verificação da lógica de vencedor e perdedor
    if escolha_computador == escolha_usuario:
        resultado = "Empate!"

    # Usuário ganha
    elif (escolha_usuario == "pedra" and escolha_computador == "tesoura") or (escolha_usuario == "papel" and escolha_computador == "pedra") or (escolha_usuario == "tesoura" and escolha_computador == "papel"):
        resultado = "Você Ganhou!!!"
        
    # Computador ganha
    elif (escolha_usuario == "pedra" and escolha_computador == "papel") or (escolha_usuario == "papel" and escolha_computador == "tesoura") or (escolha_usuario == "tesoura" and escolha_computador == "pedra"):
        resultado = "Computador Ganhou!"

    return escolha_usuario, escolha_computador, resultado

def rodar_adivinhe_num(numero_usuario):
    # Computador escolhe um número aleatório entre 0 e 100
    escolha_computador = randint(0, 100)
    resultado = ""
    numero_usuario = int(numero_usuario) # Converte a entrada do usuário para inteiro

    # Verificação do Resultado
    return numero_usuario, resultado