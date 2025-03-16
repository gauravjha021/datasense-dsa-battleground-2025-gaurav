from __future__ import annotations
def sort_by_tupple_sum(lst:list[tupple])->list[tupple]:

    originalSum = []
    sortedSum   = []
    listTuple2  = []
    listCount = len(lst)

    for z in lst:
        y=0
        for x in z:
            y=y+x;
        originalSum.append(y)
    sortedSum = originalSum.copy()
    sortedSum.sort()

    for z in range(listCount):
        v = sortedSum[z]
        for a in range(listCount):
            t = originalSum[a]
            if v==t:
                q = lst[a]
                if q not in listTuple2:
                    listTuple2.append(q)
                
            else:
                continue
    return listTuple2