class Solution:
    def isRectangleOverlap(self, rec1: List[int], rec2: List[int]) -> bool:
        x1, y1, x2, y2 = rec1
        x3, y3, x4, y4 = rec2
        ix1 = max(x1, x3)
        ix2 = min(x2, x4)
        iy1 = max(y1, y3)
        iy2 = min(y2, y4)
        if ix2 - ix1 > 0 and iy2 - iy1 > 0: return True
        return False


"""             
        (1, 1)  (2, 1) 
(0, 0)  (1, 0)

"""