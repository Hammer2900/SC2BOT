from sc2.constants import UnitTypeId

from sc2bot.Configuration import Configuration
from sc2bot.components.Component import Component


class Zealot(Component):

    async def act(self, iteration: int):
        gateways = self.bot.units(UnitTypeId.GATEWAY).ready.noqueue

        if not len(gateways):
            return

        for gateway in gateways:
            await self.bot.do(gateway.train(UnitTypeId.ZEALOT))

    def should_act(self):
        zealots = len(self.bot.units(UnitTypeId.ZEALOT))

        return self.bot.can_afford(UnitTypeId.ZEALOT) \
            and self.bot.units(UnitTypeId.GATEWAY).ready.noqueue != 0 \
            and zealots < Configuration.MAX_ZEALOTS
