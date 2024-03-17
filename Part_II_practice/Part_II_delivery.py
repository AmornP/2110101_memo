# What can be improved
# 1. don't forget that when you calculate the days in febulary use the christian one
# 2. when copying please check the print statement
# 3. check the strict format like devery_id don't cast it into int
# 4. please memorize the logic of date conversion

def check_invalid_year(y : str) :
    y = int(y)
    return y < 2558

def get_day_list(y : str) :
    y = int(y)
    y = y-543
    day_list = [31,28,31,30,31,30,31,31,30,31,30,31]
    if (y%400 == 0) or (y%4 == 0 and y%100 != 0) :
        day_list[1] = 29
    return day_list

def check_invalid_month(m : str) :
    m = int(m)
    return m < 1 or m > 12

def check_invalid_date(d : str , m : str , y : str) :
    
    m = int(m)
    d = int(d)
    day_list = get_day_list(y)
    return d < 1 or d > day_list[m-1]

def get_shipping_period(t : str) :

    periods = {"E" : 1, "Q" : 3, "N" : 7, "F" : 14}
    if t in periods :
        return periods[t]
    else :
        return -1
    
def calc_date(t : str , d : str , m : str , y : str) :
    d = int(d)
    m = int(m)
    shipping_period = get_shipping_period(t)
    day_list = get_day_list(y)
    time_elapse = sum(day_list[:m-1]) + d + shipping_period
    m = 0
    cum_date = sum(day_list)
    if time_elapse > cum_date :
        y = str(int(y) + 1)
        m = 1
        d = time_elapse % cum_date
    else :
        for dl in day_list :
            if time_elapse < dl :
                d = time_elapse
                m += 1
                break
            elif time_elapse == dl :
                d = dl
                m+=1
                break
            else :
                time_elapse -= dl
                m+=1
    return str(d) , str(m) , str(y)


if __name__ == "__main__" :

    logs = []
    while True :
        x = input().strip().split()
        if x[0] == "END" :
            break
        ship_id , t , d , m , y = x
        if check_invalid_year(y) :
            print(f"Error: {ship_id} {t} {d} {m} {y} --> Invalid year")
        elif check_invalid_month(m) :
            print(f"Error: {ship_id} {t} {d} {m} {y} --> Invalid month")
        elif check_invalid_date(d,m,y) :
            print(f"Error: {ship_id} {t} {d} {m} {y} --> Invalid date")
        elif get_shipping_period(t) == -1 :
            print(f"Error: {ship_id} {t} {d} {m} {y} --> Invalid delivery type")
        else :
            d_ , m_ , y_ = calc_date(t,d,m,y)
            logs.append([int(y_),int(m_),int(d_),str(ship_id)])
    
    logs.sort()    
    print("\n".join([f"{x[3]}: delivered on {x[2]}/{x[1]}/{x[0]}" for x in logs]))

