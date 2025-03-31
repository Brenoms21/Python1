'''media_final = float(input("Media final de 0 a 10:"))

if media_final >= 6:
    print("Aprovado!")
else:
    print("Reprovado!")
#Exercício 1
velocidade = float(input("Velocidade do carro:"))
if velocidade > 80:
 print("Você foi multado")
 multa = (velocidade - 80)*5
 print(f"0 valor da multa é R$ {multa:.2f}")
else:
 print("Você está dentro da velocidade permitida")
#Exercicio2
num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
num3 = float(input("Digite o terceiro número: "))

maior = max(num1, num2, num3)
menor = min(num1, num2, num3)

print(f"O maior número é {maior} e o menor número é {menor}.")'''

#Exercício3
salario = float(input("Digite o salário do funcionário: R$ "))
if salario > 1250:
    aumento = salario * 0.10
else:
    aumento = salario * 0.15

novo_salario = salario + aumento
print(f"O aumento foi de R$ {aumento:.2f}, e o novo salário é R$ {novo_salario:.2f}.")