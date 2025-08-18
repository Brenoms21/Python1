'''nomes_alunos = ["Giovanna", "Gustavo", "Vinicius", "Davi"]
pesquisa = input("Digite o nome do aluno:").capitalize()

x = 0
for nome in nomes_alunos:
    if nome == pesquisa:
        print("Nome encontrado.")
        print(x)
        break
    x += 1

else:
    print("Nome não encontrado.")'''
'''numeros_pares = []
for num in range(2,11,2):
    numeros_pares.append(num)
    print(numeros_pares) '''
'''L = [1,7,2,4]
maximo = L[0]
for e in L:
    maximo = e
print(maximo)'''

'''notas = [8,5.5,7.8,9.6,10,6.2]
maxima = notas[0]

for nota in notas:
    if nota > maxima:
        maxima = nota
print(maxima)'''
#Exercicio1
'''L = [1, 7, 2, 4]
minimo = L[0]
for e in L:
if e < minimo:
minimo = e
print(minimo)
#Exercicio2
T = [-10, -8, 0, 1, 2, 5, -2, -4]
maior = T[0]
menor = T[0]
soma = 0
for e in T:
if e > maior:
maior = e
if e < menor:
menor = e
soma += e
print(f"Temperatura maior = {maior}ºC")
print(f"Temperatura menor = {menor}ºC")
print(f"Temperatura média = {soma/len(T)}")
#Exercicio3
V = [9, 8, 7, 12, 0, 13, 21]
P = []
I = []
for e in V:
if e % 2 == 0:
P.append(e)
else:
I.append(e)
print("Pares:",P)
print("Ímpares:",I)
#Exercicio4
compras = []
while True:
item = input("Entre com o item: ")
if item == "fim":
break
compras.append(item)
for i in compras:
print(i) '''


