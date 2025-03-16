from __future__ import annotations
def filter_strings(lst: list[str],k:int,m:int)->list[str]:

    stringCount = len(lst)
    newList = []
    listVowel = ['a','e','i','o','u']
    vowelCount = len(listVowel)

    for x in lst:
        sc = len(x)
        if sc>=k:
            c=0
            for y in x:
                for z in range(vowelCount):
                    q = listVowel[z]
                    if y==q:
                        c=c+1
                    else:
                        continue
            if c>=m:
                newList.append(x)
    return newList