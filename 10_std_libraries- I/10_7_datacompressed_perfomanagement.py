import time
# import lzma
import bz2
import gzip
from timeit import Timer


# data = b"This is a sample data" * 9999000
# print("original data size:", len(data))
#
# start = time.time()
# cd_lzma = lzma.compress(data)
# end = time.time()
#
# print(end-start)
# print(len(cd_lzma))
#
# start = time.time()
# cd_gzip =gzip.compress(data)
# end = time.time()
#
# print(end-start)
# print(len(cd_gzip))
#
# start = time.time()
# cd_bz2 =bz2.compress(data)
# end = time.time()
#
# print(end-start)
# print(len(cd_bz2))

# PERFORMANCE MANAGEMENT


# a = Timer('t=a; a=b; b=t', 'a=100; b=200').timeit()
# print(a)
# b = Timer('a,b = b,a', 'a=100; b=200').timeit()
# print(b)

# def average(values):
#     """Computes the arithmetic mean of a list of numbers.
#
#         print(average([20, 30, 70]))
#     40.0
#     """
#     return sum(values) / len(values)
#
#
#
# import doctest
# doctest.testmod()
# import unittest
#
# class TestStatisticalFunctions(unittest.TestCase):
#
#     def test_average(self):
#         self.assertEqual(average([20, 30, 70]), 40.0)
#         self.assertEqual(round(average([1, 5, 7]), 1), 4.3)
#         with self.assertRaises(ZeroDivisionError):
#             average([])
#         with self.assertRaises(TypeError):
#             average(20, 30, 70)
#
#
#
# unittest.main()



