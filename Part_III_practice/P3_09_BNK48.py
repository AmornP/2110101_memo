# Don't forget that there is a case where idol has 0 ota marking as kamioshi 
# so we must include everyone name in this function
mode = None
ota_count = {}
oshi_score = {}
vote_record = {}

def top_by_total_vote(oshi_score : dict) :
    return [x[0] for x in sorted(oshi_score.items() , key = lambda x : [-1*x[1],x[0]])][:3]
def top_by_ota_count(ota_count : dict) :
    return [x[0] for x in sorted(ota_count.items(),key=lambda x : [-1*len(x[1]),x[0]])][:3]
def top_by_kamioshi(vote_record : dict,oshi_score : dict) :
    payload = {k:0 for k,v in oshi_score.items()}
    for k,v in vote_record.items() :
        x = sorted(v.items(),key=lambda x : [-1*x[1],x[0]])[0][0]
        if x not in payload :
            payload[x] = 0
        payload[x] += 1
    return [x[0] for x in sorted(payload.items() , key = lambda x : [-1*x[1],x[0]])][:3]
while True :
    payload = input().split()
    if len(payload) == 1 :
        mode = payload[0]
        break
    else :
        ota , oshi , vote = payload
        if oshi not in ota_count :
            ota_count[oshi] = set()
        ota_count[oshi].add(ota)
        if oshi not in oshi_score :
            oshi_score[oshi] = 0
        oshi_score[oshi] += int(vote)
        if ota not in vote_record :
            vote_record[ota] = {}
        if oshi not in vote_record[ota] :
            vote_record[ota][oshi] = 0
        vote_record[ota][oshi] += int(vote)

if mode == "1" :
    print(", ".join(top_by_total_vote(oshi_score)))
elif mode == "2" :
    print(", ".join(top_by_ota_count(ota_count)))
else :
    print(", ".join(top_by_kamioshi(vote_record,oshi_score)))
