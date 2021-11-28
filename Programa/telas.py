



espacos_100 = (" "*100)
SEARCH = ("|     SEARCH     |")
ROTTEN_A = ("ROTTEN ANIMES")
top_bar = (" |LOGIN| |   SEARCH| ")
trending = (" |TRENDING ANIMES| ")
caixas = (" |NARUTO| |ONE PIECE| |DEATH NOTE| |FULLMETAL ALCHEMIST|")
ADS = ("| BUSCO PATROCÍNIO |")
#para a tela do login
espaco_input = ("|          |")
login = ("| LOGIN |")
email = ("|EMAIL:    |")
password = ("|PASSWORD: |")
cadastro = ("|cadastre-se|")
#para a tela do anime
nome_str = ("NOME:")
status_str = ("status: ")
episodios_str = ("episodios: ")
autor_str  = ("autor: ")
temporadas_str = ("quantidade de temporadas: ")
avaliacao_str = ("avaliação: ")

resenha_str = ("resenha: ")

class Tela:


    def tela_inicial():
        print("\033[7;31m{}\033[m".format(ROTTEN_A.ljust(50)), "\033[7;40m{}\033[m".format(top_bar.rjust(50)),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(ADS.center(100)),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(SEARCH.center(100)),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(trending.ljust(100)),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(caixas.center(100)),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(101 * " "),
        )

    def tela_login():
        print("\033[7;31m{}\033[m".format(ROTTEN_A.ljust(50)), "\033[7;40m{}\033[m".format(top_bar.rjust(50)),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(login.center(100)),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(email.center(100)),
        "\033[7;40m\n{}".format(espaco_input.center(100)),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(password.center(100)),
        "\033[7;40m\n{}".format(espaco_input.center(100)),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(cadastro.center(100)),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(trending.ljust(100)),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(caixas.center(100)),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(101 * " "),
        )

    def exposicao_anime(nome, status, Qt_ep, autor, resenha, temporadas, avaliacao):
        print("\033[7;31m{}\033[m".format(ROTTEN_A.ljust(50)), "\033[7;40m{}\033[m".format(top_bar.rjust(50)),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{} {}".format(nome_str, nome).center(100),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{} {}".format(status_str, status).ljust(100),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(temporadas_str, temporadas).ljust(100),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{} {}".format(autor_str, autor).ljust(100),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(episodios_str, Qt_ep).ljust(100),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{} {}".format(avaliacao_str, avaliacao).ljust(100),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(resenha_str).ljust(100),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(resenha).center(100)),
        "\033[7;40m\n{}".format(espacos_100),
        "\033[7;40m\n{}".format(101 * " ")
