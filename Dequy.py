def tinhtong(n):
    if(n/10==0):
        return n
    return (tinhtong(n/10)+n%10)

def Giaithua(n):
    if(n==1):
        return n
    return (Giaithua(n-1)+n)
def Tich(a,b):
    if(a==1 or b==1):
        return a
    return Tich(a,b-1)*a
def Uocchung(a,b):
    if(a==0):
        return b
    return Uocchung(b,a%b)
    
    
