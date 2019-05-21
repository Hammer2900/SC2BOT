from sc2 import BotAI

from sc2bot.components import COMPONENTS
from sc2.data import Result

class Sc2Bot(BotAI):

    def __init__(self):
        super().__init__()

        self._components = [component(self)
                            for component in COMPONENTS]

    async def on_step(self, iteration: int):
        for component in self._components:
            await component(iteration)
