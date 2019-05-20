from sc2 import BotAI
from abc import abstractmethod


class Component:
    """
    Component's contract is simple: if ``should_act`` returns ``True``, ``act``
    is called to perform the necessary logic.
    """

    def __init__(self, bot: BotAI):
        self._bot = bot

    @property
    def bot(self) -> BotAI:
        return self._bot

    async def __call__(self, iteration: int):
        if self.should_act():
            await self.act(iteration)

    @abstractmethod
    async def act(self, iteration: int):
        return NotImplemented

    @abstractmethod
    def should_act(self) -> bool:
        return NotImplemented
