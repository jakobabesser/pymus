__author__ = 'Jakob Abesser'

import math

class Convert:

    def __init__(self):
        pass

    @staticmethod
    def midiPitch2NoteName(pitch, delimiter='', accidental='b', upperCase=False):
        """ Convert MIDI pitch to note name (note spelling + octave number)
        :param pitch: (int) MIDI pitch value
        :param delimiter: (string) Delimiter between note spelling & octave number
        :param accidental: (string) Key accidental ('b' or '#')
        :return: (string) Note name
        """
        noteNames = dict()
        noteNames['b'] = ['c', 'db', 'd', 'eb', 'e', 'f', 'gb', 'g', 'ab', 'a', 'bb', 'b']
        noteNames['#'] = ['c', 'c#', 'd', 'd#', 'e', 'f', 'f#', 'g', 'g#', 'a', 'a#', 'b']
        noteName = "{}{}{}".format(noteNames[accidental][Convert.pitch2Chroma(pitch)],
                                delimiter,
                                Convert.pitch2Octave(pitch))
        if upperCase:
            noteName = noteName[0].upper() + noteName[1:]
        return noteName

    @staticmethod
    def pitch2Octave(pitch):
        """ Converts MIDI pitch to octave number
        :param pitch: MIDI pitch
        :return: octave: (int) octave number
        """
        return int(math.floor(pitch/12.)-1)

    @staticmethod
    def pitch2Chroma(pitch):
        """ Convert MIDI pitch to chroma value
        :param pitch: MIDI pitch
        :return: chroma value
        """
        return pitch % 12

