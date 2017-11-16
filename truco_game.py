#encoding: utf8
import random
from jogador import Jogador
log1 = open('resultados.log', 'w')

DEBUG = False

def cangou(jogadorA, jogadorB, i, caso=0):
	empate = Jogador('empate')

	if i == 0:
		if jogadorA.mao.get_maior() > jogadorB.mao.get_maior():
			return jogadorA
		elif jogadorA.mao.get_maior() < jogadorB.mao.get_maior():			
			return jogadorB
		else:
			if jogadorA.mao.get_menor() > jogadorB.mao.get_menor():
				return jogadorA
				
			if jogadorA.mao.get_menor() < jogadorB.mao.get_menor():
				return jogadorB

			if jogadorA.mao.get_menor() == jogadorB.mao.get_menor():
				return empate
			
	else:
 		if jogadorA.pontos > jogadorB.pontos:
			return jogadorA

		if jogadorA.pontos < jogadorB.pontos:
			return jogadorB


def jogo_de_truco(jogadorA, jogadorB, jogo=1):
	ordem = [[jogadorA, jogadorB], [jogadorB, jogadorA]]
	i = 0
	comecante = [0, 1]
	random.shuffle(ordem)
	
	k = comecante[0]
	
	while i <= 2:
		#debug( '\nRodada', i + 1, '\n')
		
		carta1 = ordem[k][0].joga()
		#debug( '\n')
		carta2 = ordem[k][1].joga()
		
		if carta1 > carta2:
			ordem[k][0].pontos += (i * i) - (2 * i) + 2
		elif carta1 < carta2:
			ordem[k][1].pontos += i*i -2*i + 2
		else:
			debug('\nCangou!\n')
			ganhador = cangou(ordem[k][0], ordem[k][1], i)

			debug(ganhador)
			break
			
		if ordem[k][0].pontos >= 3:
			ganhador = ordem[k][0]
			if i == 1:
				pass
			
			if i == 2:
				pass
			
			print ganhador
			break
			
			#return ganhador
		if ordem[k][1].pontos >= 3:
			ganhador = ordem[k][1]
			
			if i == 1:
				pass
			
			if i == 2:
				pass
			print ganhador
			break

			#return ganhador	

		#Is useful ?
		if carta1 > carta2:
			print "Torna a maior"
		elif carta1 < carta2:
			buff = k
			print 'Torna a maior'
			if buff == 0:
				k = 1			
			if buff == 1:
				k = 0
	
		i += 1


def acaba(jogador):
	debug('\nThe winner is... ' + str(jogador))


def teste_de_truco(jogadorA, jogadorB, A=[], B=[], jogo=1):
	logx = ''
	ordem=[[jogadorA, jogadorB], [jogadorB, jogadorA]]
	i = 0
	comecante = [0, 1]
	k = comecante[0]
	
	logx += str(jogadorA.mao.cartas[0]) + ';' + str(jogadorA.mao.cartas[1]) + ';' + str(jogadorA.mao.cartas[2]) + ';'
	logx += str(jogadorB.mao.cartas[0]) + ';' +  str(jogadorB.mao.cartas[1]) + ';' + str(jogadorB.mao.cartas[2]) + ';'

	while i <= 2:
		debug('\n---------------------------------------------Rodada' +  str(i + 1))
		carta1 = ordem[k][0].joga(A[i])
		
		debug('\n')
		
		carta2 = ordem[k][1].joga(B[i])

		if carta1 > carta2:
			ordem[k][0].pontos += i*i -2*i + 2
			
		if carta1 < carta2:
			ordem[k][1].pontos += i*i -2*i + 2
			
		if carta1 == carta2:
			debug('\nCangou!\n')
			ganhador = cangou(ordem[k][0], ordem[k][1], i)
			acaba(ganhador)
			logx += str(ganhador) + ';' + str(i + 1)
			break
			
		if ordem[k][0].pontos >= 3:
			ganhador = ordem[k][0]
			acaba(ganhador)
			logx += str(ganhador) + ';' + str(i + 1)
			break
			
		if ordem[k][1].pontos >= 3:
			ganhador = ordem[k][1]
			acaba(ganhador)
			logx += str(ganhador) + ';' + str(i + 1)
			break
		
		if carta1 > carta2:
			debug('Torna a maior') 
		elif carta1 < carta2:
			buff = comecante[0]
			debug('Torna a maior')
			if buff == 0:
				k = 1			
			if buff == 1:
				k = 0
			i += 1

	log1.write(logx + '\n')

def debug(string):
	if DEBUG:
		print string
