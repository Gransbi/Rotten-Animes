from Programa.Model import Cadastrar
from Programa.telas import Tela
import telas
import controller
import Model

from controller import Anime

telas = telas.Tela
tratamento = controller.Tratamento
usuario = controller.Usurio
leitura = Model.Leitura

# Armazenamento de dados em csv
# 
# 


# Barra superior 
# 		1-Home
# 		2-Login
# 		3-Anime naruto
# 		4-Lista de animes 
# 		5-Pesquisa
# 	Home
# 		7-Em alta
# 		8-Ultimo adicionados
# 	Animes
# 		7-Lista de Generos
# 		8...Animes por ordem alfabetica
# 
comando = '1'
banco = {}
banco = leitura.animes_de_dados

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
					comando = 1
					break


	if (int(comando) == 3):
		telas.exposicao_anime


		if (usuario.validar("coneccao") == True):
			while True:
				avaliacao = str(input(""))
				verificação = tratamento.avaliacao(avaliacao, 0, 5)
				if (verificação == True):
					break
			

			if (usuario.validar("adiministrador") == True):
                                pass
	

	if (int(comando) == 4):
		pesquisa = str(input(""))
		if (pesquisa in banco):
			dados = tratamento.format_anime()

			anime = Anime()
			anime.nome = dados[0]
			anime.status = dados[1]
			anime.Qt_ep = dados[2]
			anime.autor = dados[3]
			anime.resenha = dados[4]
			anime.temporadas = dados[5]
			anime.avaliacao = dados[6]
			anime.avaliacao_list = dados[7]

			controller.Anime.print_anime()




	if (((usuario.validar("coneccao") and usuario.validar("adiministrador")) == True) and int(comando) == 5):
                edit = input(str("Deseja fazer alterações no nime?(S ou N):\n"))
                if edit == "N":
                        continue
                elif edit == "S":
                        anime = input(str("Nome do anime para atualização: \n"))
                        print("escreva o item que deseja editar ou SAIR para encerrar a edição\n")
                        escolha  = ""
                        while escolha != "SAIR":
                                escolha  = input(str("status, Qt_ep, autor, resenha, temporadas, avaliação"))

                                if escolha == "status":
                                        status = input(str("Novo status: "))
                                elif escolha == "Qt_ep":
                                        Qt_ep = input(str("Nova Quantidade de episodios: "))
                                elif escolha == "autor":
                                        autor = input("Editar nome do(a) Autor(a): ")
                                elif escolha == "resenha": 
                                        resenha = input("editar resenha: ")
                                elif escolha == "temporadas":
                                        temporadas = input(str("Editar temporadas: "))
                                elif escolha == "avaliação":
                                        avaliacao = input(str("nova avaliação: "))
                                elif escolha == "avaliação_lista":
                                        avaliacao_lista = input(str("nova avaliação: "))
                                elif escolha == "SAIR":
                                        continue

                        anime_csv = (f'{anime} = ({anime};; {status};; {Qt_ep};; {autor};;{resenha};;{temporadas};;{avaliacao};;{avaliacao};;{avaliacao_lista})')
                        Cadastrar.anime(anime)
                        