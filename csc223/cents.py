cents = input("Enter your cents ")
cents=int(cents)

#This is a github test
def Tens(cents):
    if cents>=1000:
        tens=cents/1000
        cents=cents%1000         
        print(tens,"ten dollar bills")
    else:
        print("0 ten dollar bills")    
    return cents

def Fives(cents):
    if cents>=500:
        fives=cents/500
        cents=cents%500
        print(fives,"five dollar bills")
    else:
        print("0 five dollar bills")
    return cents

def Ones(cents):
    if cents>=100:
        ones=cents/100
        cents=cents%100
        print(ones,"one dollar bills")
    else:
        print("0 one dollar bills")
    return cents

def Quaters(cents):
    if cents>=25:
        quaters=cents/25
        cents=cents%25
        print(quaters,"quaters")
    else:
        print("0 Quaters")
    return cents

def Dimes(cents):
    if cents>=10:
        dimes=cents/10
        cents=cents%10
        print(dimes,"dimes")
    else:
        print("0 dimes")
    return cents

def Nickel(cents):
    if cents>=5:
        nickel=cents/5
        cents=cents%5
        print(nickel,"nickel")
    else:
        print("0 Nickles")
    return cents

def Pennies(cents):
    pennies=cents/1
    cents=cents%1
    print(pennies,"pennies")
    return cents


cents=Tens(cents)
cents=Fives(cents)
cents=Ones(cents)
cents=Quaters(cents)
cents=Dimes(cents)
cents=Nickel(cents)
cents=Pennies(cents)


