class Restaurante:
    def __init__(self, nome, categoria):
        self.nome = nome
        self.categoria = categoria
        self.ativo = False

    def __str__(self):
        return f'{self.nome} | {self.categoria} | {self.ativo}'

teste = Restaurante('Cantina', 'italiana')
novo = Restaurante('Novo', 'Francesa')
restaurantes = [teste, novo]
print(f'{novo}\n{teste}')
