class Solution:
    def numberToWords(self, num: int) -> str:
        NUM_MAP = {
            0: "Zero",
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
        if num <= 20:
            return NUM_MAP[num]
        if num < 100:
            res = []
            tenth_str = NUM_MAP[num // 10 * 10]
            res.append(tenth_str)
            if num % 10:
                digit_str = NUM_MAP[num % 10]
                res.append(digit_str)
            return ' '.join(res)
        if num < 1000:
            res = []
            before = self.numberToWords(num // 100)
            res.extend([before, NUM_MAP[100]])
            if num % 100:
                after = self.numberToWords(num % 100)
                res.append(after)
            return ' '.join(res)
        if num < 1000000:
            res = []
            before = self.numberToWords(num // 1000)
            res.extend([before, NUM_MAP[1000]])
            if num % 1000:
                after = self.numberToWords(num % 1000)
                res.append(after)
            return ' '.join(res)
        if num < 1000000000:
            res = []
            before = self.numberToWords(num // 1000000)
            res.extend([before, NUM_MAP[1000000]])
            if num % 1000000:
                after = self.numberToWords(num % 1000000)
                res.append(after)
            return ' '.join(res)
        else:
            res = []
            before = self.numberToWords(num // 1000000000)
            res.extend([before, NUM_MAP[1000000000]])
            if num % 1000000000:
                after = self.numberToWords(num % 1000000000)
                res.append(after)
            return ' '.join(res)
        