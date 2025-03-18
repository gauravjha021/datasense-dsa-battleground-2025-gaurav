from __future__ import annotations

def min_size_sub_array_sum(nums:list[int],t:int)->str:
    l  = len(nums)
    sum = ""
    all_sub_array = []
    final_sub_array = []
    we = ""
    
    for x in range(l):
        sum = 0
        for y in range(x,l):
                sum = sum + nums[y]
                if sum >=t:
                    all_sub_array.append(nums[x:y+1])
                else:
                    continue
    
    if len(all_sub_array)==0:
        final_sub_array.append(None)
        final_sub_array.append(None)
        we = 0
    else:
        f = len(all_sub_array)            
        for z in range(0,f-1):
            if len(all_sub_array[z])>=len(all_sub_array[z+1]):
                we = len(all_sub_array[z+1])
                final_sub_array.clear()
                final_sub_array=all_sub_array[z+1].copy()
    return f"Subarray : {final_sub_array}\nLength : {we}"