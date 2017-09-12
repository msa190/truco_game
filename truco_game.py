#encoding: utf8
_numeros = ['3','2','As','K','J','Q','4','7']
_naipes=['ouros', 'paus','copas','espadas']
class Carta:
	def __init__(self, a, b):
		if(a in _numeros and b in _naipes ):
			self.numero = a		
			self.naipe = b
		if(a in range(len(_numeros)) and b in range(len(_naipes))):
			self.numero = _numeros[a]
			self.naipe = _naipes[b]
	def __str__(self):
		return self.numero + ' de ' + self.naipe
	def __eq__(self, b):
		if self.numero == b.numero and self.naipe == b.naipe:
			return True
		else:
			return False
	valor = 0
#class jogador:
	
class Mao(list):
	cartas = []
	def __str__(self):
		for i in self.cartas:
			return i.numero + ' de ' + i.naipe
class Baralho(Mao):
	cartas = []
	#define o zap
	zap = Carta(6,1)
	cartas.append(Carta(6,1))
	Carta(6,1).valor = 9
	
	#define o sete de copas
	cartas.append(Carta(7,2))
	Carta(7,2).valor = 8

	#define o espadilha
	cartas.append(Carta(2,1))
	Carta(2,1).valor = 7

	#define o sete de ouro
	cartas.append(Carta(7,0))
	Carta(7,0).valor = 6
	
	#completar 3 e 2
	for i,j in enumerate(_numeros[0:2]):
		for k in _naipes:
			cartas.append(Carta(j,k))
			if i == 0:
				#print Carta(j,k), "tem valor 5"
				Carta(j,k).valor = 5			
			if i == 1:
				Carta(j,k).valor = 4
	#completar As
	for i,j in enumerate(_numeros[2:3]):
		for k in _naipes[0:3]:
			cartas.append(Carta(j,k))
			Carta(j,k).valor =  3
	#completar K,J,Q
	for i,j in enumerate(_numeros[3:6]):
		for k in _naipes:
			cartas.append(Carta(j,k))
			if i == 0:
				Carta(j,k).valor = 2
			if i == 1:
				Carta(j,k).valor = 1
			if i == 2:
				Carta(j,k).valor = 0
Baralho = Baralho()
for i in Baralho.cartas:
	print i, i.valor
