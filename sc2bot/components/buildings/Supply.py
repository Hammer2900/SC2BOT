from sc2.constants import UnitTypeId

from sc2bot.Configuration import Configuration
from sc2bot.components.Component import Component


class Supply(Component):

    async def act(self, iteration: int):
        map_center = self.bot.game_info.map_center
        near = self.bot.townhalls.first.position

        await self.bot.build(UnitTypeId.PYLON,
                             near.towards(map_center, 5))

    def should_act(self) -> bool:
        return self.bot.supply_left < Configuration.MIN_SUPPLY \
            and self.bot.can_afford(UnitTypeId.PYLON) \
            and not self.bot.already_pending(UnitTypeId.PYLON)
