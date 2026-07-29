class Solution:
    def numberToWords(self, num: int) -> str:
        if not num: return 'Zero'
        number_to_letters = {
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
        }
        res = []
        def dfs(num):
            if not num: return
            if num in number_to_letters:
                res.append(number_to_letters[num])
                return
            elif num < 100:
                digit = num % 10
                tenth = num // 10 * 10
                res.append(number_to_letters[tenth])
                res.append(number_to_letters[digit])
                return 
            elif num < 1000:
                digit = num // 100
                res.append(number_to_letters[digit])
                res.append('Hundred')
                dfs(num % 100)
            elif num < 1000000:
                # handled hundreds
                dfs(num // 1000)
                res.append('Thousand')
                # handled rest
                dfs(num % 1000)
            elif num < 1000000000:
                dfs(num // 1000000)
                res.append('Million')
                dfs(num % 1000000)
            else:
                dfs(num // 1000000000)
                res.append('Billion')
                dfs(num % 1000000000)
        dfs(num)
        return ' '.join(res)