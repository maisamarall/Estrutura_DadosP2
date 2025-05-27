from biblioteca import Biblioteca

biblioteca = Biblioteca()

def exibir_menu_principal():
    
    while True:
        print(f"""
📚 Sistema de Controle de Biblioteca 📚

{"-" * 42}
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
{"-" * 42}
        """)

        opcao = input("Digite o número que deseja: ")
        if opcao == '1':
            biblioteca.cadastrar_livro()
            print("\n-- Conteúdo atual de livros --")
            for isbn_livro, obj_livro in biblioteca.livros.items():
                print(f"\nISBN: {isbn_livro}\nTítulo: {obj_livro.titulo}\nCópias: {obj_livro.num_copias}\nAutor: {obj_livro.autor}")
            print("-" * 30)

        elif opcao == '2':
            biblioteca.cadastrar_usuario()
            print("\n-- Conteúdo atual de usuários --")
            for id_usuario, obj_usuario in biblioteca.usuarios.items():
                print(f"\nID: {obj_usuario.id_usuario}\nNome: {obj_usuario.nome}")
            print("-" * 30)

        elif opcao == '3':
            biblioteca.emprestar_livro()

        elif opcao == '4':
            biblioteca.devolver_emprestimo()

        elif opcao == '5':
            biblioteca.renovar_emprestimo()

        elif opcao == '6':
            biblioteca.buscar_livros()

        elif opcao == '7':
            biblioteca.listar_livros()

        elif opcao == '8':
            biblioteca.listar_usuarios()

        elif opcao == '9':
            biblioteca.listar_emprestimos()

        elif opcao == '10':
            print("Saindo do sistema.. Até mais!")
            break
        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    exibir_menu_principal()