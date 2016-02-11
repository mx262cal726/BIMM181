__author__ = 'kyle'

<<<<<<< HEAD
def coins(text):
    in_file = open(text)
    lines = in_file.read().split("\n")
    total = int(lines[0])
    tmp = lines[1].split(",")
    coins_available = list()

    for i in tmp:
        coins_available.append(int(i))
    coins_available.sort()
    coin_bag = list()


    for i in range(0, len(coins_available)):
        coin_bag.insert(i, Coin(int(coins_available[i]),total/int(coins_available[i])))

    return starting_sum(coin_bag, total)


def starting_sum(coins, total):
    number_of_coins = len(coins)-1
    count = 0
    path = ""
    check=total
    while 0 <= number_of_coins:
        coin = coins[number_of_coins].value
        path += str(coin)+" "
        while total >= coin:
            print total/(coin+(coin - coins[number_of_coins-1].value)),"<", coins[number_of_coins-1].value
            print (total/coins[number_of_coins-1].value), "<=", coins[0].value
            if total %coins[number_of_coins-1].value == 0:
                coins[number_of_coins-1].min_div = total/coins[number_of_coins-1].value
                print "Total:",total
                print "Count:",count
                divs = total/coins[number_of_coins-1].value
                print "total/21:",total /divs
                print "divs",divs

                tmp_count = count+total/coins[number_of_coins-1].value

                print tmp_count,count

                if tmp_count < check:
                    check = tmp_count
                    if tmp_count < check:
                        count = check
                    if total < 1:
                        return count
                if divs < coins[number_of_coins-1].value:
                    number_of_coins -= 1
            if total/(coin+(coin - coins[number_of_coins-1].value)) < coins[number_of_coins-1].value:
                print total%21
                print total, coins[number_of_coins-1].value**2


            total -= coin
            count += 1
            if check < count:
                count = check
            if total < 1:
                return count
        path += str(coin)+" + "+str(total)+" "
        number_of_coins -= 1
        tmp_val = coins[get_largest_divisible(coins, total)].value
        number_of_coins = check_mod(coins, tmp_val, total, number_of_coins)
        print "CHECK:",check
    if tmp_count < check:
        return check
    return count


def check_mod(coins, val, total, index):
    while 0 <= index:
        if coins[index] <= total and coins[index].value%val==0:
            return index
        index -= 1

def get_largest_divisible(coin, total):
    count = len(coin)-1
    while 0 <= count:
        if coin[count].is_divisible(total):
            return count
        count -= 1
    return

class Coin:

    def __init__(self, value,min_div):
        self.min_div = min_div
        self.value = value


    def is_divisible(self, total):
        return 0 == total%self.value

    def get_remaining(self, total):
=======

def coins(text):
    in_file = open(text)
    lines = in_file.read().split("\n")
    total = lines[0]
    coins_available = lines[1].split(",")
    coin_bag = list()
    print "hi"
    for i in range(0, len(coins_available)):
        coin_bag.insert(i,Coin(coins_available[i]))
        print coin_bag[i].value

    print get_remaining(total)



class Coin:
    def __init__(self, value):
        self.value = valu

    def is_divisible(self,total):
        return 0 == total%self.value

    def get_remaining(self,total):
>>>>>>> 9c227b03a489a7a06dfc5e5b7dd8d3a192553c9b
        return total%self.value

    def get_lower_count(self, value2, total):
        if total/self.value < total/value2:
            return total/self.value
        else:
            return total/value2

    def remove_n_minus_one(self,total):
        count = 0
<<<<<<< HEAD
        while count+self.value < total-self.value:
            count += self.value
        return count/self.value, total-count

print coins("rosalind_ba5a.txt")

# Driver program to test above function
=======
        while count+self.value < total:
            count += self.value
        return count/self.value, total-count

coins("input.txt")
>>>>>>> 9c227b03a489a7a06dfc5e5b7dd8d3a192553c9b
