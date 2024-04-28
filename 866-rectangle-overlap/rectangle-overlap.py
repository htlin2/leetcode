class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        max_x = max(x1, x3)
        min_x = min(x2, x4)
        max_y = max(y1, y3)
        min_y = min(y2, y4)
        if min_x - max_x <= 0 or min_y - max_y <= 0: return False
        return True