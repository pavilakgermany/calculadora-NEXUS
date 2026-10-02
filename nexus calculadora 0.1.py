import time
import os
from datetime import datetime
import threading

TEMPO_INATIVIDADE = 100
ultimo_movimento = time.time()


def atualizar_atividade():
    global ultimo_movimento
    ultimo_movimento = time.time()


def monitorar_inatividade():
    while True:
        if time.time() - ultimo_movimento >= TEMPO_INATIVIDADE:
            os.system("cls")
            print("NEXUS encerrado por inatividade.")
            time.sleep(2)
            os._exit(0)

        time.sleep(1)


threading.Thread(
    target=monitorar_inatividade,
    daemon=True
).start()


def clean():
    os.system("cls")


def algarismos():

    a = input("Digite o primeiro número: ")
    atualizar_atividade()

    b = input("Digite o segundo número: ")
    atualizar_atividade()

    return float(a), float(b)


def registrar_log(calculo, resultado):

    os.makedirs("logs", exist_ok=True)

    horario = datetime.now().strftime("%d/%m/%Y %H:%M:%S")

    with open("logs/calculos.txt", "a", encoding="utf-8") as arquivo:
        arquivo.write(f"[{horario}] {calculo} = {resultado}\n")


def calculadora_simples():

    print("Calculadora Simples")
    print("Escolha uma das opções abaixo:")
    print("1- Soma")
    print("2- Subtração")
    print("3- Multiplicação")
    print("4- Divisão")

    opcao = input("Digite a opção desejada: ")
    atualizar_atividade()

    clean()

    if opcao == "1":

        a, b = algarismos()

        resultado = a + b

        print(f"O resultado da soma é: {resultado}")

        registrar_log(f"{a} + {b}", resultado)

        inicio()

    elif opcao == "2":

        a, b = algarismos()

        resultado = a - b

        print(f"O resultado da subtração é: {resultado}")

        registrar_log(f"{a} - {b}", resultado)

        inicio()

    elif opcao == "3":

        a, b = algarismos()

        resultado = a * b

        print(f"O resultado da multiplicação é: {resultado}")

        registrar_log(f"{a} * {b}", resultado)

        inicio()

    elif opcao == "4":

        a, b = algarismos()

        if b == 0:

            print("Erro: Divisão por zero não é permitida.")

            calculadora_simples()

        else:

            resultado = a / b

            print(f"O resultado da divisão é: {resultado}")

            registrar_log(f"{a} / {b}", resultado)

            inicio()

    else:

        print("Opção inválida. Tente novamente.")

        calculadora_simples()


def menu():

    print("███╗   ██╗███████╗██╗  ██╗██╗   ██╗███████╗")
    time.sleep(0.5)

    print("████╗  ██║██╔════╝╚██╗██╔╝██║   ██║██╔════╝")
    time.sleep(0.5)

    print("██╔██╗ ██║█████╗   ╚███╔╝ ██║   ██║███████╗")
    time.sleep(0.5)

    print("██║╚██╗██║██╔══╝   ██╔██╗ ██║   ██║╚════██║")
    time.sleep(0.5)

    print("██║ ╚████║███████╗██╔╝ ██╗╚██████╔╝███████║")
    time.sleep(0.5)

    print("╚═╝  ╚═══╝╚══════╝╚═╝  ╚═╝ ╚═════╝ ╚══════╝")

    print(" ")

    print("Bem vindo usuário à calculadora NEXUS")
    print("Escolha uma das opções abaixo:")
    print("1-Calculadora Simples")
    print("2-Calculadora Cientifica")
    print("3-Sair")

    escolha = input("Digite a opção desejada: ")
    atualizar_atividade()

    if escolha == "1":

        clean()
        calculadora_simples()

    elif escolha == "2":

        print("Calculadora Cientifica ainda não implementada.")

        clean()
        inicio()

    elif escolha == "3":

        for i in range(3):

            print("Saindo do programa.")
            time.sleep(0.5)

            clean()

            print("Saindo do programa..")
            time.sleep(0.5)

            clean()

            print("Saindo do programa...")
            time.sleep(0.5)

            clean()

        exit()

    else:

        print("Opção inválida. Tente novamente.")

        menu()


def inicio():

    clean()
    menu()


inicio()