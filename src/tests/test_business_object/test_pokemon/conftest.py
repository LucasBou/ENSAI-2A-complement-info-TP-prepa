from pytest import fixture
from business_object.pokemon.defender_pokemon import DefenderPokemon
from business_object.pokemon.abstract_pokemon import AbstractPokemon
from business_object.statistic import Statistic


@fixture
def snorlax() -> AbstractPokemon:
    return DefenderPokemon(
        level=5,
        stat_current=Statistic(
            hp=160, attack=100, defense=100, sp_atk=65, sp_def=110, speed=30
        ),
    )
