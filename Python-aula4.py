'''x = 1
while x <= 100:
    print(x)
    x = x+1

x = 50
while x <= 100:
    print(x)
    x = x+50'''

x = 10
while x >= 0:
    print(x)
    x -= 1

print("Fogo")
#exercicio 4 - Imprimir de 1 até N mostrando apenas os ímpares
n = int(input("Digite um número: "))
i = 1

while i <= n:
    if i % 2 != 0:
        print(i)
    i += 1
#exercício 5 -  Escrever os 10 primeiros múltiplos de 3
contador = 1
while contador <= 10:
    print(contador * 3)
    contador += 1
#exercicio 6 - Tabuada de um número (de 1 a 10)
num = int(input("Digite o número da tabuada: "))
i = 1

while i <= 10:
    print(f"{num} x {i} = {num * i}")
    i += 1
#exercicio 7 - num = int(input("Digite o número da tabuada: "))
inicio = int(input("Digite o início: "))
fim = int(input("Digite o fim: "))

i = inicio
while i <= fim:
    print(f"{num} x {i} = {num * i}")
    i += 1
#exercicio 8 - deposito = float(input("Depósito inicial: "))
juros = float(input("Taxa de juros (% ao mês): ")) / 100

mes = 1
total = deposito

while mes <= 24:
    total += total * juros
    print(f"Mês {mes}: R${total:.2f}")
    mes += 1

ganho = total - deposito
print(f"Total ganho com juros: R${ganho:.2f}")
#exercicio 9 - Poupança com depósitos mensais
deposito = float(input("Depósito inicial: "))
juros = float(input("Taxa de juros (% ao mês): ")) / 100
mensal = float(input("Depósito mensal: "))

mes = 1
total = deposito

while mes <= 24:
    total += total * juros
    total += mensal
    print(f"Mês {mes}: R${total:.2f}")
    mes += 1

ganho = total - (deposito + mensal * 24)
print(f"Total ganho com juros: R${ganho:.2f}")
#exercicios 10 - Ler números até digitar 0 e mostrar soma e média
soma = 0
quantidade = 0

num = int(input("Digite um número (0 para sair): "))
while num != 0:
    soma += num
    quantidade += 1
    num = int(input("Digite outro número (0 para sair): "))

if quantidade > 0:
    media = soma / quantidade
    print(f"Quantidade: {quantidade}, Soma: {soma}, Média: {media:.2f}")
else:
    print("Nenhum número foi digitado.")
#exercicio 11 - Máquina registradora com códigos
total = 0

while True:
    codigo = int(input("Digite o código do produto (0 para sair): "))
    if codigo == 0:
        break

    if codigo in [1, 2, 3, 5, 9]:
        quantidade = int(input("Digite a quantidade: "))
        if codigo == 1:
            preco = 0.50
        elif codigo == 2:
            preco = 1.00
        elif codigo == 3:
            preco = 4.00
        elif codigo == 5:
            preco = 7.00
        elif codigo == 9:
            preco = 8.00
        total += preco * quantidade
    else:
        print("Código inválido.")

print(f"Total da compra: R${total:.2f}")
