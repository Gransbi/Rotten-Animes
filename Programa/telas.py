espacos_100 = (" "*100)
SEARCH = ("|     SEARCH     |")
ROTTEN_A = ("ROTTEN ANIMES")
top_bar = (" |LOGIN| |   SEARCH| ")
trending = (" |TRENDING ANIMES| ")
caixas = (" |NARUTO| |ONE PIECE| |DEATH NOTE| |FULLMETAL ALCHEMIST|")
ADS = ("| BUSCO PATROCÍNIO |")

class Tela:


    def tela_inicial():
        ("\033[7;31m{}\033[m".format(ROTTEN_A.ljust(50)), "\033[7;40m{}\033[m".format(top_bar.rjust(50)),
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
        pass

    def exposicao_anime():
        pass


