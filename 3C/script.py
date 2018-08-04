import sys
import os





def CalculateMinNumCoins(m, coins):
	MinNumCoins={0:0}
	for i in range(1,m+1):
		dif = [MinNumCoins[i-coins[j]]+1 for j in range(len(coins)) if i-coins[j] in MinNumCoins]
		MinNumCoins[i]= min(dif)
	return MinNumCoins[m]


# coins=[5, 4, 1]
# d= CalculateMinNumCoins(23,coins)
# keys = d.keys()
# sorted(keys)
# print " ".join(str(d[k]) for k in keys[13:])
	


money = 19508
coins=[22,11,10,5,3,1]
print CalculateMinNumCoins(money, coins)