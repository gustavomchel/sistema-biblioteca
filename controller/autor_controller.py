from model.autor_model import AutorModel 

class AutorController:
    def __init__(self):
        self.autor_model = AutorModel() # Objeto da classe 'AutorModel' para enviar argumentos;

    def cadastrar_autor(self, nome, nacionalidade):
        if nome and nacionalidade:
            self.autor_model.inserir_autor(nome, nacionalidade)
            print("\nAutor cadastrado com sucesso!\n")
        else:
            print("Erro ao cadastrar.")

    def listar_autores(self):
        autores = self.autor_model.listar_autor()

        if not autores:
            print("Nenhum autor cadastrado!")
        else:
            print("\n===== Lista de Autores =====")
            for autor in autores:
                print(f"ID: {autor[0]} | Nome: {autor[1]} | Nacionalidade: {autor[2]}")

    def atualizar_autor(self, nome, nacionalidade, id_autor):
        if nome and nacionalidade and id_autor:
                self.autor_model.atualizar_autor(nome, nacionalidade, id_autor)
                print("\nAutor atualizado com sucesso!\n")

        else:
            print("Erro ao atualizar.")

    def excluir_autor(self, id_autor):
        if id_autor:
            self.autor_model.excluir_autor(id_autor)
            print("\nAutor excluído com sucesso!\n")

        else:
            print("\nErro ao excluir: ID não encontrado.")








    

