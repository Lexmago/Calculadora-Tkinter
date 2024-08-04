import re
from functools import reduce

def div(entry):
    op = entry
    nums = re.findall(r'\d+',op)
    nums = [int(num) for num in nums]

    if not nums:
        return 0 # Evita bugs
    
    r = reduce(lambda x, y: x / y, nums)
    return r