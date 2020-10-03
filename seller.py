class Seller:
    def __init__(self, amount, sum):
        self.amount = amount
        self.sum = sum
    
    def __str__(self):
        text = "You have {} shoes with a total price of ${}".format(self.amount, self.sum)
        return text

    def seller_fee(self, fee):
        self.sum *= ((100 - fee)/100)
        print("You will make ${}".format(round(self.sum, 2)))


def print_seller(seller):
    print("{}\t".format(seller),end="")

def sum_price(amount, price):
    total = 0
    for i in range(amount):
        total += price[i]
    return round(total, 2)

def main():    
    numPeople = int(input("How many sellers are there? "))
    print()
    for x in range(numPeople):
        print("Seller {}: ".format(x + 1))
        amount = int(input("How may sneakers do you have? "))
        price = []
        for i in range(amount):
            price.append(float(input("what is the price of sneaker #{}? ".format(i + 1))))
        sum = sum_price(amount, price)        
        seller = Seller(amount, sum)        
        print_seller(seller)
        print()
        ans = input("Do you want to sell your sneakers? y/n: ")
        if ans == 'y':
            fee = float(input("What is the seller fee percentage? "))
            seller.seller_fee(fee)

        if x == numPeople - 1:
            print("Goodbye")
        else:
            print("Next")


        print()
        print()
        del seller

if __name__ == "__main__":
    main()