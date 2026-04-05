from rich import print
from Jogos.lib.funcoes import leiaInt
from Jogos.Ped_Pap_Tes import Pedra_Papel_Tesoura

while True:
    opcao = leiaInt("""Qual Jogo você deseja jogar?
[ 1 ] Pedra, Papel e Tesoura
[ 2 ] Jogo de advinhar o número
[ 3 ]Sair do programa
Opção: """)
    
    if opcao == 1:
        Pedra_Papel_Tesoura.JogarPPT()

    elif opcao == 2:
        break

    elif opcao == 3:
        break
