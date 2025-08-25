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

# ================================
# Código unindo Aula 05, 06 e 07
# ================================

# Aula 05 -> Listas: criar, adicionar elementos com append(), calcular média, pesquisa :contentReference[oaicite:0]{index=0}
notas = []  
for i in range(5):  # Aula 06 -> for com range para repetição controlada :contentReference[oaicite:1]{index=1}
    nota = float(input(f"Digite a nota {i+1}: "))
    notas.append(nota)  # usando método append da Aula 05
print("Notas digitadas:", notas)

# Aula 05 -> cálculo da média usando lista
media = sum(notas) / len(notas)
print(f"Média das notas = {media:.2f}")

# Aula 06 -> percorrer lista para encontrar maior e menor valor :contentReference[oaicite:2]{index=2}
maior = notas[0]
menor = notas[0]
for n in notas:
    if n > maior:
        maior = n
    if n < menor:
        menor = n
print(f"Maior nota = {maior}")
print(f"Menor nota = {menor}")

# Aula 07 -> Dicionário com nome:nota :contentReference[oaicite:3]{index=3}
alunos = {
    "Ana": 8.5,
    "Bruno": 6.7,
    "Carla": 9.2,
    "Diego": 7.3,
    "Eva": 8.0
}
print("\nDicionário de alunos:", alunos)

# Aula 07 -> acessar valores por chave
print("Nota da Carla:", alunos["Carla"])

# Aula 07 -> calcular média das notas do dicionário
media_alunos = sum(alunos.values()) / len(alunos)
print(f"Média da turma = {media_alunos:.2f}")

# Aula 07 -> Tupla para representar uma posição fixa (exemplo de empacotamento/desempacotamento)
posicao = (10, 20)  # coordenada (x,y)
x, y = posicao
print(f"\nExemplo de tupla: posição X={x}, Y={y}")

# Aula 06 -> usar for com range para imprimir números pares até 10 :contentReference[oaicite:4]{index=4}
print("\nNúmeros pares até 10:")
for i in range(0, 11, 2):
    print(i, end=" ")

print("\n\nPrograma finalizado com sucesso!")

