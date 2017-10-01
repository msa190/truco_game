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
