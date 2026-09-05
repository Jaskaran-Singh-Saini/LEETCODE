class Solution:
    def reverseVowels(self, s: str) -> str:
        st = ('a','e','i','o','u','A','E','I','O','U')
        l,r = 0, len(s)-1
        s = list(s)

        while l<r:
            if s[l] not in st:
                l+=1
            elif s[r] not in st:
                r-=1
            else:
                s[l], s[r] = s[r], s[l]
                l+=1
                r-=1
        return "".join(s)