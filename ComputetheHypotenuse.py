from math import sqrt

def hypo(n, m):
    return sqrt(n ** 2 + m ** 2)

def main():
    n = int(input('Enter one short side of the triangle: '))
    m = int(input('Enter the other short side of the triangle: '))
    if n <=0 or m <= 0:
        print ('Please enter positive integers')
    else:
        hypotenuse = format (hypo(n, m))
        print (hypotenuse)

if __name__ == "__main__":
    main()