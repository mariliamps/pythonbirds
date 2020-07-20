class Pessoa:
    def __init__(self, *filhos, nome=None, idade=36):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__=='__main__':
    marilia = Pessoa(nome='Marilia', idade=12)
    jose = Pessoa(marilia, nome='Jose2', idade=37)
    print(Pessoa.cumprimentar(jose))
    #print (jose.cumprimentar())
    print(jose.nome)
    print(jose.idade)
    for filho in jose.filhos:
        print(filho.nome)
        print(filho.idade)
    jose.sobrenome = 'Silva'
    print(jose.sobrenome)