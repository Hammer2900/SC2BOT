import sc2

from .. import Action


class Worker(Action):
    """
    Constructs a Worker, if possible and needed.
    """

    async def act(self, iteration: int):
        town_halls = self.bot.townhalls.ready.noqueue
        await self.bot.do(town_halls.first.train(sc2.UnitTypeId.PROBE))

    def should_act(self, iteration: int) -> bool:
        return self.bot.can_afford(sc2.UnitTypeId.PROBE) \
               and len(self.bot.townhalls.ready.noqueue) != 0
