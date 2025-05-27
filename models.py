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

class RegistroEmprestimo:
    def __init__(self, isbn, id_usuario, data, status):
        self.isbn = isbn
        self.id_usuario = id_usuario
        self.data = data
        self.status = status 

    def __str__(self):
        data_formatada = self.data.strftime("%Y-%m-%d %H:%M")
        return f"ID: {self.id_usuario}, ISBN: {self.isbn}, Data: {data_formatada}, Status: {self.status.captalize()}"