cardlist = "A23456789TJQK"
facelist = "CDHS"
        
x = input()
checker = [x[i-2:i] for i in range(2,len(x)+1,2)]
for i in range(1,len(checker)) :
    if checker[i-1][0] == checker[i][0] :
        ret = (facelist.index(checker[i-1][1]) + 1) - (facelist.index(checker[i][1]) + 1)
    else :
        ret = (cardlist.index(checker[i-1][0]) + 1) - (cardlist.index(checker[i][0]) + 1)
    
    if ret > 0 :
        ret = "+" + str(ret)
    print(ret,end="")
        
