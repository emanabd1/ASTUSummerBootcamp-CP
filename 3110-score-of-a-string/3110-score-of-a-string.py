class Solution(object):
    def scoreOfString(self, s):
        """
        :type s: str
        :rtype: int
        """
        y = 0
        for i in range (len(s) - 1):
            x = abs((ord(s[i])) - (ord(s[i+1])))
            y +=x
        return y
        