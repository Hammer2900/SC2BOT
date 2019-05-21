from sc2bot.components.Component import Component
from sc2.constants import UnitTypeId
from sc2bot.Configuration import Configuration


class Gateway(Component):

    async def act(self, iteration: int):
        map_center = self.bot.game_info.map_center
        near = self.bot.townhalls.first.position

        await self.bot.build(UnitTypeId.GATEWAY,
                             near.towards(map_center, 5))

    def should_act(self) -> bool:
        """
        We only build a Gateway when we can afford it, do not yet have the
        maximum number of Gateways, and are not already constructing one.
        """
        gateways = len(self.bot.units(UnitTypeId.GATEWAY))

        return self.bot.can_afford(UnitTypeId.GATEWAY) \
            and gateways < Configuration.MAX_GATEWAYS \
            and not self.bot.already_pending(UnitTypeId.GATEWAY)
