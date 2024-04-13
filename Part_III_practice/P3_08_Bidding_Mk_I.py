# don't forget to clear the bids before assigning new one
# it's pitfall that we didn't remember that if there's no 
# withdrawal and it's like [123,1,P1] , [120,5,P1] the first one
# will be considered as a biggest one which is not true because
# at time t = 5 he changed his bids to 120 which is not the maximum

# Further Thinking : How can we improve this procedure ? 
# how about using dict of user name ? and let the rest be the backend on calc bidding result ?

def calc_bidding_result(shop,users) :
    user_bag = {u:{"price" : 0 , "items" : []} for u in users}
    for itm,bids in shop.items() :
        if len(bids) :
            price , idx , user = sorted(bids,key=lambda x : [-1*x[0],x[1]])[0]
            user_bag[user]["price"] += price
            user_bag[user]["items"].append(itm)
    return sorted(user_bag.items(),key=lambda x : x[0])

n = int(input())
shop = {}
users = set()
for i in range(n) :
    payload = input().split()
    if payload[0] == "B" :
        command , user , item , price = payload
        users.add(user)
        if item not in shop :
            shop[item] = []
        bids = [x for x in shop[item] if user not in x]
        shop[item] = bids
        shop[item].append([int(price),i, user])
    elif payload[0] == "W" :
        command , user , item = payload
        bids = [x for x in shop[item] if user not in x]
        shop[item] = bids
    else :
        pass

for u , payload in calc_bidding_result(shop,users) :
    if payload["price"] == 0 :
        print(u + ":","$" + str(payload["price"]))
    else :
        print(u + ":","$" + str(payload["price"]),"->"," ".join(sorted(payload["items"])))