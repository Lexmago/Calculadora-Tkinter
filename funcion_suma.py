import re

def suma(entry):
    op = entry
    nums = re.findall(r'\d+',op)
    nums = [int(num) for num in nums]
    suma = sum(nums)
    return suma


#suma('2+2')