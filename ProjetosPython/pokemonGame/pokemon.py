import random

class Pokemon:
    def __init__(self, especie, level=None, nome=None):
        self.especie = especie

        if level:
            self.level = level
        else:
            self.level = random.randint(1, 100)

        if nome:
            self.nome = nome
        else:
            self.nome = especie

        self.ataque = self.level * 5
        self.vida = self.level * 10

    def __str__(self):
        return (f"{self.nome} ({self.level})")

    def atacar(self, pokemon):
        pokemon.vida -= self.ataque
        print(f"{pokemon} perdeu {self.ataque} de vida")

        if pokemon.vida <= 0:
            print(f"{pokemon} recebeu um golpe muito forte e esta fora de jogo...")
            return True
        else:
            return False


class PokemonEletrico(Pokemon):
    tipo = "eletrico"

    def atacar(self, pokemon):
        print(f"{self} lançou um raio do trovão em {pokemon}")
        return super().atacar(pokemon)

class PokemonFogo(Pokemon):
    tipo = "fogo"

    def atacar(self, pokemon):
        print(f"{self} lançou bola de fogo na cabeça de {pokemon}")
        return super().atacar(pokemon)

class PokemonAgua(Pokemon):
    tipo = "água"

    def atacar(self, pokemon):
        print(f"{self} lançou um jato d'água em {pokemon}")
        return super().atacar(pokemon)