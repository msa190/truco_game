# from truco_test import *
import random
from datetime import datetime
import baralho
import jogador
import truco_game

mapa = [
	[1,1,1],		#[1,2,3],
	[1,2,1],		#[1,3,2],
	[2,1,1],		#[2,1,3],
	[2,2,1],		#[2,3,1],
	[3,1,1],		#[3,1,2],
	[3,2,1]			#[3,2,1],
]

N = 0 
baralho = baralho.BaralhoDeTruco()
baralho.shuffle()
baralho.shuffle()
cartas_separadas = [baralho.cartas.pop(),baralho.cartas.pop(),baralho.cartas.pop(),baralho.cartas.pop(),baralho.cartas.pop(),baralho.cartas.pop()]
jogador1 = jogador.Jogador("Mauricio")

jogador2 = jogador.Jogador('Gabriel')

for i in mapa:
	for j in mapa:
		jogador1.clear()
		jogador2.clear()
		# jogador1.mao = MaoDeTruco([cartas_separadas[0],cartas_separadas[1],cartas_separadas[2]])
		jogador1.mao.add_carta(cartas_separadas[0])
		jogador1.mao.add_carta(cartas_separadas[1])
		jogador1.mao.add_carta(cartas_separadas[2])

		# jogador2.mao = MaoDeTruco([cartas_separadas[3],cartas_separadas[4],cartas_separadas[5]])
		jogador2.mao.add_carta(cartas_separadas[3])
		jogador2.mao.add_carta(cartas_separadas[4])
		jogador2.mao.add_carta(cartas_separadas[5])
		
		truco_game.teste_de_truco(jogador1, jogador2, i, j)
		# truco_game.jogo_de_truco(jogador1, jogador2)
