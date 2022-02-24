class Solution:
    def removeInvalidParentheses(self, s: str) -> List[str]:
        self.refAns = set()
        self.refDict = {}

        def minRemovals(s):
            if len(s) == 0:
                return 0
            stack = []
            for i in s:
                if i == '(':
                    stack.append(i)
                elif i == ')':
                    if not stack or stack[-1] == ')':
                        stack.append(')')
                    else:
                        stack.pop(-1)
            # print(stack)
            return len(stack)

        def getAns(s, mn):
            if s in self.refDict:
                return

            self.refDict[s] = True

            if mn == 0:
                if s not in self.refAns:
                    if minRemovals(s) == 0:
                        self.refAns.add(s)
                return
            else:
                for i in range(len(s)):
                    if s[i] == '(' or s[i] == ')':
                        # print(s, i, s[:i] + s[i+1:], mn)
                        getAns(s[:i] + s[i+1:], mn-1)

        mn = minRemovals(s)
        if mn == len(s):
            return [""]
        getAns(s, mn)
        return list(self.refAns)
