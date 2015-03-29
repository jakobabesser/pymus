__author__ = 'Jakob Abesser'

import unittest
import sys
from os import path
sys.path.append(path.dirname(path.dirname(path.abspath(__file__))))
from convert.convert import Convert


class TestConvert(unittest.TestCase):

    def setUp(self):
        pass

    def testPitch2Octave(self):
        """ Unit test for pitch2octave() """
        self.assertEqual(Convert.pitch2Octave(0), -1)
        self.assertEqual(Convert.pitch2Octave(11), -1)
        self.assertEqual(Convert.pitch2Octave(12), 0)
        self.assertEqual(Convert.pitch2Octave(23), 0)
        self.assertEqual(Convert.pitch2Octave(24), 1)
        self.assertEqual(Convert.pitch2Octave(48), 3)

    def testPitch2Chroma(self):
        """ Unit test for pitch2Chroma() """
        self.assertEqual(Convert.pitch2Chroma(0), 0)
        self.assertEqual(Convert.pitch2Chroma(3), 3)
        self.assertEqual(Convert.pitch2Chroma(11), 11)
        self.assertEqual(Convert.pitch2Chroma(12), 0)
        self.assertEqual(Convert.pitch2Chroma(25), 1)

    def testMidiPitch2NoteName(self):
        """ Unit test for midiPitch2NoteName() """
        self.assertEqual(Convert.midiPitch2NoteName(24), 'c1')
        self.assertEqual(Convert.midiPitch2NoteName(24, delimiter=' '), 'c 1')
        self.assertEqual(Convert.midiPitch2NoteName(24, delimiter='-'), 'c-1')
        self.assertEqual(Convert.midiPitch2NoteName(25, upperCase=True), 'Db1')
        self.assertEqual(Convert.midiPitch2NoteName(25, upperCase=False), 'db1')
        self.assertEqual(Convert.midiPitch2NoteName(25, accidental='#'), 'c#1')
        self.assertEqual(Convert.midiPitch2NoteName(25, accidental='b'), 'db1')


if __name__ == "__main__":
    unittest.main()