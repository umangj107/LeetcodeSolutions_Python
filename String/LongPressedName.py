class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        if len(typed) < len(name):
            return False
        cur1 = 0
        cur2 = 0
        while cur1 < len(name) and cur2 < len(typed):
            if not name[cur1] == typed[cur2]:
                return False
            count1 = 0
            count2 = 0
            while cur1+1 < len(name) and name[cur1+1] == name[cur1]:
                count1 += 1
                cur1 += 1
            while cur2+1 < len(typed) and typed[cur2+1] == typed[cur2]:
                count2 += 1
                cur2 += 1
            if count1 > count2:
                return False
            cur1 += 1
            cur2 += 1
        if cur1 < len(name) or cur2 < len(typed):
            return False
        return True
