"""
 Implement an algorithm to determine if a string has all unique characters. What if you cannot use additional data structures?
"""
import unittest

#Time O(n^2) space O(1)
def isUnique(s):
    for i in range(len(s) - 1):
        for j in range(i + 1, len(s)):
            if s[i] == s[j]:
                return False
    return True

#using set time O(n) space O(n)
def isUniqueUsingSet(s):
    setString = set(s)
    if len(setString) == len(s):
        return True
    return False

#driver
print(isUnique("tesgj45jjkgm"))
