from Modelos.Restaurante import Restaurante

restaurante_praca =Restaurante('Cantina', 'Italiana')
restaurante_praca.receber_avaliacao('Val', 5)
restaurante_praca.receber_avaliacao('Gica', 2)
restaurante_praca.receber_avaliacao('Katia', 0)
# restaurante_mexicano = Restaurante('mexicano food', 'mexicano')
# restaurante_japones = Restaurante('Japa', 'japonesa')
def main():
    Restaurante.listar_restaurantes()




if __name__ == '__main__':
    main()