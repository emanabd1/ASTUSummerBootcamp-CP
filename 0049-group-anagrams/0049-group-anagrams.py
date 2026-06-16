class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        groups = defaultdict(list)
        for s in strs:
            sorted_key = ''.join(sorted(s))
            groups[sorted_key].append(s)
        return list(groups.values())
        