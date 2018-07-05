import sys

def Composition(k,Text):
	return sorted([Text[i:i+k] for i in range(len(Text)-k+1)])

def GenomePath(Dna):    
	t = len(Dna)
	return Dna[0]+"".join([Dna[i][-1] for i in range(1,t)])

# if __name__ == "__main__":
#   lines = sys.stdin.read().splitlines()
#   print(GenomePath(lines))

# Dna=["TCGGGGAATGCATC",
# "CGGGGAATGCATCA",
# "GGGGAATGCATCAC",
# "GGGAATGCATCACA",
# "GGAATGCATCACAA",
# "GAATGCATCACAAA",
# "AATGCATCACAAAG",
# "ATGCATCACAAAGT",
# "TGCATCACAAAGTG",
# "GCATCACAAAGTGC",
# "CATCACAAAGTGCA",
# "ATCACAAAGTGCAG"]


def OverlapGraph(Dna):  
	Dict={x:[] for x in Dna}
	Dna = list(set(Dna))    
	t=len(Dna)
	for i in range(t):
		for j in range(i+1,t):
			if Dna[i][1:]==Dna[j][0:-1]:
				Dict[Dna[i]].append(Dna[j])
			if Dna[j][1:]==Dna[i][0:-1]:
				Dict[Dna[j]].append(Dna[i])
	return Dict


def DeBruijnText(k,Text):
	k-=1
	kmers = [Text[i:i+k] for i in range(len(Text)-k)]   
	graph = [(kmers[i],kmers[i+1]) for i in range(len(kmers)-1)]    
	Dna=list(set(kmers))
	Dict={x:[] for x in Dna}
	for t in graph:
		Dict[t[0]].append(t[1]) 
	return Dict

# def DeBruijn(Patterns):   
#   keys=[]
#   for Pattern in Patterns:
#       keys+=[Pattern[:-1],Pattern[1:]]
#   Dict={key:[] for key in keys}
#   t=len(keys)
#   graph=[]    
#   for i in range(t):
#       for j in range(i,t):
#           if keys[i][1:]==keys[j][0:-1] and keys[i]+keys[j][-1] in Patterns:
#               graph.append((keys[i],keys[j]))
#               Patterns.remove(keys[i]+keys[j][-1])
#   for k,v in graph:
#       Dict[k].append(v)
#   return Dict


def DeBruijn(Patterns):
	Dict={}
	for pattern in Patterns:
		if pattern[:-1] in Dict:
			Dict[pattern[:-1]]+=[pattern[1:]]
		else:
			Dict[pattern[:-1]]=[pattern[1:]]
	return Dict



#Patterns=["GAGG","CAGG","GGGG","GGGA","CAGG","AGGG","GGAG"]
# Patterns = sys.stdin.read().splitlines()
# dict = DeBruijn(Patterns)
# keys = sorted(dict.keys())
# for item in keys:
#   if dict[item]:
#       print(item+" -> "+",".join(dict[item]))


# AGG -> GGG
# CAG -> AGG,AGG
# GAG -> AGG
# GGA -> GAG
# GGG -> GGA,GGG

# dict = DeBruijn(2,"TAATGCCATGGGATGTT") 
# keys = sorted(dict.keys())
# for item in keys:
#   if dict[item]:
#       print(item+" -> "+",".join(dict[item]))


# dict = DeBruijn(3,"TAATGCCATGGGATGTT") 
# keys = sorted(dict.keys())
# for item in keys:
#   if dict[item]:
#       print(item+" -> "+",".join(dict[item]))



# dict = DeBruijn(4,"TAATGCCATGGGATGTT")
# keys = sorted(dict.keys())
# for item in keys:
#   if dict[item]:
#       print(item+" -> "+",".join(dict[item]))






# if __name__ == "__main__":
#   k = int(sys.stdin.readline())
#   lines = sys.stdin.readline()
#   dict = DeBrujin(k,lines)
#   keys = sorted(dict.keys())
#   for item in keys:
#       if dict[item]:
#           print(item+" -> "+",".join(dict[item]))


# def compare(file1, file2):
#   f1 = open(file1,"r")
#   f2 = open(file2,"r")
#   index=0
#   for l1,l2 in zip(f1,f2):        
#       if l1.strip()!=l2.strip():
#           print index,l1,l2
#           break
#       index+=1



# compare("output.txt","De_Bruijn_Graph_from_kmer.txt")







# def kuniversal(k,binary):
#   patterns = [binary[i:i+k] for i in range(len(binary)-k+1)]
#   list1 = list(set(patterns))
#   if len(patterns)!=len(list1):
#       print "NO UNIVERSAL"
#   else:
#       print "UNIVERSAL"


# kuniversal(3,"0100011101")
# kuniversal(3,"1111000111")
# kuniversal(3,"0101010100")
# kuniversal(3,"1100011011")
# kuniversal(3,"0111010001")
# kuniversal(3,"0011101000")


import random

def EurelianCycle(Graph):       
	stack = [random.choice(Graph.keys())]
	path = []
	while stack:		
		if Graph[stack[0]]:
			w = random.choice(Graph[stack[0]])
			Graph[stack[0]].remove(w)
			stack.insert(0,w)			
		else:
			a=stack[0]
			path.append(stack[0])
			stack.remove(a)	
	path.reverse()
	return path



# graph = {0:[3],1:[0],2:[1,6],3:[2],4:[2],5:[4],6:[5,8],7:[9],8:[7],9:[6]}





# graph = {}
# lines = sys.stdin.read().splitlines() # read in the input from STDIN
# for i in xrange(len(lines)):
# 	line = lines[i].split("->")
# 	graph[int(line[0])] = [int(x) for x in line[1].split(",")]


graph = {0: [2],
1 : [3],
2 : [1],
3 : [0,4],
6 : [3,7],
7 : [8],
8 : [9],
9 : [6]}

# print "->".join([str(x) for x in EurelianCycle(graph)])


def indegree(Graph):
	nodes = {}
	for item in Graph:
		for node in Graph[item]:
			if not(node in nodes):
				nodes[node]=0		
			nodes[node]+=1
	return nodes

def EulerianPath(Graph):
	indegrees = indegree(Graph)
	InKeys = set(indegrees.keys())
	GraphKeys = set(Graph.keys())
	diff = InKeys^GraphKeys
	for k in diff:
		Graph[k]=[]	
	unbalancedNodes=[]
	for item in Graph:
		if len(Graph[item]) != indegrees[item]:
			unbalancedNodes.append(item)
	for node in unbalancedNodes:
		Graph[node]+=unbalancedNodes
		Graph[node].remove(node)
	##remove added edges
	return EurelianCycle(Graph)


print "->".join([str(x) for x in EulerianPath(graph)])

# 6->7->8->9->6->3->0->2->1->3->4
# 9->6->7->8->9->3->0->2->1->3->4

