class Pessoa:
    olhos = 2
    def __init__(self, *filhos, nome=None, idade=36):
        self.nome = nome
        self.idade = idade
        self.filhos = list(filhos)

    def cumprimentar(self):
        return f'Olá {id(self)}'

    @staticmethod
        #funciona como uma função da classe pessoa, não precisa receber atributo
    def metodo_estatico():
        return 42

    @classmethod
    def nome_e_atributos_de_classe(cls):
        return f'{cls} - olhos {cls.olhos} '

if __name__=='__main__':
    marilia = Pessoa(nome='Marilia', idade=12)
    marilia.olhos=4
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
    print(Pessoa.olhos)
    print(marilia.olhos)
    print(jose.olhos)
    print(Pessoa.metodo_estatico())
    print(Pessoa.nome_e_atributos_de_classe())