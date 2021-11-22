class Usurio:


	def __init__(self,login,senha,apelido,adiministrador = False):
		self.login = login
		self.senha = senha
		self.apelido = apelido
		self.adiministrador = adiministrador

        
    	def conectar_on(self,login,senha,banco):
            if(login in banco.itens()):
                if (banco.get(login) == senha):
                    pass
                else:
                    print("Sua senha esta invalida.")
            else:
                print("Seu login não existe.")
                return False
