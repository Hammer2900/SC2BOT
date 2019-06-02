from abc import ABC, abstractmethod

from sc2bot import Configuration, Sc2Bot


class Action(ABC):
    """
    Base class for actions. When this functor is called, the contract is such
    that *if* ``should_act`` returns ``True``, ``act`` is guaranteed to be
    called.
    """
    def __init__(self, bot: Sc2Bot):
        self._bot = bot

    @property
    def bot(self) -> Sc2Bot:
        """
        Convenience method for the associated BotAI.
        """
        return self._bot

    @property
    def configuration(self) -> Configuration:
        """
        Convenience method for the associated Configuration object.
        """
        return self._bot.configuration

    @abstractmethod
    async def act(self, iteration: int):
        return NotImplemented

    @abstractmethod
    def should_act(self, iteration: int) -> bool:
        """
        Determines if the action should be performed, based on the returned
        boolean value.
        """
        return NotImplemented

    async def __call__(self, iteration: int):
        if self.should_act(iteration):
            await self.act(iteration)
