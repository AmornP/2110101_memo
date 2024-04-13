def printIndexer(n : int , k : int) :
    dash_count = n + 1
    text = ""
    for i in range(1,k+1) :
        text += str(i)
        if i == k :
            dash_count -= 1
            text += (dash_count - len(str(i))) * "-"
        else :
            text += (dash_count - len(str(i))) * "-"
    return text
            
def g_code_gen(n : int) :
    starter = ['0','1']
    for i in range(n-1) :
        l = ["0" + x for x in starter]
        r = ["1" + x for x in starter[::-1]]
        starter = l+r
    return starter

n = int(input())
k = int(input())

if (n < 1 or n > 15) and (k < 1 or k > 100) :
    print("Invalid n and k")
elif n < 1 or n > 15 :
    print("Invalid n")
elif k < 1 or k > 100 :
    print("Invalid k")
else :
    num_range = [str(x) for x in list(range(1,k))]
    print(printIndexer(n,k))
    codes = g_code_gen(n)
    payload = []
    i = 1
    temp_payload = []
    for c in codes:
        temp_payload.append(c)
        i += 1
        if i == k + 1 :
            payload.append(temp_payload)
            temp_payload = []
            i = 1
    if len(temp_payload) : payload.append(temp_payload)
    for x in payload :
        print(",".join(x))



