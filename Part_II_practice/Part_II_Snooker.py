payload = []

def cal_score(payload : list[any]) :
    player_score = {"1" : 0 , "2" : 0}
    score_ = {"R" : 1 , "Y" : 2 , "G" : 3 , "W" : 4, "B" : 5 , "P" : 6 , "K" : 7 , "X" : 0}
    for x in payload :
        player_score[x[0]] += sum([score_[g] for g in x[1:]])
    return player_score

while True :

    hit = input()
    payload.append(hit)
    if len(hit) == 2 and hit[-1] == "K" :
        break

ret_ = cal_score(payload)

print(ret_["1"],ret_["2"])
if ret_["1"] == ret_["2"] :
    print("Tie")
elif ret_["1"] < ret_["2"] :
    print("Player 2 wins")
else :
    print("Player 1 wins")
