class Usurio_comun:
	def __init__(self,login,senha,apelido,adiministrador = False):
		self.login = login
		self.senha = senha
		self.apelido = apelido
		self.adiministrador = adiministrador