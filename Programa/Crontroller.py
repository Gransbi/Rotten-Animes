class Anime:


    def __init__(self, status, Qt_ep, autor, relacionados, resenha, temporadas, avaliacao, administrador = False):
        self.status = status
        self.Qt_ep = Qt_ep
        self.autor = autor
        self.relacionados = relacionados
        self.resenha = resenha
        self.temporadas = temporadas
        self.avaliacao = avaliacao

        

    def acesso(self, status_usuario):
        self.status_usuario = status_usuario
        if status_usuario == True:
            print("Adminitrador")
        else:
            print("mambro comum")
    
    def print_resenha(self, opção):
        if self.print_resenha:
            print(self.resenha)

        
            
Naruto = Anime("terminado", 500, "Masashi Kishimoto", "boruto, Naruto the Last, Naruto shippuden", "resenha grande demais para escrever",
10, "5 estrelas")

print("digite: ")
nome = input()
