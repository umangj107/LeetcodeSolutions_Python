class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        if len(flowerbed) == 1:
            if n == 0:
                return True
            if flowerbed[0] == 0:
                return True
            if flowerbed[0] == 1:
                return False
        k = 0

        if flowerbed[0] == flowerbed[1] == 0:
            flowerbed[0] = 1
            k += 1
        if k == 0:
            to_start = 1
        else:
            to_start = k+1
        for i in range(to_start, len(flowerbed)-1):
            if flowerbed[i-1] == 0 and flowerbed[i] == 0 and flowerbed[i+1] == 0:
                flowerbed[i] = 1
                k += 1
        if flowerbed[-1] == flowerbed[-2] == 0 and flowerbed[-3] == 1:
            k += 1
        return k >= n
