"""
The knows API is already defined for you.
@param a, person a
@param b, person b
@return a boolean, whether a knows b
you can call Celebrity.knows(a, b)
"""


class Solution:
    # @param {int} n a party with n people
    # @return {int} the celebrity's label or -1
    def findCelebrity(self, n):
        celebrity = 0
        for i in range(1, n):
            if Celebrity.knows(celebrity, i):
                celebrity = i

        for i in range(n):
            if celebrity != i and (Celebrity.knows(celebrity, i) or not Celebrity.knows(i, celebrity)):
                return -1

        return celebrity
