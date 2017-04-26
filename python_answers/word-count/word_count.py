def word_count(x):
    words = x.split()
    occur = {}
    for word in words:
        word = word.lower()
        if word in occur:
            occur[word]+=1
        else:
            occur[word]=1
    return occur

