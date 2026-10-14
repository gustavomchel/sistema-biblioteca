from controller.livro_controller import LivroController

class LivroView:
    def __init__(self):
        self.livro_controller = LivroController() # Objeto da classe 'LivroController' para enviar argumentos;

    def submenu_livro(self):
        while True:
            print("\n===== GERENCIAR LIVRO =====")
            print("1. Cadastrar Livro")
            print("2. Listar Livros")
            print("3. Atualizar Livro")
            print("4. Excluir Livro")
            print("5. Voltar ao menu principal\n")

            try: 
                opcao = int(input("\nEscolha uma opção:"))

                if opcao == 1:
                    titulo = input("\nDigite o título do livro: ")
                    ano_publicacao = int(input("Digite o ano de publicação: "))
                    id_autor = int(input("Digite o id do autor do livro: "))
            
                    self.livro_controller.cadastrar_livro(titulo, ano_publicacao, id_autor)

                elif opcao == 2:
                    self.livro_controller.listar_livros()

                elif opcao == 3:
                    try:
                        id_livro = int(input("\nID do livro a atualizar: "))
                        titulo = input("Novo título: ")
                        ano_publicacao = int(input("Novo ano de publicação: "))
                        id_autor = int(input("ID do autor a vincular: "))

                        self.livro_controller.atualizar_livro(id_livro, titulo, ano_publicacao, id_autor)

                    except ValueError:
                        print("\nEntrada Inválida.\n")
                        return None, None, None, None                   
                    
                elif opcao == 4:
                    try:
                        id_livro = int(input("Informe o ID do livro a excluir: "))
                        self.livro_controller.excluir_livro(id_livro)

                    except ValueError:
                        print("\nEntrada inválida!\n")
                        return None   

                elif opcao == 5:
                    print("\nVoltando ao menu principal...\n")
                    break

            except ValueError:
                print("\nOpção inválida. Digite um número.\n")
