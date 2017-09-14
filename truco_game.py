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
	def permutacao(self, v = []):
		u = self.cartas
		if len(u) != len(v):
			raise
		w = []
		for i in v:
			w.append(u[i-1])
		return w

	def __mul__(self,v=[]):
		u = self.cartas
		return self.permutacao(v)
	def __len__(self):
		return len(self.cartas)
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
		return a[0]
	#	if a[0]>a[2]:
	#		return a[0]
	#	if (a[0]>a[2])==None:
	#		return a[0]
	#	if a[2]>a[0]:
	#		return a[2]
	#if a[0]>a[2]:
	#	if a[0]>a[1]:
	#		return a[0]
	#	if (a[0]>a[1])==None:
	#		return a[0]
	#	if a[1]>a[0]:
	#		return a[1]
	if a[1]>a[0]:
		return a[1]
	#	if a[1]>a[2]:
	#		return a[1]
	#	if (a[2]>a[1])==None:
	#		return a[2]	
	#	if a[2]>a[1]:
	#		return a[2]
	#if a[1]>a[2]:
	#	if a[1]>a[0]:
	#		return a[0]
	#	if (a[1]>a[0])==None:
	#		return a[1]
	#	if a[0]>a[1]:
	#		return a[0]
	#if a[2]>a[0]:
	#	if a[2]>a[1]:
	#		return a[2]
	#	if (a[2]>a[0])==None:
	#		return a[2]
	#	if a[1]> a[2]:
	#		return a[1]
	#if a[2]>a[1]:
	#	if a[2]>a[0]:
	#		return a[2]
	#	if (a[2]>a[0])==None:
	#		return a[2]
	#	if a[0]> a[2]:
	#		return a[0]
def cangou(jogadorA,jogadorB):
	if mao_da_maior(jogadorA.cartas) > mao_da_maior(jogadorB.cartas):
		return 'jogadorA'
	if mao_da_maior(jogadorA.cartas) < mao_da_maior(jogadorB.cartas):
		return 'jogadorB'
	
def jogo_de_truco(jogadorA,jogadorB):
	def acaba():
		return ganhador
	i = 0
	while i<= 2:
		if jogadorA.cartas[i]>jogadorB.cartas[i]:
			jogadorA.pontos += i*i -2*i + 2
		if jogador.cartasA[i]<jogadorB.cartas[i]:
			jogadorB.pontos += i*i -2*i + 2
		else:
			cangou(jogadorA,jogadorB,i)
			break
		if jogadorA.pontos == 3:
			ganhador = jogadorA			
			acaba()
		if jogadorB.pontos == 3:
			ganhador = jogadorB
			
		i+=1
baralho = BaralhoDeTruco()
jogador1 = MaoDeTruco([baralho.cartas[4],baralho.cartas[10],baralho.cartas[3]])
jogador2 = MaoDeTruco([baralho.cartas[2],baralho.cartas[5],baralho.cartas[20]])
permutacao1 = [0,2,1]
permutacao2 = [0,2,1]
pontos_jogador1 = 0
pontos_jogador2 = 0
i =0
#uma função organizadora
#dada uma lista com n elementos, "multiplicamos" uma lista por uma permutação e lista*permutação e obtemos uma lista permutada
while i<=2:
	print 'Rodada',i+1
	print '\n'
	print 'Jogador A\n',jogador1
	print '\n'
	print 'Jogador B\n',jogador2
	print jogador1.cartas[permutacao1[i]],"       ",jogador2.cartas[permutacao2[i]]
	if i==0 and jogador1.cartas[permutacao1[i]].valor == jogador2.cartas[permutacao2[i]].valor:
		print 'cangou!'
		print mao_da_maior(jogador1.cartas),'       ',mao_da_maior(jogador2.cartas)
		print cangou(jogador1,jogador2), 'ganhou'
		break
	if jogador1.cartas[permutacao1[i]] > jogador2.cartas[permutacao2[i]]:
		pontos_jogador1 +=i*i -2*i + 2
		print "rodada do jogador 1"
	if jogador1.cartas[permutacao1[i]] < jogador2.cartas[permutacao2[i]]:
		pontos_jogador2 +=i*i -2*i+2
		print "rodada do jogador 2"
	print '\n'
	i+=1
if pontos_jogador1 > pontos_jogador2:
	print 'Jogador 1 ganhou'
if pontos_jogador1 < pontos_jogador2:
	print 'Jogador 2 ganhou'

lista1=MaoDeTruco([5,6,7,8])
lista2=[1,2,4,3]
print lista1*lista2	
