import unittest
import numpy
from mergeSort import mergeSort

class mergeTest(unittest.TestCase):

    def Test_empty_array(self):
        arr = [0]
        mergArray = mergeSort(arr)
        try:
            numpy.testing.assert_array_equal(arr, [])
            self.assertTrue(True)
        except AssertionError as error:
            self.assertTrue(False, error)

    def test_one_element_array(self):
        arr = numpy.array([2])
        mergArray = mergeSort(arr)
        try:
            numpy.testing.assert_array_equal(mergArray, arr)
            self.assertTrue(True)
        except AssertionError as error:
            self.assertTrue(False, error)

    def test_small_array(self):
        arr = numpy.array([4, 8, 3, 9, 0, 8])
        mergeArray = mergeSort(arr)
        try:
            numpy.testing.assert_array_equal(mergeArray, numpy.array([0, 3, 4, 8, 8, 9]))
            self.assertTrue(True)
        except AssertionError as error:
            self.assertTrue(False, error)


if __name__ == "__main__":
    unittest.main()