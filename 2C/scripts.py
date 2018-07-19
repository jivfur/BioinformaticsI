import sys
import random
import copy

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


# def DeBruijn(Patterns):
# 	Dict={}
# 	for pattern in Patterns:
# 		if pattern[:-1] in Dict:
# 			Dict[pattern[:-1]]+=[pattern[1:]]
# 		else:
# 			Dict[pattern[:-1]]=[pattern[1:]]
# 	return Dict



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


 # 6->8->7->9->6->5->4->2->1->0->3->2->6


# graph = {}
# lines = sys.stdin.read().splitlines() # read in the input from STDIN
# for i in xrange(len(lines)):
# 	line = lines[i].split("->")
# 	graph[int(line[0])] = [int(x) for x in line[1].split(",")]


# graph = {0: [2],
# 1 : [3],
# 2 : [1],
# 3 : [0,4],
# 6 : [3,7],
# 7 : [8],
# 8 : [9],
# 9 : [6]}

# print "->".join([str(x) for x in EurelianCycle(graph)])


# def EulerianPath(Graph):
# 	indegrees = indegree(Graph)
# 	InKeys = set(indegrees.keys())
# 	GraphKeys = set(Graph.keys())
# 	diff = InKeys^GraphKeys
# 	for k in diff:
# 		Graph[k]=[]	
# 	unbalancedNodes=[]
# 	for item in Graph:
# 		if len(Graph[item]) != indegrees[item]:
# 			unbalancedNodes.append(item)
# 	for node in unbalancedNodes:
# 		Graph[node]+=unbalancedNodes
# 		Graph[node].remove(node)
# 	##remove added edges
# 	return EurelianCycle(Graph)







# Dna =["CTTA",
#      "ACCA",
#      "TACC",
#      "GGCT",
#      "GCTT",
#      "TTAC"]

# Patterns = sys.stdin.read().splitlines()
# graph = DeBruijn(Patterns[1:])
# print graph
# path=EurelianPath(graph)
# print(joinEurelianPath(path))


# lines = sys.stdin.read().splitlines() # read in the input from STDIN
# for i in xrange(len(lines)):
# 	line = lines[i].split("->")
# 	graph[int(line[0])] = [int(x) for x in line[1].split(",")]
# print("->".join([str(x) for x in EurelianPath(graph)]))

def joinEurelianPath(path):
	text = path[0]
	for p in path[1:]:
		text+=p[-1]
	return text

def circularString(k):
	b = 2**k
	Dna=[]
	cad = "0"*(k)	
	for i in range(b):
		a = cad+bin(i)[2:]		
		Dna.append(a[len(a)-k:])		
	graph = DeBruijn(Dna)	
	return EurelianCycle(graph)

def joinCirculaString(cycle,k):	
	first = "0"*k
	edges = [cycle[i]+cycle[i+1][-1] for i in range(len(cycle[:-1]))]	
	index=edges.index(first)
	edges_sorted=[edges[index]]
	i=index+1
	l = len(edges)
	while edges[i%l]!=first:
		edges_sorted.append(edges[i%l])
		i+=1	
	print len(edges)
	print edges
	print len(edges_sorted)
	print edges_sorted
	text = edges_sorted[0]
	for p in edges_sorted[1:-k+1]:
		text+=p[-1]	
	return text
	
	

# k = int(sys.stdin.read())
# print joinCirculaString(circularString(k),k)


# def PairedComposition(k,d,text):
# 	return [(text[i:i+k],text[i+k+d:i+2*k+d]) for i in range(len(text)-(2*k+d)+1)]
	

# kdmer= PairedComposition(3,2,"TAATGCCATGGGATGTT")
# cad = []
# for kd in kdmer:
# 	cad.append("("+kd[0]+"|"+kd[1]+") ")
# print "".join(sorted(cad))

# Path=["AG|AG",
# "AG|TG",
# "CA|CT",
# "CT|CA",
# "CT|CT",
# "GC|GC",
# "GC|GC",
# "GC|GC",
# "TG|TG"]


def inoutdegree(Graph):
	indegrees = indegree(Graph)
	InKeys = set(indegrees.keys())
	GraphKeys = set(Graph.keys())
	diff = InKeys-GraphKeys
	for k in diff:
		Graph[k]=[]	
	diff = GraphKeys-InKeys
	for k in diff:
		indegrees[k]=0		
	nodes={}
	for item in Graph:		
		nodes[item]=(indegrees[item],len(Graph[item]),indegrees[item]==len(Graph[item]))
	return nodes

def indegree(Graph):
	nodes = {}
	for item in Graph:
		for node in Graph[item]:			
			if not(node in nodes):
				nodes[node]=0		
			nodes[node]+=1
	return nodes

def EurelianPath(graph):	
	degrees = inoutdegree(graph)	
	print "Degrees",degrees
	start = [x for x in degrees if degrees[x][1]-degrees[x][0]==1]
	print start
	eu=[]
	for s in start:
		Graph=copy.deepcopy(graph)
		stack = [s]	
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
		eu.append(path)
	return eu
	

def StringSpelledByGappedPatterns(k,d,p):
	# p = [tuple(kmer.split("|")) for kmer in path]	
	prefix=""
	suffix=""		
	for i in range(len(p)-1):
		prefix+=p[i][0][0]
		suffix+=p[i][1][0]
	prefix+=p[-1][0]
	suffix+=p[-1][1]
	print prefix
	print suffix
	print "***************************"		
	if(prefix[k+d:]!=suffix[:-k-d]):
		return False	
	return prefix+suffix[-k-d:]

def DeBruijnkd(Patterns):
	graph={p:[] for p in Patterns}
	for pattern in Patterns:		
		for p2 in Patterns:			
			if pattern[0][1:]==p2[0][:-1] and pattern[1][1:]==p2[1][:-1]:
				graph[pattern].append(p2)
	return graph

# import time
# import copy
# random.seed(time.time())
# k,d = sys.stdin.readline().split()
# lines=sys.stdin.read().splitlines()
# path=[]
# for i in range(len(lines)):
# 	path.append(tuple(lines[i].strip().split("|")))
# g=DeBruijnkd(path)
# print g
# ep=EurelianPath(g)
# a = StringSpelledByGappedPatterns(int(k),int(d),ep[0])




def MaximalNonBranchingPaths(graph):
	MaxPath=[]
	invout = inoutdegree(graph)	
	startSymbols = [x for x in invout if invout[x][1]>0 and not(invout[x][0]==invout[x][1]==1)]		
	for key in startSymbols:			
		path=[]
		for k in graph[key]:			
			path=[key]
			path.append(k)			
			while invout[k][0]==invout[k][1]==1:
				k = graph[k][0]
				path.append(k)			
			MaxPath.append(path)
	
	#How to identify cycles
	oneone = [x for x in invout if invout[x][0]==invout[x][1]==1]
	#find cycles
	for x in oneone:		
		for y in graph[x]:
			path=[x]
			while y in oneone:
				path.append(y)
				oneone.remove(y)
				if(path[0]==y):
					break
				y=graph[y][0]
			if len(path)>1 and path[0]==y:
				MaxPath.append(path)		
	return MaxPath

# graph={}
# lines = sys.stdin.read().splitlines() # read in the input from STDIN
# for i in range(len(lines)):
# 	line = lines[i].split("->")	
# 	graph[line[0].strip()] = [x.strip() for x in line[1].split(",")]
# MaxP=MaximalNonBranchingPaths(graph)
# for m in MaxP:
# 	print " -> ".join(m)

def DeBruijn(Patterns):
	Dict={}
	for pattern in Patterns:
		if pattern[:-1] in Dict:
			Dict[pattern[:-1]]+=[pattern[1:]]
		else:
			Dict[pattern[:-1]]=[pattern[1:]]
	return Dict

def joinNonBranchingPath(NonBranching):
	contings=[]
	for branch in NonBranching:
		contings.append(branch[0]+"".join([x[-1] for x in branch[1:]]))
	return contings
# Patterns = sys.stdin.read().splitlines()
# print Patterns
# graph = DeBruijn(Patterns)
# print graph
# print joinEurelianPath(EurelianPath(graph))

def loadRNACodonTable(fileName):
	f = open(fileName,"r")
	table={}
	for line in f:
		l=line.split()
		if len(l)==1:
			table[l[0]]=""
		else:
			table[l[0]]=l[1]
	return table

def RNA2Aminoacid(text,table):
	return "".join([table[text[t:t+3]] for t in range(0,len(text),3)])


table=loadRNACodonTable("RNA_codon_table_1.txt")

text = sys.stdin.read().splitlines()
for t in text:
	print RNA2Aminoacid(t,table)

def loadRNACodonTable2(fileName):
	f = open(fileName,"r")
	table={}
	table["STOP"]=[]
	for line in f:
		l=line.split()
		if(len(l)==1): #STOP
			table["STOP"].append(l)
		else:
			if not(l[1] in table):
				table[l[1]]=[]
			table[l[1]].append(l[0])
	return table

def complement(kmer):
	dict={"A":"T","C":"G","G":"C","T":"A"}
	return "".join([dict[x] for x in kmer])[::-1]


import numpy as np

def productoCruz(vec1,vec2):
	res=[]
	for v1 in vec1:
		row=[]
		for v2 in vec2:
			row.append(v1+v2)
		res.append(row)	
	res = np.reshape(res,len(res)*len(res[0]),1)
	return res



def PeptideEncodingProblem(Text,peptide,table):
	DNAStrings=[]
	for p in peptide:
		kmers = table[p]		
		dna=[]
		for rna in kmers:
			dna.append(rna.replace("U","T"))			
		DNAStrings.append(dna)	
	filas = len(DNAStrings)	
	vec1 = np.transpose(DNAStrings[0])
	for fila in range(1,filas):		
		vec2 = DNAStrings[fila]
		vec1=productoCruz(vec1,vec2)
	vec2 = [complement(v) for v in vec1]
	vec = vec1.tolist()+vec2	
	elements=[]
	for i in range(len(Text)-len(vec[0])):
		for v in vec:			
			if v==Text[i:i+len(v)]:
				elements.append(v)
	return elements





# table=loadRNACodonTable2("RNA_codon_table_1.txt")
# Text=Patterns = sys.stdin.read().strip()
# peptide="VKLFPWFNQY"

# print len(PeptideEncodingProblem(Text,peptide,table))
def loadMass(filename):
	f = open(filename)
	dict={}
	for l in f:
		l = l.split()
		dict[l[0]]=int(l[1])
	return dict

def LinearSpectrum(Peptide,AminoAcidMass):
	prefimax=[0]
	for i in range(len(Peptide)):		
		prefimax.append(prefimax[i]+AminoAcidMass[Peptide[i]])		
	linear=[0]
	for i in range(len(prefimax)-1):
		for j in range(i+1,len(prefimax)):			
			linear.append(prefimax[j]-prefimax[i])
	return sorted(linear)
	
def cyclicSpectrum(Peptide,AminoAcidMass):
	prefimax=[0]
	lp = len(Peptide)
	for i in range(lp):		
		prefimax.append(prefimax[i]+AminoAcidMass[Peptide[i]])		
	linear=[0]
	peptideMass=prefimax[lp]	
	for i in range(len(prefimax)-1):
		for j in range(i+1,len(prefimax)):			
			linear.append(prefimax[j]-prefimax[i])
			if i>0 and j<lp:
				linear.append(peptideMass-(prefimax[j]-prefimax[i]))
	return sorted(linear)




#print " ".join([str(x) for x in cyclicSpectrum(peptide,mass)])


def Expand(Peptides, mass):
	Pep2=[]
	for p in Peptides:
		for m in mass:
			Pep2.append(p+m)
	return Pep2

def calculateMass(peptide,mass):
	m=0
	for p in peptide:
		m+=mass[p]
	return m

def consistent(linearspec,spectrum):
	for ls in linearspec:
		if ls in spectrum:
			spectrum.remove(ls)
		else:
			return False
	return True

def CyclopeptideSequencing(spectrum,mass):
	
	Peptides = [""] #Strings of peptides consistent with spectrum
	founds=[]
	while Peptides:
		Peptides=Expand(Peptides,mass)		
		Peps = copy.deepcopy(Peptides)
		for Pep in Peptides:
			ls=LinearSpectrum(Pep,mass)			
			if max(ls)==max(spectrum):
				if cyclicSpectrum(Pep,mass)==spectrum:
					founds.append(Pep)
				Peps.remove(Pep)
			else:
				if not(consistent(ls,copy.deepcopy(spectrum))):
					Peps.remove(Pep)
		Peptides=Peps			
	return founds

mass= loadMass("integer_mass_table.txt")
# peps=CyclopeptideSequencing([0,71,101,113,131,184,202,214,232,285,303,315,345,416],mass)
# print peps
# cad=""
# for pep in peps:
# 	cad+="-".join(str(mass[p]) for p in pep)+" "

# print cad


spectrum=[0,71,99,101,103,128,129,199,200,204,227,230,231,298,303,328,330,332,333]
peps=["CET","TCE","CTV","VAQ","ETC","AQV"]
for p in peps:
	ls=LinearSpectrum(p,mass)
	if consistent(ls,copy.deepcopy(spectrum)):
		print p


