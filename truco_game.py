#encoding: utf8
class Carta:
	_numeros = ['As','2','3','4','5','6','7','8','9','10','J','Q','K']
	_naipes=['ouros', 'paus','copas','espadas']
	valor = 0	
	numero = None
	naipe = None

	def __init__(self, a, b):
		if(a in self._numeros and b in self._naipes ):
			self.numero = a		
			self.naipe = b
		if(a in range(len(self._numeros)) and b in range(len(self._naipes))):
			self.numero = self._numeros[a]
			self.naipe = self._naipes[b]
	def __str__(self):
		return self.numero + ' de ' + self.naipe
	
	def __eq__(self, b):
		if self.numero == b.numero and self.naipe == b.naipe:
			return True
		else:
			return False
	def __lt__(self,b):
		if self.valor < b.valor:
			return True
	def __gt__(self,b):
		if self.valor > b.valor:
			return True
	
class Mao:
	cartas = []
	def __str__(self):
		for i in self.cartas:
			string = ''
			for i in self.cartas:
				string +=i.numero +' de '+i.naipe
				string +='\n'
		return string
class MaoDeTruco(Mao):
	def __init__(self,a = []):
		self.cartas = a[:]
		
class BaralhoDeTruco(Mao):
	def __init__(self):
		#define o zap
		self.cartas.append(Carta(3,1))
		self.cartas[-1].valor = 9
	
		#define o sete de copas
		self.cartas.append(Carta(6,2))
		self.cartas[-1].valor = 8

		#define o espadilha
		self.cartas.append(Carta(0,1))
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
class Jogador:
	nome = ""
	def __init__(self, nome):
		self.nome = nome
	def joga(self):
		mesa.cartas.append()
		del self.cartas[-1]
	cartas = []
	pontos = 0
	
def mao_da_maior(a =[]):
	if a[0]>a[1]:
		if a[0]>a[2]:
			return a[0]
		if (a[0]>a[2])==None:
			return a[0]
		if a[2]>a[0]:
			return a[2]
	if a[0]>a[2]:
		if a[0]>a[1]:
			return a[0]
		if (a[0]>a[1])==None:
			return a[0]
		if a[1]>a[0]:
			return a[1]
	if a[1]>a[0]:
		if a[1]>a[2]:
			return a[1]
		if (a[2]>a[1])==None:
			return a[2]	
		if a[2]>a[1]:
			return a[2]
	if a[1]>a[2]:
		if a[1]>a[0]:
			return a[0]
		if (a[1]>a[0])==None:
			return a[1]
		if a[0]>a[1]:
			return a[0]
	if a[2]>a[0]:
		if a[2]>a[1]:
			return a[2]
		if (a[2]>a[0])==None:
			return a[2]
		if a[1]> a[2]:
			return a[1]
	if a[2]>a[1]:
		if a[2]>a[0]:
			return a[2]
		if (a[2]>a[0])==None:
			return a[2]
		if a[0]> a[2]:
			return a[0]
def cangou(jogadorA,jogadorB,i):
	if i == 0:
		if mao_da_maior(jogadorA) > mao_da_maior(jogadorB):
			jogadorA.ganha()
		if mao_da_maior(jogadorA) < mao_da_maior(jogadorB):
			jogadorB.ganha()
		else:
			jogo.acaba()
	else:
		if jogadorA.pontos> jogadorB.pontos:
			jogadorA.ganha()
		if jogadorA.pontos< jogadorB.pontos:
			jogadorB.ganha()
			

def jogo_de_truco(jogadorA,jogadorB):
	def acaba():
		return ganhador
	i = 0
	while i<= 2:
		if jogadorA.cartas[i]>jogadorB.cartas[i]:
			jogadorA.pontos += i*i -2*i + 1
		if jogador.cartasA[i]<jogadorB.cartas[i]:
			jogadorB.pontos += i*i -2*i + 1
		else:
			cangou(jogadorA,jogadorB,i)
			break
		if jogadorA.pontos == 3:
			ganhador = jogadorA			
			acaba()
		if jogadorB.pontos == 3:
			ganhador = jogadorB
			acaba
		i+=1
baralho = BaralhoDeTruco()
jogador1 = MaoDeTruco([baralho.cartas[21],baralho.cartas[7],baralho.cartas[9]])
jogador2 = MaoDeTruco([baralho.cartas[4],baralho.cartas[5],baralho.cartas[20]])
