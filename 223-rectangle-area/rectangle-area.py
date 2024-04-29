class Solution:
    def cal_area(self, x1, x2, y1, y2):
        return (x2 - x1) * (y2 - y1)

    def computeArea(self, ax1: int, ay1: int, ax2: int, ay2: int, bx1: int, by1: int, bx2: int, by2: int) -> int:
        x1 = max(ax1, bx1)
        x2 = min(ax2, bx2)
        y1 = max(ay1, by1)
        y2 = min(ay2, by2)
        is_overlap = x2 - x1 > 0 and y2 - y1 > 0
        if is_overlap:
            intersection = self.cal_area(x1, x2, y1, y2)
        else:
            intersection = 0
        a_area = self.cal_area(ax1, ax2, ay1, ay2)
        b_area = self.cal_area(bx1, bx2, by1, by2)
        return a_area + b_area - intersection