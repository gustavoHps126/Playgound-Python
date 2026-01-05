from models.restaurante import Restaurante
from models.cardapio.prato import Prato
from models.cardapio.bebida import Bebida
from models.cardapio.sobremesa import sobremesa

restaurante_praca = Restaurante('praça', 'Gourmet')
restaurante_pizza = Restaurante('pizza express', 'Italiana')
restaurante_mexi = Restaurante('Mexi', 'Mexicano')
Bebida_suco = Bebida('Suco de Laranja', 7.50, '500ml')
Bebida_suco.aplicarDesconto()
Prato_burger = Prato('Cheeseburger', 25.00, 'Hambúrguer com queijo, alface, tomate e molho especial')
Prato_burger.aplicarDesconto()
sobremesa_brownie = sobremesa('Brownie com Sorvete', 15.00, 'Brownie quente servido com sorvete de baunilha')
sobremesa_brownie.aplicarDesconto()

restaurante_praca.adicionarCardapio(sobremesa_brownie)
restaurante_praca.adicionarCardapio(Bebida_suco)
restaurante_praca.adicionarCardapio(Prato_burger)



def main():
   restaurante_praca.exibir_cardapio
        

if __name__ == '__main__':
    main()

   