from pokemon import Pokemon
from typing import List


class Trainer:
    def __init__(self, name: str):
        self.name = name
        self.pokemons: List[Pokemon] = []

    def add_pokemon(self, pokemon: Pokemon):
        if pokemon.pokemon_details() in self.pokemons:
            return "This pokemon is already caught"
        self.pokemons.append(pokemon.pokemon_details())
        return f"Caught {pokemon.pokemon_details()}"

    def release_pokemon(self, pokemon_name: str):
        for pokemon_stats in self.pokemons:
            current_pokemon = pokemon_stats.split()[0]
            if current_pokemon == pokemon_name:
                self.pokemons.remove(pokemon_stats)
                return f"You have released {pokemon_name}"
        return "Pokemon is not caught"

    def trainer_data(self):
        trainer_name = self.name
        the_amount_of_pokemon_caught = len(self.pokemons)
        result = f"Pokemon Trainer {trainer_name}\nPokemon count {the_amount_of_pokemon_caught}"
        for pokemon_details in self.pokemons:
            result += f"\n- {pokemon_details}"
        return result


# Test code:
pokemon = Pokemon("Pikachu", 90)
print(pokemon.pokemon_details())
trainer = Trainer("Ash")
print(trainer.add_pokemon(pokemon))
second_pokemon = Pokemon("Charizard", 110)
print(trainer.add_pokemon(second_pokemon))
print(trainer.add_pokemon(second_pokemon))
print(trainer.release_pokemon("Pikachu"))
print(trainer.release_pokemon("Pikachu"))
print(trainer.trainer_data())
