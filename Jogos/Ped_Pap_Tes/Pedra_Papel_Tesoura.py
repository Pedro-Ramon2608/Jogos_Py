from rich import print
from random import randint
from ..lib.funcoes import leiaInt

ppt = [
    "Pedra", # Número 1
    "Papel", # Número 2
    "Tesoura" #Número 3
]


def JogarPPT():
    while True:
        opcao = leiaInt("""
Digite a opção desejada:
[ 1 ] Pedra
[ 2 ] Papel
[ 3 ] Tesoura
[ 4 ] Encerrar Jogo
Opção: """)

        computador = randint(1, 3)

        if opcao == 1: # Usuário escolheu Pedra
            
            if computador == 1: # Computador jogou Pedra
                break
            elif computador == 2: # Computador jogou Papel
                break
            elif computador == 3: # Computador jogou Tesoura
                break


        elif opcao == 2: # Usuário jogou Papel

            if computador == 1: # Computador jogou Pedra
                break
            elif computador == 2: # Computador jogou Papel
                break
            elif computador == 3: # Computador jogou Tesoura
                break


        elif opcao == 3: # Usuário jogou Tesoura

            if computador == 1: # Computador jogou Pedra
                break
            elif computador == 2: # Computador jogou Papel
                break
            elif computador == 3: # Computador jogou Tesoura
                break

        elif opcao == 4: # Encerra o programa
            break
        else:
            print("ERRO! Número inválido.")
