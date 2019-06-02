from sc2bot.Configuration import Configuration
from numpy.testing import assert_equal


def test_max_gateways():
    for max_gateways in range(10):
        config = Configuration(dict(max_gateways=max_gateways))

        assert_equal(config.max_gateways, max_gateways,
                     err_msg='Configuration max gateways not same as input!')


def test_max_workers():
    for max_workers in range(10):
        config = Configuration(dict(max_workers=max_workers))

        assert_equal(config.max_workers, max_workers,
                     err_msg='Configuration max workers not same as input!')

# TODO test more Configuration properties
