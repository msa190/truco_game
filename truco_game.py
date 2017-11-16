#encoding: utf8
import random
from jogador import Jogador
log1 = open('log1.log', 'a')

DEBUG = True

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
#logx = [jogo;,jogador;,carta;,jogador;,carta;,jogador;,carta;,jogador;,carta;,jogador;,carta;,jogador;,carta;,ganhador]] 
logx = []
def jogo_de_truco(jogadorA, jogadorB, jogo=1):
	ordem = [[jogadorA, jogadorB], [jogadorB, jogadorA]]
	i = 0
	#log1.write('\n'+str(jogo) + ';')
	logx.append('\n'+str(jogo)+';')
	comecante = [0, 1]
	random.shuffle(ordem)
	
	k = comecante[0]
	#log1.write(str(ordem[k][1]))
	logx.append(str(ordem[k][1])+';')
	
	while i <= 2:
		#print k
		print '\nRodada', i + 1, '\n'
		
		carta1 = ordem[k][0].joga()
		print '\n'
		carta2 = ordem[k][1].joga()
		
		if carta1 > carta2:
			ordem[k][0].pontos += (i * i) - (2 * i) + 2
		elif carta1 < carta2:
			ordem[k][1].pontos += i*i -2*i + 2
		else:
			print '\nCangou!\n'
			ganhador = cangou(ordem[k][0], ordem[k][1], i)
			
			#funcao acaba() -------------- implementar
			#log1.write(';' + ganhador.name)
			logx.append(';;;;;;;;'+ganhador.name)
			print ganhador
			#return ganhador
			break
			#-----------------------------------------
			
		if ordem[k][0].pontos >= 3:
			ganhador = ordem[k][0]
			#funcao acaba() -------------- implementar		
			#log1.write(';' + ganhador.name)
			if i == 1:
				logx.append(';;;;;;;;' + ganhador.name)
			
			if i == 2:
				logx.append(';;;;' + ganhador.name)
			
			print ganhador
			break
			#-----------------------------------------
			
			#return ganhador
		if ordem[k][1].pontos >= 3:
			ganhador = ordem[k][1]
			
			#funcao acaba() -------------- implementar
			#log1.write(';' + ganhador.name)
			if i == 1:
				logx.append(';;;;;;;;' + ganhador.name)
			
			if i == 2:
				logx.append(';;;;' + ganhador.name)
			print ganhador
			break
			#-----------------------------------------
			
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
		
	log1.write(logx)
def acaba(jogador):
	#debug('\nThe winner is... ' + 'null')
	print '\nThe winner is...: ', jogador
	

def teste_de_truco(jogadorA, jogadorB, A=[], B=[], jogo=1):
	ordem=[[jogadorA, jogadorB], [jogadorB, jogadorA]]
	i = 0
	#log1.write('\n'+str(jogo)+';')
	comecante = [0, 1]
	#random.shuffle(ordem)
	k = comecante[0]
	#log1.write(str(ordem[k][1]))
	
	while i <= 2:
		#print k
		# print '\n---------------------------------------------Rodada', i + 1
		#debug('\n---------------------------------------------Rodada' +  str(i + 1))
		carta1 = ordem[k][0].joga(A[i])
		# print '\n'
		#debug('\n')
		carta2 = ordem[k][1].joga(B[i])
		
		if carta1 > carta2:
			ordem[k][0].pontos += i*i -2*i + 2
			
		if carta1 < carta2:
			ordem[k][1].pontos += i*i -2*i + 2
			
		if carta1 == carta2:
			# print '\nCangou!\n'
		#	debug('\nCangou!\n')
			ganhador = cangou(ordem[k][0], ordem[k][1], i)
			acaba(ganhador)
			break
			#-----------------------------------------
			
		if ordem[k][0].pontos >= 3:
			ganhador = ordem[k][0]
			acaba(ganhador)
			break
			#-----------------------------------------
			
			#return ganhador
		if ordem[k][1].pontos >= 3:
			ganhador = ordem[k][1]
			acaba(ganhador)
			break
			#-----------------------------------------
		
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


def debug(string):
	if DEBUG:
		print string
