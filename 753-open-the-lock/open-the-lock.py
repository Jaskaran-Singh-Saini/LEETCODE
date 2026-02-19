class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        dead = set(deadends)
        if "0000" in dead:
            return -1
        if target == "0000":
            return 0
        
        q = deque(["0000"])
        seen = {"0000"}
        steps = 0

        while q:
            for _ in range(len(q)):
                curr = q.popleft()

                if curr in dead:
                    continue
                if curr == target:
                    return steps
                
                for i in range(4):
                    digit = int(curr[i])

                    for move in (-1, 1):
                        new_digit = (digit + move) % 10
                        nxt = curr[:i] + str(new_digit) + curr[i+1 :]

                        if nxt not in dead and nxt not in seen:
                            seen.add(nxt)
                            q.append(nxt)
                    
            steps += 1
                
        return -1