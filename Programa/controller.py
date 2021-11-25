class Anime:


    def __init__(self, status, Qt_ep, autor, relacionados, resenha, temporadas, avaliacao = 0, avaliacao_list = []):
        self.status = status
        self.Qt_ep = Qt_ep
        self.autor = autor
        self.relacionados = relacionados
        self.resenha = resenha
        self.temporadas = temporadas
        self.avaliacao = avaliacao
        self.avaliacao_list = avaliacao_list


        def avaliar(self, avaliacao):
                self.avaliacao_list.append(avaliacao)
                self.avaliacao = (sum(avaliacao_list) / len(avaliacao_list))
        

        def acesso(self, status_usuario):
                self.status_usuario = status_usuario
                if status_usuario == True:
                   print("Adminitrador")
                else:
                        print("mambro comum")
    

        def print_resenha(self, opção):
                if self.print_resenha:
                        print(self.resenha)

        def mudar(self):
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
                                print("Sua senha esta invalida.")
                else:
                        print("Seu login não existe.")
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



