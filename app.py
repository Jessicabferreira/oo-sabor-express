from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida

restaurante_praca = Restaurante('praça', 'Gourmet')
bebida_suco = Bebida('Suco de Melancia', 5.0,'grande')
restaurante_praca.adicionar_no_cardapio(bebida_suco)


def main():
    print(bebida_suco)


if __name__ == '__main__':
    main()
