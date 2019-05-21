from .Component import Component
from .units import UNITS


class Train(Component):

    def __init__(self, bot):
        super().__init__(bot)

        self._units = [unit(bot) for unit in UNITS]

    async def act(self, iteration: int):
        for unit in self._units:
            await unit(iteration)

    def should_act(self):
        return True
