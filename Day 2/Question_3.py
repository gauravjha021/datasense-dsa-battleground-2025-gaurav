def last_word_length(sentence:str)->int: 
    collection = []
    collection = sentence.split(' ').copy()
    onlyWords = []
    l = len(collection)
    for x in range(l):
        q = collection[x]
        if q !="":
            onlyWords.append(q)
        else:
            continue
    return len(onlyWords[-1])