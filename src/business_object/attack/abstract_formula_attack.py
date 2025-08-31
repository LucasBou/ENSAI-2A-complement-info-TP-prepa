from .abstract_attack import AbstractAttack
from abc import ABC, abstractmethod
from ..pokemon.abstract_pokemon import AbstractPokemon


class AbstractFormulaAttack(AbstractAttack):
    def __init__(
        self, power: int, name: str, description: str, randomness_source: int = 0
    ):
        super().__init__(power=power, name=name, description=description)

    def compute_damage(
        self, attacking_pokemon: AbstractPokemon, defending_pokemon: AbstractPokemon
    ) -> int:
        level_factor = ((attacking_pokemon.level * 2) / 5) + 2
        to_be_added_two = (
            level_factor
            * self._power
            * self.get_attack_stat(attacking_pokemon)
            / (self.get_defense_stat(defending_pokemon) * 50)
        )
        randomness = 1
        other_multipliers = 1
        return (to_be_added_two + 2) * randomness * other_multipliers

    @abstractmethod
    def get_attack_stat(self, a_pokemon: AbstractPokemon) -> float: ...

    @abstractmethod
    def get_defense_stat(self, a_pokemon: AbstractPokemon) -> float: ...
