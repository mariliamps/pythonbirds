class Pessoa:
    def __init__(self, nome=None, idade=36):
        self.nome = nome
        self.idade = idade

    def cumprimentar(self):
        return f'Olá {id(self)}'


if __name__=='__main__':
    p = Pessoa('Jose')
    print(id(p))
    print (p.cumprimentar())
    print (p.nome)
    p.nome='Marilia'
    print(p.nome)
    print(p.idade)