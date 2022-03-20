# Approach-1

import math


class Solution:
    def minDominoRotations(self, tops: List[int], bottoms: List[int]) -> int:
        def getSwaps(arrA, arrB, target):
            numSwaps = 0
            for i in range(len(arrA)):
                if arrA[i] != target and arrB[i] != target:
                    return math.inf
                elif arrA[i] != target:
                    numSwaps += 1
            return numSwaps

        minSwaps = min(getSwaps(tops, bottoms, tops[0]), getSwaps(tops, bottoms, bottoms[0]), getSwaps(
            bottoms, tops, tops[0]), getSwaps(bottoms, tops, bottoms[0]))

        return -1 if minSwaps == math.inf else minSwaps


# Approach-2

class Solution:
    def minDominoRotations(self, A: List[int], B: List[int]) -> int:
        def check(x):
            """
            Return min number of swaps 
            if one could make all elements in A or B equal to x.
            Else return -1.
            """
            # how many rotations should be done
            # to have all elements in A equal to x
            # and to have all elements in B equal to x
            rotations_a = rotations_b = 0
            for i in range(n):
                # rotations coudn't be done
                if A[i] != x and B[i] != x:
                    return -1
                # A[i] != x and B[i] == x
                elif A[i] != x:
                    rotations_a += 1
                # A[i] == x and B[i] != x
                elif B[i] != x:
                    rotations_b += 1
            # min number of rotations to have all
            # elements equal to x in A or B
            return min(rotations_a, rotations_b)

        n = len(A)
        rotations = check(A[0])
        # If one could make all elements in A or B equal to A[0]
        if rotations != -1 or A[0] == B[0]:
            return rotations
        # If one could make all elements in A or B equal to B[0]
        else:
            return check(B[0])
