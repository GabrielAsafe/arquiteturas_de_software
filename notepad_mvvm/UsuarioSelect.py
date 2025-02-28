from PySide6.QtWidgets import QMainWindow, QListWidget, QPushButton, QVBoxLayout, QWidget
import sqlite3

class UsuarioSelect(QMainWindow):
    def __init__(self, usuario_view_model, usuario_view):
        super().__init__()
        self.usuario_view_model = usuario_view_model
        self.usuario_view = usuario_view
        self.setWindowTitle("Seleção de Usuário")
        self.setGeometry(100, 100, 300, 200)

        # Lista de usuários para seleção
        self.lista_usuarios = QListWidget(self)
        self.carregar_usuarios()

        # Botão para selecionar o usuário
        self.botao_selecionar = QPushButton("Selecionar", self)
        self.botao_selecionar.clicked.connect(self.selecionar_usuario)

        layout = QVBoxLayout()
        layout.addWidget(self.lista_usuarios)
        layout.addWidget(self.botao_selecionar)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def carregar_usuarios(self):
        # Carrega os usuários do banco de dados
        con = sqlite3.connect('usuarios.db')
        cursor = con.cursor()
        cursor.execute("SELECT * FROM usuarios")
        usuarios = cursor.fetchall()
        con.close()

        for usuario in usuarios:
            self.lista_usuarios.addItem(f"{usuario[1]} - {usuario[2]}")

    def selecionar_usuario(self):
        selected_item = self.lista_usuarios.currentItem().text()
        nome, idade = selected_item.split(" - ")
        idade = int(idade)

        # Recupera o usuário do banco de dados
        con = sqlite3.connect('usuarios.db')
        cursor = con.cursor()
        cursor.execute("SELECT id FROM usuarios WHERE nome=? AND idade=?", (nome, idade))
        usuario_id = cursor.fetchone()[0]
        con.close()

        # Carrega o usuário selecionado na ViewModel
        self.usuario_view_model.carregar_usuario(usuario_id)

        # Navega para a tela de detalhes de usuário
        self.usuario_view.atualizar_view()
        self.usuario_view.show()
        self.close()
