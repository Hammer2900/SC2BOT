from .Component import Component
from sc2.constants import UnitTypeId
from sc2bot.Configuration import Configuration


class Attack(Component):

    async def act(self, iteration: int):
        units = self.bot.units.of_type([UnitTypeId.STALKER,
                                        UnitTypeId.ZEALOT]).idle

        if not len(units):
            return

        close_units = units.closer_than(5, units.center)

        # If the units are not grouped together, let us first ensure this
        # is the case.
        if len(close_units) < Configuration.MIN_UNITS_ATTACK_MOVE:
            await self.group(units.center, units - close_units)
        else:       # once they are, we are ready to attack the enemy base!
            await self.attack(units)

    def should_act(self):
        units = self.bot.units.of_type([UnitTypeId.STALKER, UnitTypeId.ZEALOT])

        return len(units) > Configuration.MIN_UNITS_ATTACK_MOVE \
            and not len(self.bot.known_enemy_units)

    async def group(self, to, units):
        await self.bot.do_actions([unit.move(to) for unit in units])

    async def attack(self, units):
        await self.bot.do_actions([unit.attack(self.target())
                                   for unit in units])

    def target(self):
        enemies = self.bot.known_enemy_units

        if enemies:             # we know enemy units - those take precedence
            return enemies.first

        return self.bot.enemy_start_locations[0]
