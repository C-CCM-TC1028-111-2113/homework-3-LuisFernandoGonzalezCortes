def es_bisiesto(año):
    if año % 4 == 0:
        return True
    elif año % 100 == 0:
        return False
    elif año % 400 == 0:
        return True
    else:
        return False
    
def main():

    año=int(input("Dame un año: "))

    print("El año es bisiesto? ",es_bisiesto(año))
    
if __name__ == '__main__':
    main()
