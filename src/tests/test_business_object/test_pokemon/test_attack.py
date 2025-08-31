from business_object.attack.fixed_damage_attack import FixedDamageAttack
from business_object.attack.special_formula_attack import SpecialFormulaAttack


def test_same_power_as_given(snorlax):
    any_pokemon = snorlax
    attackpower = 15
    attack = FixedDamageAttack(
        power=attackpower,
        name="Fly",
        description="Jumps into the air and slams on the opponent the next turn.",
    )

    damage = attack.compute_damage(any_pokemon, any_pokemon)

    assert damage == attackpower


def test_special_formula_attack(snorlax):
    attack = SpecialFormulaAttack(
        power=100,
        name="Flamethrower",
        description="Engulfes the opponent into scorching hot flames.",
    )

    expected_damage = ((4*100*65)/(110*50))+2

    result_dammage = attack.compute_damage(snorlax, snorlax)

    assert expected_damage == result_dammage
