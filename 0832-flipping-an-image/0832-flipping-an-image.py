class Solution(object):
    def flipAndInvertImage(self, image):
        """
        :type image: List[List[int]]
        :rtype: List[List[int]]
        """
        for row in image:
            left = 0
            right = len(row) - 1
            
            while left <= right:
                if row[left] == row[right]:
                    row[left] = row[left] ^ 1
                    if left != right:
                        row[right] = row[right] ^ 1
                
                left += 1
                right -= 1
                
        return image