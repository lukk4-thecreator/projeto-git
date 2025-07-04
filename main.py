import random

# Escala pentatônica menor de E por corda (EADG)
escala_pentatonica = {
    'E': [0, 3],
    'A': [0, 2, 3],
    'D': [0, 2],
    'G': [0, 2],
}

# Todas as cordas da tablatura
todas_cordas = ['e', 'B', 'G', 'D', 'A', 'E']

# Comprimento do riff
riff_length = 16

def gerar_motivo_base():
    """Gera um pequeno padrão de 3 ou 4 notas que pode ser repetido"""
    motivo = []
    for _ in range(random.randint(3, 4)):
        corda = random.choice(list(escala_pentatonica.keys()))
        traste = random.choice(escala_pentatonica[corda])
        motivo.append((corda, traste))
    return motivo

def gerar_riff_musical_com_motivos():
    riff = []
    while len(riff) < riff_length:
        motivo = gerar_motivo_base()

        # Adiciona o motivo ou uma pequena variação dele
        if random.random() < 0.3:
            motivo = [(c, f + 1 if f + 1 in escala_pentatonica.get(c, []) else f) for c, f in motivo]
        riff.extend(motivo)
    return riff[:riff_length]

def formatar_tablatura(riff):
    tab = {s: [] for s in todas_cordas}
    for nota in riff:
        for s in todas_cordas:
            if s == nota[0]:
                tab[s].append(f"{nota[1]:<2}")
            else:
                tab[s].append("--")
    print("\n🎸 Riff Musical em Escala Pentatônica:\n")
    for s in reversed(todas_cordas):
        print(f"{s}|", end="")
        for f in tab[s]:
            print(f"{f}", end="-")
        print()

# Gerar e mostrar riff musical
riff = gerar_riff_musical_com_motivos()
formatar_tablatura(riff)
