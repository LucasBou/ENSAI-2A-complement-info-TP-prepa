from business_object.pokemon.defender_pokemon import DefenderPokemon
from business_object.statistic import Statistic


class TestDefenderPokemon:
    def test_get_coef_damage_type(self, snorlax):

        # WHEN
        multiplier = snorlax.get_pokemon_attack_coef()

        # THEN
        assert multiplier == 2


if __name__ == "__main__":
    import pytest

    pytest.main([__file__])
