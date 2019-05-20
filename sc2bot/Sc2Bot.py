from sc2 import BotAI

from sc2bot.components import Expansion, Supply, Worker


class Sc2Bot(BotAI):

    def __init__(self):
        super().__init__()

        self._expansion = Expansion(self)
        self._worker = Worker(self)
        self._supply = Supply(self)

    async def on_step(self, iteration: int):
        await self._expansion(iteration)
        await self._worker(iteration)
        await self._supply(iteration)
