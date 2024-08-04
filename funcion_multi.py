import re
from functools import reduce
import operator

def multi(entry):
    op = entry
    nums = re.findall(r'\d+',op)
    nums = [int(num) for num in nums]

    if not nums:
        return 0 # Evita bugs
    
    r = reduce(operator.mul, nums, 1)
    return r


    
