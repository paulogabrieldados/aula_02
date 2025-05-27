

try:
    numero_01 = int(input("Digite o primeiro número: "))
    numero_02 = int(input("Digite o segundo número: "))
    resultado= numero_01 // numero_02
    print(f"O resultado da divisão inteira é: {resultado}")
except:
    print("Erro: Certifique-se de que você digitou números inteiros válidos.")
else:
    print(f"O resultado da divisão inteira de {numero_01} por {numero_02} é: {resultado}")
finally:
    print("Fim do programa.")