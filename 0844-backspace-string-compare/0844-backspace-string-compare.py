class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
   
        def stacker(S):
            stack = []
            for char in S:
                if char is not "#":
                    stack.append(char)
                else:
                    if not stack:
                        continue
                    stack.pop()
            return stack
        
        l1 = stacker(s)
        l2 = stacker(t)
        return l1 == l2