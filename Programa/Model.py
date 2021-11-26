class Cadastrar:


	def anime(escrever):
		arquivo = open("animes.csv", "a")
		arquivo.write(escrever)
		arquivo.close()

class Leitura:


	def animes_de_dados():
		arquivo = open("animes.csv", "r")
		for line in arquivo:
			line_banco = line.split(";;")
			
			anime = {line_banco[0]:{"Status":line_banco[1],"Qt_ep":line_banco[2],"Autor": line_banco[3], 
			"Resenha":line_banco[4], "Temporadas":line_banco[5],"Avaliação":line_banco[6],"Avaliação lista": line_banco[7]}}

		arquivo.close()

		return anime