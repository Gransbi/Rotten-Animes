class Anime:


	def __init__(self, nome,status, Qt_ep, autor, relacionados, resenha, temporadas, avaliacao = 0, avaliacao_list = []):
		self.nome = nome
		self.status = status
		self.Qt_ep = Qt_ep
		self.autor = autor
		self.resenha = resenha
		self.temporadas = temporadas
		self.avaliacao = avaliacao
		self.avaliacao_list = avaliacao_list


	def avaliar(self, avaliacao):
		self.avaliacao_list.append(avaliacao)
		self.avaliacao = (sum(self.avaliacao_list) / len(self.avaliacao_list))
	

	def acesso(self, status_usuario):
		self.status_usuario = status_usuario
		if status_usuario == True:
		   print("Adminitrador")
		else:
			print("mambro comum")
    

	def print_resenha(self, opção):
		if self.print_resenha:
			print(self.resenha)

	def editar_anime(self):
		if (Usurio.validar("adiministrador") == True):
			pass


class Episodeo:

	def __init__(self, nome_anime, nome_ep, num_ep,cannon,resenha):
		self.nome_anime = nome_anime
		self.nome_ep = nome_ep
		self.num_ep = num_ep
		self.cannon = cannon
		self.resenha = resenha


	def editar_ep(self):
		if (Usurio.validar("adiministrador") == True):
			pass

class Usurio:


	def __init__(self,login,senha,apelido,coneccao = False,adiministrador = False):
		self.login = login
		self.senha = senha
		self.apelido = apelido
		self.adiministrador = adiministrador
		self.coneccao = coneccao


	def conectar_on(self,login,senha,banco):
		if(login in banco.itens()):
			if (banco.get(login) == senha):
				print("Você logou com sucesso.")
				self.coneccao == True
				return True

			else:
				print("A senha informada é invalida.")
		else:
			print("O login informado é invalido.")
			return False

	def validar(self, escolha):
		if (escolha == "coneccao"):
			return self.coneccao
		elif (escolha == "adiministrador"):
			return self.adiministrador


class Tratamento:
	def entrada(valor, parametro_1, parametro_2):
		if ((valor.isalnum() == True) and (valor.isalpha() == False)):
			if (int(valor) >= parametro_1 and int(valor) <= parametro_2):
				print("Você informol um valor invalido")
				return True


		else:
			return False
		
	def avaliacao_(valor, parametro_1, parametro_2):
		if ((valor.isalnum() == True) and (valor.isalpha() == False)):
			if (int(valor) >= parametro_1 and int(valor) <= parametro_2):
				print("Você informol um valor invalido")
				return True


		else:
			return False



