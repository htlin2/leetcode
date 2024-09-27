class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        def flip(n):
            reverse_arr = arr[:n + 1][::-1]
            arr[:n + 1] = reverse_arr
        res = []
        end_idx = len(arr) - 1
        while True:
            if end_idx == 0:
                return res
            max_num = max(arr[:end_idx + 1])
            max_idx = arr.index(max_num)
            if max_idx == end_idx:
                end_idx -= 1
                continue
            flip(max_idx)
            res.append(max_idx + 1)
            flip(end_idx)
            res.append(end_idx + 1)
            end_idx -= 1

"""
Input: arr = [3,2,4,1]
Output: [4,2,4,3]
[3,2,4,1] k = 3
     i
[4,2,3,1]
[1,3,2,4] k = 1
   i
[3,1,2,4]
[2,1,3,4] k =1
[1,2,3,4]

"""