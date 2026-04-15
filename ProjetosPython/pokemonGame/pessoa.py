import random
from pokemon import *


NOMES = ["Gary", "Leitinho", "Bruto", "Trem Bala", "Red", "Ashe"]

POKEMONS = [
    PokemonFogo("Chamander"),
    PokemonFogo("Charmilion"),
    PokemonFogo("Charizard"),
    PokemonEletrico("Pikachu"),
    PokemonEletrico("Raichu"),
    PokemonAgua("Mudkip")
]

class Pessoa:

    def __init__(self, nome=None, pokemons=[]):
        if nome:
            self.nome = nome
        else:
            self.nome = random.choice(NOMES)

        self.pokemons = pokemons

    def __str__(self):
        return self.nome

    def mostrar_pokemons(self):
        if self.pokemons:
            print("Pokemons de: " + self.nome)
            for i, pokemon in enumerate(self.pokemons):
                print(f"{i} - {pokemon}")
        else:
            print(f"{self.nome} não tem nenhum pokemon")

    def escolher_pokemon(self):
        if self.pokemons:
            pokemon_escolhido = random.choice(self.pokemons)
            print(f"{self} escolheu {pokemon_escolhido}.")
            return pokemon_escolhido
        else:
            print("ERRO: Esse jogador não possui nenhum pokemon para ser escolhido")
            return None

            

    def batalhar(self, pessoa):
        print(f"{self}, iniciou uma batalha com {pessoa}")

        pessoa.mostrar_pokemons()
        
        pokemon_inimigo = pessoa.escolher_pokemon()
        pokemon = self.escolher_pokemon()

        if pokemon and pokemon_inimigo:
            while True:
                vitoria = pokemon.atacar(pokemon_inimigo)
                if vitoria:
                    print(f"{self} ganhou a batalha")
                    break

                vitoria_inimiga = pokemon_inimigo.atacar(pokemon)
                if vitoria_inimiga:
                    print(f"{pessoa} ganhou a batalha")
                    break

                if pokemon.vida <= 0:
                    print(f"{pokemon} recebeu um golpe muito forte e esta fora de jogo...")
                elif pokemon_inimigo.vida <= 0:
                    print(f"{pessoa} perdeu a batalha.")

        else:
            print("Essa batalha não pode ocorrer")
            

        

class Player(Pessoa):
    tipo = "player"

    def capturar(self, pokemon):
        self.pokemons.append(pokemon)
        print(f"{self} capturou {pokemon}!")


    def escolher_pokemon(self):
        self.mostrar_pokemons()

        if self.pokemons:
            while True:
                try:
                    escolha = int(input("Escolha seu pokemon: "))
                    pokemon_escolhido = self.pokemons[escolha]
                    print(f"{pokemon_escolhido} eu escolho você!!!!")
                    return pokemon_escolhido
                except:
                    print("Escolha invalida")
        else:
            print("ERRO: Esse jogador não possui nenhum pokemon para ser escolhido")



class Inimigo(Pessoa):
    tipo = "inimigo"

    def __init__(self, nome=None, pokemons=[]): 
        if not pokemons:
            for i in range(random.randint(1, 6)):
                pokemons.append(random.choice(POKEMONS))

        super().__init__(nome=nome, pokemons=pokemons)