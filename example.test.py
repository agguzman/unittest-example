# -*- coding: utf-8 -*-


import unittest
import mock
from example import rm


class RmTestCase(unittest.TestCase):

    @mock.patch('example.os')
    def test_rm(self, mock_os):
        rm('any file')

        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with('any file')


if __name__ == '__main__':
    unittest.main()