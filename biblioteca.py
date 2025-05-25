import datetime

emprestimos = {}
livros = {}
usuarios = {}

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


def cadastrar_livro():
    print("\n-- Cadastro de Livro --")
    isbn = input("Digite o ISBN do livro: ")
    if isbn in livros: 
        print("Livro com este ISBN já cadastrado em nosso sistema.")
        return
    titulo = input("Digite o título do livro: ")
    autor = input("Digite o autor/a do livro: ")
    try:
        num_copias = int(input("Digite o número de cópias: "))
        if num_copias < 0:
            print("O número de cópias não pode ser negativo.")
            return
    except ValueError:
        print("Número de cópias inválido. Digite um número inteiro.")
        return
    livros[isbn] = Livro(titulo, autor, num_copias)
    print(f"Livro '{titulo}' cadastrado com sucesso!")


def cadastrar_usuario():
    print("\n-- Cadastro de Usuário --")
    id_usuario = input("Digite o ID do usuário: ")
    if id_usuario in usuarios: 
        print("Usuário com este ID já cadastrado.") 
        return
    nome = input("Digite o nome do usuário: ")
    usuarios[id_usuario] = Usuario(nome, id_usuario) 
    print(f"Usuário '{nome}' cadastrado com sucesso!")


def emprestar_livro():
    print("\n--Empréstimo de Livros--")
    id_cliente = input("Digite o ID do usuario: ") 
    isbn = input("Digite o ISBN do Livro a ser emprestado:")

    if id_cliente not in usuarios: 
        print("Cliente não encontrado em sistema.")
        print()
        return
    if isbn not in livros:
        print("Livro não encontrado no nosso sistema.")
        print()
        return

    livro = livros[isbn]
    if livro.num_copias > 0:
        chave_emprestimo = (isbn, id_cliente) 
        data_e_hora_do_momento = datetime.datetime.now()
        emprestimos[chave_emprestimo] = data_e_hora_do_momento
        livro.num_copias -= 1
        data_formatada_para_exibicao = data_e_hora_do_momento.strftime("%Y-%m-%d %H:%M")
        print(f"Livro '{livro.titulo}' emprestado para o cliente '{usuarios[id_cliente].nome}' em {data_formatada_para_exibicao}.")
    else:
        entrar_fila = input(f"Não há cópias desse livro disponíveis de '{livro.titulo}'. Deseja entrar na fila de espera? (sim | não ): ").lower()
        if entrar_fila == 'sim':
            if id_cliente in livro.fila_espera:
                print(f"Você já está na fila de espera para '{livro.titulo}'.")
            else:
                livro.fila_espera.append(id_cliente) 
                print(f"Você entrou na fila de espera para o livro: '{livro.titulo}'.")
        else:
            print(f"Empréstimo não foi realizado, pois não há cópias disponíveis de '{livro.titulo}' em nosso sistema.'")
            print()

#def para listar livros
def listar_livros():
  if not livros:
    print("\nNenhum livro cadastrado.")
    return

  ordem_livros = list(livros.items())

  print("\n-----------Listar Livros-----------")
  while ordem_livros:
    isbn, livro = ordem_livros.pop()
    print(f"\nISBN: {isbn}\nTítulo: {livro.titulo}\nAutor: {livro.autor}\nCópias Disponíveis: {livro.num_copias}")
  print("-"*35)

#def para listar usuários
def listar_usuarios():
  if not usuarios:
    print("\nNenhum usuário cadastrado.")
    return

  ordem_usuarios = list(usuarios.items())

  print("\n-----------Listar Usuários-----------")
  while ordem_usuarios:
    id_usuario, usuario = ordem_usuarios.pop()
    print(f"\nID: {id_usuario}\nNome: {usuario.nome}")
  print("-"*37)


#def para listar os empréstimos
def listar_emprestimos():
    if not emprestimos:
        print("\nNenhum empréstimo registrado.")
        return

    ordem_emprestimos = list(emprestimos.items())

    print("\n-----------Listar Empréstimos-----------")
    while ordem_emprestimos:
        (isbn, id_usuario), data = ordem_emprestimos.pop()
        livro = livros.get(isbn)
        usuario = usuarios.get(id_usuario)
        data_formatada = data.strftime("%Y-%m-%d %H:%M")

        print(f"\nRA: {id_usuario}\nNome: {usuario.nome}\nISBM do livro: {isbn}\nTítulo: {livro.titulo}\nAutor: {livro.autor}\nData do empréstimo: {data_formatada}")
    print("-"*40)


def exibir_menu_principal():
    print(f"""
📚 Sistema de Controle de Biblioteca 📚

{"-" * 30}
Selecione uma opção:
- 1. Cadastrar Livro
- 2. Cadastrar Usuário
- 3. Emprestar Livro
- 4. Devolver Empréstimo
- 5. Renovar Empréstimo
- 6. Buscar Livros
- 7. Listar Livros
- 8. Listar Usuários
- 9. Listar Empréstimos
- 10. Sair
{"-" * 30}
        """)

if __name__ == "__main__":
    while True:
        exibir_menu_principal()
        opcao = input("Digite o número que deseja: ")
        if opcao == '1':
            cadastrar_livro()
            print("\n-- Conteúdo atual de livros--")
            for isbn_livro, obj_livro in livros.items():
                print(f"ISBN: {isbn_livro}, Título: {obj_livro.titulo}, Cópias {obj_livro.num_copias}")
            print("-" * 30)

        elif opcao == '2':
            cadastrar_usuario()
            print("\n-- Conteúdo atual de usuarios ")
            for id_usuario, obj_usuario in usuarios.items():
                print(f"ID: {obj_usuario.id_usuario}, Nome: {obj_usuario.nome}")
            print("-" * 30)

        elif opcao == '3':
            emprestar_livro()

        elif opcao == '7':
            listar_livros()

        elif opcao == '8':
            listar_usuarios()

        elif opcao == '9':
            listar_emprestimos()

        elif opcao == '10':
            print("Saindo do sistema.. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")