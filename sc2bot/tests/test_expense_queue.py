from sc2bot.ExpenseQueue import ExpenseQueue
from sc2 import BotAI
from numpy.testing import assert_


def test_empty():
    queue = ExpenseQueue(BotAI())
    assert_(queue.is_empty())                   # queue is initially empty

    queue.put(lambda item: None)
    assert_(not queue.is_empty())               # there is an action enqueued

    queue.get()
    assert_(queue.is_empty())                   # and now it should be gone
