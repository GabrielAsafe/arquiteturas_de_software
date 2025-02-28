from Usuario import *

class UsuarioViewModel:
    def __init__(self):
        self.usuario = None

    def carregar_usuario(self, usuario_id):
        # Recupera os dados do banco e atualiza a instância do Usuario
        self.usuario = Usuario.obter_usuario_por_id(usuario_id)

    def get_nome(self):
        return self.usuario.nome if self.usuario else ""

    def get_idade(self):
        return str(self.usuario.idade) if self.usuario else ""

    def atualizar_usuario(self, nome, idade):
        if self.usuario:
            Usuario.atualizar_usuario(self.usuario.id, nome, idade)
            self.usuario.nome = nome
            self.usuario.idade = idade
