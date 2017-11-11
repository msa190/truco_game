import baralho
log1 = open('log1.log','a')

class Jogador():
	name = ""
	pontos = 0
	mao = None
	def __init__(self,name):
		self.mao = baralho.Mao()
		self.name = name
		return
	def __str__(self):
		return self.name
	
	def clear(self):
		self.mao = baralho.Mao()
		self.pontos = 0

	def joga(self, carta = None):
		print self
		if not carta: 
			print '\n'
			print self.mao
			carta = input('Que carta deseja jogar?  ')
		a = self.mao.cartas[carta-1]	
		del self.mao.cartas[carta-1]
		log1.write(';'+str(a))
		print str(a)
		return a

if __name__ == '__main__':
	j = Jogador('ze')
	b = baralho.BaralhoDeTruco()
	b.shuffle()

	j.mao.add_carta(b.pop())
	j.mao.add_carta(b.pop())
	j.mao.add_carta(b.pop())

	print j.mao.get_maior()
	print j.mao.get_menor()

