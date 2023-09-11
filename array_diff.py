from typing import List


def array_diff(a: List[int], b: List[int]) -> List[int]:
    b_set = set(b)
    result = [x for x in a if x not in b_set]
    return result


a = [2, 2, 1, 3]
b = [1, 2]

print(array_diff(a=a, b=b))
