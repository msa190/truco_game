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
		if self.valor == b.valor:
			return True
		else:
			return False

	def __lt__(self,b):
		if self.valor < b.valor:
			return True
		else:
			return False
	
	def __gt__(self,b):
		if self.valor > b.valor:
			return True
		else:
			return False

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
		string = ''
		for j,i in enumerate(self.cartas):
			string += ' ' + str(j+1)
			string += ')'
			string += i.numero
			string +=' de '
			string += i.naipe
			string +='\n'
		return string
