__author__ = 'kyle'


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
        return total%self.value

    def get_lower_count(self, value2, total):
        if total/self.value < total/value2:
            return total/self.value
        else:
            return total/value2

    def remove_n_minus_one(self,total):
        count = 0
        while count+self.value < total:
            count += self.value
        return count/self.value, total-count

coins("input.txt")