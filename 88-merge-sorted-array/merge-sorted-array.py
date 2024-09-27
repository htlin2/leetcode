class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        last_idx = m + n - 1
        m -= 1
        n -= 1
        while 0 <= m and 0 <= n:
            if nums1[m] <= nums2[n]:
                nums1[last_idx] = nums2[n]
                n -= 1
            else:
                nums1[last_idx] = nums1[m]
                m -= 1
            last_idx -= 1
        if n >= 0:
            nums1[:n + 1] = nums2[:n + 1]