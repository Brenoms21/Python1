# Vídeo: https://youtu.be/XNun7PU-btk
# Integrantes: Breno Silva (RM 563685), Leonardo Eiji (RM 562934), Henrique Augusto Cruz (RM 564586)

# Dados simulados: [velocidade_kmh, direcao_graus, umidade_%]
leituras = [
    [20, 45, 50],
    [25, 60, 48],
    [80, 170, 18],   # Crítica: velocidade e umidade
    [85, 300, 96],   # Crítica: velocidade, direção, umidade
    [78, 90, 22],
    [40, 270, 55],
    [90, 100, 15],   # Crítica: velocidade e umidade
    [60, 250, 99],   # Crítica: umidade
    [25, 245, 55],
    [30, 265, 52]
]

total_leituras = len(leituras)
leituras_criticas = 0
velocidades = []
direcoes = []
umidades = []

print("### Relatório do SmartWind Guardian ###\n")

for i in range(total_leituras):
    vel, dir, umi = leituras[i]
    velocidades.append(vel)
    direcoes.append(dir)
    umidades.append(umi)

    alerta = False

    if vel > 75:
        alerta = True
    if umi < 20 or umi > 95:
        alerta = True
    if i > 0:
        variacao_direcao = abs(dir - leituras[i-1][1])
        if variacao_direcao > 100:
            alerta = True

    if alerta:
        print(f"Leitura {i+1}: Alerta: Condições de vento severo identificadas!")
        leituras_criticas += 1
    else:
        print(f"Leitura {i+1}: Sistema estável. Nenhuma anomalia detectada.")

# Cálculo de média e desvio padrão (manual)
def media(lista):
    soma = 0
    for valor in lista:
        soma += valor
    return soma / len(lista)

def desvio_padrao(lista):
    m = media(lista)
    soma = 0
    for valor in lista:
        soma += (valor - m) ** 2
    return (soma / len(lista)) ** 0.5

media_vel = media(velocidades)
media_dir = media(direcoes)
media_umi = media(umidades)

dp_vel = desvio_padrao(velocidades)
dp_dir = desvio_padrao(direcoes)
dp_umi = desvio_padrao(umidades)

print("\n--- Estatísticas ---")
print(f"Média da Velocidade do Vento: {media_vel:.2f} km/h")
print(f"Desvio Padrão da Velocidade: {dp_vel:.2f}")
print(f"Média da Direção do Vento: {media_dir:.2f}°")
print(f"Desvio Padrão da Direção: {dp_dir:.2f}")
print(f"Média da Umidade: {media_umi:.2f}%")
print(f"Desvio Padrão da Umidade: {dp_umi:.2f}")

# Estado geral
percentual_critico = (leituras_criticas / total_leituras) * 100
estado = "Instável" if percentual_critico > 40 else "Estável"
print(f"\nEstado Geral: {estado}")

# Análise histórica
print("\n--- Análise Histórica ---")
print(f"Velocidade - Máxima: {max(velocidades)} km/h, Mínima: {min(velocidades)} km/h")
print(f"Direção - Máxima: {max(direcoes)}°, Mínima: {min(direcoes)}°")
print(f"Umidade - Máxima: {max(umidades)}%, Mínima: {min(umidades)}%")

# Tendência da velocidade (básico: crescente, decrescente ou estável)
if velocidades[-1] > velocidades[0]:
    print("Tendência da Velocidade do Vento: Crescente")
elif velocidades[-1] < velocidades[0]:
    print("Tendência da Velocidade do Vento: Decrescente")
else:
    print("Tendência da Velocidade do Vento: Estável")
