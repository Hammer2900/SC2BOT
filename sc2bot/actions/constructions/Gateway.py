import sc2

from .. import Action


class Gateway(Action):
    """
    Constructs a Gateway, if possible and needed.
    """

    async def act(self, iteration: int):
        near = self.bot.townhalls.first.position
        map_center = self.bot.game_info.map_center

        await self.bot.build(sc2.UnitTypeId.GATEWAY,
                             near.towards(map_center, 5))

    def should_act(self, iteration: int):
        return self.bot.can_afford(sc2.UnitTypeId.GATEWAY) \
               and not self.bot.already_pending(sc2.UnitTypeId.GATEWAY)
