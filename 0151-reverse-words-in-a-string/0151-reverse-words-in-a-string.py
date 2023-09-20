import re

class Solution:
    def reverseWords(self, s: str) -> str:
        words = re.sub('\s+', '-', s.strip()).split('-')

        return ' '.join([word for word in words[::-1]])
