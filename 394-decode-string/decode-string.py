class Solution:
    def decodeString(self, s: str) -> str:
        stack = []

        for i in range(len(s)):
            if s[i] !=']':
                stack.append(s[i])
            else:
                sbstr = ''
                while stack[-1] != '[':
                    sbstr = stack.pop() + sbstr
                stack.pop()

                k=''
                while stack and stack[-1].isdigit():
                    k= stack.pop()+k
                stack.append(int(k)*sbstr)
        return "".join(stack)