#/usr/bin/env python

import os
import numpy as np
import unittest

def cleanup(line):

    return line.strip().strip('\n').split()

def get_gold_pressures():

    return np.load('test.npy')

def get_cmg_pressures():

    with open('assignment18.txt') as f:

        raw_content = f.readlines()


    pressure = []
    for i in range(len(raw_content)):
        line = raw_content[i]
        clean_line = cleanup(line) 

        if clean_line != []:
            if clean_line[1] == 'K':
                pressure += [cleanup(raw_content[i+1])]

    return np.array(pressure, dtype=np.double)


class TestSolution(unittest.TestCase):


    def test_output_pressures(self):

        np.testing.assert_allclose(get_cmg_pressures(), get_gold_pressures(),
                                   atol=0.1)
        return


if __name__ == '__main__':
            unittest.main()
