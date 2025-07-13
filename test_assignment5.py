# -*- coding: utf-8 -*-
"""
Created on Fri Jul 11 10:28:08pm 2025

@author: Brooklyn Rimes 
"""

import unittest
from assignment5 import fahrenheit_to_celsius, fibonacci

class TestAssignment5(unittest.TestCase):

    # Fahrenheit to Celsius Tests 

    def test_fahrenheit_to_celsius_valid_inputs(self):
        self.assertAlmostEqual(fahrenheit_to_celsius(32), 0.0)
        self.assertAlmostEqual(fahrenheit_to_celsius(212), 100.0)
        self.assertAlmostEqual(fahrenheit_to_celsius(98.6), 37.0, places=1)

    def test_fahrenheit_to_celsius_invalid_type(self):
        with self.assertRaises(TypeError):
            fahrenheit_to_celsius("hot")
        with self.assertRaises(TypeError):
            fahrenheit_to_celsius(None)

    # Fibonacci Tests 

    def test_fibonacci_base_cases(self):
        self.assertEqual(fibonacci(0), 0)
        self.assertEqual(fibonacci(1), 1)

    def test_fibonacci_valid_numbers(self):
        self.assertEqual(fibonacci(5), 5)
        self.assertEqual(fibonacci(10), 55)
        self.assertEqual(fibonacci(15), 610)

    def test_fibonacci_negative_input(self):
        with self.assertRaises(ValueError):
            fibonacci(-1)

    def test_fibonacci_invalid_type(self):
        with self.assertRaises(TypeError):
            fibonacci("ten")
        with self.assertRaises(TypeError):
            fibonacci(3.5)
        with self.assertRaises(TypeError):
            fibonacci(None)

# Run tests
if __name__ == "__main__":
    unittest.main()