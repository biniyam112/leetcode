class Solution:
    def intToRoman(self, num: int) -> str:
        thousands, num = divmod(num, 1000)
        hundreds, num = divmod(num, 100)
        tens, ones = divmod(num, 10)
        td = ["", "M", "MM","MMM"]
        hd = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        ed = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        od = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]
        
        return td[thousands] + hd[hundreds] + ed[tens] + od[ones]
    
