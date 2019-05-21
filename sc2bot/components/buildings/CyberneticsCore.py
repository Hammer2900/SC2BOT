from sc2.constants import UnitTypeId

from sc2bot.Configuration import Configuration
from sc2bot.components.Component import Component


class CyberneticsCore(Component):

    async def act(self, iteration: int):
        map_center = self.bot.game_info.map_center
        near = self.bot.townhalls.first.position

        await self.bot.build(UnitTypeId.CYBERNETICSCORE,
                             near.towards(map_center, 5))

    def should_act(self) -> bool:
        cybernetics = len(self.bot.units(UnitTypeId.CYBERNETICSCORE))

        return cybernetics < Configuration.MAX_CYBERNETICS_CORES \
            and len(self.bot.units(UnitTypeId.GATEWAY).ready) != 0 \
            and self.bot.can_afford(UnitTypeId.CYBERNETICSCORE) \
            and not self.bot.already_pending(UnitTypeId.CYBERNETICSCORE)
