import datetime

emprestimos = {}
livros = {}
usuarios = {}
historico_renovacoes= {}


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
    print("\n---Cadastro de Livro----")
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
    print("\n---Empréstimo de Livros---")
    id_usuario = input("Digite o ID do usuario: ") 
    isbn = input("Digite o ISBN do Livro a ser emprestado:")

    if id_usuario not in usuarios: 
        print("Cliente não encontrado em sistema.")
        print()
        return
    if isbn not in livros:
        print("Livro não encontrado no nosso sistema.")
        print()
        return

    livro = livros[isbn]
    if livro.num_copias > 0:
        chave_emprestimo = (isbn, id_usuario) 
        data_e_hora_do_momento = datetime.datetime.now()
        emprestimos[chave_emprestimo] = data_e_hora_do_momento
        livro.num_copias -= 1
        data_formatada_para_exibicao = data_e_hora_do_momento.strftime("%Y-%m-%d %H:%M")
        print(f"Livro '{livro.titulo}' emprestado para o cliente '{usuarios[id_usuario].nome}' em {data_formatada_para_exibicao}.")
    else:
        entrar_fila = input(f"Não há cópias desse livro disponíveis de '{livro.titulo}'. Deseja entrar na fila de espera? (sim | não ): ").lower()
        if entrar_fila == 'sim':
            if id_usuario in livro.fila_espera:
                print(f"Você já está na fila de espera para '{livro.titulo}'.")
            else:
                livro.fila_espera.append(id_usuario) 
                print(f"Você entrou na fila de espera para o livro: '{livro.titulo}'.")
        else:
            print(f"Empréstimo não foi realizado, pois não há cópias disponíveis de '{livro.titulo}' em nosso sistema.'")
            print()

def obter_validar_dados():
    while True:
        id_usuario = input("Digite o ID do usuario (ou 'sair' para sair): ") 
        if id_usuario.lower() == "sair":
            return None, None
        if id_usuario not in usuarios:
            continuar = input("ID de usuário não encontrado.\nDeseja tentar novamente? (s | n): ").lower()
            if continuar != "s":
                return None, None
            continue
        
        isbn = input("Digite o ISBN do Livro a ser devolvido:")
        if isbn.lower() == "sair":
            return None, None
        if isbn not in livros:
            continuar = input("ID de usuário não encontrado.\nDeseja tentar novamente? (s | n): ").lower()
            if continuar != "s":
                return None, None
            continue

        return id_usuario, isbn

def devolver_emprestimo():
    print("\n-- Devolução de Empréstimo --\n")
    id_usuario, isbn = obter_validar_dados()
    chave = (isbn, id_usuario)
    if not id_usuario or not isbn:
        print("Operação cancelada. Voltando ao menu.")
        return

    if chave not in emprestimos:
        print("Nenhum empréstimo encontrado para esse usuário e livro.")
        return
    
    livro = livros[isbn]
    livro.num_copias += 1
    del emprestimos[chave]

    print(f"Livro '{livro.titulo}' devolvido com sucesso.")

    if livro.fila_espera:
        proximo_id = livro.fila_espera.pop(0)
        nova_chave = (isbn, proximo_id)
        emprestimos[nova_chave] = datetime.datetime.now()
        livro.num_copias -= 1
        print(f"O próximo da fila é '{usuarios[proximo_id].nome}' (RA: {proximo_id}).")


def renovar_emprestimo():
    print("\n-- Renovação de Empréstimo --")

    id_usuario, isbn = obter_validar_dados()
    chave = (isbn, id_usuario)
    if not id_usuario or not isbn:
        print("Operação cancelada. Voltando ao menu.")
        return

    if chave not in emprestimos:
       print("Empréstimo não encontrado...")
       return
    
    nova_data = datetime.datetime.now()
    emprestimos[chave] = nova_data

    if chave not in historico_renovacoes:
       historico_renovacoes[chave] = []

    historico_renovacoes[chave].append(nova_data)

    print(f"Empréstimo do livro '{livros[isbn].titulo}' foi renovado em {nova_data.date()}.")
    print(f"Total de renovações: {len(historico_renovacoes[chave])}")

def buscar_livros():
    print("\n-- Buscar Livros --")

    pesquisa = input("Digite o nome do título ou do autor: ").lower()

    encontrados = False

    for isbn, livro in livros.items():
        if pesquisa in livro.titulo.lower() or pesquisa in livro.autor.lower():
            print(f"Título: {livro.titulo} \nAutor: {livro.autor} \nCópias disponíveis: {livro.num_copias}")
            encontrados = True

    if not encontrados:
       print("Nenhum livro ou autor encontrado com essa pesquisa...")



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
                print(f"\nISBN: {isbn_livro}\nTítulo: {obj_livro.titulo}\nCópias {obj_livro.num_copias}")
            print("-" * 30)

        elif opcao == '2':
            cadastrar_usuario()
            print("\n-- Conteúdo atual de usuarios ")
            for id_usuario, obj_usuario in usuarios.items():
                print(f"\nID: {obj_usuario.id_usuario}\nNome: {obj_usuario.nome}")
            print("-" * 30)

        elif opcao == '3':
            emprestar_livro()

        elif opcao == '4':
            devolver_emprestimo()

        elif opcao == '5':
            renovar_emprestimo()

        elif opcao == '6':
            buscar_livros()

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