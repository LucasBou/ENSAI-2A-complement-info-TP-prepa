from .abstract_attack import AbstractAttack


class FixedDamageAttack(AbstractAttack):
    def compute_damage(self, attacking_pokemon, defending_pokemon) -> int:
        return self._power
