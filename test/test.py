#!/usr/bin/env python

import random
import unittest
import sys
sys.path.append('../src/')
import number_play

class TestSequenceFunctions(unittest.TestCase):

    def setUp(self):
        self.seq = range(10)

    def test_shuffle(self):
        # make sure the shuffled sequence does not lose any elements
        random.shuffle(self.seq)
        self.seq.sort()
        self.assertEqual(self.seq, range(10))

        # should raise an exception for an immutable sequence
        self.assertRaises(TypeError, random.shuffle, (1,2,3))

    def test_choice(self):
        element = random.choice(self.seq)
        self.assertTrue(element in self.seq)

    def test_sample(self):
        with self.assertRaises(ValueError):
            random.sample(self.seq, 20)
        for element in random.sample(self.seq, 5):
            self.assertTrue(element in self.seq)

    def testFail(self):
        self.failIf(False, 'test failures')

    def test_add_them(self):
        self.assertEqual(10, number_play.add_them(7, 3))
        self.assertEqual(11, number_play.add_them(-7, 18))

if __name__ == '__main__':
    unittest.main()
