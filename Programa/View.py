import telas
import controller


telas = telas.Tela
tratamento = controller.Tratamento
usuario = controller.Usurio


# Armazenamento de dados em csv
# 
# 


# Barra superior 
# 		1-Home
# 		2-Login
# 		3-Anime naruto
# 		4-Lista de animes 
# 	Home
# 		7-Em alta
# 		8-Ultimo adicionados
# 	Animes
# 		7-Lista de Generos
# 		8...Animes por ordem alfabetica
# 


comando = '1'


while True:


	if (int(comando) == 1):
		telas.tela_inicial


		while True:
			comando = str(input(""))
			verificação = tratamento.entrada(comando, 1, 6)
			if (verificação == True):
				break


	if (int(comando) == 2):
		telas.Tela.tela_login
		while True:
			login = str(input(""))
			senha = str(input(""))
			check_conctar = usuario.conectar_on(login,senha,banco)
			if (check_conctar == True):
				break
			else:
				tentar_novamente = int(input("Quer tentar novamente ? \nSim (1) \nNão (2)"))
				if (tentar_novamente == 1):
					pass
				else:
					break


	if (int(comando) == 3):
		telas.exposicao_anime

	if (int(comando) == 4):
		pass


	
