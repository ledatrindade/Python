import math

while True:
    print("Por favor, selecione o comando desejado:")
    print("1 ( Adição )\n2 ( Subtração )\n3 ( Multiplicação )\n4 ( Divisão )\n5 ( Raiz Quadrada )\n6 ( Maior de 3 Números)\n7 ( Média de 4 Números )\n 8 ( Sair )")

    escolha = input("Digite o número do comando desejado: ")

    if escolha == "1":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 + num2
        print(f"Resultado da adição: {resultado}")
    elif escolha == "2":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 - num2
        print(f"Resultado da subtração: {resultado}")
    elif escolha == "3":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        resultado = num1 * num2
        print(f"Resultado da multiplicação: {resultado}")
    elif escolha == "4":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        if num2 != 0:
            resultado = num1 / num2
            print(f"Resultado da divisão: {resultado}")
        else:
            print("Não é possível dividir por zero.")
    elif escolha == "5":
        num = float(input("Digite o número para calcular a raiz quadrada: "))
        resultado = math.sqrt(num)
        print(f"Raiz quadrada: {resultado}")
    elif escolha == "6":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        num3 = float(input("Digite o terceiro número: "))
        maior = max(num1, num2, num3)
        print(f"O maior número é: {maior}")
    elif escolha == "7":
        num1 = float(input("Digite o primeiro número: "))
        num2 = float(input("Digite o segundo número: "))
        num3 = float(input("Digite o terceiro número: "))
        num4 = float(input("Digite o quarto número: "))
        media = (num1 + num2 + num3 + num4) / 4
        print(f"Média dos 4 números: {media}")
    elif escolha == "8":
        print("Saindo do programa.")
        break
    else:
        print("Escolha inválida. Por favor, escolha uma opção válida.")