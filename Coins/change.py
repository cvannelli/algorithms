import math
from operator import add


class Coins:

    def __init__(self, purse, total):
        self.coins = purse
        self.total = total

    def printAll(self):
        print(self.values)
        print(self.total)

    def changedp(self):
        # array stores coin type used per amount
        X = [-1] * (self.total + 1)

        # array stores number of coins per amount
        Y = [float("inf")] * (self.total + 1)

        # array keeps track of number of coin types used
        denoms = [0] * len(self.coins)

        # initializes first element of amount array to 0
        Y[0] = 0

        # iterates through both arrays
        for i in range(len(self.coins)):
            for j in range(1, self.total + 1):

                # checks if coin type amounts to less or equal current total
                if self.coins[i] <= j:

                    # checks if value at index is greater
                    # than 1 more than (j - coin size)
                    if Y[j] > 1 + Y[j - self.coins[i]]:

                        # adds 1 to (j - coin size) into array index
                        Y[j] = 1 + Y[j - self.coins[i]]

                        # puts coin type in X array
                        X[j] = i

        # variable declared for last index of X
        end = len(X) - 1

        # loops down through X
        while end != 0:

            # sets coin to the coin type contained at x[end]
            coin = self.coins[X[end]]

            # increments the coin type in the denomination array
            denoms[X[end]] = denoms[X[end]] + 1

            # sets end to coin steps to the left of its current position
            end = end - coin

        return denoms, Y[len(Y) - 1]

    def changegreedy(self):
        # keeps track of the current total value of coins
        currentTotal = self.total

        # array keeps track of number of coin types used
        denoms = [0] * len(self.coins)

        # keeps track of the number of coins used
        coinsUsed = 0

        # iterates down the coin demoninations
        for i in range(len(self.coins) - 1, -1, -1):

            # determines number of specific coins that can fit within total
            denoms[i] = int(currentTotal / self.coins[i])

            # increments the coins used by the number of coins determined
            coinsUsed += int(currentTotal / self.coins[i])

            # updates the current total
            currentTotal = currentTotal % self.coins[i]

        return denoms, coinsUsed

    def changeslow(self):
        # calls recursive helper function
        denoms = self._changeslowHelper()

        # calculates number of coins used
        return denoms[0], denoms[1]

    def _changeslowHelper(self, n=-1):
        if n == -1:
            n = self.total

        # creates an array for holding number of denoms
        out = [0] * len(self.coins)

        # base case finds out if denom equals the total
        for i in range(0, len(self.coins)):
            if n == self.coins[i]:
                out[i] = 1
                return [out, 1]

        minsum = n + 1

        # divides and conquers through array obtaining all
        # possible coin combinations
        for i in range(1, int(n / 2) + 1):
            a = self._changeslowHelper(n - i)
            b = self._changeslowHelper(i)
            tmp = map(add, a[0], b[0])
            tmpsum = a[1] + b[1]

            if tmpsum < minsum:
                out = tmp
                minsum = tmpsum

        return [out, sum(out)]
