#encoding: utf8
import random
from Truco import *
from Jogador import Jogador
log1 = open('log1.txt','a')
# vai ter um while aqui:
jogo=1



def teste_de_truco(jogadorA,jogadorB, A = [], B = [],jogo = 1):
	ordem=[[jogadorA,jogadorB],[jogadorB,jogadorA]]
	i = 0
	#log1.write('\n'+str(jogo)+';')
	comecante = [0,1]
	random.shuffle(ordem)
	k = comecante[0]
	#log1.write(str(ordem[k][1]))
	
	while i<= 2:
		#print k
		print '\nRodada',i+1,'\n'
		
		carta1 = ordem[k][0].joga(A[i])
		print '\n'
		carta2 = ordem[k][1].joga(B[i])
		
		if carta1>carta2:
			ordem[k][0].pontos += i*i -2*i + 2
			
		if carta1<carta2:
			ordem[k][1].pontos += i*i -2*i + 2
			
		if carta1==carta2:
			print "\nCangou!\n"
			ganhador = cangou(ordem[k][0],ordem[k][1],i)
			
			#funcao acaba() -------------- implementar
		#	log1.write(';'+ganhador.name)
			print ganhador
			#return ganhador
			break
			#-----------------------------------------
			
		if ordem[k][0].pontos >= 3:
			ganhador = ordem[k][0]
			
			#funcao acaba() -------------- implementar		
		#	log1.write(';'+ganhador.name)
			print ganhador
			break
			#-----------------------------------------
			
			#return ganhador
		if ordem[k][1].pontos >= 3:
			ganhador = ordem[k][1]

			#funcao acaba() -------------- implementar
		#	log1.write(';'+ganhador.name)
			print ganhador
			break
			#-----------------------------------------
			
			#return ganhador	
		if carta1>carta2:
			print "Torna a maior"
		if carta1<carta2:
			buff = k
			print 'Torna a maior'
			if buff == 0:
				k = 1			
			if buff == 1:
				k = 0
				
		i+=1
