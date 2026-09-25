class Solution:
    def compress(self, chars: list[str]) -> int:
        insrt = 0
        i = 0
        while i<len(chars):
            grp = 1
            while (grp+i) < len(chars) and chars[grp+i] == chars[i]:
                grp += 1
            chars[insrt] = chars[i]
            insrt += 1
            if grp>1:
                string = str(grp)
                chars[insrt:insrt+len(string)] = list(string)
                insrt += len(string)
            i+=grp
        return insrt