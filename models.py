class Livro:
    def __init__(self, titulo, autor, num_copias):
        self.titulo = titulo
        self.autor = autor
        self.num_copias = num_copias
        self.fila_espera = [] 

    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Cópias Disponíveis: {self.num_copias}"

class Usuario:
    def __init__(self, nome, id_usuario): 
        self.nome = nome
        self.id_usuario = id_usuario 

    def __str__(self):
        return f"Nome: {self.nome}, ID: {self.id_usuario}" 
