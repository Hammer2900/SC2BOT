from collections import deque
from typing import Callable

from sc2 import BotAI


class ExpenseQueue:
    """
    Keeps track of expenses to be made.
    """

    def __init__(self, bot: BotAI):
        self._bot = bot
        self._queue = deque()

    def put(self, action: Callable):
        self._queue.appendleft(action)

    def get(self) -> Callable:
        return self._queue.pop()

    def is_empty(self) -> bool:
        return len(self._queue) == 0

    def resolve(self):
        """
        Attempts to resolve the current queue in order.
        """
        while not self.is_empty():
            action = self.get()

            if not action():                    # action did not succeed, so
                self._queue.append(action)      # add it as first-most action
                break                           # for the next iteration.
