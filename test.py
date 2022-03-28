import unittest
import syllogistic

class TestCalc(unittest.TestCase):
	def test_type_of_a_first_premise(self):
		result = syllogistic.check_the_type_of_a_first_premise()
