from .Component import Component
from sc2bot.Configuration import Configuration
from sc2.constants import UnitTypeId


class Defend(Component):

    async def act(self, iteration: int):
        units = self.bot.units.of_type([UnitTypeId.STALKER, UnitTypeId.ZEALOT])

        for unit in units:
            await self.bot.do(unit.attack(
                self.bot.known_enemy_units.first.position))

    def should_act(self) -> bool:
        """
        We only need to defend if there are enemy units close to our bases.
        """
        defense_distance = Configuration.DEFENSE_RANGE

        return any(len(self.bot.known_enemy_units.closer_than(defense_distance,
                                                              nexus))
                   for nexus in self.bot.townhalls)
