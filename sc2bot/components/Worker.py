from sc2.constants import UnitTypeId

from sc2bot.Configuration import Configuration
from .Component import Component


class Worker(Component):

    async def __call__(self, iteration: int):
        # This need not be done every iteration.
        if any(self.bot.workers.idle) or iteration % 10 == 0:
            await self.bot.distribute_workers()

        await super().__call__(iteration)

    async def act(self, iteration: int):
        nexuses = self.bot.units(UnitTypeId.NEXUS).ready.noqueue

        if len(nexuses):
            await self.bot.do(nexuses.first.train(UnitTypeId.PROBE))

    def should_act(self) -> bool:
        """
        Tests if we should build more workers.
        """
        return self.bot.can_afford(UnitTypeId.PROBE) \
            and len(self.bot.workers) < Configuration.MAX_WORKERS
