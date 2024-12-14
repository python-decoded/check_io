
class Warrior:
    health = 50
    attack = 5
    defense = 0

    @property
    def is_alive(self) -> bool:
        return self.health > 0

    def deal_dmg(self, unit: "Warrior"):
        unit.health -= max(0, self.attack - unit.defense)


class Knight(Warrior):
    attack = 7


class Defender(Warrior):
    health = 60
    attack = 3
    defense = 2


def fight(unit_1: Warrior, unit_2: Warrior) -> bool:

    while unit_1.is_alive:
        unit_1.deal_dmg(unit_2)
        if not unit_2.is_alive:
            break
        unit_2.deal_dmg(unit_1)

    return unit_1.is_alive
