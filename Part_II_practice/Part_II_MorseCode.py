fn = input().strip()
mode = ""
morse_dict = {}
reverse_morse_dict = {}
mode_list = ["M2T","T2M"]

def extract_morse_dict(t : str) :
    t = t.replace("]","")
    md = {}
    char_list = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ"
    temp = ""
    curr_key = ""
    for idx,x in enumerate(t,1) :
        if x in char_list :
            curr_key = x
            temp = ""
        elif x == "[" and idx != 1 :
            md[curr_key] = temp
        else :
            temp += x
    return md
    

with open(fn,"r") as fp :
    for idx , data in enumerate(fp.readlines(),1) :
        if idx == 1 :
            mode = data.strip()
            if mode not in mode_list :
                print("Invalid code")
                break
        elif idx == 2 :
            morse_dict =  extract_morse_dict(data)
            reverse_morse_dict = {v:k for k,v in morse_dict.items()}
        else :
            if mode == "M2T" :
                payload = []
                for x in data.strip("\n").split(" ") :
                    if x not in reverse_morse_dict :
                        print("Invalid : {}".format(data.strip("\n")))
                        break
                    else :
                        payload.append(reverse_morse_dict[x])     
                if len(payload) == len(data.strip("\n").split(" ")) :
                    print("".join(payload))              
            else :
                payload = []
                for x in data.strip("\n") :
                    if x not in morse_dict :
                        print("Invalid : {}".format(data.strip("\n")))
                        break
                    else :
                        payload.append(morse_dict[x])   
                if len(payload) == len(data.strip("\n")) :
                    print(" ".join(payload))
        