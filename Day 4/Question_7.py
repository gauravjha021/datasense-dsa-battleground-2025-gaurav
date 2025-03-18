from __future__ import annotations
def diff_highest_lowest(nums:list[int],k:int)->str:
    sorted_nums = sorted(nums,reverse=True)
    return_nums = []
    lenght = len(sorted_nums)
    diff = ""
    c = 0
    
    if k!=2 or lenght<2:
        diff = 0
        return_nums.append(None)
    else:
        for x in range(lenght-1):
            c = c + 1
            for y in range (c,lenght):
                current = sorted_nums[x]-sorted_nums[y]
                if diff == "":
                    diff = current
                    return_nums.clear()
                    return_nums.append(sorted_nums[x])
                    return_nums.append(sorted_nums[y])
                
                elif diff > current:
                    diff = current
                    return_nums.clear()
                    return_nums.append(sorted_nums[x])
                    return_nums.append(sorted_nums[y])
                
    print(f"Numbers: {return_nums}\nDifference: {diff}")