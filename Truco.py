from Baralho import *
class BaralhoDeTruco(Mao):
	def __init__(self):
		#define o zap
		self.cartas.append(Carta(3,1))
		self.cartas[-1].valor = 9
	
		#define o sete de copas
		self.cartas.append(Carta(6,2))
		self.cartas[-1].valor = 8

		#define o espadilha
		self.cartas.append(Carta(0,3))
		self.cartas[-1].valor = 7

		#define o sete de ouro
		self.cartas.append(Carta(6,0))
		self.cartas[-1].valor = 6
	
		for i in range(13):
			for j in range(4):
				if i == 0:
					if j!= 3:
						self.cartas.append(Carta(i,j))
						self.cartas[-1].valor = 3
				if i == 1:
					self.cartas.append(Carta(i,j))
					self.cartas[-1].valor = 4
				if i == 2:
					self.cartas.append(Carta(i,j))
					self.cartas[-1].valor = 5	
				if i == 10:
					self.cartas.append(Carta(i,j))
					self.cartas[-1].valor = 1
				if i == 11:
					self.cartas.append(Carta(i,j))
					self.cartas[-1].valor = 0
				if i == 12:
					self.cartas.append(Carta(i,j))

					self.cartas[-1].valor = 2
class MaoDeTruco(Mao):
	def __init__(self,a = []):
		self.cartas = a[:]
	
	def mao_da_maior(self):
		if self.cartas[0]>self.cartas[1]:
			return self.cartas[0]
		if self.cartas[1]>self.cartas[0]:
			return self.cartas[1]

def cangou(jogadorA,jogadorB,i):
	if i == 0:
		if jogadorA.mao.mao_da_maior() > jogadorB.mao.mao_da_maior():
			return jogadorA
		if jogadorA.mao.mao_da_maior() < jogadorB.mao.mao_da_maior():
			return jogadorB
	else:
 		if jogadorA.pontos> jogadorB.pontos:
			return jogadorA
		if jogadorA.pontos<jogadorB.pontos:
			return jogadorB


