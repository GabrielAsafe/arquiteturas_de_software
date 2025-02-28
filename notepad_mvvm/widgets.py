#1. QPushButton (Botão)
from PySide6.QtWidgets import QApplication, QPushButton

app = QApplication([])
button = QPushButton("Clique Aqui")
button.show()
app.exec()
#2. QLabel (Rótulo de Texto)
from PySide6.QtWidgets import QApplication, QLabel

app = QApplication([])
label = QLabel("Olá, Mundo!")
label.show()
app.exec()
#3. QLineEdit (Campo de Entrada de Texto)
from PySide6.QtWidgets import QApplication, QLineEdit

app = QApplication([])
line_edit = QLineEdit()
line_edit.setPlaceholderText("Digite algo...")
line_edit.show()
app.exec()
#4. QTextEdit (Área de Texto)
from PySide6.QtWidgets import QApplication, QTextEdit

app = QApplication([])
text_edit = QTextEdit()
text_edit.setText("Texto inicial...")
text_edit.show()
app.exec()
#5. QCheckBox (Caixa de Seleção)
from PySide6.QtWidgets import QApplication, QCheckBox

app = QApplication([])
checkbox = QCheckBox("Aceito os termos")
checkbox.show()
app.exec()
#6. QRadioButton (Botão de Opção)
from PySide6.QtWidgets import QApplication, QRadioButton

app = QApplication([])
radio = QRadioButton("Opção 1")
radio.show()
app.exec()
#7. QComboBox (Caixa de Seleção)
from PySide6.QtWidgets import QApplication, QComboBox

app = QApplication([])
combo = QComboBox()
combo.addItems(["Item 1", "Item 2", "Item 3"])
combo.show()
app.exec()
#8. QListWidget (Lista de Itens)
from PySide6.QtWidgets import QApplication, QListWidget

app = QApplication([])
list_widget = QListWidget()
list_widget.addItems(["Item A", "Item B", "Item C"])
list_widget.show()
app.exec()
#9. QSpinBox (Caixa Numérica)
from PySide6.QtWidgets import QApplication, QSpinBox

app = QApplication([])
spinbox = QSpinBox()
spinbox.setRange(0, 100)
spinbox.show()
app.exec()
#10. Slider (Controle Deslizante)
from PySide6.QtWidgets import QApplication, QSlider
from PySide6.QtCore import Qt

app = QApplication([])
slider = QSlider(Qt.Horizontal)
slider.setRange(0, 100)
slider.show()
app.exec()
#11. QProgressBar (Barra de Progresso)
from PySide6.QtWidgets import QApplication, QProgressBar

app = QApplication([])
progress = QProgressBar()
progress.setValue(50)  # Define 50% completo
progress.show()
app.exec()
#12. QTabWidget (Abas)
from PySide6.QtWidgets import QApplication, QTabWidget, QWidget, QVBoxLayout, QLabel

app = QApplication([])
tab_widget = QTabWidget()

tab1 = QWidget()
tab1_layout = QVBoxLayout()
tab1_layout.addWidget(QLabel("Conteúdo da Aba 1"))
tab1.setLayout(tab1_layout)

tab2 = QWidget()
tab2_layout = QVBoxLayout()
tab2_layout.addWidget(QLabel("Conteúdo da Aba 2"))
tab2.setLayout(tab2_layout)

tab_widget.addTab(tab1, "Aba 1")
tab_widget.addTab(tab2, "Aba 2")

tab_widget.show()
app.exec()
#13. QGroupBox (Grupo de Controles)
from PySide6.QtWidgets import QApplication, QGroupBox, QVBoxLayout, QLabel

app = QApplication([])
group_box = QGroupBox("Configurações")
layout = QVBoxLayout()
layout.addWidget(QLabel("Opção 1"))
layout.addWidget(QLabel("Opção 2"))
group_box.setLayout(layout)
group_box.show()
app.exec()
#14. QFrame (Quadro)
from PySide6.QtWidgets import QApplication, QFrame

app = QApplication([])
frame = QFrame()
frame.setFrameShape(QFrame.Box)
frame.setFixedSize(100, 100)
frame.show()
app.exec()
#15. QFileDialog (Selecionar Arquivo)
from PySide6.QtWidgets import QApplication, QFileDialog

app = QApplication([])
file_name, _ = QFileDialog.getOpenFileName(None, "Selecione um arquivo")
print("Arquivo selecionado:", file_name)
#16. QColorDialog (Selecionar Cor)
from PySide6.QtWidgets import QApplication, QColorDialog

app = QApplication([])
color = QColorDialog.getColor()
if color.isValid():
    print("Cor escolhida:", color.name())
#17. QFontDialog (Selecionar Fonte)
from PySide6.QtWidgets import QApplication, QFontDialog

app = QApplication([])
font, ok = QFontDialog.getFont()
if ok:
    print("Fonte selecionada:", font.family())
#18. QMainWindow (Janela Principal)
from PySide6.QtWidgets import QApplication, QMainWindow

app = QApplication([])
main_window = QMainWindow()
main_window.setWindowTitle("Janela Principal")
main_window.show()
app.exec()
#19. QMessageBox (Caixa de Diálogo)
from PySide6.QtWidgets import QApplication, QMessageBox

app = QApplication([])
msg = QMessageBox()
msg.setText("Mensagem Exemplo")
msg.exec()
#20. QDockWidget (Painel Acoplável)
from PySide6.QtWidgets import QApplication, QMainWindow, QDockWidget, QLabel

app = QApplication([])
main_window = QMainWindow()
dock = QDockWidget("Painel")
dock.setWidget(QLabel("Conteúdo do Painel"))
main_window.addDockWidget(Qt.RightDockWidgetArea, dock)
main_window.show()
app.exec()