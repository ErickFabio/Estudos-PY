import random
import operacoes
from colorama import Fore

def exibir_menu():
    print("1. Soma")
    print("2. Subtraçao")
    print("3. multiplicacao")
    print("4. divisão")
    print("5. Número Aleatório")
    print("0. Sair")

def obter_numeros():
    a = float(input("Digite o primeiro número: "))
    b = float(input("Digite o segundo número: "))
    return[a, b]

while True:
    exibir_menu()

    opcao = input ("Escolha uma opção: ")
    if (opcao == "0") :
        print("Saindo do Sistema!")
        break

    if (opcao == "1"):
        a, b = obter_numeros()
        resultado = operacoes.soma(a, b)
        print(f"Resultado: {resultado}")
    elif (opcao == "2"):
        a, b = obter_numeros()
        resultado = operacoes.subtracao(a, b)
        print(f"Resultado: {resultado}")
    elif (opcao == "3"):
        a, b = obter_numeros()
        resultado = operacoes.multiplicacao(a, b)
        print("Resultado: ", {resultado})
    elif opcao == "4":
        a, b = obter_numeros()
        if b != 0:
            resultado = operacoes.divisão(a, b)
            print("Resultado: ", {resultado})
        else:
            print("Não é possivel dividir por Zero!")
    elif opcao == "5":
        a, b = obter_numeros()
        resultado = random.randint(a, b)
        print("Resultado: ", {resultado})

    else:
        print(Fore.RED+"Opção Inválida. Tente novamente!")