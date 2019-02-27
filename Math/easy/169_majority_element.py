

def majority_element_memo(nums: list) -> int:
    d = dict()

    for x in nums:
        if not d.get(x):
            d[x] = 0
        d[x] += 1
    return max(d, key=d.get)


def majority_element(nums: list) -> int:
    c = t = 0

    for x in nums:
        if c < 1:
            t = x
            c = 1
        elif t != x:
            c -= 1
        else:
            c += 1
    return t

