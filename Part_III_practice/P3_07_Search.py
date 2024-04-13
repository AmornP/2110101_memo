def split_all_words(t : str) :
    return t.split()

def get_unique_words_count(t : list) :
    x = split_all_words(t)
    return len(set(x))

def get_specific_word_count(t : str,key : str) :
    x = split_all_words(t)
    x = [k for k in x if k == key]
    return len(x)

def get_all_word_count(t : str) :
    return len(split_all_words(t))

def calculate_relavance_index(t : str , key : str) :
    awc = get_all_word_count(t)
    occ = get_specific_word_count(t,key)
    uwc = get_unique_words_count(t)

    freq = occ / awc
    c_ = 1 / uwc

    return freq * c_

def find_relavance(articles : dict,x : str) :
    
    ret = sorted([[title,calculate_relavance_index(text,x)] for title,text in articles.items()],key=lambda x : -1*x[1])
    if ret[0][1] == 0 :
        print("NOT FOUND")
    else :
        print(ret[0][0])
n = int(input())
articles = {}
for i in range(n) :
    title = input()
    text = input()
    articles[title] = text

while True :
    x = input()
    if x == "-1" :
        break
    else :
        find_relavance(articles,x)