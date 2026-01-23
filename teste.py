from abc import abstractmethod



class Animal:
    def __init__(self, nome, peso, idade,raca,patas):
        self.nome = nome
        self.peso = peso
        self.idade = idade
        self.raca = raca
        self.patas = patas

        @abstractmethod
        def saudar(self):
            pass

class Cachorro(Animal):
        def __init__(self, nome, peso, idade, raca,patas):
            super().__init__(nome,peso,idade,raca,patas)

        def saudar(self):
            print("Auau")

class Gato(Animal):
        def __init__(self,nome,peso,idade,raca,patas):
            super().__init__(nome, peso, idade, raca, patas)

        def saudar(self):
            print("Miau")

cachorro1 = Cachorro('Max', 3, 2, 'Doberman', 4)
gato1 = Gato('Roger', 1, 2, 'Pelo Curto Brasileiro', 4 )
