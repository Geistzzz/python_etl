import os
from unittest import TestCase

from utils.file_util import get_file_list


class TestFileUtil(TestCase):
    def setUp(self) -> None:
        self.project_root_path = os.path.dirname(os.getcwd())

    def test_get_dir_list(self):
        result1 = get_file_list(self.project_root_path + '/' + 'test_dir', recursive=False)
        self.assertEqual(result1,['1','2'])

    def tearDown(self):
        pass
