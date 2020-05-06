def cost(n):
    if n == 1:
        return (10.95)
    else:
        return (10.95 + ((n-1) * 2.95))

def main():
    n = int(input("How many items would you like to purchase?: "))
    if n < 1:
        print ('You have to purchase at least one item')
    else:
        price = float(format(cost(n)))
        print (round(price, 2))

if __name__ == "__main__":
    main()