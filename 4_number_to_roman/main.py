"""
เขียบนโปรแกรมแปลงตัวเลยเป็นตัวเลข roman

[Input]
number: list of numbers

[Output]
roman_text: roman number

[Example 1]
input = 101
output = CI

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_roman(self, number: int) -> str:
        def number_to_roman(num):
        if num <= 0:
            return "number can not less than 0"
 
        num_map = [(1000, 'M'), (900, 'CM'), (500, 'D'), (400, 'CD'), (100, 'C'), (90, 'XC'),
                   (50, 'L'), (40, 'XL'), (10, 'X'), (9, 'IX'), (5, 'V'), (4, 'IV'), (1, 'I')]
 
        roman_num = ''
        i = 0
        while num > 0:
            for _ in range(num // num_map[i][0]):
                roman_num += num_map[i][1]
                num -= num_map[i][0]
            i += 1
        return roman_num