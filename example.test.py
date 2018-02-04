# -*- coding: utf-8 -*-


import unittest
import mock
from example import rm


class RmTestCase(unittest.TestCase):

    @mock.patch('example.os.path')
    @mock.patch('example.os')
    def test_rm(self, mock_os, mock_path):

        mock_path.isfile.return_value = False

        rm('any file')

        # test that the remove call was not called
        self.assertFalse(mock_os.remove.called, 'Failed to remove file if not present')

        # make the file exist
        mock_path.isfile.return_value = True

        rm('any file')

        # test that rm called os.remove with the right parameters
        mock_os.remove.assert_called_with('any file')


if __name__ == '__main__':
    unittest.main()