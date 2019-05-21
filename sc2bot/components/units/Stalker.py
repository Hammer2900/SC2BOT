from sc2.constants import UnitTypeId

from sc2bot.Configuration import Configuration
from sc2bot.components.Component import Component


class Stalker(Component):

    async def act(self, iteration: int):
        gateways = self.bot.units(UnitTypeId.GATEWAY).ready.noqueue

        if not len(gateways):
            return

        for gateway in gateways:
            await self.bot.do(gateway.train(UnitTypeId.STALKER))

    def should_act(self):
        stalkers = len(self.bot.units(UnitTypeId.STALKER))

        return self.bot.can_afford(UnitTypeId.STALKER) \
            and self.bot.units(UnitTypeId.GATEWAY).ready.noqueue != 0 \
            and stalkers < Configuration.MAX_STALKERS
