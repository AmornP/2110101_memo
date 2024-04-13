def lstrip(x : list) :
    padder = 0
    isBreak = False
    for j in range(len(x[0])) :
        for i in range(len(x)) :
            if x[i][j] != "." :
                isBreak = True
                break
        if isBreak : break
        padder += 1
    return [k[padder:] for k in x]

def rstrip(x : list) :
    padder = len(x[0])
    isBreak = False
    for j in range(len(x[0])-1,-1,-1) :
        for i in range(len(x)) :
            if x[i][j] != "." :
                isBreak = True
                break
        if isBreak : break
        padder -= 1
    return [k[:padder] for k in x]

def strip_pos(x : list) :
    pos = []
    isBreak = False
    for j in range(len(x[0])) :
        for i in range(len(x)) :
            if x[i][j] != "." :
                isBreak = True
                break
        if isBreak :
            isBreak = False
            continue
        pos.append(j)
    return pos
def reconstruct(x : list , strip_pos : list) :
    payload = ['' for x in range(len(x))]
    for i in range(len(x)) :
        for j in range(len(x[0])) :
            if j in strip_pos :
                continue
            payload[i] += x[i][j]
    return payload

fn = input().strip()
fp = open(fn,"r",encoding="utf-8")
command = input().strip()
x = [x.strip("\n") for x in fp.readlines()]
if command == "LSTRIP" :
    print("\n".join(lstrip(x)))
elif command == "RSTRIP" :
    print("\n".join(rstrip(x)))
elif command == "STRIP" :
    print("\n".join(rstrip(lstrip(x))))
elif command == "STRIP_ALL" :
    print("\n".join(reconstruct(x,strip_pos(x))))
else :
    print("Invalid command")


fp.close()