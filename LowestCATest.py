import unittest

import LowestCA
from LowestCA import findLCA, findLCAUtil

class FirstTest(unittest.TestCase):

    def test(self):
        result = 2
        self.assertEqual(findLCA(4, 5), result)