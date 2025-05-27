class NoArvore:
    def __init__(self, titulo, livro):
        self.titulo = titulo.lower()
        self.livro = livro
        self.esquerda = None
        self.direita = None

class ArvoreBinaria:
    def __init__(self):
        self.raiz = None

    def inserir(self, titulo, livro):
        novo_no = NoArvore(titulo, livro)
        if self.raiz is None:
            self.raiz = novo_no
        else:
            self.inserirRecursivo(self.raiz, novo_no)

    def inserirRecursivo(self, atual, novo_no):
        if novo_no.titulo < atual.titulo:
            if atual.esquerda is None:
                atual.esquerda = novo_no
            else:
                self.inserirRecursivo(atual.esquerda, novo_no)

        else:
            if atual.direita is None:
                atual.direita = novo_no
            else:
                self.inserirRecursivo(atual.direita, novo_no)
    
    def buscar(self, pesquisa):
        return self.buscarResultado(self.raiz, pesquisa.lower())
    
    def buscarResultado(self, atual, pesquisa):
        if atual is None:
            return None
        
        if pesquisa == atual.titulo:
            return atual.livro
        elif pesquisa < atual.titulo:
            return self.buscarResultado(atual.esquerda, pesquisa)
        else:
            return self.buscarResultado(atual.direita, pesquisa)
