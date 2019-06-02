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


def test_put_get_same_result():
    def sentinel(): pass

    queue = ExpenseQueue(BotAI())
    queue.put(sentinel)

    assert_(queue.get() is sentinel)            # equality is insufficient!


def test_resolve_empty():
    queue = ExpenseQueue(BotAI())
    queue.resolve()                             # this should not have effect


def test_resolve_requeue():
    def false(): return False

    queue = ExpenseQueue(BotAI())

    queue.put(false)                            # since the return value is
    queue.resolve()                             # False, the action should
    assert_(queue.get() is false)               # remain enqueued.


def test_resolve():
    def true(): return True

    queue = ExpenseQueue(BotAI())

    queue.put(true)                             # since the return value is
    queue.resolve()                             # True, the action should
    assert_(queue.is_empty())                   # have been processed.


def test_is_fifo_queue():
    def first(): return None

    def second(): return None

    assert_(first is not second)                # sanity check

    queue = ExpenseQueue(BotAI())

    queue.put(first)                            # queue should be FIFO; since
    queue.put(second)                           # we placed first before second
    assert_(queue.get() is first)               # we should get them back in
    assert_(queue.get() is second)              # the same order.
