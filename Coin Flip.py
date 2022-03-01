import random 
class CoinFlip():
    def __int__(self,balance):
        self.balance = balance

    def getBalanceAmaount(self):
        print(f"You have Rs {self.balance} in your wallet")

    def doBetting(self):
        a = int(input("How many times you want to bet ? "))
        b = [0]
        e = [0]
        g = [0]

        for i in range(1,a+1):
            randNo = random.randint(0,1)
            g.append(randNo)
            f = int(input(f"Enter 0 or 1 To Bet in Round {i} in which bet = 0 or 1 representing heads or tails: "))
            c = int(input(f"Enter Your Bet Amount For Round {i} : Rs "))
            e.append(f)
            b.append(c)

        d = sum(b)
        if (d <= self.balance):
             for i in range(1,a+1):
                 if(g[i]==e[i]):
                     self.balance = (2 * b[i]) + self.balance
                     print(f"Congratulations You Won in Round {i}")
                 else:
                     self.balance = self.balance - b[i]
                     print(f"Sorry You Lost in Round {i}")
             print(f"You have Rs {self.balance} in your wallet")
             
        else :
            print("You Can't do Betting as you have insufficient balance in your wallet")


person = CoinFlip()
person.balance = 100
exi = 'c'
while (person.balance>0 and exi =='c'):
    person.getBalanceAmaount()
    person.doBetting()
    exi = input("You Do want to bet more or exit Enter 'c' for continue and type any other key for exit : ")