from sc2.constants import UnitTypeId

from sc2bot.Configuration import Configuration
from .Component import Component


class Expansion(Component):

    async def act(self, iteration: int):
        await self.bot.expand_now()

    def should_act(self) -> bool:
        """
        We expand when the number of workers per Nexus exceeds a threshold, and
        we do not yet have the maximum number of Nexuses.
        """
        ratio = len(self.bot.workers) / len(self.bot.units(UnitTypeId.NEXUS))
        num_nexuses = len(self.bot.units(UnitTypeId.NEXUS))

        return ratio > Configuration.WORKERS_PER_NEXUS \
            and num_nexuses < Configuration.MAX_NEXUSES \
            and not self.bot.already_pending(UnitTypeId.NEXUS)
