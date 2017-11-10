from truco_test import *
import random
from datetime import datetime

mapa = [
	[1,1,1],		#[1,2,3],
	[1,2,1],		#[1,3,2],
	[2,1,1],		#[2,1,3],
	[2,2,1],		#[2,3,1],
	[3,1,1],		#[3,1,2],
	[3,2,1]			#[3,2,1],
	]

N = 0 
baralho = BaralhoDeTruco()
random.shuffle(baralho.cartas)
random.shuffle(baralho.cartas)

cartas_separadas = [baralho.cartas.pop(),baralho.cartas.pop(),baralho.cartas.pop(),baralho.cartas.pop(),baralho.cartas.pop(),baralho.cartas.pop()]
jogador1 = Jogador("Mauricio")

jogador2 = Jogador('Gabriel')

for i in mapa:
	for j in mapa:
			jogador1.mao= MaoDeTruco([cartas_separadas[0],cartas_separadas[1],cartas_separadas[2]])
			jogador2.mao= MaoDeTruco([cartas_separadas[3],cartas_separadas[4],cartas_separadas[5]])
			teste_de_truco(jogador1,jogador2,mapa[0],mapa[0])
