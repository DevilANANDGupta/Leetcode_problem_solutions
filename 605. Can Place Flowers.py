class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
    # def can_place_flowers(flowerbed, n):
        i = 0
        while i < len(flowerbed) and n > 0:
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                n -= 1
            i += 1
        return n == 0
