import unittest
import numpy
from Quicksort import quicksort
from Quicksort import partition
from Quicksort import getPivot


class QuickSortTest(unittest.TestCase):

    def test_empty_array(self):
        arr = numpy.empty(0)
        quicksort(arr,0, len(arr) - 1)
        try:
            numpy.testing.assert_array_equal(arr, [])
            self.assertTrue(True)
        except AssertionError as error:
            self.assertTrue(False, error)

    def test_one_element_array(self):
        arr = numpy.array([2])
        quicksort(arr,0, len(arr) - 1)
        try:
            numpy.testing.assert_array_equal(arr,numpy.array([2]))
            self.assertTrue(True)
        except AssertionError as error:
            self.assertTrue(False, error)

    def test_small_array(self):
        arr = numpy.array([4, 8, 3, 9, 0, 8])
        quicksort(arr,0, len(arr) - 1)
        try:
            numpy.testing.assert_array_equal(arr, numpy.array([0, 3, 4, 8, 8, 9]))
            self.assertTrue(True)
        except AssertionError as error:
            self.assertTrue(False, error)

if __name__ == "__main__":
    unittest.main()