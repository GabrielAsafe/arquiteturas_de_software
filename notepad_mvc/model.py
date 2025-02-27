import sqlite3

class NotaModel:
    def __init__(self):
        self.conn = sqlite3.connect("meu_banco.db")
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS notas (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                titulo TEXT NOT NULL,
                conteudo TEXT NOT NULL
            )
        """)
        self.conn.commit()

    def buscar_notas(self):
        """Retorna todas as notas no banco de dados."""
        self.cursor.execute("SELECT * FROM notas")
        return self.cursor.fetchall()

    def buscar_nota_por_id(self, id_nota):
        """Retorna uma nota específica pelo ID."""
        self.cursor.execute("SELECT * FROM notas WHERE id = ?", (id_nota,))
        return self.cursor.fetchone()

    def salvar_nota(self, titulo, conteudo):
        """Salva uma nova nota no banco de dados."""
        self.cursor.execute("INSERT INTO notas (titulo, conteudo) VALUES (?, ?)", (titulo, conteudo))
        self.conn.commit()

    def atualizar_nota(self, id_nota, titulo, conteudo):
        """Atualiza uma nota existente."""
        self.cursor.execute("UPDATE notas SET titulo = ?, conteudo = ? WHERE id = ?", (titulo, conteudo, id_nota))
        self.conn.commit()

    def excluir_nota(self, id_nota):
        """Exclui uma nota do banco de dados."""
        self.cursor.execute("DELETE FROM notas WHERE id = ?", (id_nota,))
        self.conn.commit()

    def fechar_conexao(self):
        """Fecha a conexão com o banco de dados."""
        self.conn.close()
