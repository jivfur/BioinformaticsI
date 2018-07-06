import sys

def Composition(k,Text):
	return sorted([Text[i:i+k] for i in range(len(Text)-k+1)])

def GenomePath(Dna):    
	t = len(Dna)
	return Dna[0]+"".join([Dna[i][-1] for i in range(1,t)])

# if __name__ == "__main__":
# 	lines = sys.stdin.read().splitlines()
# 	print(GenomePath(lines))

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


def DeBruijn(k,Text):
	k-=1
	kmers = [Text[i:i+k] for i in range(len(Text)-k)]	
	graph = [(kmers[i],kmers[i+1]) for i in range(len(kmers)-1)]	
	Dna=list(set(kmers))
	Dict={x:[] for x in Dna}
	for t in graph:
		Dict[t[0]].append(t[1]) 
	return Dict

def DeBruijn(Patterns):




# dict = DeBruijn(2,"TAATGCCATGGGATGTT") 
# keys = sorted(dict.keys())
# for item in keys:
# 	if dict[item]:
# 		print(item+" -> "+",".join(dict[item]))


# dict = DeBruijn(3,"TAATGCCATGGGATGTT") 
# keys = sorted(dict.keys())
# for item in keys:
# 	if dict[item]:
# 		print(item+" -> "+",".join(dict[item]))



# dict = DeBruijn(4,"TAATGCCATGGGATGTT")
# keys = sorted(dict.keys())
# for item in keys:
# 	if dict[item]:
# 		print(item+" -> "+",".join(dict[item]))






# if __name__ == "__main__":
# 	k = int(sys.stdin.readline())
# 	lines = sys.stdin.readline()
# 	dict = DeBrujin(k,lines)
# 	keys = sorted(dict.keys())
# 	for item in keys:
# 		if dict[item]:
# 			print(item+" -> "+",".join(dict[item]))


