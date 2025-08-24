# Last updated: 8/23/2025, 11:36:38 PM
class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        border_top = 0
        border_bottom = len(matrix) - 1
        border_left = 0
        border_right = len(matrix[0]) - 1

        result = []

        while (border_top <= border_bottom
        and border_left <= border_right):
            
            for c in range(border_left, border_right+1):
                result.append(matrix[border_top][c])
            border_top += 1

            for r in range(border_top, border_bottom+1):
                result.append(matrix[r][border_right])
            border_right -= 1
            
            if (border_top <= border_bottom):
                for c in range(border_right, border_left-1, -1):
                    result.append(matrix[border_bottom][c])
                border_bottom -= 1
            
            if (border_left <= border_right):
                for r in range(border_bottom, border_top-1, -1):
                    result.append(matrix[r][border_left])
                border_left += 1

        return result


        