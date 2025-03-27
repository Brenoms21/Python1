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
#Exercicios
num1 = int(input("Numero 1:"))
num2 = int(input("Numero 2:"))
soma = num1 + num2
print("Resultado",soma)
