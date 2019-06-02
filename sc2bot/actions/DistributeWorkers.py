from .Action import Action


class DistributeWorkers(Action):
    """
    Distributes workers over the available, owned resource pools.
    """

    async def act(self, iteration: int):
        await self.bot.distribute_workers()

    def should_act(self, iteration: int):
        return True
