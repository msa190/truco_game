file = open('resultados.log', 'r')


def contains_zap(jogada):
    if '3|1' in jogada[0:5]:
        return True
    else:
        return False


def zap_wins(jogada):
    if ('3|1' in jogada[0:2] and jogada[6] == 'A') or ('3|1' in jogada[3:5] and jogada[6] == 'B'):
        return True
    else:
        return False


zap_count = 0
zap_wins = 0

with file:
    for line in file:
        jogada = line.split(';')
        
        if contains_zap(jogada):
            zap_count += 1
        if zap_wins(jogada):
            zap_wins += 1
