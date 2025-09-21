class Solution:
    def numberToWords(self, num: int) -> str:
        hashmap = {
            0: 'Zero',
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
        if num in hashmap:
            return hashmap[num]
        elif num < 100:
            tenth = num // 10 * 10
            digits = num % 10
            res.append(self.numberToWords(tenth))
            if digits:
                res.append(self.numberToWords(digits))
        elif num < 1000:
            hundred = num // 100
            res.append(self.numberToWords(hundred))
            res.append('Hundred')
            if num % 100:
                res.append(self.numberToWords(num % 100))
        elif num < 1000000:
            thousand = num // 1000
            res.append(self.numberToWords(thousand))
            res.append('Thousand')
            if num % 1000:
                res.append(self.numberToWords(num % 1000))
        elif num < 1000000000:
            million = num // 1000000
            res.append(self.numberToWords(million))
            res.append('Million')
            if num % 1000000:
                res.append(self.numberToWords(num % 1000000))
        else:
            billion = num // 1000000000
            res.append(self.numberToWords(billion))
            res.append('Billion')
            if num % 1000000000:
                res.append(self.numberToWords(num % 1000000000))
        return ' '.join(res).strip()