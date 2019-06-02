from sc2bot.actions.Action import Action
import sc2bot
from numpy.testing import assert_


class ActionImpl(Action):
    """
    Test dummy implementation.
    """

    def should_act(self, iteration: int): return True

    async def act(self, iteration: int): pass


def test_bot():
    bot = sc2bot.Sc2Bot()
    action = ActionImpl(bot)

    assert_(action.bot is bot)


def test_configuration():
    bot = sc2bot.Sc2Bot()
    action = ActionImpl(bot)

    assert_(action.configuration is bot.configuration)
