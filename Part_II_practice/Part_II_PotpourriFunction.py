def convex_polygon_area(p):
    p.append(p[0])
    upper_part = 0
    for i in range(len(p)-1) :
        upper_part += p[i][0] * p[i+1][1]
    lower_part = 0
    for i in range(len(p)-1) :
        lower_part += p[i][1] * p[i+1][0]
    return abs(0.5 * (upper_part-lower_part))

def is_heterogram(s):
    k = sorted(s.lower())
    charlist = "abcdefghijklmnopqrstuvwxyz"
    prev = k[0]
    for x in k[1:] :
        if x == prev and x in charlist:
            return False
        prev = x
    return True
        
def replace_ignorecase(s, a, b):
    pattern_length = len(a)
    curr_idx = 0
    payload = ""
    while curr_idx < len(s) :
        if s[curr_idx:curr_idx+pattern_length].lower() == a.lower() :
            payload += b
            curr_idx += pattern_length
        else :
            payload += s[curr_idx]
            curr_idx += 1
    return payload
        
def top3(votes):
    payload = [[-1*v,k] for k,v in votes.items()]
    payload.sort()
    payload = [x[1] for x in payload]
    return payload[:3]


# ต้องมีคำสั่งข้ำงล่ำงนี้ ตอนส่งให้ Grader ตรวจ
for k in range(2):
    exec(input().strip())
