from typing import Any, Dict

import yaml


class Configuration:

    def __init__(self, data: Dict[str, Any] = None):
        if data is None:
            data = load()

        self._configuration = data

    @property
    def max_gateways(self):
        return self._configuration['max_gateways']

    @property
    def max_workers(self):
        return self._configuration['max_workers']

    # TODO add more properties as needed


def load() -> Dict[str, Any]:
    """
    Reads the configuration file from the filesystem.
    """
    with open('sc2bot/configuration.yml') as file:
        return yaml.safe_load(file)
