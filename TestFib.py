import Fib
import unittest

class TestPerfectNumber(unittest.TestCase):
	def test_fib_1(self):
		c = Fib.fib()
		self.assertEqual(c.next(), 1)
		self.assertEqual(c.next(), 2)
		self.assertEqual(c.next(), 3)
		self.assertEqual(c.next(), 5)
		self.assertEqual(c.next(), 8)
		self.assertEqual(c.next(), 13)

if __name__ == '__main__':
	unittest.main()
