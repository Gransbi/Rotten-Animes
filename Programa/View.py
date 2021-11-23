import telas
import controller

telas = telas.Tela
tratamento = controller.Tratamento
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
		telas.Tela.tela_inicial

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


	if (int(comando) == 3):
		telas.Tela.exposicao_anime

	if (int(comando) == 4):
		pass


	
