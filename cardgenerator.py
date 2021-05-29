import random
first_6=400000 # IIN For Banking Industry(6 digits)
def luhn():
    global first_6  
    card_no = [int(i) for i in str(first_6)]  # To find the checksum digit on
    card_num = [int(i) for i in str(first_6)]  # Actual account number
    seventh_15 = random.sample(range(9), 9)  # Acc no (9 digits)
    for i in seventh_15:
        card_no.append(i)
        card_num.append(i)
    for t in range(0, 15, 2):  # odd position digits
        card_no[t] = card_no[t] * 2
    for i in range(len(card_no)):
        if card_no[i] > 9:  # deduct 9 from numbers greater than 9
            card_no[i] -= 9
    s = sum(card_no)
    mod = s % 10
    check_sum = 0 if mod == 0 else (10 - mod)
    card_num.append(check_sum)
    card_num = [str(i) for i in card_num]
    return ''.join(card_num)
print(luhn())

"""
import random
def gennum(a,b):
    return random.randint(a,b)

iim = "400000"
iim = [int(i) for i in str(iim)]

v = [gennum(0,9) for i in range(2,15)]                
v[0:5] = iim

print(v)
for c in range(6,len(v)-1):
    i = v[c]
    if i % 2 == 0:
        d = v[i]*2
        if d > 9:
            f = [i for i in str(d)]
            q= f[0]
            s = f[1]
            print(f,q,s)
            d = int(q) + int(s)
        v[i] = d

v.append(sum(v))
v[0] = 4
print(str(v).replace(",","").replace("'","").replace("[","").replace("]","").replace(" ",""))
"""
