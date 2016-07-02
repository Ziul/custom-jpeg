from __future__ import print_function
from sys import argv, stdout
from glob import glob
import os
import sys
import fnmatch
import json

from multiprocessing.pool import ThreadPool
# import matplotlib.pyplot as plt
# import matplotlib.animation as animation
import numpy as np
import itertools
import cv2


_MAX_THREADS = 10
_pool = ThreadPool(processes=_MAX_THREADS)
_options = _parser.parse_args()


def print(data, end='\n'):
    """overwrite print"""
    if _options.verbose:
        stdout.write(str(data) + end)


class FileNotFound(Exception):
    """docstring for FileNotFound exception"""

    def __init__(self, arg=''):
        if len(arg) > 1:
            output = "Figure not found or isn't a valid figure: "
        else:
            output = "Figure not found or isn't a valid figure."

        super(FileNotFound, self).__init__(output + arg)


class EmptyFile(Exception):
    """docstring for EmptyFile exception"""

    def __init__(self, arg=''):
        output = "There is nothing to fill the output"
        if arg:
            output += ': [{}]'.format(arg)
        super(EmptyFile, self).__init__(output)


class CustomJpeg(object):
    """docstring for CustomJpeg"""

    def __init__(self, filename):
        super(CustomJpeg, self).__init__()
        self.filename = filename
        # 0 is to read as grayscale
        self.figure = cv2.imread(self.filename, 0)
        if not _options.output:
            self.output_filename = self.filename.replace(
                self.filename.split('.')[-1], 'cjpeg')
        else:
            self.output_filename = _options.output
        if self.figure is None:
            raise FileNotFound(self.filename)
        self.shape = self.figure.shape
        self.pixs = _options.size
        self.scrambled = np.array([])

        self.bitarray = Bitset()
        self.bitarray.name = self.output_filename
        self.bitarray.verbose = _options.verbose

    def encode(self, output=''):
        """encode de file"""
        self.blocks_split()
        self.output = self.scrambled.copy()
        for i in range(len(self.scrambled)):
            self.output[i] = CustomJpeg._customDCT_(self.scrambled[i])
        self.output = self._blocks_merge_(
            self.output, self.figure.shape, self.pixs)
        # save

    def blocks_merge(self):
        """merge splited image into one"""

        self.figure = CustomJpeg._blocks_merge_(
            self.scrambled,
            self.figure.shape,
            self.pixs
        )

    def blocks_split(self):
        """split a image into NxN blocks. N=self.pixs"""
        self.scrambled = CustomJpeg._blocks_split_(
            self.figure, self.pixs)

    def show(self, name=''):
        """show the figure"""
        if name == '':
            name = self.output_filename
        cv2.imshow(name, self.figure)
        cv2.waitKey(0)

    def write(self):
        """write the bitarray to a file"""
        if not len(self.bitarray):
            raise EmptyFile(self.bitarray.name)
        self.bitarray.to_file()

    @staticmethod
    def _customDCT_(block):
        """applying DCT in a macroblock"""
        imf = np.float32(block) / 255.0  # float conversion/scale
        dst = cv2.dct(imf)           # the dct
        img = np.uint8(dst) * 255.0

        return img

    @staticmethod
    def _blocks_merge_(scrambled, shape, pixs=8):

        no_rows, no_cols = shape

        rows_n = int((no_rows / pixs) * pixs)
        cols_n = int((no_cols / pixs) * pixs)
        figure = np.zeros(shape, scrambled.dtype)

        next_block = 0

        # reassemble the blocks
        for row in range(rows_n - pixs + 1):
            for col in range(cols_n - pixs + 1):
                if (row % pixs == 0 and col % pixs == 0):
                    cur_block = scrambled[next_block].copy()
                    next_block += 1
                    figure[row:row + pixs, col:col + pixs] = cur_block

        return figure

    @staticmethod
    def _blocks_split_(figure, pixs=8):
        scrambled = figure.copy()

        no_rows, no_cols = scrambled.shape

        rows_n = int((no_rows / pixs) * pixs)
        cols_n = int((no_cols / pixs) * pixs)

        scrambled = cv2.resize(scrambled, (cols_n, rows_n))

        allBlocks = []

        # for loops to extract all blocks
        for row in range(rows_n - pixs + 1):
            for col in range(cols_n - pixs + 1):
                if (row % pixs == 0 and col % pixs == 0):
                    block = scrambled[row:row + pixs, col:col + pixs].copy()
                    allBlocks.append(block)

        return np.array(allBlocks, dtype=figure.dtype)

    @staticmethod
    def zig_zag(figure):
        """return the zig-zag of a block
            don't edit original block
        """
        if figure.shape[0] != figure.shape[1]:
            raise Exception('Block sould be square')

        n = figure.shape[0]
        output = np.array([], dtype=figure.dtype)

        def move(i, j):
            """inside method"""
            if j < (n - 1):
                return max(0, i - 1), j + 1
            else:
                return i + 1, j

        x, y = 0, 0
        for v in figure.flatten():
            output = np.append(output, figure[y][x])
            if (x + y) & 1:
                x, y = move(x, y)
            else:
                y, x = move(y, x)

        return output


def main():
    if (not _options.filename):
        if _options.args:
            _options.filename = _options.args
        else:
            _parser.print_help()
            return

    cj = CustomJpeg(_options.filename)
    cj.encode()
    cv2.imshow('k', cj.output)
    cj.show()

    cv2.waitKey(0)

if __name__ == '__main__':
    main()
