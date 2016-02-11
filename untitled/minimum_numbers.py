__author__ = 'rouse'


def minimum_numbers(text):
    lines = open(text)
    line = lines.read()
    split_lines = line.split("\n")
    total = int(split_lines[0])
    coins = split_lines[1]
    split_coins = coins.split(",")
    count = 0
    number_of_coins = len(split_coins)-1
    print(split_lines)
    while 0 <= number_of_coins:
        coin = int(split_coins[number_of_coins])
        print "coin",coin
        while total >= coin:
            print total
            total -= coin
            print total
            count += 1
        number_of_coins -= 1
    print count

    number_of_coins = 0
    while True:
        coin = int(split_coins[number_of_coins])
        print "coin",coin
        while total >= coin:
            print total
            total -= coin
            print total
            count += 1
        for j in range(0,len())

        number_of_coins += 1
    print count
minimum_numbers("rosalind_ba3d.txt")



class Coin:

    def __init__(self, value):
        self.value = value

    def is_divisible(self, total):
        return 0 == total%self.value

    def get_remaining(self, total):
        return total%self.value

    def get_lower_count(self, value2, total):
        if total/self.value < total/value2:
            return total/self.value
        else:
            return total/value2

    def remove_n_minus_one(self,total):
        count = 0
        while count+self.value < total-self.value:
            count += self.value
        return count/self.value, total-count


