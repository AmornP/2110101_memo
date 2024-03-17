# thing to beware (beware of the given pronounciation from AJ)

matcher = {"0" : "soon","1" : "neung" , "2" : "song" , "3" : "sam" , "4" : "si" , "5" : "ha" , "6" : "hok" , "7" : "chet" , "8" : "paet" , "9" : "kao"}
unit = ["","sip","roi","pun"]

def to_Thai( N: int):
    N = str(N)
    payload = []
    for idx,x in enumerate(N,1) :
        if x == "1" and idx == len(N) and len(N) == 1 :
            payload.append(matcher["1"])
        elif x == "1" and idx == len(N) :
            payload.append("et")
        elif x == "1" and idx == len(N)-1 :
            payload.append("sip")
        elif x == "2" and idx == len(N)-1 :
            payload.append("yi")
            payload.append("sip")
        elif x == "0" and idx == len(N) and len(N) == 1 :
            payload.append(matcher["0"])
        elif x != "0" :
            payload.append(matcher[x])
            if unit[len(N)-idx] != "" :
                payload.append(unit[len(N)-idx])
    return " ".join(payload)


exec(input().strip()) # ตอ้ งมคี ำสั่งนี้ ตรงนี้ตอนสง่ ให้Grader ตรวจ
