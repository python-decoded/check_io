from collections import UserList

from tasks.season_1.wariors import fight


class Army(UserList):

    def add_units(self, unit_type: type, count: int):
        self.data.extend(unit_type() for _ in range(count))


class Battle:

    def fight(self, army1: Army, army2: Army) -> bool:

        while army1 and army2:
            unit1, unit2 = army1[0], army2[0]
            if fight(unit1, unit2):
                army2.pop(0)
            else:
                army1.pop(0)
        return bool(army1)
