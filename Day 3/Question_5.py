from __future__ import annotations
def product_except_self(nums:list[int])->list[int]:
    l = len(nums)
    p_list = []
    for x in range(l):
        p = 1
        for y in range(l):
            if nums[x]!=nums[y]:
                p=p*nums[y]
            else:
                continue
        p_list.append(p)
    return p_list