from model import NotaModel
from view import NotaView
from view import NotaEditor

class NotaController:
    def __init__(self):
        self.model = NotaModel()
        self.view = NotaView(self)
        self.view.show()

    def buscar_notas(self):
        """Busca todas as notas no banco e as retorna para a View."""
        return self.model.buscar_notas()

    def abrir_janela_nota(self, id_nota=None):
        """Abre a janela de edição de uma nota."""
        if id_nota:
            nota = self.model.buscar_nota_por_id(id_nota)
            if nota:
                id_nota, titulo, conteudo = nota
                self.nota_editor = NotaEditor(self, id_nota, titulo, conteudo)
            else:
                return
        else:
            self.nota_editor = NotaEditor(self)

        self.nota_editor.show()

    def salvar_nota(self, id_nota, titulo, conteudo):
        """Salva ou atualiza uma nota e recarrega a lista na View."""
        if id_nota:
            self.model.atualizar_nota(id_nota, titulo, conteudo)
        else:
            self.model.salvar_nota(titulo, conteudo)

        self.view.carregar_notas()
