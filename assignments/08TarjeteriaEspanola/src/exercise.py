def pliego(x):
    return x*12

def plumones(y):
    return y*35
    
def main():

    x=int(input("Dame la cantidad de pliegos de papel albanene: "))
    y=int(input("Dame la cantidad de plumones: "))

    i=pliego(x)
    u=plumones(y)

    if u > i:
        print ("El número máximo de tarjetas que se pueden hacer es:",i)
        
    elif i > u:
        print("El número máximo de tarjetas que se pueden hacer es: ",u)

    elif u == i:
        print("El número máximo de tarjetas que se pueden hacer es: ",u)

if __name__ == '__main__':
    main()
