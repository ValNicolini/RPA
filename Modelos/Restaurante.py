class Restaurante:
    restaurantes = []

    def __init__(self, nome, categoria):
        self._nome = nome.title()
        self.categoria = categoria.upper()
        self._ativo = False
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self._nome} | {self.categoria}'

    @classmethod
    def listar_restaurantes(cls):
        print(f"{'Nome'.ljust(20)} | {'Categoria'.ljust(20)} | {'Status'.ljust(20)}")
        for restaurante in Restaurante.restaurantes:
            print(f'{restaurante._nome.ljust(20)} | {restaurante.categoria.ljust(20)} | {restaurante.ativo.ljust(20)}')

    @property
    def ativo(self):
        return 'Ativo' if self._ativo else 'Inativo'

    def alternar_status(self):
        self._ativo = not self._ativo

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_pizza = Restaurante('Pizza Express', 'Italiana')

restaurante_pizza.alternar_status()
Restaurante.listar_restaurantes()
