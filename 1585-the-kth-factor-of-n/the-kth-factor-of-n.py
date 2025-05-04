class Solution:
    def kthFactor(self, n: int, k: int) -> int:
        front, back = [], []
        for i in range(1, int(sqrt(n)) + 1):
            if n % i == 0:
                front.append(i)
                back.append(n // i)
        
        if front[-1] == back[-1]:
            back.pop()
        
        res = front + back[::-1]
        return res[k - 1] if k - 1 < len(res) else -1