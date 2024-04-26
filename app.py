from Modelos.Restaurante import Restaurante

restaurante_praca =Restaurante('Cantina', 'Italiana')
restaurante_praca.receber_avaliacao('Val', 10)
restaurante_praca.receber_avaliacao('Gica', 7)
restaurante_praca.receber_avaliacao('Katia', 8)
# restaurante_mexicano = Restaurante('mexicano food', 'mexicano')
# restaurante_japones = Restaurante('Japa', 'japonesa')
def main():
    Restaurante.listar_restaurantes()




if __name__ == '__main__':
    main()