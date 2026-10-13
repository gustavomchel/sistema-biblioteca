from view.autor_view import AutorView
from view.livro_view import LivroView

class MenuView:
    def __init__(self):
        # Instancia da classe do submenu para poder usá-la aqui dentro
        self.autor_view = AutorView()
        self.livro_view = LivroView()

    def iniciar_menu(self):
        while True:
            print("\n===== MENU =====")
            print("1. Gerenciar Autor")
            print("2. Gerenciar Livro")
            print("3. Sair\n")

            try:
                opcao = int(input("Digite uma opção(1-3): "))

                if opcao == 1:
                    self.autor_view.submenu_autor()

                elif opcao == 2:
                    self.livro_view.submenu_livro()
                    
                elif opcao == 3:
                    print("Saindo do sistema...")
                    break

            except ValueError:
                print("Opção inválida. Digite um número.")
        