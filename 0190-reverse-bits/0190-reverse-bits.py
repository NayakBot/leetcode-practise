class Solution:
    def reverseBits(self, n: int) -> int:
        result = 0
        for _ in range(32):
            result <<= 1         # Shift result to left to make room for next bit
            result |= (n & 1)    # Set the least significant bit of result if least significant bit of n is 1
            n >>= 1              # Right shift n to process next bit
        return result
