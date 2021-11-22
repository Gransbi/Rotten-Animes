
import telas 
import tratamento

# Barra superior 
# 		1-Home
# 		2-Animes
# 		3-Filmes 
# 		4-Fila
# 		5-Pesquisa
# 		6-login
# 
# 	Home
# 		7-Em alta
# 		8-Ultimo adicionados
# 	Animes
# 		7-Lista de Generos
# 		8...Animes por ordem alfabetica
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
# 
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
		pass

	if (int(comando) == 3):
		pass

	if (int(comando) == 4):
		pass

	if (int(comando) == 5):
		pass

	if (int(comando) == 6):
		pass


	
