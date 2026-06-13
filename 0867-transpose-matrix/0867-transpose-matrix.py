class Solution(object):
    def transpose(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[List[int]]
        """
        R = len(matrix)
        C = len(matrix[0])
        result = [[0] * R for _ in range(C)]
        
        for r in range(R):
            for c in range(C):
                result[c][r] = matrix[r][c]
                
        return result