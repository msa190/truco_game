log1 = open('log1.txt','a')
class Jogador():
	name = ""
	pontos = 0
	mao = 0
	#cartas = []
	def __init__(self,name):
		#for i,j in enumerate(u):
		#	self.mao.cartas.append(u[i])		
		#self.cartas = u[:]		
		self.name = name
		return
	def __str__(self):
		return self.name
	def joga(self):
		print self
		print '\n'
		print self.mao
		carta = input('Que carta deseja jogar?  ')
		a = self.mao.cartas[carta-1]	
		del self.mao.cartas[carta-1]
		log1.write(';'+str(a))
		print str(a)
		return a
		# comentário aleatório
