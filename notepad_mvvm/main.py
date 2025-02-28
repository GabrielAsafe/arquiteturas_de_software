from PySide6.QtWidgets import QApplication
from Usuario import *
from UsuarioViewModel import *
from UsuarioView import *
from UsuarioSelect import *

def main():
    app = QApplication([])

    # Cria o banco de dados (se não existir)
    Usuario.criar_tabela()

    # Cria o ViewModel e esse puto tem uma instância do usuário na classe. 
    #então o self é uma instância do user selecionado mas inicializa como none
    usuario_view_model = UsuarioViewModel()

    # Cria a View de Atualização
    usuario_view = UsuarioView(usuario_view_model)
    
    # Cria a View de Seleção de Usuário
    usuario_select = UsuarioSelect(usuario_view_model, usuario_view)

    # Exibe a tela de seleção
    usuario_select.show()

    app.exec()

if __name__ == "__main__":
    main()



