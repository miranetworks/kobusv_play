#!/usr/bin/env python

import random
import unittest
import sys
import xmlrunner
sys.path.append('../src/')
import number_play

class MiscTests(unittest.TestCase):

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
        self.failIf(True, 'test a failure')

    def test_add_them(self):
        self.assertEqual(10, number_play.add_them(7, 3))
        self.assertEqual(11, number_play.add_them(-7, 18))

def run_tests_1():
    unittest.main()

def run_tests_2():
    suite = unittest.TestLoader().loadTestsFromTestCase(MiscTests)
    unittest.TextTestRunner(verbosity=1).run(suite)

def run_tests_3():
    suite = unittest.TestLoader().loadTestsFromTestCase(MiscTests)
    #runner = xmlrunner.XMLTestRunner(sys.stdout)
    runner = xmlrunner.XMLTestRunner('./output/')
    runner.run(suite)

if __name__ == '__main__':
    run_tests_3()
