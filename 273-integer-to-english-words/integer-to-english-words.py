class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0: return "Zero"
        hashmap = {
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
            90: "Ninety"
            # 100: "Hundred",
            # 1000: "Thousand",
            # 1000000: "Million",
            # 1000000000: "Billion"
        }
        res = []
        def dfs(num):
            if num in hashmap:
                res.append(hashmap[num])
            elif num < 100:
                res.append(dfs(num // 10 * 10))
                res.append(dfs(num % 10))
            elif num < 1000:
                res.append(dfs(num // 100))
                res.append('Hundred')
                res.append(dfs(num % 100))
            elif num < 1000000:
                res.append(dfs(num // 1000))
                res.append('Thousand')
                res.append(dfs(num % 1000))
            elif num < 1000000000:
                res.append(dfs(num // 1000000))
                res.append('Million')
                res.append(dfs(num % 1000000))
            else:
                res.append(dfs(num // 1000000000))
                res.append('Billion')
                res.append(dfs(num % 1000000000))
        dfs(num)
        res = [r for r in res if r]
        return ' '.join(res)