from pokemon import *
from pessoa import *

def escolher_pokemon_inicial(player):
    print(f"Olá {player}, você podera escolher agora o pokemon que irá lhe acompanhar nessa jornada!")

    pokemon1 = PokemonEletrico("Pikachu", level=5)
    pokemon2 = PokemonFogo("Charmander", level=5)
    pokemon3 = PokemonAgua("Squirtle", level=5)

    print("Você possui 3 escolhas: ")
    print("1 - ", pokemon1)
    print("2 - ", pokemon2)
    print("3 - ", pokemon3)
   
    while True:
        escolha = input("Escolha seu pokemon: ")

        if escolha == "1":
            player.capturar(pokemon1)
            break
        elif escolha == "2":
            player.capturar(pokemon2)
            break
        elif escolha == "3":
            player.capturar(pokemon3)
            break
        else:
            print("Escolha invalida")

player = Player("Miguel")
player.capturar(PokemonFogo("Chamander", level=5))


inimigo = Inimigo(nome="Gary", pokemons=[PokemonAgua("Squirtle", level=5)])

player.batalhar(inimigo)