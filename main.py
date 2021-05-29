import random
import string
import secrets
import datetime

# alphabet = [chr(i) for i in range(97,123)]
jobs = ["sweep"
,"model"
"actor/actress"
,"astronaut"
,"author/ess"
,"baker"
,"barber"
,"beautician"
,"biologist"
,"bricklayer, brickie"
,"bus driver"
,"butcher"
,"caretaker"
,"carpenter"
,"chef"
,"chemist"
,"childcare assistant"
,"coach"
,"construction worker"
,"cook"
,"cosmetician"
,"customer adviser"
,"dentist"
,"doctor"
,"electrician"
,"engineer"
,"explorer"
,"farmer"
,"fashion designer"
,"firefighter"
,"fitness instructor"
,"florist"
,"gardener"
,"glazier"
,"graphic artist/designer"
,"hairdresser hairstylist"
,"hunter/huntsman"
,"jounalist"
,"make-up artist"
,"mechanic"
,"miner"
,"nurse"
,"nursery-school teacher"
,"painter"
,"paramedic"
,"physiotherapist"
,"pilot"
,"plumber"
,"police officer"
,"research scientist"
,"roofer"
,"secretary"
,"shepherd/ess"
,"shop assistant"
,"singer"
,"slater"
,"social worker"
,"surgeon"
,"taxi/cab driver"
,"teacher"
,"thatcher"
,"tiler"
,"tour guide"
,"truck driver"
,"undertaker"
,"vet"
,"vocalist"
,"waiter/waitress"
,"zoologist"
]
cards_details = {

        "cup":{
        "name":"China Union Pay",
        "INN Range":[[620000]],
        "NOD":[16,19]
        },
        "dis":{
        "name":"Discover",
        "INN Range":[[601100]],
        "NOD":[16,19]
        },
        "jcb":{
        "name":"JCB",
        "INN Range":[[352800,358900]],
        "NOD":[16]
        },
        "mac":{
        "name":"Master Card",
        "INN Range":[[222100,272000]],
        "NOD":[16]
        },
        "rup":{
        "name":"RuPay",
        "INN Range":[[607000]],
        "NOD":[16]
        },
        "visa":{
        "name":"Visa",
        "INN Range":[[400000]],
        "NOD":[13,16,19]
        }
}


def main():
    birth = genbirth()
    print("Day : "+str(birth[0])+" Month : "+str(birth[1])+" Year : "+str(birth[2]))
    gender = gengender()
    print("Sex : "+gender)
    pwd = genpwd()
    print("Password : "+pwd)
    name = genname(gender.lower())
    print("Name : "+name)
    username = genusername(name)
    print("Username : "+username)
    (longt, latit) = genloc()
    print("Longtitude : "+str(longt)+" Latitude : "+str(latit))
    print("E-Mail : "+genmail(username))
    cc = gencc()
    print("Credit Card Type : "+cc[0])
    print("Credit Card Number : "+str(cc[1]))
    print("Job : "+genjob())

def genusername(name):
    return "".join(name.lower().split()).replace("a","4").replace("o","0")
def gennum(a,b):
    return random.randint(a,b)

def genpwd():
    return "".join(secrets.choice(string.ascii_letters + string.digits+"@") for i in range(16))

def genname(gender):
    lfn = "dist.all.last.txt"
    ffns = ["dist.male.first.txt","dist.female.first.txt"]
    if gender == "male":
        ffn = ffns[0]
    elif gender == "female":
        ffn = ffns[1]
    else:
        ffn = ffns[gennum(0,len(ffns)-1)]

    data = list()
    with open(ffn,"r") as f:
        for i in f:
            data.append(i)

    fd = [i.split(" ")[0].lower() for i in data]
    data = list()
    with open(lfn,"r") as f:
        for i in f:
            data.append(i)
    ld = [i.split(" ")[0].lower() for i in data]

    fn = list(fd[gennum(0,len(fd)-1)])
    ln = list(ld[gennum(0,len(ld)-1)])
    fn[0] = fn[0].upper()
    ln[0] = ln[0].upper()
    return "".join(fn)+" "+"".join(ln)

def genmail(username):
    mail_networks = ["gmail.com","yahoo.com","outlook.com","protonmail.com"]
    return username+"@"+mail_networks[gennum(0,len(mail_networks)-1)]

def genbirth():
    year = gennum(1970,int(datetime.datetime.now().date().strftime("%Y"))-18)
    month = gennum(1,13)
    if not month == 2:
        day = gennum(1,31)
    else:
        day = gennum(1,29)
    return (day,month,year)

def genloc():
    latitude = gennum(-90,90)
    longtitude = gennum(-180,180)
    return (longtitude,latitude)

def gengender():
    gens = ["Male","Female","Bisexual","Non-Binary"]
    return gens[gennum(0,len(gens)-1)]

def genjob():
    return jobs[gennum(0,len(jobs)-1)]
    
def gencc():
    cards_network = ["cup","dis","jcb","mac","rup","visa"]
    card_type = cards_network[gennum(0,len(cards_network)-1)]
    card_details = cards_details[card_type]
    first_6=card_details["INN Range"]
    try:
        first_6 = gennum(first_6[0][0],first_6[0][1])
    except:
        first_6 = first_6[0][0]
    return (card_details["name"],luhn(first_6))

def luhn(first_6):  
    card_no = [int(i) for i in str(first_6)] 
    card_num = [int(i) for i in str(first_6)]
    seventh_15 = random.sample(range(9), 9)
    for i in seventh_15:
        card_no.append(i)
        card_num.append(i)
    for t in range(0, 15, 2):
        card_no[t] = card_no[t] * 2
    for i in range(len(card_no)):
        if card_no[i] > 9:
            card_no[i] -= 9
    s = sum(card_no)
    mod = s % 10
    check_sum = 0 if mod == 0 else (10 - mod)
    card_num.append(check_sum)
    card_num = [str(i) for i in card_num]
    return ''.join(card_num)

    
if __name__ == "__main__":
    main()