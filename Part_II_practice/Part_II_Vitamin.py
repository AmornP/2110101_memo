# everything is in the problem statement (read it carefully !)
def show_(vit_chart : dict) :
    for k,v in vit_chart.items() :
        print(f"{k} {' '.join([str(j) for j in v])}")

def get_(vit_chart : dict , command : str) :
    query = command.split()[-1]
    if query in vit_chart :
        print(f"{query} {' '.join([str(j) for j in vit_chart[query]])}")
    else :
        print(f"{query} not found")

def avg_(vit_chart : dict , command : str) :
    query = int(command.split()[-1])
    ret = [v[query-1] for k,v in vit_chart.items()]
    print(round(sum(ret)/len(ret),4))

def max_(vit_chart : dict, command : str) :
    query = int(command.split()[-1])
    comparer = [[-1*v[query-1],k,v] for k,v in vit_chart.items()]
    comparer.sort()
    print(comparer[0][1],comparer[0][0] * -1)

def sort_(vit_chart : dict,command : str) :
    query = int(command.split()[-1])
    comparer = [[v[query-1],k,v] for k,v in vit_chart.items()]
    comparer.sort()
    print(" ".join([x[1] for x in comparer]))

# input
n = int(input())
vit_chart = {}
for i in range(n) :
    x = input().split()
    fruit = x[0]
    vitamins = [float(j) for j in x[1:]]
    vit_chart[fruit] = vitamins
command = input().split()
if command[0] == "get" :
    command = " ".join(command)
    get_(vit_chart,command)
elif command[0] == "show" :
    command = " ".join(command)
    show_(vit_chart)
elif command[0] == "avg" :
    command = " ".join(command)
    avg_(vit_chart,command)
elif command[0] == "max" :
    command = " ".join(command)
    max_(vit_chart,command)
elif command[0] == "sort" :
    command = " ".join(command)
    sort_(vit_chart,command)