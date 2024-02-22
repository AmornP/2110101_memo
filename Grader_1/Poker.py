# =================== Winning Type ==================== #
# flush - same face x5
# straight - consecutive number
# royal straight flush - Royal + flush + straight
# straight flush - flush + straight
# ===================================================== #

# ====================== Faces ======================== #
# D
# H
# S
# C
# ===================================================== #

def pokerType(data) :
    data = [list(x) for x in data[1:-1].split("|")]
    isRoyal = RoyalCheck(data)
    isConsqCheck = ConsqCheck(data)
    isSameFace = FaceCheck(data)

    if isConsqCheck and isSameFace :
        if isRoyal :
            return "Royal Straight Flush"
        else :
            return "Straight Flush"
    elif isConsqCheck and not isSameFace :
        return "Straight"
    elif isSameFace and not isConsqCheck :
        return "Flush"
    else :
        return "None"
    
def RoyalCheck(data) :
    
    temp = "".join(x[0] for x in data)
    if temp == "AKQJX" :
        return True
    return False

def ConsqCheck(data) :
    
    card_list = list("AKQJX987654321A")
    curr_idx = -1
    
    for x in data :
        if curr_idx == -1 :
            curr_idx = card_list.index(x[0])
        else :
            curr_idx += 1
        if x[0] != card_list[curr_idx] :
            return False
    
    return True

def FaceCheck(data) :
    temp = "".join([x[1] for x in data])
    pf = temp[0]
    for x in temp : 
        if x != pf :
            return False
    return True

if __name__ == "__main__" :
    n = int(input())
    for i in range(n) :
        temp = input()
        print(pokerType(temp))