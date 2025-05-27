import datetime
from models import Livro, Usuario
from arvore_binaria import ArvoreBinaria

class Biblioteca:
    def __init__(self):
        self.emprestimos = {}
        self.livros = {}
        self.usuarios = {}
        self.historico_renovacoes= {}
        self.arvore_titulos = ArvoreBinaria()

    def cadastrar_livro(self):
        print("\n-- Cadastro de Livro --")
        isbn = input("Digite o ISBN do livro: ")
        if isbn in self.livros: 
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
        self.livros[isbn] = Livro(titulo, autor, num_copias)
        self.arvore_titulos.inserir(titulo, self.livros[isbn])
        print(f"Livro '{titulo}' cadastrado com sucesso!")


    def cadastrar_usuario(self):
        print("\n-- Cadastro de Usuário --")
        id_usuario = input("Digite o ID do usuário: ")
        if id_usuario in self.usuarios: 
            print("Usuário com este ID já cadastrado.") 
            return
        nome = input("Digite o nome do usuário: ")
        self.usuarios[id_usuario] = Usuario(nome, id_usuario) 
        print(f"Usuário '{nome}' cadastrado com sucesso!")


    def emprestar_livro(self):
        print("\n--Empréstimo de Livros--")
        id_usuario = input("Digite o ID do usuario: ") 
        isbn = input("Digite o ISBN do Livro a ser emprestado:")

        if id_usuario not in self.usuarios: 
            print("Cliente não encontrado em sistema.\n")
            return
        if isbn not in self.livros:
            print("Livro não encontrado no nosso sistema.\n")
            return

        livro = self.livros[isbn]

        if livro.num_copias > 0:
            chave_emprestimo = (isbn, id_usuario) 
            data_e_hora_do_momento = datetime.datetime.now()
            self.emprestimos[chave_emprestimo] = data_e_hora_do_momento
            livro.num_copias -= 1
            data_formatada_para_exibicao = data_e_hora_do_momento.strftime("%Y-%m-%d %H:%M")
            print(f"Livro '{livro.titulo}' emprestado para o cliente '{self.usuarios[id_usuario].nome}' em {data_formatada_para_exibicao}.")
        else:
            entrar_fila = input(f"Não há cópias desse livro disponíveis de '{livro.titulo}'. Deseja entrar na fila de espera? (sim | não ): ").lower()
            if entrar_fila == 'sim':
                if id_usuario in livro.fila_espera:
                    print(f"Você já está na fila de espera para '{livro.titulo}'.")
                else:
                    livro.fila_espera.append(id_usuario) 
                    print(f"Você entrou na fila de espera para o livro: '{livro.titulo}'.")
            else:
                print(f"Empréstimo não foi realizado, pois não há cópias disponíveis de '{livro.titulo}' em nosso sistema.'\n")

    #função para obter os dados de id e isbn e garantir que eles já existam
    def obter_validar_dados(self):
        while True:
            id_usuario = input("Digite o ID do usuário (ou 'sair' para sair): ") 
            if id_usuario.lower() == "sair":
                return None, None
            if id_usuario not in self.usuarios:
                continuar = input("ID de usuário não encontrado.\nDeseja tentar novamente? (s | n): ").lower()
                if continuar != "s":
                    return None, None
                continue
            
            isbn = input("Digite o ISBN do Livro:")
            if isbn.lower() == "sair":
                return None, None
            if isbn not in self.livros:
                continuar = input("ID de usuário não encontrado.\nDeseja tentar novamente? (s | n): ").lower()
                if continuar != "s":
                    return None, None
                continue

            return id_usuario, isbn

    #função para devolver o empréstimo, também atualiza a qtd de cópias disponiveis e atualiza a fila de espera
    def devolver_emprestimo(self):
        print("\n-- Devolução de Empréstimo --\n")

        id_usuario, isbn = self.obter_validar_dados()
        chave = (isbn, id_usuario)

        if not id_usuario or not isbn:
            print("Operação cancelada. Voltando ao menu.")
            return

        if chave not in self.emprestimos:
            print("Nenhum empréstimo encontrado para esse usuário e livro.")
            return
        
        livro = self.livros[isbn]
        livro.num_copias += 1
        del self.emprestimos[chave]

        print(f"Livro '{livro.titulo}' devolvido com sucesso.")

        if livro.fila_espera:
            proximo_id = livro.fila_espera.pop(0)
            nova_chave = (isbn, proximo_id)
            self.emprestimos[nova_chave] = datetime.datetime.now()
            livro.num_copias -= 1
            print(f"O próximo da fila é '{self.usuarios[proximo_id].nome}' (ID: {proximo_id}).")

    #função de renovar os emprestimos e garantir que não sejam feitas 2 renovações no mesmo dia pelo mesmo usuário
    def renovar_emprestimo(self):
        print("\n-- Renovação de Empréstimo --")

        id_usuario, isbn = self.obter_validar_dados()
        chave = (isbn, id_usuario)

        if not id_usuario or not isbn:
            print("Operação cancelada. Voltando ao menu.")
            return

        if chave not in self.emprestimos:
            print("Empréstimo não encontrado...")
            return
        
        hoje = datetime.date.today()

        if chave not in self.historico_renovacoes:
            self.historico_renovacoes[chave] = set()

        if hoje in self.historico_renovacoes[chave]:
            print("Esse empréstimo já foi renovado hoje...")
            return
        
        nova_data = datetime.datetime.now()
        self.emprestimos[chave] = nova_data
        self.historico_renovacoes[chave].add(hoje)

        print(f"Empréstimo do livro '{self.livros[isbn].titulo}' foi renovado em {nova_data.date()}.")
        print(f"Total de renovações: {len(self.historico_renovacoes[chave])}")

    #função para listar os livros usando a árvore binária para uma pesquisa mais eficiente
    def buscar_livros(self):
        print("\n-- Buscar Livros --")
        pesquisa = input("Digite o título do livro: ").lower()

        resultado = self.arvore_titulos.buscar(pesquisa)

        if resultado:
            print(f"Título: {resultado.titulo} \nAutor: {resultado.autor} \nCópias disponíveis: {resultado.num_copias}")
        else:
            print("Nenhum livro ou autor encontrado com esse título...")

        # encontrados = False
        # for isbn, livro in self.livros.items():
        #     if pesquisa in livro.titulo.lower() or pesquisa in livro.autor.lower():
        #         print(f"Título: {livro.titulo} \nAutor: {livro.autor} \nCópias disponíveis: {livro.num_copias}")
        #         encontrados = True
        # if not encontrados:
        #     print("Nenhum livro ou autor encontrado com essa pesquisa...")

    def listar_livros(self):
        if not self.livros:
            print("\nNenhum livro cadastrado.")
            return

        ordem_livros = list(self.livros.items())

        print("\n-----------Listar Livros-----------")
        while ordem_livros:
            isbn, livro = ordem_livros.pop()
            print(f"\nISBN: {isbn}\nTítulo: {livro.titulo}\nAutor: {livro.autor}\nCópias Disponíveis: {livro.num_copias}")
        print("-"*35)

    #def para listar usuários
    def listar_usuarios(self):
        if not self.usuarios:
            print("\nNenhum usuário cadastrado.")
            return

        ordem_usuarios = list(self.usuarios.items())

        print("\n-----------Listar Usuários-----------")
        while ordem_usuarios:
            id_usuario, usuario = ordem_usuarios.pop()
            print(f"\nID: {id_usuario}\nNome: {usuario.nome}")
        print("-"*37)

    def listar_emprestimos(self):
        if not self.emprestimos:
            print("\nNenhum empréstimo registrado.")
            return

        ordem_emprestimos = list(self.emprestimos.items())

        print("\n-----------Listar Empréstimos-----------")
        while ordem_emprestimos:
            (isbn, id_usuario), data = ordem_emprestimos.pop()
            livro = self.livros.get(isbn)
            usuario = self.usuarios.get(id_usuario)
            data_formatada = data.strftime("%Y-%m-%d %H:%M")

            print(f"\nID: {id_usuario}\nNome: {usuario.nome}\nISBM do livro: {isbn}\nTítulo: {livro.titulo}\nAutor: {livro.autor}\nData do empréstimo: {data_formatada}")
        print("-"*40)