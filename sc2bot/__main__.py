import sc2
from sc2 import Race, maps
from sc2.player import Bot, Computer, Difficulty

from . import Sc2Bot


sc2.run_game(maps.get("AbyssalReefLE"),
             [Bot(Race.Protoss, Sc2Bot(), name="SC2BOT"),
              Computer(Race.Protoss, Difficulty.Easy)],
             realtime=False)
