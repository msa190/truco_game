import itertools
import random
import baralho
import jogador
import truco_game

N = 0 
baralho = baralho.BaralhoDeTruco()
jogador1 = jogador.Jogador('A')

jogador2 = jogador.Jogador('B')

if __name__ == '__main__':
	i = 0

	for  rodada in itertools.permutations(baralho.cartas, 6):
		jogador1.clear()
		jogador2.clear()

		jogador1.mao.add_carta(rodada[0])
		jogador1.mao.add_carta(rodada[1])
		jogador1.mao.add_carta(rodada[2])

		jogador2.mao.add_carta(rodada[3])
		jogador2.mao.add_carta(rodada[4])
		jogador2.mao.add_carta(rodada[5])

		truco_game.teste_de_truco(jogador1, jogador2, [1,1,1], [1,1,1])

		i += 1

print i
