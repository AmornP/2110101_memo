# longest pattern matching

def patternMatch(data , pattern) :
    
    dataLen = len(data)
    patternLen = len(pattern)
    i = patternLen
    counter = 0
    isMatched = False
    
    while i < dataLen + 1 :
        
        if data[i-patternLen:i] == pattern :
            counter += 1
            isMatched = True
            i += patternLen

        else :
            if isMatched and counter < 2 :
                counter = 0
                isMatched = False
            
            else :
                break
        
            i += 1
    
    if counter < 2 :
        counter = 0

    return counter


if __name__ == "__main__" :
    pattern = input()
    n = int(input())

    for x in range(n) :
        t = input()
        print(patternMatch(t,pattern))
