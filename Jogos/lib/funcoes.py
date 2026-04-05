from rich import print

def leiaInt(num):
    try:
        resposta = int(input(num))
    except (ValueError, TypeError):
        print("[red]\nERRO! Digite um número Inteiro válido.[/]")
    except KeyboardInterrupt:
        print("[red]\nERRO! Usuário preferiu não digitar.[/]")
    else:
        return resposta
