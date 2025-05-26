# 📚 Sistema de Controle de Biblioteca - CLI Python 📚

## 💡 Sobre o Sistema: O Quê e Como Funciona
Este projeto é um sistema simples e em desenvolvimento para o **gerenciamento de bibliotecas**.. Ele visa cobrir as operações essenciais para o funcionamento de uma biblioteca, desde o **cadastro de livros e usuários**, e até o **controle de empréstimos, devoluções, renovar empréstimo, buscas e listar livros**. Nosso objetivo foi criar uma solução eficiente e fácil de usar, com foco na organização e acesso rápido aos dados.

---

## 👥 Integrantes

* Jênie Danielle - RA: 1993310
* Maisa Amaral - RA: 1997058
* Simone Siqueira - RA: 2001915

---

## 🚀 Como Executar o Sistema

Para rodar este sistema, você precisará ter o **Python 3** instalado em sua máquina.

1.  **Clone o repositório:**
    `git clone https://github.com/seu-usuario/seu-repositorio.git`
2.  **Navegue até a pasta do projeto:**
    `cd nome-da-sua-pasta-do-projeto`
3.  **Execute o script principal:**
    `python seu_arquivo_principal.py` (Ex: `python biblioteca.py`)

Não são necessárias dependências adicionais além do Python padrão.

---

## ✨ Funcionalidades Implementadas

### Por *Maisa Amaral*

* **Cadastro de Livros:** Permite adicionar livros com Título, Autor, ISBN (identificador único) e número de cópias.
* **Cadastro de Usuários:** Permite registrar usuários com Nome e ID (identificador único).
* **Empréstimo de Livros:** Gerencia o empréstimo, decrementando cópias e oferecendo **fila de espera** se o livro estiver indisponível.

### Justificativa de cada Estruturas de Dados utilizadas por *Maisa Amaral*

* **Dicionários (`{}`):**
    * **Onde:** `livros`, `usuarios` e `emprestimos`.
    * **Por quê:** Permitem **acesso rápido** através de chaves únicas.
        * Para `livros`: A chave é o **ISBN**.
        * Para `usuarios`: A chave é o **ID do usuário**.
        * Para `emprestimos`: A chave é uma **tupla `(ISBN, Id_Usuario)`**, que combina o identificador do livro com o do usuário para criar uma chave única para cada empréstimo.
* **Listas (`[]`):**
    * **Onde:** `fila_espera` (dentro de cada objeto `Livro`).
    * **Por quê:** Gerenciam a **ordem** dos usuários que aguardam por um livro específico.
---
### Por *Jênie Danielle*
---
### Por *Simone Siqueira*

* **Listagem de Livros Cadastrados:** 
    * Permite ver os livros cadastrados, com as suas respectivas informações (ISBN, autor, título e número de cópias).

* **Listagem de usuários Cadastrados:** 
    * Permite ver os usuários cadastrados, com as suas respectivas informações (ID do usuário e nome)

* **Listagem de empréstimos realizados:** 
    *Permite ver os empréstimos realizados pelos usuários, com as suas respectivas informações (ID do usuário, nome do usuário, ISBN, título do livro, autor e a data em que o empréstimo foi realizado — essa data será atualizada conforme a renovação do livro).

* **Padronização das funções de listagem** 
    *Conforme a criação das minhas funções, estabeleci um modelo padrão para as listagens, com o objetivo de economizar tempo e manter o código organizado. Todas as funções seguem a mesma estrutura lógica: verificação do dicionário, conversão em lista de tuplas e exibição das informações.

* **Verificação de dicionários vazios** 
    *Adicionei uma condição em cada função para verificar se os dicionários (`livros`, `usuarios`, `emprestimos`) estão vazios. Caso estejam, uma mensagem será exibida (`“Nenhum livro cadastrado”`, `“Nenhum usuário cadastrado”` ou `“Nenhum empréstimo registrado”`), evitando assim erros e exibindo uma resposta clara.

* **Uso de variável para guardar os elementos dos dicionários** 
    *Após a verificação, os dicionários são convertidos para listas de tuplas utilizando o método `.items()`, o que facilita a manipulação e ordenação dos dados no momento da listagem

* **Uso da estrutura de pilha nas listagens** 
    *Para exibir primeiro os elementos mais recentemente cadastrados, utilizei uma abordagem baseada na estrutura de dados tipo pilha. Ao transformar os dicionários em listas, apliquei o método `.pop()` dentro de um laço `while`, que remove e retorna sempre o último item da lista. Dessa forma, os registros mais recentes são listados no topo, o que melhora a visualização dos dados.

