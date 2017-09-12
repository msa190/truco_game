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
#class jogador:
	
class Mao(list):
	cartas = []
	def __str__(self):
		for i in self.cartas:
			return i.numero + ' de ' + i.naipe
class Baralho():
	cartas = []
	
	#define o zap
	cartas.append(Carta(3,1))
	cartas[-1].valor = 9
	
	#define o sete de copas
	cartas.append(Carta(6,2))
	cartas[-1].valor = 8

	#define o espadilha
	cartas.append(Carta(0,1))
	cartas[-1].valor = 7

	#define o sete de ouro
	cartas.append(Carta(6,0))
	cartas[-1].valor = 6
	
	for i in range(13):
		for j in range(4):
			if i == 0:
				if j!= 3:
					cartas.append(Carta(i,j))
					cartas[-1].valor = 3
			if i == 1:
				cartas.append(Carta(i,j))
				cartas[-1].valor = 4
			if i == 2:
				cartas.append(Carta(i,j))
				cartas[-1].valor = 5	
			if i == 10:
				cartas.append(Carta(i,j))
				cartas[-1].valor = 1
			if i == 11:
				cartas.append(Carta(i,j))
				cartas[-1].valor = 0
			if i == 12:
				cartas.append(Carta(i,j))
				cartas[-1].valor = 2
def combate(a,b):
	if a>b:
		print a,"mata",b
	if a<b:
		print b,"mata",a
	else:
		print "Empate"
for i in baralho.cartas:
	print i, i.valor

baralho = Baralho()
