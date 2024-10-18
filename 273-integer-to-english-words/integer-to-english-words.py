class Solution:
    def __init__(self):
        self.hashmap = {
            0: "",
            1: "One",
            2: "Two",
            3: "Three",
            4: "Four",
            5: "Five",
            6: "Six",
            7: "Seven",
            8: "Eight",
            9: "Nine",
            10: "Ten",
            11: "Eleven",
            12: "Twelve",
            13: "Thirteen",
            14: "Fourteen",
            15: "Fifteen",
            16: "Sixteen",
            17: "Seventeen",
            18: "Eighteen",
            19: "Nineteen",
            20: "Twenty",
            30: "Thirty",
            40: "Forty",
            50: "Fifty",
            60: "Sixty",
            70: "Seventy",
            80: "Eighty",
            90: "Ninety",
            100: "Hundred",
            1000: "Thousand",
            1000000: "Million",
            1000000000: "Billion"
        }
    def numberToWords(self, num: int) -> str:
        if not num: return 'Zero'
        def dfs(num):
            if num <= 20:
                return self.hashmap[num]
            elif num < 100:
                res = []
                tenth = self.hashmap[num // 10 * 10] # 95 // 10 -> 9
                res.append(tenth)
                rem = dfs(num % 10) # 95 % 10 -> 5
                if rem:
                    res.append(rem)
                return ' '.join(res)
            elif num < 1000:
                res = [] # 932
                res.append(dfs(num // 100))
                res.append('Hundred')
                rem = dfs(num % 100) # 32 -> Thirty Two
                if rem:
                    res.append(rem)
                return ' '.join(res)
            elif num < 1000000:
                res = [] # 1234
                thousand = dfs(num // 1000)
                res.append(thousand)
                res.append('Thousand')
                rem = dfs(num % 1000) # 234 -> Two hundred thirty Four
                if rem:
                    res.append(rem)
                return ' '.join(res)
            elif num < 1000000000:
                res = []
                res.append(dfs(num // 1000000))
                res.append('Million')
                rem = dfs(num % 1000000)
                if rem:
                    res.append(rem)
                return ' '.join(res)
            else:
                res = []
                res.append(dfs(num // 1000000000))
                res.append('Billion')
                rem = dfs(num % 1000000000)
                if rem:
                    res.append(rem)
                return ' '.join(res)
        return dfs(num)