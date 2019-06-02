from typing import List, Type

from .Action import Action
from .DistributeWorkers import DistributeWorkers
from .constructions import CONSTRUCTIONS
from .units import UNITS

ACTIONS: List[Type[Action]] = [
    DistributeWorkers,
    *CONSTRUCTIONS,
    *UNITS
]
