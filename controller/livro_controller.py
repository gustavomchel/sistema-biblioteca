from model.livro_model import LivroModel 

class LivroController:
    def __init__(self):
        self.livro_model = LivroModel() # Objeto da classe 'LivroModel' para enviar argumentos;

    def cadastrar_livro(self, titulo, ano_publicacao, id_autor):
        if titulo and ano_publicacao and id_autor:
            self.livro_model.inserir_livro(titulo, ano_publicacao, id_autor)
            print("\nLivro cadastrado com sucesso!\n")
        else:
            print("Não foi possível cadastrar o livro.")

    def listar_livros(self):
        livros = self.livro_model.listar_livros()

        if not livros:
            print("Nenhum livro cadastrado!")
        else:
            print("\n===== Lista de Livros =====")
            for livro in livros:
                print(f"ID: {livro[0]} | Título: {livro[1]} | Ano de publicação: {livro[2]} | Autor: {livro[3]}")

    def atualizar_livro(self, id_livro, titulo, ano_publicacao, id_autor):
        try:
            if id_livro and titulo and ano_publicacao and id_autor:
                self.livro_model.atualizar_livro(titulo, ano_publicacao, id_autor, id_livro)
                print("\nLivro atualizado com sucesso!\n")

        except Exception as e:
            print("Erro ao atualizar.", e)

    def excluir_livro(self, id_livro):
        if id_livro:
            self.livro_model.excluir_livro(id_livro)
            print("\nLivro excluído com sucesso!\n")

        else:
            print("\nErro ao excluir livro: ID não encontrado.")






    

