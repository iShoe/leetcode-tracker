# Last updated: 8/23/2025, 11:54:32 PM
class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        

        # tranpose along the diagonal 
        for i in range(n):
            for j in range(i):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]
        
        # reverse each row
        for row in matrix:
            row.reverse()

        
