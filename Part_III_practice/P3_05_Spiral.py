def iterate_spiral_square(x,y,n,payload,k,r,u,d,l) :
    while y != n or x != n :
        if r :
            payload[y][x] = k
            if payload[y-1][x] == 0 :
                y -=1
                r,u,d,l = False , True , False , False
            else :
                x += 1
                r,u,d,l = True , False , False , False
        elif l :
            payload[y][x] = k 
            if payload[y+1][x] == 0 :
                y += 1
                r,u,d,l = False , False , True , False
            else :
                x -= 1
                r,u,d,l = False , False , False , True
        elif d :
            payload[y][x] = k
            if payload[y][x+1] == 0 :
                x += 1
                r,u,d,l = True , False , False , False
            else :
                y += 1
                r,u,d,l = False , False , True , False

        elif u :
            payload[y][x] = k
            if payload[y][x-1] == 0 :
                x-=1
                r,u,d,l = False , False , False , True
            else :
                y -= 1 
                r,u,d,l = False , True , False , False
        k += 1
    payload[y][x] = k
    return payload
  
    


def spiral_square(n): # n is a positive odd number
    if n == 1 :
        return [[1]]
    payload = [[0 for x in range(n+2)] for x in range(n+2)]
    x , y = (n+2)//2, (n+2)//2
    payload[y][x] = 1
    payload = iterate_spiral_square(x+1,y,n,payload,2,True,False,False,False)
    return [x[1:-1] for x in payload][1:-1]

def print_square(S):
 # เรยีกใชฟ้ ังกช์ นั นเี้พอื่ แสดงคา่ ของ S ที่เป็นลิสต์ของลิสต์ของจ านวนเต็ม
 for i in range(len(S)):
    print(' '.join([(2*' '+str(e))[-3:] for e in S[i]]))

exec(input().strip()) 