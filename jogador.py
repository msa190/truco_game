import baralho


class Jogador():
	name = ""
	pontos = 0
	mao = None

	def __init__(self, name):
		self.mao = baralho.Mao()
		self.name = name
		return

	def __str__(self):
		return self.name
	
	def clear(self):
		self.mao = baralho.Mao()
		self.pontos = 0

	def joga(self, carta=None):
		if not carta: 
			print '\n'
			print self.mao
			carta = input('Que carta deseja jogar?  ')
		
		a = self.mao.pop()
		
		return a