def longest_substring(word:str)->str:
    list_chars = []
    set_chars = set()
    unique_chars = []
    temp_collect = []
    temp_length = 1
    false_collect = []
    l = len(word)
    indicator = ""
    large_subs_str =""
    
    for x in word:
        list_chars.append(x)
    set_chars.update(list_chars)
    
    for y in set_chars:
        unique_chars.append(y)
    
    for a in range(l):
        for b in range(l):
            indicator = True
            c = word[a:b+1]
    
            if c!="":
                for z in unique_chars:
                    char_count = c.count(z)
                    if char_count>=2:
                        indicator = False
                    else:
                        continue
                   
                if indicator==True:
                    temp_collect.append(c)
                else:
                    false_collect.append(c)
            else:
                continue
    
    for s in temp_collect:
        if temp_length<len(s):
            temp_length=len(s)
            large_subs_str = s
        else:
            continue
    txt = f"Substring : {large_subs_str}\nLength : {temp_length}"
    return txt
