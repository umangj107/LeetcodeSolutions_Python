class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        hash_map = collections.defaultdict(list)
        for path in paths:
            spit = path.split(" ")
            for i in range(1, len(spit)):
                n = spit[i].split("(")
                hash_map[n[1][:-1]].append(spit[0]+'/'+n[0])
        out = []
        for c, d in hash_map.items():
            if len(d) > 1:
                out.append(d)
        return out
