from __future__ import annotations
def element_postion(nums:list[int],t:int)->list[int]:
    l = len(nums)
    c = 0
    indexList = []
    for x in range(l):
        if nums[x]==t:
            indexList.append(x)
            c+=1
        else:
            continue
    if c==0:
        indexList.append(-1)
        indexList.append(-1)
    
    return indexList