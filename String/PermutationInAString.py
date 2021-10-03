class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        patternCounter = defaultdict(None, Counter(s1))
        windowCounter = defaultdict(lambda: 0, Counter(s2[:len(s1)]))
        startIdx = 0

        for endIdx in range(len(s1), len(s2)):

            if windowCounter == patternCounter:
                return True

            if s2[startIdx] in windowCounter:
                if windowCounter[s2[startIdx]] == 1:
                    windowCounter.pop(s2[startIdx])
                else:
                    windowCounter[s2[startIdx]] -= 1
            startIdx += 1
            windowCounter[s2[endIdx]] += 1

        return windowCounter == patternCounter
