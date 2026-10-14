class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        alt = 0
        mx_alt = 0

        for i in gain:
            alt += i
            mx_alt = max(mx_alt,alt)
        return mx_alt