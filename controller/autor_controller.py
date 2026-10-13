from model.autor_model import AutorModel 

class AutorController:
    def __init__(self):
        # Instancia da classe de 'autor_model' e 'autor_view' para poder usá-la aqui dentro
        self.autor_model = AutorModel()

    def cadastrar_autor(self, nome, nacionalidade):
        if nome and nacionalidade:
            self.autor_model.inserir_autor(nome, nacionalidade)
            print("\nAutor cadastrado com sucesso!\n")

    def listar_autores(self):
        autores = self.autor_model.listar_autor()

        if not autores:
            print("Nenhum autor cadastrado!")
        else:
            print("\n===== Lista de Autores =====")
            for autor in autores:
                print(f"ID: {autor[0]} | Nome: {autor[1]} | Nacionalidade: {autor[2]}")

    def atualizar_autor(self, nome, nacionalidade, id_autor):
        try:
            if nome and nacionalidade and id_autor:
                self.autor_model.atualizar_autor(nome, nacionalidade, id_autor)
                print("\nAutor atualizado com sucesso!\n")

        except Exception as e:
            print("Erro ao atualizar.", e)

    def excluir_autor(self, id_autor):
        if id_autor:
            self.autor_model.excluir_autor(id_autor)
            print("\nAutor excluído com sucesso!\n")

        else:
            print("\nErro ao excluir: ID não encontrado.")








    

