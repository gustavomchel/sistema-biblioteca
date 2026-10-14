from controller.autor_controller import AutorController

class AutorView:
    def __init__(self):
        self.autor_controller = AutorController() # Objeto da classe 'AutorController' para enviar argumentos; 

    def submenu_autor(self):
        while True:
            print("\n===== GERENCIAR AUTOR =====")
            print("1. Cadastrar Autor")
            print("2. Listar Autores")
            print("3. Atualizar Autor")
            print("4. Excluir Autor")
            print("5. Voltar ao menu principal\n")

            try: 
                opcao = int(input("\nEscolha uma opção:"))

                if opcao == 1:
                    try:
                        nome = input("\nDigite o nome do autor(a): ")
                        nacionalidade = input("Digite a nacionalidade do autor(a): ")
                
                        self.autor_controller.cadastrar_autor(nome, nacionalidade)

                    except ValueError:
                        print("\nEntrada Inválida.\n")
                        return None, None 


                elif opcao == 2:
                    self.autor_controller.listar_autores()

                elif opcao == 3:
                    try:
                        id_autor = int(input("\nID do autor a atualizar: "))
                        nome = input("Novo nome: ")
                        nacionalidade = input("Nova nacionalidade: ")

                        self.autor_controller.atualizar_autor(nome, nacionalidade, id_autor)

                    except ValueError:
                        print("\nEntrada Inválida.\n")
                        return None, None, None                    
                    
                elif opcao == 4:
                    try:
                        id_autor = int(input("\nInforme o ID do autor a excluir: "))
                        self.autor_controller.excluir_autor(id_autor)

                    except ValueError:
                        print("\nEntrada inválida!\n")
                        return None   

                elif opcao == 5:
                    print("\nVoltando ao menu principal...\n")
                    break

            except ValueError:
                print("\nOpção inválida. Digite um número.\n")
    


    