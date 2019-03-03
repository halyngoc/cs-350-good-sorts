import unittest
import numpy
import heapsort

class HeapSortTest(unittest.TestCase):

    def test_empty_array(self):
        sorted_arr = heapsort.sort(numpy.empty(0))
        try:
            numpy.testing.assert_array_equal(sorted_arr, [])
            self.assertTrue(True)
        except AssertionError as error:
            self.assertTrue(False, error)

    def test_one_element_array(self):
        sorted_arr = heapsort.sort(numpy.array([2]))
        try:
            numpy.testing.assert_array_equal(sorted_arr, numpy.array([2]))
            self.assertTrue(True)
        except AssertionError as error:
            self.assertTrue(False, error)

    def test_small_array(self):
        sorted_arr = heapsort.sort(numpy.array([4, 8, 3, 9, 0, 8]))
        try:
            numpy.testing.assert_array_equal(sorted_arr, numpy.array([0, 3, 4, 8, 8, 9]))
            self.assertTrue(True)
        except AssertionError as error:
            self.assertTrue(False, error)

if __name__ == "__main__":
    unittest.main()
