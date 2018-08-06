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

# l=[int(x) for x in sys.stdin.readline().split()]
# lines = sys.stdin.read().splitlines()
# Down=[]
# for i in range(l[0]):
# 	row = [int(x) for x in lines[i].split()]
# 	Down.append(row)
# Right=[]
# start=l[0]+1
# for j in range(l[0]+1):
# 	row = [int(x) for x in lines[start+j].split()]
# 	Right.append(row)
# Diag=[]
# start+=j+2
# for j in range(l[1]):
# 	row = [int(x) for x in lines[start+j].split()]
# 	Diag.append(row)

# print ManhattanProblemDiag(l[0],l[1],Down,Right,Diag)

def pretty(P):
	for p in P:
		print p


def LCSBackTrack(v, w):
	lenV = len(v)
	lenW = len(w)	
	S=[[0 for i in range(lenW+1)]for j in range(lenV+1)]
	B =[[0 for i in range(lenW)]for j in range(lenV)]	
	for i in range(lenV): #8
		for j in range(lenW): #9
			S[i+1][j+1]=max(S[i][j+1],S[i+1][j],(v[i]==w[j])+S[i][j])
			if S[i+1][j+1]==S[i][j+1]:
				B[i][j]="D"
			elif S[i+1][j+1]==S[i+1][j]:
				B[i][j]="R"
			elif (S[i+1][j+1]==S[i][j]+1) and v[i]==w[j]:
				B[i][j]="T"
	return S,B


# def OutputLCS(backtrack, v, i, j):	
# 	if i==-1 or j==-1:
# 		return ""
# 	elif backtrack[i][j]=="D":
# 		return OutputLCS(backtrack,v,i-1,j)
# 	elif backtrack[i][j]=="R":
# 		return OutputLCS(backtrack,v,i,j-1)
# 	else:		
# 		return v[i]+OutputLCS(backtrack,v,i-1,j-1)
def OutputLCS(backtrack, v, i, j):
	cad=""
	while(i>=0 and j>=0):
		if backtrack[i][j]=="D":
			i-=1
		elif backtrack[i][j]=="R":
			j-=1
		else:		
			cad+=v[i]
			i-=1
			j-=1
	return cad

#It should return a list
def topologicalOrder(graph):
	







I = int(sys.stdin.readline())
J = int(sys.stdin.readline())
lines = sys.stdin.read().splitlines()
D=abs(I-J)+1
graph=[[0 for i in range(D)] for j in range(D)]
for l in lines:
	temp = l.split("->")
	temp2 = temp[1].split(":")
	graph[int(temp[0])][int(temp2[0])]=int(temp2[1])
tp=topologicalOrder(graph)



# lines = sys.stdin.read().splitlines()
# w=lines[0].strip()
# v=lines[1].strip()
# S,B=LCSBackTrack(v,w)
# # pretty(S)
# # pretty(B)
# print OutputLCS(B,v,len(v)-1,len(w)-1,)[::-1]

# if S[i+1][j+1]==S[i][j]+2 and v[i]==w[j]:				
# 				B[i][j] = "T"
# 			elif S[i+1][j+1]==S[i+1][j]:				
# 				B[i][j] = "R"
# 			elif S[i+1][j+1]==S[i][j+1]:
# 				B[i][j] = "D"



