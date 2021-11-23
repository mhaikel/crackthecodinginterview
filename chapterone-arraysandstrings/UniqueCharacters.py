"""
 Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
"""
import unittest

def isUnique(s):
    for i in range(len(s) - 1):
        if s[i] == s[i + 1]:
            return False
    return True

print(isUnique("siters"))