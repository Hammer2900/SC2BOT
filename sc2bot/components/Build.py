from .Component import Component
from .buildings import BUILDINGS


class Build(Component):

    def __init__(self, bot):
        super().__init__(bot)

        self._buildings = [building(bot)
                           for building in BUILDINGS]

    async def act(self, iteration: int):
        for building in self._buildings:
            await building(iteration)

    def should_act(self):
        return True
