class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows, cols = len(matrix), len(matrix[0])
        top, bot = 0, rows - 1

        while top <= bot:
            curr_row = (top + bot) // 2
            if target < matrix[curr_row][0]:
                bot = curr_row - 1
            elif target > matrix[curr_row][-1]:
                top = curr_row + 1
            else:
                break
        
        if top > bot:
            return False
        
        row = (top + bot) // 2
        l, r = 0, cols - 1
        
        while l <= r:
            mid = (l + r) // 2
            if target < matrix[row][mid]:
                r = mid - 1
            elif target > matrix[row][mid]:
                l = mid + 1
            else:
                return True
        
        return False
