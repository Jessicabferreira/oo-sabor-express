from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0,'grande')
bebida_suco.aplicar_desconto()
restaurante_praca.adicionar_no_cardapio(bebida_suco)


def main():
    restaurante_praca.exibir_cardapio


if __name__ == '__main__':
    main()
