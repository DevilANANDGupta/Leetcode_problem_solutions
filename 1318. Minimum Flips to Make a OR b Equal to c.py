class Solution:
    def minFlips(self, a: int, b: int, c: int) -> int:
        flips = 0

        while a or b or c:
            bit_a = a & 1
            bit_b = b & 1
            bit_c = c & 1

            if bit_c == 1:
                if bit_a == 0 and bit_b == 0:
                    flips += 1
            else:
                if bit_a == 1 and bit_b == 1:
                    flips += 2
                elif bit_a == 1 or bit_b == 1:
                    flips += 1

            a >>= 1
            b >>= 1
            c >>= 1

        return flips
