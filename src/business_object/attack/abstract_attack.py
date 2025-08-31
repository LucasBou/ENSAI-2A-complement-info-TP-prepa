from abc import ABC, abstractmethod
from ..pokemon.abstract_pokemon import AbstractPokemon


class AbstractAttack(ABC):
    def __init__(self, power: int, name: str, description: str):
        self._power = power
        self._name = name
        self._description = description

    @abstractmethod
    def compute_damage(
        self, attacking_pokemon: AbstractPokemon, defending_pokemon: AbstractPokemon
    ) -> int: ...
