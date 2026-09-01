class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        temp, res = set(), set()

        for i in range(len(s)-9):
            cur  = s[i: i+10]
            if cur in temp:
                res.add(cur)
            temp.add(cur)
        
        return list(res)