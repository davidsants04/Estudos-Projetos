class Pessoa:
  def __init__(self, nome: str, idade: int, altura: float):
    self.nome = nome
    self.idade = idade
    self.altura = altura

#Na barra de cima é o objeto e abaixo é os metodos....

  def dizer_ola(self):
    print(f'Olá, meu nome é {self.nome}. Tenho {self.idade} '
          f'anos e minha altura é {self.altura}m.')

  def cozinhar(self, receita: str):
    print(f'Estou cozinhando um(a): {receita}')

  def andar(self, distancia: float):
    print(f'Saí para andar. Volto quando completar {distancia} metros')

# Instancia um objeto da Classe "Pessoa"
pessoa = Pessoa(nome="David" , idade=20 , altura= 1.72)

# Chama os métodos de "Pessoa"
pessoa.dizer_ola()
pessoa.cozinhar("miojo")
pessoa.andar(3750.5)
