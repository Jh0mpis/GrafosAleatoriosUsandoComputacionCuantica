def ROT(n,word):
    newWord=""
    lowerAbecedary = "abcdefghijklmnopqrstuvwxyz"
    upperAbecedary = lowerAbecedary.upper()
    for i in word:
        if( i==i.upper()):
            index = upperAbecedary.index(i)
            newWord += upperAbecedary[(index+n)%len(upperAbecedary)]
        else:
            index = lowerAbecedary.index(i)
            newWord += lowerAbecedary[(index+n)%len(upperAbecedary)]
    return newWord