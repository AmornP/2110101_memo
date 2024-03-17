def is_odd(n):
    return n%2 == 1
def has_odds(x):
    return any([is_odd(j) for j in x])
def all_odds(x):
    return all([is_odd(j) for j in x])
def no_odds(x):
    return not has_odds(x)
def get_odds(x):
    return [j for j in x if is_odd(j)]
def zip_odds(a, b):
    
    l1 = get_odds(a)
    l2 = get_odds(b)
    i = 0
    payload = []
    while len(l1) >= 0 and len(l2) >= 0 :
        
        if i%2 == 0 :
            if len(l1) > 0 :
                payload.append(l1.pop(0))
            else :
                payload += l2
                break
        else :
            if len(l2) > 0 :
                payload.append(l2.pop(0))
            else :
                payload += l1
                break
        
        i+=1
        
    return payload
        

exec(input().strip())
