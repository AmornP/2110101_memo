# beware of the spacing

a = input()
b = input()

def counter(t : str) :
    t = sorted(t.lower())
    t = "".join([x for x in t if x in "abcdefghijklmnopqrstuvwxyz"])
    payload = {}
    for x in t :
        if x in payload : 
            payload[x] += 1
        else :
            payload[x] = 1
    return payload

def keys_padding(a : dict , b : dict) :
    keys = list(a.keys()) + list(b.keys())
    for k in keys :
        if k not in a :
            a[k] = 0
        if k not in b :
            b[k] = 0

counter_a = counter(a)
counter_b = counter(b)
keys_padding(counter_a,counter_b)
counter_a , counter_b = dict(sorted(counter_a.items())) , dict(sorted(counter_b.items()))
remove_from_a = {}
remove_from_b = {}

for x in counter_a.keys() :

    if counter_a[x] == counter_b[x] :
        pass
    elif counter_a[x] > counter_b[x] :
        remove_from_a[x] = counter_a[x] - counter_b[x]
    elif counter_b[x] > counter_a[x] :
        remove_from_b[x] = counter_b[x] - counter_a[x]

print(a)
if len(remove_from_a) == 0 :
    print(" - None")
else :
    for k , v in remove_from_a.items() :
        print(f" - remove {v} {k}",end="")
        print("\'s" if v > 1 else "")

print(b)
if len(remove_from_b) == 0 :
    print(" - None")
else :
    for k , v in remove_from_b.items() :
        print(f" - remove {v} {k}",end="")
        print("\'s" if v > 1 else "")


