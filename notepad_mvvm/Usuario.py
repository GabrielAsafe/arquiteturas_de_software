import sqlite3

class Usuario:
    def __init__(self, id=None, nome=None, idade=None):
        self.id = id
        self.nome = nome
        self.idade = idade

    @staticmethod
    def criar_tabela():
        con = sqlite3.connect('usuarios.db')
        cursor = con.cursor()
        cursor.execute('''CREATE TABLE IF NOT EXISTS usuarios
                          (id INTEGER PRIMARY KEY, nome TEXT, idade INTEGER)''')
        con.commit()
        con.close()

    @staticmethod
    def adicionar_usuario(nome, idade):
        con = sqlite3.connect('usuarios.db')
        cursor = con.cursor()
        cursor.execute("INSERT INTO usuarios (nome, idade) VALUES (?, ?)", (nome, idade))
        con.commit()
        con.close()

    @staticmethod
    def obter_usuario_por_id(id):
        con = sqlite3.connect('usuarios.db')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM usuarios WHERE id=?", (id,))
        resultado = cursor.fetchone()
        con.close()
        if resultado:
            return Usuario(id=resultado[0], nome=resultado[1], idade=resultado[2])
        return None

    @staticmethod
    def atualizar_usuario(id, nome, idade):
        con = sqlite3.connect('usuarios.db')
        cursor = con.cursor()
        cursor.execute("UPDATE usuarios SET nome=?, idade=? WHERE id=?", (nome, idade, id))
        con.commit()
        con.close()
