import random 

class Carta():
	_numeros = ['As','2','3','4','5','6','7','8','9','10','J','Q','K']
	_naipes=['ouros', 'paus','copas','espadas']
	valor = 0	
	numero = None
	naipe = None
	
	def __init__(self, a, b, valor=0):
		if(a in self._numeros and b in self._naipes ):
			self.numero = a		
			self.naipe = b
		if(a in range(len(self._numeros)) and b in range(len(self._naipes))):
			self.numero = self._numeros[a]
			self.naipe = self._naipes[b]
		
		self.valor = valor

	def __str__(self):
		return self.numero + ' de ' + self.naipe
	
	def __eq__(self, b):
		# if self.valor == b.valor:
		# 	return True
		# else:
		# 	return False
		True if self.valor == b.valor: else False

	def __lt__(self,b):
		# if self.valor < b.valor:
		# 	return True
		# else:
		# 	return False
		True if self.valor < b.valor: else False
	
	def __gt__(self,b):
		# if self.valor > b.valor:
		# 	return True
		# else:
		# 	return False
		True if self.valor > b.valor: else False
	
	def __le__(self, b):
		# if self.valor <= b.valor:
		# 	return True
		# else:
		# 	return False
		True if self.valor <= b.valor: else False

	def __ge__(self,b):
		# if self.valor >= b.valor:
		# 	return True
		# else:
		# 	return False
		True if self.valor >= b.valor: else False

	def __ne__(self, b):
		# if self.valor != b.valor:
		# 	return True
		# else:
		# 	return False
		True if self.valor != b.valor else False

class Mao():
	cartas = []

	def __init__(self):
		self.cartas = []

	def __mul__(self,v=[]):
		u = self.cartas
		return self.permutacao(v)

	def __len__(self):
		return len(self.cartas)

	def __str__(self):
		string = ''
		for j, i in enumerate(self.cartas):
			string += ' ' + str(j+1)
			string += ')'
			string += i.numero
			string +=' de '
			string += i.naipe
			string +='\n'
		return string
	
	def shuffle(self):
		random.shuffle(self.cartas)

	def pop(self):
		return self.cartas.pop()

	def add_carta(self, carta):
		self.cartas.append(carta)

	def get_maior(self):
		c = Carta(0, 0, 0)

		for i in self.cartas:
			if i.valor > c.valor:
				c = i

		return c

	def get_menor(self):
		c = Carta(0, 0, 0)

		for i in self.cartas:
			if i.valor < c.valor:
				c = i

		return c


class BaralhoDeTruco(Mao):
	def __init__(self):
		#define o zap
		self.cartas.append(Carta(3,1,9))
	
		#define o sete de copas
		self.cartas.append(Carta(6,2,8))

		#define o espadilha
		self.cartas.append(Carta(0,3,7))


		#define o sete de ouro
		self.cartas.append(Carta(6,0,6))
	
		for i in range(13):
			for j in range(4):
				if i == 0:
					if j!= 3:
						self.cartas.append(Carta(i,j,3))
				if i == 1:
					self.cartas.append(Carta(i,j,4))
				if i == 2:
					self.cartas.append(Carta(i,j,5))
				if i == 10:
					self.cartas.append(Carta(i,j,1))
				if i == 11:
					self.cartas.append(Carta(i,j,0))
				if i == 12:
					self.cartas.append(Carta(i,j,2))