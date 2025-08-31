from .abstract_pokemon import AbstractPokemon


class DefenderPokemon(AbstractPokemon):
    def get_pokemon_attack_coef(self) -> float:
        return 1 + (self.attack_current + self.defense_current) / 200
