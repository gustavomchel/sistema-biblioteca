import psycopg2

class LivroModel:
    def __init__(self):
        try:
            self.connexao = psycopg2.connect(
                host="localhost",
                database="biblioteca",
                user="postgres",
                password="1234"
            )
        except Exception as e:
            print("Erro ao conectar com o banco de dados:", e)

    # Métodos que recebem parâmetros de 'livro_controller' para persistir dados;
    def inserir_livro(self, titulo, ano_publicacao, id_autor):
        try:
            cursor = self.connexao.cursor()

            cursor.execute(
                """
                INSERT INTO livros(titulo, ano_publicacao, id_autor)
                VALUES (%s, %s, %s);
                """, (titulo, ano_publicacao, id_autor)
            )

            self.connexao.commit()   
            cursor.close()

        except Exception as e:
            print("Erro ao inserir livro: ", e)

    def listar_livros(self):
        try:
            cursor = self.connexao.cursor()

            cursor.execute(
                """
                SELECT l.id_livro, l.titulo, l.ano_publicacao, a.nome AS autor
                FROM livros l JOIN autores a ON l.id_autor = a.id_autor
                """
            )

            livros = cursor.fetchall() # Recuperação de todas as linhas de resultado

            cursor.close()
            return livros
        
        except Exception as e:
            print("Erro ao listar livro: ", e)

    def atualizar_livro(self, titulo, ano_publicacao, id_autor, id_livro):
        try:
            cursor = self.connexao.cursor()

            cursor.execute(
                """
                UPDATE livros SET titulo = %s, ano_publicacao = %s, id_autor = %s WHERE id_livro = '%s';
                """, (titulo, ano_publicacao, id_autor, id_livro)
            )

            self.connexao.commit()
            cursor.close()

        except Exception as e:
            print("Erro ao atualizar livro: ", e)

    def excluir_livro(self, id_livro):
        try:
            cursor = self.connexao.cursor()

            cursor.execute(
                """
                DELETE FROM livros WHERE id_livro = %s;
                """, [id_livro]
            )
        
            self.connexao.commit()
            cursor.close()

        except Exception as e:
            print("Erro ao excluir livro: ", e)