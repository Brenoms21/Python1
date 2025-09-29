# Integrantes do grupo: Breno Martins da Silva(563685)
#Guilherme Gama Massela(563635)
from sympy.codegen.ast import continue_


def validar_nota(nota):
    try:
        valor = float(nota)
        if 0 <= valor <= 10:
            return valor
        else:
            print("Nota inválida. Digite um valor entre 0 e 10.")
            return None
    except ValueError:
        print("Entrada inválida. Digite um número.")
        return None

def obter_notas(avaliacoes):
    notas = {}
    for chave in avaliacoes:
        while True:
            nota = input(f'Digite a nota para {chave}: ')
            valor = validar_nota(nota)
            if valor is not None:
                notas[chave] = valor
                break
    return notas

def calcular_media_semestre(notas):
    # Descartar o menor checkpoint
    cp = [notas["Checkpoint 1"], notas["Checkpoint 2"], notas["Checkpoint 3"]]
    cp.sort(reverse=True)
    cp_maiores = cp[:2]
    soma = sum(cp_maiores) + notas["Sprint 1"] + notas["Sprint 2"]
    media_40 = soma / 4
    media_sem = (media_40 * 0.4) + (notas["Global Solution"] * 0.6)
    return media_sem

def main():
    disciplina = input("Digite o nome da disciplina: ")
    nome = input("Digite o seu nome: ")

    notas = {'1º semestre': {}, '2º semestre': {}}
    for semestre in ["1º semestre", "2º semestre"]:
        print(f"Notas do {semestre}:")
        avaliacoes = [
            "Checkpoint 1",
            "Checkpoint 2",
            "Checkpoint 3",
            "Sprint 1",
            "Sprint 2",
            "Global Solution"
        ]
        notas[semestre] = obter_notas(avaliacoes)

    # Armazena as notas por semestre em um dicionário com no mínimo duas chaves
    medias = {
        '1º semestre': calcular_media_semestre(notas["1º semestre"]),
        '2º semestre': calcular_media_semestre(notas["2º semestre"])
    }

    media_final = (medias['1º semestre'] * 0.4) + (medias['2º semestre'] * 0.6)

    # Solicita e valida a frequência
    while True:

        freq = input("Digite a frequência (em %): ")
        try:
            freq_valor = float(freq)
            if 0 <= freq_valor <= 100:
                break
            else:
                print("Frequência deve estar entre 0 e 100.")
        except ValueError:
            print("Entrada inválida. Digite um número.")




    # Situação final (aprovado/reprovado)
    if freq_valor < 75 or media_final < 6:
        situacao = "Reprovado"
    else:
        situacao = "Aprovado"

    if media_final >= 4 or media_final < 6:
            situacao = "exame"


    print(f'\nDisciplina: {disciplina}')
    print(f'\nNome: {nome}')
    print(f'Média final: {media_final:.1f}')
    print(f'Situação final: {situacao}')





if __name__ == "__main__":
    main()
