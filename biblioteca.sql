CREATE TABLE autores(
	id_autor SERIAL PRIMARY KEY,
	nome VARCHAR(200) NOT NULL,
	nacionalidade VARCHAR(100) NOT NULL
);

CREATE TABLE livros(
	id_livro SERIAL PRIMARY KEY,
	titulo VARCHAR(200) NOT NULL,
	ano_publicacao INTEGER NOT NULL,
	id_autor INTEGER REFERENCES autores(id_autor)
);