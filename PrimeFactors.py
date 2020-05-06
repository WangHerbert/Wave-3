n = int(input("Enter an integer (2 or greater): "))
factor = 2

if n < 2:
    print ('Please enter an integer 2 or greater')
else:
    print ('The prime factors of 72 are:')
    while factor <= n:
        if n % factor == 0:
            print (factor)
            n = n / factor
        else:
            factor += 1