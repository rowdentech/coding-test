"""
Author: Sedar Olmez
Email: olmez49@gmail.com
Date: 19/09/2024
Description: This script contains unit tests for the Calculator object.
"""

import unittest
from maths_calculator import Calculator


class TestCalculator(unittest.TestCase):
    """
    Description: This class contains unit tests for the Calculator class.
    """

    def setUp(self) -> None:
        """
        Description: This class contains unit tests for the Calculator.
        arguments: None
        output: None
        """
        self.calculator = Calculator()

    def test_subtract(self) -> None:
        """
        Description: This function contains a unit test for the
        Calculator method subtraction.
        argument: None
        output: None
        """

        self.assertEqual(self.calculator.subtract(3, 1), 2)
        self.assertTrue(self.calculator.subtract(3, 2), 1)

    def test_add(self) -> None:
        """
        Description: This function contains a unit test for the calculator method addition.
        argument: None
        output: None
        """

        self.assertEqual(self.calculator.add(4.0, 1), 5.0)
        self.assertTrue(self.calculator.add(4.6, 1.4), 6.0)
        # NOTE: checking if the TypeError is thrown here.
        # Won't repeat an assertion test due to time constraints.
        with self.assertRaises(TypeError):
            self.calculator.add("2.0", 4.0)

    def test_multiply(self) -> None:
        """
        Description: This function contains a unit test for the calculator method multiplication.
        argument: None
        output: None
        """
        self.assertEqual(self.calculator.multiply(3.0, 2.0), 6.0)
        self.assertNotEqual(self.calculator.multiply(3.0, 3.25), 6.0)

    def test_divide(self) -> None:
        """
        Description : This function contains a unit test for the calculator method division.
        argument: None
        output: None
        """

        self.assertEqual(self.calculator.divide(6.0, 3.0), 2.0)
        self.assertNotEqual(self.calculator.divide(6.0, 2.0), 2.10)
        self.assertGreater(self.calculator.divide(12.0, 2.0), 5.9)
