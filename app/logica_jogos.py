from random import choice

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

def rodar_adivinhe_num(numero_usuario, escolha_computador):
    # Verificação do Resultado
    if numero_usuario == escolha_computador:
        resultado = "Ih rapaz, passou longe em... Longe de ERRAR! Você Acertou!!!"
    elif numero_usuario > escolha_computador:
        resultado = "Eita, pensou alto em, assim você não vai acertar mesmo..."
    elif numero_usuario < escolha_computador:
        resultado = f"Rapaz, se você tentasse um {numero_usuario} + x, talvez você acertasse..."

    return numero_usuario, resultado
