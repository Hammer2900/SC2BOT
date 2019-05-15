from sc2 import BotAI


class Sc2Bot(BotAI):

    async def on_step(self, iteration: int):
        await self.distribute_workers()

    # TODO
