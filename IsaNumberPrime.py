n = int(input('Enter an Integer: '))

def prime(n): 
    for i in range (2, n):
        if n % i == 0:
            return False
    return True

def main():
    if prime(n):
        print('True')
    else:
        print('False')

if __name__ == "__main__":
    main()
