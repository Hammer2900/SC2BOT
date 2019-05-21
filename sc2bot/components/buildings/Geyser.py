from sc2.constants import UnitTypeId

from sc2bot.Configuration import Configuration
from sc2bot.components.Component import Component
from functools import lru_cache


class Geyser(Component):
    """
    TODO the current use of ``assimilators()`` is not terribly efficient.
    Profile to check if this is problematic.
    """

    async def act(self, iteration: int):
        for nexus in self.bot.townhalls.ready:
            for geyser in self.nearest_geysers(nexus):
                worker = self.bot.select_build_worker(geyser.position)

                if worker is None:
                    return

                if not self.assimilators().closer_than(1.0, geyser).exists:
                    await self.bot.do(worker.build(UnitTypeId.ASSIMILATOR,
                                                   geyser))

    def should_act(self):
        if not self.bot.can_afford(UnitTypeId.ASSIMILATOR):
            return False

        return any(not self.assimilators().closer_than(1.0, geyser).exists
                   for nexus in self.bot.townhalls
                   for geyser in self.nearest_geysers(nexus))

    @lru_cache(None)
    def nearest_geysers(self, nexus):
        return self.bot.state.vespene_geyser.closer_than(
            Configuration.RESOURCE_MAX_DISTANCE,
            nexus)

    def assimilators(self):
        return self.bot.units(UnitTypeId.ASSIMILATOR)
