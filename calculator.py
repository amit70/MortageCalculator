
def montlyPayment(p,n,si):
    mp = (p + si) / (n * 12)
    return float(mp)

def simpleInterest(p,n,r):
    si = (p*n*r) / 100
    return float(si)

def userInput():
     p = int(raw_input("Enter the Principal amount"))
     n = int(raw_input("Enter the term"))
     r = int(raw_input("Enter rate of interest"))
     return (p,n,r)

def main():
    (p,n,r) = userInput()
    si = simpleInterest(p,n,r)
    mp = montlyPayment(p,n,si)
    print "Your montly payments is $%s" % round(mp , 2)

if __name__ == "__main__":
    main()