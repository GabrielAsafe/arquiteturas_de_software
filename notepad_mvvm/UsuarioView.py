from PySide6.QtWidgets import QMainWindow, QLineEdit, QPushButton, QVBoxLayout, QWidget

class UsuarioView(QMainWindow):
    def __init__(self, usuario_view_model):
        super().__init__()
        self.usuario_view_model = usuario_view_model
        self.setWindowTitle("Atualização de Usuário")
        self.setGeometry(100, 100, 300, 200)

        # Campos de texto para exibir e atualizar os dados
        self.nome_line_edit = QLineEdit(self)
        self.idade_line_edit = QLineEdit(self)

        # Botão para atualizar os dados
        self.botao_atualizar = QPushButton("Atualizar", self)
        self.botao_atualizar.clicked.connect(self.atualizar_usuario)

        layout = QVBoxLayout()
        layout.addWidget(self.nome_line_edit)
        layout.addWidget(self.idade_line_edit)
        layout.addWidget(self.botao_atualizar)

        container = QWidget()
        container.setLayout(layout)
        self.setCentralWidget(container)

    def atualizar_view(self):
        # Preenche os campos com os dados do usuário
        nome = self.usuario_view_model.get_nome()
        idade = self.usuario_view_model.get_idade()
        self.nome_line_edit.setText(nome)
        self.idade_line_edit.setText(idade)

    def atualizar_usuario(self):
        nome = self.nome_line_edit.text()
        idade = int(self.idade_line_edit.text())

        # Atualiza os dados no banco de dados através do ViewModel
        self.usuario_view_model.atualizar_usuario(nome, idade)

        # Feedback para o usuário (poderia ser uma janela de sucesso, por exemplo)
        print(f"Usuário atualizado: {nome} - {idade}")
