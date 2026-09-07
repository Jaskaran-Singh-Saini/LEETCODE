class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.strip()
        words = s.split()
        reverse = words[::-1]
        return ' '.join(reverse)