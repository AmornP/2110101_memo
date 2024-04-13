def printRuler(k : int) :
    n = k // 10
    r = k % 10
    ret = ""
    for i in range(1,n+1) :
        dash_count = 10 - len(str(i))
        ret += "-" * dash_count + str(i)
    ret += "-" * r
    print(ret)

fn = input().strip()
k = int(input())
fp = open(fn,"r",encoding="utf-8")
printRuler(k)
payload = [y for x in [x.strip().split(".") for x in fp.readlines()] for y in x ]
t = ""
for p in payload :
    t += "." + p
    if len(t.strip(".")) > k :
        t = t[:-1*(len(p)+1)]
        print(t.strip("."))
        t = ""
        if len(p) > k :
            print(p.strip("."))
        else :
            t += "." + p
if len(t) : print(t.strip("."))
fp.close()