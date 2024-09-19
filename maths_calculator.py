"""
Author: Sedar Olmez
Email: olmez49@gmail.com
Date: 19/09/2024
Description: This script contains an object that mimic 
the behaviour of a calculator with basic arithmetic.
"""


class Calculator:
    """
    Description: This class represents a simple calculator with basic arithmetic operations.
    """

    def __init__(self) -> None:
        """
        Description: The constructor of the calculator object.
        arguments: None
        output: None
        """
        pass

    def subtract(self, numberA: float, numberB: float) -> float:
        """
        Description: Subtracts two numbers.
        arguments:
            numberA (float): The first number to be subtracted.
            numberB (float): The second number to be subtracted.
        output: float: The result of the subtraction.
        """
        return numberA - numberB

    def add(self, numberA: float, numberB: float) -> float:
        """
        Description: Adds two numbers.
        arguments:
            numberA (float): The first number to be added.
            numberB (float): The second number to be added.
        output: float: The result of the addition.
        """
        return numberA + numberB

    def multiply(self, numberA: float, numberB: float) -> float:
        """
        Description: Multiplies two numbers.
        arguments:
            numberA (float): The first number to be multiplied.
            numberB (float): The second number to be multiplied.
        output: float: The result of the multiplication.
        """
        return numberA * numberB

    def divide(self, numberA: float, numberB: float) -> float:
        """
        Description: Divides two numbers.
        arguments:
            numberA (float): The dividend.
            numberB (float): The divisor.
        output: float: The result of the division.
        """
        if numberB == 0:
            return "Error: Division by zero is not allowed."
        return numberA / numberB
