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
	


# money = 19508
# coins=[22,11,10,5,3,1]
# print CalculateMinNumCoins(money, coins)

def ManhattanProblem(M,N,Down, Right):
	S=[[0 for i in range(N+1)]for  j in range(M+1)]
	for i in range(M): 
		S[i+1][0]= S[i][0]+Down[i][0]
	for j in range(N):
		S[0][j+1]= S[0][j]+Right[0][j]
	for i in range(M):
		for j in range(N):
			S[i+1][j+1]= max(S[i][j+1]+Down[i][j+1], S[i+1][j]+Right[i+1][j])
	return S[M][N]

def ManhattanProblemDiag(M,N,Down,Right,Diag):
	S=[[0 for i in range(N+1)]for  j in range(M+1)]
	for i in range(M): 
		S[i+1][0]= S[i][0]+Down[i][0]
	for j in range(N):
		S[0][j+1]= S[0][j]+Right[0][j]
	for i in range(M):
		for j in range(N):
			S[i+1][j+1]= max(S[i][j+1]+Down[i][j+1], S[i+1][j]+Right[i+1][j],S[i][j]+Diag[i][j])
	return S[M][N]

l=[int(x) for x in sys.stdin.readline().split()]
lines = sys.stdin.read().splitlines()
Down=[]
for i in range(l[0]):
	row = [int(x) for x in lines[i].split()]
	Down.append(row)
Right=[]
start=l[0]+1
for j in range(l[0]+1):
	row = [int(x) for x in lines[start+j].split()]
	Right.append(row)
Diag=[]
start+=j+2
for j in range(l[1]):
	row = [int(x) for x in lines[start+j].split()]
	Diag.append(row)

print ManhattanProblemDiag(l[0],l[1],Down,Right,Diag)





