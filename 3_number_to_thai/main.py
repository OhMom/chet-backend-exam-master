"""
เขียบนโปรแกรมแปลงตัวเลยเป็นคำอ่านภาษาไทย

[Input]
number: positive number rang from 0 to 10_000_000

[Output]
num_text: string of thai number call

[Example 1]
input = 101
output = หนึ่งร้อยเอ็ด

[Example 2]
input = -1
output = number can not less than 0
"""


class Solution:

    def number_to_thai(self, number: int) -> str:
        if number < 0:
            return "number cannot be less than 0"
 
        thai_digits = {
            0: "", 1: "หนึ่ง", 2: "สอง", 3: "สาม", 4: "สี่",
            5: "ห้า", 6: "หก", 7: "เจ็ด", 8: "แปด", 9: "เก้า"
        }
        thai_places = ["", "สิบ", "ร้อย", "พัน", "หมื่น", "แสน"]
 
        result = ""
        num_str = str(number)
        for i in range(len(num_str)):
            digit = int(num_str[i])
            place = len(num_str) - i - 1
            if digit != 0:
                if place == 1 and digit == 1:
                    result += "สิบ"
                elif place == 1 and digit == 2:
                    result += "ยี่สิบ"
                elif place == 0 and digit == 1:
                    result += "เอ็ด"
                else:
                    result += thai_digits[digit] + thai_places[place]
 
        return result
