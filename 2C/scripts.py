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


# table=loadRNACodonTable("RNA_codon_table_1.txt")

# text = sys.stdin.read().splitlines()
# for t in text:
# 	print RNA2Aminoacid(t,table)

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


# peps=CyclopeptideSequencing([0,71,101,113,131,184,202,214,232,285,303,315,345,416],mass)
# print peps
# cad=""
# for pep in peps:
# 	cad+="-".join(str(mass[p]) for p in pep)+" "

# print cad


# spectrum=[0,71,99,101,103,128,129,199,200,204,227,230,231,298,303,328,330,332,333]
# peps=["CET","TCE","CTV","VAQ","ETC","AQV"]
# for p in peps:
# 	ls=LinearSpectrum(p,mass)
# 	if consistent(ls,copy.deepcopy(spectrum)):
# 		print p




def score(peptide, spectrum):
	mass= loadMass("integer_mass_table.txt")
	cS=cyclicSpectrum(peptide,mass)
	lcs=len(cS)
	lspectrum=len(spectrum)
	a=cS
	b=spectrum #mas gde
	if lspectrum<lcs:
		a=spectrum
		b=cS
	count =0
	for c in a:
		if c in b:
			count+=1
			b.remove(c)
	return count



# pep = sys.stdin.readline().strip()
# spectrum= [int(x) for x in sys.stdin.readline().split()]

# print score(pep,spectrum)

def linearScore(Peptide,Spectrum, AminoAcidMass):	
	linear= LinearSpectrum(Peptide, AminoAcidMass)	
	lcs=len(linear)
	lspectrum=len(Spectrum)
	a=linear
	b=Spectrum #mas gde
	if lspectrum<lcs:
		a=Spectrum
		b=linear
	count =0
	for c in a:
		if c in b:
			count+=1
			b.remove(c)
	return count


# pep = sys.stdin.readline().strip()
# spectrum= [int(x) for x in sys.stdin.readline().split()]
# print(linearScore(pep,spectrum))
def Trim(Leaderboard, Spectrum, N, AminoAcidMass):	
	dict={}
	for l in Leaderboard:
		s=linearScore(l,copy.deepcopy(Spectrum),AminoAcidMass)		
		if not(s in dict):
			dict[s]=[]
		dict[s].append(l)	
	s = sorted(dict.keys(),reverse=True)
	board=[]
	for a in s:
		board+=dict[a]	
	return board[0:N]

# AminoAcidMass = loadMass("integer_mass_table.txt")
# Leaderboard=["VEADPFIFWMSEQIAMKIKAFPCNRCDNHPLSDAFTDPVYYIVFERL",
# "YNGGGTCMVPEYGADIGPMCTTCILKPHHFNCLGVNNDKIKRMCISW",
# "MYAECIDQRCMPEKGSCDQMCSLEQWVWQWHIGFYYMQIFDIPCFDG",
# "AVQVFHERRNYSGFLGWPEDSMCHETFVRTSAYYTWDQPHWNDYMVM",
# "DPPIGMKQISTVCGDGDDSVYIHTFNTLKPWETKGCCPHIMVEESTG",
# "WGLCLDDILEWWHWPVHYGNYDWLAFSTWALWYNPMYDNHKLSDSQK",
# "MKACRNQGAATPFYIVHVKAWHLWVMIDKNFFQTDSGDEAYALRTEQ",
# "DMTCEVQWDDTVCCCSAKMGFTQLELCIYLINIGWQYEASDQSPTRF",
# "YAGSKCFDQQRIYGWTFHYPIQRRNLMFAVMYPSGVADGPDSQHHQG",
# "WLFTCFMCAPEILHSQHGSFWSVEKFQTCKVCGHGWHVDPPSKPYLC",
# "LWSSPNFCTFFMTRQSNLDGFDTWRDMEVFTRVVEYPHCQNKSCITT",
# "DNTRMVCEDRFIQRETLLPLSTVKRPIEWSDEMHESNLDHAIVIPDS",
# "KGWWNAGMGFLHWNKMSDRYDHKGVMTTVPNERHHIDVMCDCCARAC",
# "MHSHIALPQKAWHVPTVYVFRRQAIECWFCHWGSISIDSLMKTQAKQ",
# "HNKGGYYFIHGPMAVEAKSIVHINVTLLGLMIWAWEDVQACPCKCKW",
# "RVWSNKWQMQCRWRSTELVPWGGMKNKQWYHEQDHPANAWEIYVGRT",
# "TAMPICSAVQTDNPWDFMKQHMGDNTHVFCPIEDTKTWVVLRALEPR",
# "YGVDTVYFFHACWEDFLTQSLNCDDGWNRYFWCLPFWQVPEFCHVVA",
# "AMSNPDESQHKVDQNIDCNWENALDHHHEPRVINMCKCHWVYCWLWV"]

# Spectrum=[0,57,57,71,71,71,71,71,87,87,97,97,99,99,99,99,99,101,101,101,113,113,113,113,113,113,115,115,128,128,128,128,129,131,137,137,147,147,147,156,156,156,156,156,156,158,163,170,170,170,172,174,186,186,186,194,196,198,199,200,200,200,208,210,210,212,212,218,227,234,238,241,243,246,250,253,256,257,257,257,259,260,262,267,269,269,269,271,276,278,284,285,287,295,303,303,307,307,309,309,309,311,314,314,315,321,321,323,328,331,340,342,342,342,346,347,352,366,368,371,372,374,380,381,382,385,386,386,390,391,393,404,404,404,406,406,406,408,408,412,413,413,418,418,420,422,434,434,439,441,441,443,443,455,459,461,465,465,467,477,477,479,479,480,487,489,498,505,505,509,514,514,517,519,519,519,519,521,521,522,526,527,532,534,535,538,538,540,542,546,549,560,562,572,576,576,576,576,576,578,581,585,588,590,592,593,599,599,608,609,616,618,624,633,634,635,635,639,645,645,647,647,650,650,650,652,655,661,663,663,663,675,675,675,677,677,677,689,690,690,700,707,710,713,717,721,723,728,732,732,732,732,732,734,734,737,746,746,748,755,762,762,765,771,774,775,776,776,778,778,780,787,788,790,792,797,803,803,806,808,814,818,819,819,833,833,833,835,836,841,845,845,845,847,847,856,860,861,861,863,863,869,875,885,886,891,893,900,902,902,904,906,912,918,920,923,927,931,931,932,932,933,934,934,936,944,944,946,948,948,953,958,962,966,969,970,978,988,989,992,994,997,999,999,1017,1017,1019,1021,1022,1028,1031,1033,1040,1040,1041,1041,1043,1046,1047,1049,1049,1054,1057,1057,1062,1063,1068,1074,1076,1079,1093,1095,1096,1098,1103,1106,1111,1112,1114,1118,1120,1122,1122,1125,1127,1136,1148,1148,1150,1154,1156,1156,1159,1164,1166,1168,1169,1169,1177,1177,1177,1180,1187,1187,1189,1196,1197,1205,1209,1209,1210,1221,1223,1226,1226,1227,1233,1240,1240,1248,1249,1251,1251,1251,1253,1255,1258,1266,1274,1274,1276,1276,1278,1295,1297,1297,1300,1308,1310,1322,1322,1324,1324,1324,1325,1325,1326,1336,1336,1337,1338,1341,1347,1352,1352,1354,1361,1371,1373,1377,1379,1379,1382,1387,1389,1395,1396,1403,1407,1407,1409,1412,1421,1423,1423,1425,1437,1437,1438,1448,1450,1451,1453,1453,1464,1468,1469,1474,1480,1482,1483,1486,1494,1504,1507,1508,1508,1508,1508,1508,1510,1511,1516,1520,1524,1535,1536,1536,1537,1552,1554,1565,1566,1568,1575,1577,1579,1581,1581,1581,1582,1583,1593,1595,1595,1597,1598,1607,1607,1611,1617,1621,1623,1633,1636,1638,1638,1639,1644,1664,1664,1665,1667,1669,1676,1678,1681,1682,1682,1688,1694,1694,1694,1696,1699,1707,1708,1710,1710,1721,1729,1730,1731,1735,1737,1745,1753,1758,1764,1765,1767,1775,1777,1777,1780,1781,1786,1789,1793,1795,1795,1797,1800,1814,1816,1823,1829,1834,1834,1835,1843,1844,1844,1850,1850,1850,1857,1868,1873,1876,1879,1882,1886,1890,1890,1900,1901,1914,1921,1923,1923,1928,1928,1928,1933,1942,1943,1947,1947,1949,1950,1951,1957,1963,1970,1972,1983,1985,1986,1987,1988,1991,1997,1999,2006,2020,2029,2029,2037,2041,2042,2044,2046,2056,2056,2056,2062,2062,2068,2070,2079,2084,2085,2100,2100,2101,2103,2107,2107,2112,2113,2114,2116,2119,2119,2133,2138,2143,2155,2157,2157,2157,2169,2171,2176,2183,2184,2185,2193,2199,2204,2209,2214,2216,2218,2220,2226,2226,2229,2232,2242,2243,2244,2248,2254,2256,2256,2263,2270,2270,2275,2283,2294,2294,2313,2313,2314,2315,2319,2323,2327,2329,2331,2332,2351,2354,2355,2357,2357,2365,2365,2369,2369,2371,2371,2376,2376,2388,2395,2400,2410,2410,2414,2422,2426,2428,2430,2442,2442,2447,2447,2450,2452,2466,2470,2478,2484,2485,2485,2497,2499,2500,2504,2509,2513,2513,2518,2521,2523,2523,2525,2527,2527,2529,2535,2551,2555,2575,2575,2577,2584,2596,2598,2600,2610,2622,2622,2622,2628,2628,2632,2633,2634,2636,2638,2647,2655,2656,2660,2660,2676,2679,2683,2703,2709,2709,2718,2719,2731,2731,2733,2735,2737,2741,2745,2747,2757,2761,2762,2769,2775,2778,2784,2784,2792,2792,2802,2806,2808,2822,2828,2830,2832,2832,2833,2834,2846,2856,2859,2889,2889,2890,2891,2891,2893,2897,2897,2903,2904,2906,2919,2919,2927,2931,2933,2939,2945,2956,2961,2964,2964,2969,2976,2977,2990,2990,3004,3010,3018,3019,3026,3032,3034,3040,3040,3045,3046,3055,3060,3061,3066,3076,3077,3089,3089,3089,3105,3111,3113,3120,3127,3137,3142,3147,3147,3160,3168,3173,3174,3175,3176,3177,3179,3198,3204,3214,3218,3226,3233,3236,3241,3245,3250,3265,3267,3271,3275,3275,3285,3288,3303,3305,3307,3310,3317,3327,3332,3342,3346,3354,3354,3370,3373,3378,3380,3381,3398,3416,3418,3425,3431,3431,3431,3435,3441,3441,3444,3451,3467,3474,3479,3480,3483,3496,3502,3528,3544,3545,3545,3553,3554,3554,3554,3564,3566,3572,3578,3580,3581,3587,3595,3616,3621,3624,3627,3649,3651,3653,3665,3667,3673,3681,3684,3693,3696,3700,3701,3723,3736,3740,3744,3750,3752,3752,3758,3764,3766,3772,3783,3797,3814,3821,3823,3824,3837,3837,3851,3859,3865,3885,3887,3896,3896,3900,3908,3913,3930,3934,3936,3950,3952,3958,3984,3988,3993,4005,4007,4007,4009,4012,4013,4033,4059,4059,4083,4083,4086,4104,4104,4106,4106,4108,4112,4130,4144,4146,4154,4163,4199,4203,4205,4211,4215,4217,4219,4243,4245,4276,4282,4286,4298,4300,4304,4314,4316,4316,4328,4356,4397,4399,4401,4413,4413,4413,4417,4427,4427,4468,4472,4472,4484,4498,4514,4514,4526,4526,4550,4583,4585,4585,4597,4597,4621,4627,4628,4651,4668,4684,4684,4720,4722,4722,4741,4741,4783,4793,4821,4821,4840,4854,4854,4878,4892,4922,4939,4949,4953,4991,4993,5010,5048,5052,5062,5090,5123,5149,5161,5161,5189,5260,5260,5260,5262,5331,5359,5361,5430,5460,5531]
# N=6
# print " ".join(Trim(Leaderboard,Spectrum,N,AminoAcidMass))

def  LeaderboardCyclopeptideSequencing(N, Spectrum, AminoAcidMass):
	Leaderboard=[""]
	LeaderPeptide=""
	sameScore=[]
	mass_spectrum=max(Spectrum)
	scoreLeaderPeptide = score(LeaderPeptide,Spectrum)
	while Leaderboard:
		Leaderboard = Expand(Leaderboard,AminoAcidMass)
		LBcopy = copy.deepcopy(Leaderboard)
		for peptide in Leaderboard:
			ls=cyclicSpectrum(peptide,AminoAcidMass)
			mass_ls = max(ls)
			if mass_ls==mass_spectrum:
				pscore=linearScore(peptide,Spectrum,AminoAcidMass)
				if pscore>scoreLeaderPeptide:
					LeaderPeptide = peptide
					scoreLeaderPeptide=pscore
					sameScore=[LeaderPeptide]
				elif pscore==scoreLeaderPeptide:
					sameScore+=[peptide]
			elif mass_ls>mass_spectrum:
				LBcopy.remove(peptide)
		Leaderboard = LBcopy
		if Leaderboard:
			Leaderboard = Trim(Leaderboard,Spectrum,N,AminoAcidMass)
	return sameScore


AminoAcidMass = loadMass("integer_mass_table.txt")
#print LeaderboardCyclopeptideSequencing(10,[0,71,113,129,147,200,218,260,313,331,347,389,460],AminoAcidMass)
print LeaderboardCyclopeptideSequencing(1000,[0,97,99,113,114,115,128,128,147,147,163,186,227,241,242,244,244,256,260,261,262,283,291,309,330,333,340,347,385,388,389,390,390,405,435,447,485,487,503,504,518,544,552,575,577,584,599,608,631,632,650,651,653,672,690,691,717,738,745,770,779,804,818,819,827,835,837,875,892,892,917,932,932,933,934,965,982,989,1039,1060,1062,1078,1080,1081,1095,1136,1159,1175,1175,1194,1194,1208,1209,1223,1322],AminoAcidMass)


