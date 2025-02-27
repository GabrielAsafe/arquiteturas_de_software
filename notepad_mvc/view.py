from PySide6.QtWidgets import QMainWindow, QTextEdit, QWidget, QVBoxLayout, QPushButton, QScrollArea
from PySide6.QtGui import QAction, QIcon
from pathlib import Path
import os


class NotaEditor(QMainWindow):
    def __init__(self, controller, id_nota=None, titulo="", conteudo=""):
        super().__init__()
        self.controller = controller
        self.id_nota = id_nota
        self.setWindowTitle("Editar Nota" if id_nota else "Nova Nota")
        self.resize(400, 300)

        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        self.title = QTextEdit(self)
        self.title.setPlaceholderText("Título")
        self.title.setText(titulo)
        layout.addWidget(self.title)

        self.text_box = QTextEdit(self)
        self.text_box.setPlaceholderText("Conteúdo")
        self.text_box.setText(conteudo)
        layout.addWidget(self.text_box)

        self.button = QPushButton("Salvar", self)
        self.button.clicked.connect(self.salvar)
        layout.addWidget(self.button)

        self.setCentralWidget(central_widget)

    def salvar(self):
        """Salva a nota ao clicar no botão."""
        titulo = self.title.toPlainText()
        conteudo = self.text_box.toPlainText()
        self.controller.salvar_nota(self.id_nota, titulo, conteudo)
        self.close()


class NotaView(QMainWindow):
    def __init__(self, controller):
        super().__init__()
        self.controller = controller
        self.setWindowTitle("Minhas Notas")
        self.resize(400, 500)

        # Criar o widget central e layout
        central_widget = QWidget(self)
        layout = QVBoxLayout(central_widget)

        # Barra de ferramentas com botão "Nova Nota"
        path = Path(__file__).resolve().parent
        new_note = QAction(QIcon(os.path.join(path, '../images/new.png')), '&Nova Nota', self)
        new_note.setShortcut('Ctrl+N')
        new_note.setStatusTip('Criar uma nova nota')
        new_note.triggered.connect(self.nova_nota)
        
        toolbar = self.addToolBar('New')
        toolbar.addAction(new_note)

        # Área de rolagem para exibir notas
        self.scroll = QScrollArea(self)
        self.scroll.setWidgetResizable(True)
        self.notes_container = QWidget()
        self.notes_layout = QVBoxLayout(self.notes_container)

        self.scroll.setWidget(self.notes_container)
        layout.addWidget(self.scroll)

        self.setCentralWidget(central_widget)
        self.carregar_notas()

    def carregar_notas(self):
        """Carrega todas as notas na tela principal"""
        # Remove widgets antigos para atualizar a interface
        for i in reversed(range(self.notes_layout.count())):
            widget = self.notes_layout.itemAt(i).widget()
            if widget:
                widget.deleteLater()

        # Obtém notas do banco e cria botões para elas
        notas = self.controller.buscar_notas()
        for nota in notas:
            id_nota, titulo, _ = nota
            botao = QPushButton(titulo, self)
            botao.clicked.connect(lambda checked, id_nota=id_nota: self.abrir_nota(id_nota))
            self.notes_layout.addWidget(botao)

    def nova_nota(self):
        """Abre uma nova janela para criar uma nota"""
        self.controller.abrir_janela_nota()

    def abrir_nota(self, id_nota):
        """Abre uma nota existente para edição"""
        self.controller.abrir_janela_nota(id_nota)