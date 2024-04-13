n = int(input())

act_dict = {}

for i in range(n) :
    movie , ac1 , ac2 = input().split(",") 
    movie , ac1 , ac2 = movie.strip() , ac1.strip() , ac2.strip()
    if ac1 not in act_dict :
        act_dict[ac1] = []
    if ac2 not in act_dict :
        act_dict[ac2] = []
    act_dict[ac1].append(movie)
    act_dict[ac2].append(movie)

actors = [e.strip() for e in input().split(",")]

for a in actors :
    if a in act_dict :
        print(a,"->",", ".join(act_dict[a]))
    else :
        print(a,"->","Not found")