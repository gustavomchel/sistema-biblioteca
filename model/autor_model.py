import psycopg2

class AutorModel:
    def __init__(self):
        try:
            self.connexao = psycopg2.connect(
                host="localhost",
                database="biblioteca",
                user="postgres",
                password="1234"
            )
        except Exception as e:
            print("Erro ao conectar com o banco de dados: ", e)

    # Métodos que recebem parametros de 'autor_controller' para persistir dados;

    def inserir_autor(self, nome, nacionalidade):
        try:
            cursor = self.connexao.cursor()

            cursor.execute(
                """
                INSERT INTO autores(nome, nacionalidade)
                VALUES (%s, %s);
                """, (nome, nacionalidade)
            )

            self.connexao.commit()   
            cursor.close()

        except Exception as e:
            print("Erro ao inserir autor: ", e)

    def listar_autor(self):
        try:
            cursor = self.connexao.cursor()

            cursor.execute(
                """
                SELECT id_autor, nome, nacionalidade FROM autores;
                """
            )

            autores = cursor.fetchall() # Recuperação de todas as linhas de resultado

            cursor.close()
            return autores
        
        except Exception as e:
            print("Erro ao listar autor: ", e)

    def atualizar_autor(self, nome, nacionalidade, id_autor):
        try:
            cursor = self.connexao.cursor()

            cursor.execute(
                """
                UPDATE autores SET nome = %s, nacionalidade = %s WHERE id_autor = %s;
                """, (nome, nacionalidade, id_autor)
            )

            self.connexao.commit()
            cursor.close()

        except Exception as e:
            print("Erro ao atualizar autor: ", e)

    def excluir_autor(self, id_autor):
        try:
            cursor = self.connexao.cursor()

            cursor.execute(
                """
                DELETE FROM autores WHERE id_autor = %s;
                """, [id_autor]
            )
        
            self.connexao.commit()
            cursor.close()

        except Exception as e:
            print("Erro ao excluir autor: ", e)