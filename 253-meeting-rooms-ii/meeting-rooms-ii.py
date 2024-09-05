class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        rooms = []
        for start, end in intervals:
            rooms.append([start, 1])
            rooms.append([end, -1])
        rooms.sort(key=lambda x: [x[0], x[1]])
        res = 0
        curr = 0
        for _, startEnd in rooms:
            curr += startEnd
            res = max(res, curr)
        return res