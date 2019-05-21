from sc2.constants import UnitTypeId

from sc2bot.Configuration import Configuration
from .Component import Component


class Expansion(Component):

    async def act(self, iteration: int):
        await self.bot.expand_now()

    def should_act(self) -> bool:
        """
        We expand when the number of workers per Nexus exceeds a threshold, we
        do not yet have the maximum number of Nexuses, and are not currently
        already expanding.
        """
        ratio = len(self.bot.workers) / len(self.bot.townhalls)
        num_nexuses = len(self.bot.townhalls)

        return ratio > Configuration.WORKERS_PER_NEXUS \
            and num_nexuses < Configuration.MAX_NEXUSES \
            and not self.bot.already_pending(UnitTypeId.NEXUS)
