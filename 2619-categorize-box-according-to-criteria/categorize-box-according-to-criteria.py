class Solution:
    def categorizeBox(self, length: int, width: int, height: int, mass: int) -> str:
        volume = length * width * height
        is_bulky = False
        for n in [length, width, height, mass]:
            if n >= math.pow(10, 4) or volume >= 10 ** 9:
                is_bulky = True

        is_heavy = True if mass >= 100 else False
        if is_bulky and is_heavy:
            return 'Both'
        if not is_bulky and not is_heavy:
            return 'Neither'
        return 'Bulky' if is_bulky else 'Heavy'
"""
volume = length * width * height 
bulky
    dimension >= 10^4
    volume >= 10^9
heavy
    mass >= 100
both
    bulky + heavy
neither
    not bulky and not heavy
"""