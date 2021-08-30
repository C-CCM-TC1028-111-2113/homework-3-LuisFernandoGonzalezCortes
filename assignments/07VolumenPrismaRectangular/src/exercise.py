def area(x,y):
    return x*y

def volumen(x,y,z):
    return area(x,y)*z
    
def main():

    z=float(input("Dame la profundidad: "))
    x=float(input("Dame la base: "))
    y=float(input("Dame la altura: "))

    A = area(x,y)
    V = volumen(x,y,z)

    print("El volumen del prisma es: ", V)

if __name__=='__main__':
    main()
