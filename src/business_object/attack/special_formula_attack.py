from ..pokemon.abstract_pokemon import AbstractPokemon
from .abstract_formula_attack import AbstractFormulaAttack


class SpecialFormulaAttack(AbstractFormulaAttack):
    def get_attack_stat(self, a_pokemon: AbstractPokemon) -> float:
        return a_pokemon.sp_atk_current

    def get_defense_stat(self, a_pokemon: AbstractPokemon) -> float:
        return a_pokemon.sp_def_current
