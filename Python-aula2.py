"""#exer1
print("Breno Martins da Silva")
#exer2
a = 3
b = 5
resultado = (2 * a) * (3 * b)
print("O resultado de 2a * 3b é:", resultado)
#exer3
e = 5
f = 8
g = 9.1
soma = e + f + g
print(soma)
#pula linha- como saber o tipo de variável
print(type(e))
print(type(g))
#pula linha - como limitar numeros de casa decimais
numero = 3.7689
print(f"o numero com duas casas decimais é {numero:.2f}.")
#pula linha - code com verdadeiro ou falso
l = True
k = False
print(type(l))
#pula linha - sinais matemáticos
num1 = 87
num2 = 76
resultado = 87 % 76
print(87 % 76)

num3 = 87
num4 = 76
resultado = 87 // 76
print(87 // 76)

num5 = 87
num6 = 76
resultado = 87 ** 76
print(87 ** 76)
#pula linha - operadores de comparação
nota = 9
media = 6
aprovado = nota>=media
print(aprovado)
#pula linha - entrada de dados
nome_comp = input("Nome completo")
idade = int(input("idade:"))
altura = float(input("altura:"))
print(nome_comp)
print(idade)
print(altura)
anos = int(input("Anos de serviço:"))
valor_por_ano = float(input("Valor por ano:"))
bonus = anos * valor_por_ano
print("Bônus de R$", bonus)"""
# Exercício 4: Soma de dois números inteiros
def soma_dois_numeros():
    num1 = int(input("Digite o primeiro número inteiro: "))
    num2 = int(input("Digite o segundo número inteiro: "))
    print("A soma é:", num1 + num2)

# Exercício 5: Conversão de metros para milímetros
def metros_para_milimetros():
    metros = float(input("Digite um valor em metros: "))
    milimetros = metros * 1000
    print(f"{metros} metros é igual a {milimetros} milímetros.")

# Exercício 6: Cálculo total em segundos
def total_em_segundos():
    dias = int(input("Digite a quantidade de dias: "))
    horas = int(input("Digite a quantidade de horas: "))
    minutos = int(input("Digite a quantidade de minutos: "))
    segundos = int(input("Digite a quantidade de segundos: "))
    total = (dias * 86400) + (horas * 3600) + (minutos * 60) + segundos
    print("Total em segundos:", total)

# Exercício 7: Aumento de salário
def aumento_salario():
    salario = float(input("Digite o valor do salário: "))
    percentual = float(input("Digite a porcentagem do aumento: "))
    aumento = salario * (percentual / 100)
    novo_salario = salario + aumento
    print(f"Aumento: R${aumento:.2f}")
    print(f"Novo salário: R${novo_salario:.2f}")

# Exercício 8: Cálculo de desconto
def calculo_desconto():
    preco = float(input("Digite o preço da mercadoria: R$"))
    percentual = float(input("Digite o percentual de desconto: "))
    desconto = preco * (percentual / 100)
    preco_final = preco - desconto
    print(f"Valor do desconto: R${desconto:.2f}")
    print(f"Preço a pagar: R${preco_final:.2f}")

# Exercício 9: Cálculo de tempo de viagem
def tempo_viagem():
    distancia = float(input("Digite a distância a percorrer em km: "))
    velocidade_media = float(input("Digite a velocidade média em km/h: "))
    tempo = distancia / velocidade_media
    print(f"Tempo de viagem: {tempo:.2f} horas")

# Exercício 10: Conversão de temperatura
def conversao_temperatura():
    celsius = float(input("Digite a temperatura em °C: "))
    fahrenheit = (celsius * 9/5) + 32
    print(f"A temperatura em °F é: {fahrenheit:.2f}")

# Exercício 11: Cálculo de aluguel de carro
def custo_aluguel():
    dias = int(input("Digite a quantidade de dias: "))
    km_rodados = float(input("Digite a quantidade de km rodados: "))
    custo_dias = dias * 60
    custo_km = km_rodados * 0.15
    total = custo_dias + custo_km
    print(f"Custo total do aluguel: R${total:.2f}")

# Exercício 12: Cálculo de z
def calcular_z():
    x = int(input("Digite o valor de x: "))
    y = int(input("Digite o valor de y: "))
    z = (x*2 + y2) / ((x - y)*2)
    print(f"O valor de z é: {z:.2f}")

# Exercício 13: Reajuste salarial
def reajuste_salarial():
    salario = float(input("Digite o salário do funcionário: R$"))
    novo_salario = salario * 1.35
    print(f"Novo salário com reajuste de 35%: R${novo_salario:.2f}")

# Chamar funções conforme necessário
soma_dois_numeros()
metros_para_milimetros()
total_em_segundos()
aumento_salario()
calculo_desconto()
tempo_viagem()
conversao_temperatura()
custo_aluguel()
calcular_z()
reajuste_salarial()
