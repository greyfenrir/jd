from unittest.case import TestCase
from distance import minimal_distance

# from distance import min_dist as minimal_distance


class TestDistance(TestCase):
    def test_the_same(self):
        a = 'word'
        self.assertEqual(0, minimal_distance(a, a))

    def test_empty(self):
        a = 'word'
        self.assertEqual(len(a), minimal_distance(a, ''))

    def test_del(self):
        a = 'word1'
        b = 'wor'
        self.assertEqual(2, minimal_distance(a, b))

    def test_add(self):
        a = 'word1'
        b = 'wor'
        self.assertEqual(2, minimal_distance(b, a))

    def test_add_del(self):
        a = 'word1'
        b = '1word'
        self.assertEqual(2, minimal_distance(a, b))

    def test_replace(self):
        a = 'word1'
        b = 'word2'
        self.assertEqual(1, minimal_distance(b, a))

