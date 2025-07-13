
"""
Created on Fri Jul 11 08:58:26pm  2025

@author: Brooklyn Rimes 
"""

def fahrenheit_to_celsius(fahrenheit):
    """ Converts a temperature from Fahrenheit to Celsius
    formula: (F-32)* 5/9 """
    
    if not isinstance(fahrenheit, (int, float)):
        raise TypeError("Temparute must be a number (int or float).")
        
    celsius = (fahrenheit - 32) * 5.0 /9.0
    return celsius

def fibonacci(n):
    """ Returns the nth Fibonacci number.
    Fib Sequence:
        n = 0 -> 0
        n = 1 -> 1
        n > 1 -> fib(n) = fib(n-1) + fib(n-2)"""
        
    if not isinstance(n, int):
        raise TypeError("n must be an integer.")
        
    if n < 0:
        raise ValueError("n must be a non-negative integer. ")
        
    if n == 0:
        return 0
    elif n == 1:
        return 1
    
    # calculate Fibonacci 
    a, b = 0, 1
    for _ in range(2, n +1):
        a, b = b, a + b
    return b 
