from unittest import TestCase
from utils.logging_util import init_logger
from logging import RootLogger


class TestLoggingUtil(TestCase):
    def setUp(self) -> None:
        pass

    def test_logging_util(self):
        logger = init_logger()
        result = isinstance(logger, RootLogger)
        # 断言
        self.assertEqual(result, True)
        # self.assertIsInstance(logger,RootLogger)

    def tearDown(self) -> None:
        pass
