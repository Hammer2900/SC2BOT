from functools import lru_cache

import sc2

from sc2bot.Configuration import Configuration
from sc2bot.actions import ACTIONS


class Sc2Bot(sc2.BotAI):

    def __init__(self):
        super().__init__()
        self._actions = [action(self) for action in ACTIONS]

    @property
    @lru_cache(1)
    def configuration(self) -> Configuration:
        return Configuration()

    async def on_step(self, iteration: int):
        for action in self._actions:
            await action(iteration)
