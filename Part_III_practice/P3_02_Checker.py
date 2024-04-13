# don't forget that our row can only have one character

def findColor(row , col) :
    r = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'.find(row)
    if r%2 == int(col)%2 :
        return "Black"
    else:
        return "White"
    

def checker(row,column) :
    isValidrow = True
    isValidColumn = True
    if len(row) == 0 :
        isValidrow = False
    if len(column) == 0 :
        isValidColumn = False 
    if len(row) > 1 :
        isValidrow = False
    if row not in 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ' :
        isValidrow = False
    if not column.isnumeric() :
        isValidColumn = False
    elif int(column) > 52 or int(column) < 1:
        isValidColumn = False
    if not isValidrow and not isValidColumn :
        print("Invalid row and column")
    elif not isValidColumn and isValidrow :
        print("Invalid column")
    elif isValidColumn and not isValidrow :
        print("Invalid row")
    else :
        print(findColor(row,column))

command = input().strip()
row = None
column = None
if "row" not in command : # type 1
    row = command[0]
    column = command[1:].strip()
else :
    payload = command.split(",")
    if "row" in payload[0] :
        row = payload[0].split("=")[-1].strip()
        column = payload[1].split("=")[-1].strip()
    else :
        row = payload[1].split("=")[-1].strip()
        column = payload[0].split("=")[-1].strip()

checker(row,column)