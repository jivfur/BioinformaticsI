import random


def  PatternToNumber(Pattern):
	SymbolToNumber= { "A":0, "C":1, "G":2,"T":3}
	if len(Pattern)==0:
		return 0
	return 4*PatternToNumber(Pattern[:-1])+SymbolToNumber[Pattern[-1]]

def NumberToPattern(index,k):
	NumberToSymbol ={ 0:"A", 1:"C", 2:"G",3:"T"}
	if k==1:
		return NumberToSymbol[index]
	prefixIndex = index//4
	r = index%4
	symbol = NumberToSymbol[r]
	prefixPatter = NumberToPattern(prefixIndex,k-1)
	return prefixPatter+symbol

def ComputingFrequencies(text, k):
	freqArray=[0]*((4**k))
	for i in range(len(text)-k+1):
		freqArray[PatternToNumber(text[i:i+k])]+=1
	return freqArray

def ClumpFinding(genome, k, L, t):
	FrequentPatterns = []
	Clumps=[0]*((4**k))
	freqArray = ComputingFrequencies(genome[:L],k)	
	for index in range((4**k)):
		if freqArray[index]>=t:
			Clumps[index]=1				
	for i in range(1,len(genome)-L+1):				
		freqArray[PatternToNumber(genome[i-1:i-1+k])]-=1
		index =PatternToNumber(genome[i+L-k:i+L])
		freqArray[index]+=1		
		if freqArray[index]>=t:
			Clumps[index]=1
	for i in range((4**k)):
		if Clumps[i] ==1:
			FrequentPatterns.append(NumberToPattern(i,k))
	return FrequentPatterns


# genome="CGGACTCGACAGATGTGAAGAACGACAATGTGAAGACTCGACACGACAGAGTGAAGAGAAGAGGAAACATTGTAA"
# genome="AAAACGTCGAAAAA"
# genome="ACGTACGT"
#genome="CCACGCGGTGTACGCTGCAAAAAGCCTTGCTGAATCAAATAAGGTTCCAGCACATCCTCAATGGTTTCACGTTCTTCGCCAATGGCTGCCGCCAGGTTATCCAGACCTACAGGTCCACCAAAGAACTTATCGATTACCGCCAGCAACAATTTGCGGTCCATATAATCGAAACCTTCAGCATCGACATTCAACATATCCAGCG"
#genome ="CCGCCCGCCATGGAACTATGTTGACAAGTTAATTTTACATGACTGCGCGACTGCGAAGAGATGTAAGCAGCCTAGATTCAACCAATCACATCTACCCGTCACTATCCCGCGCACACATTCCTCTTAGTAACAAGGGGCCTCTCTTAACATGAAGTCTGCCTTGTCTCTATAAAGGCAGCAGACCCAAGACAAAGAGCTGCCTCCGTTGAGCTAGAGTCTCCAGCGCATCGAGTGCATATGGACAAGACGACTGTCCTTAAACTGGGTTGCGAGGCCAAAAGGCTCCAAAGAGCTAAAGGCCAAAAGGCGTAGGTATGGACCGGATGCGGTGGCCAAAAGGAGACCGAGCGCGGTCAAGTACGGCCAGGCCAAAAGGCCGGCCAAAAGGGATAATCAATTTGTCTTAACGGCCAAAAGGCTAACGCAATTTGTCTTTGTCTGGACGTCCTTGTGCAGCCGGCCAAAAGGCTTCCTCGACAATTTGTCTTATACCGCGGGCCAAAAGGTTAAGGGGGCCAAAAGGGTTGTCTAGCCAAGGCCAAAAGGGAACAGCGCGGCCAAAAGGGCCAAAAGGAACATACCGATTGATAGGCCAAAAGGTTGTCGGCCAAAAGGGCTAGCGGATATATTCCTCTCTTGGCCAAAAGGTTAGCGGGCCAAAAGGGGCCAAAAGGCCAAAAGGTCCCGGTCAATTTGTCTCTTTTTATATCAATTTGTCTCAATTTGTCTCTGATCGCCCCTCAATTTGTAGAACAAGCAGGGTGAGCGGGGTAGAACAAGCAGATAGAACAAGCGCCAAAAGGAAAGGACCTAGCGGGCCAAAATAGAACAAGCGCCTTAGAACAAGTAGAACAAGCACGTTTAATCGAAAAGAGTATGCTAGAACAAGCGATCTAGCGTGAGCGGCAGTATCTAGAACAAGCTGTCTTAGCGTGACAACACTAGAACTAGAACAAGCATTTGTCTGAGTTTCTGTACATTTTGCTAGATCTAGGCGAGATTATAGAACATATTTCTGTACACCGGCACTATAGCGTGAGCACCGGTTTTTCTTTTCTGTACAATTTCTGTACAGCGATAGAACAAGCCGTAGCGTGAGTAGAACAAGCAGCGTTTCTGTACATACAAGAATTTCTGTACATAGAACAAGCCGTGAGCTCGTTAGAACAAGCCCGAGGGAAACTGTGAATATGAATTGGGCCGTCAAAGTTTCTGTACACCTTCTTTCTGTACAAAGCAAACCTCCTGTCCTTTTTTCTTTTCTGTACATCTGTACAAAGCGCTTTCTGTACAGATTTCTGTATTTCTGTACAAGAATTTCTGTACACAAGCACTGTGTATTAAAACTACCAGCATGTTTCTGTACTTTCTGTACAGTGTTTATAGATTCTCTCAACTTAAGAAGCAATTTCTGTACACCCTTTTCTGTACACTCACCTTCGCTAGCTTTGTGTTTTTCTGTACATCACCTTTCTTTTCTGTACAGTAACGGTCAGTCCGGACCGCAAGTATATATCTTTCTGTACACAATTTCTGTACACAAGCAGTAACGCCGATCTCTGGGATTTTGGAGATTTTCTTGAGGGGAAACCCGGCTGGTTCCAGGGAGTTGAAAACTAGGATAAAGCTGAATCCCCTGTGTCGATGATTGTATAACTGGCCTTTATTGTCATCCAGCGGCCCGCCCGGCCAGGATTCGTCTACAGTACAAAATTCGGGAAGATAGTCCTATCCGAACTATTTTTCTACAACCTATTAGTGCTGAACGCAAACGCTAAGTACAATAATAATTACACCTATTAAACGCGACCAAGCTTTTACTGCACGATGAGAGCTCCCCACAACTAGATAAGATTTCCCTGTATGACTCCCGTCAGTAGCGAGCACCAGGAGAGTACCGGGGCAGTCACCACACAAAGTCAGTTATTTGGTGGTCTGCTGGCCTATATTTGATCAGAAATTTCTCTCACGCTCCTGGTTACCCCGGTCTTTGTTGAACGCACGGTAGGACCATAGGGACAGAGGCCCGACTGATGAGACGGCACCTGATAGCGGTTGGATCTTTTAACTGGATGTGGATGCCTAACTGGATTAACTGGATGACACGTGGGAACGGGTTAACCAGAGCTAACTGGATGCCACCTATAACTGGATGTTAAACATTCTGTACACTAGCGCTGCTAAGATATAGGTTATAACTGGATGCAGTAACTGGATGGTAACTGGATGATGAGGGCAACATGTTTGCTGGAATTAACTGGATGAGCTCATAGACATTATGTTATGTTCTAGACCTTCTTACGATAATAACTGGATGCTTAACTGGATGGTGACCGTTGGGGAAGAGCGCCCAAACGCATCATAATAACTGGATGTGCGATCTCCGGCACAGCTTGTCATAAGTTGCGAATTCACAGGTGTCCTAACTGGATGCAGCTTTTCCCAGACAGGTCTCCCCAGGTCATGGGCCACTTGATACAGATAACTGGATGGGGGTAACTGGATGAGTTGTAACTAACTGGATGTAACTGGATGGCCTCCAGTATCGCTTTCTAGTAGGTGTATTTTAACTGGATGATAGTAACTGGATGTATCAATATAACTGGATGAGTGATCTAACTGGTAACTGGATGGAGATTTATGAAGTTAACTGGATGAGCGACCGTGTGTCGAGGCGTACACACTTATGCGGCTAACATTCTATACCAGCTCAGACTTCATGACACACCGAGAGGGATCTACACTACAAGTTGGATACACCCACCCATCCGAGTATGAAGTCCATAAAGGCACTCAGATTCAGAAAACCGACGGGCTAGTTAATCTAGCCATTAAGGGCGACATCCAGGTGCATGGGTTGTTTGATCATGGATGAACAGCCCCCAGTGATACGGACAGCTTAAATCGTAGCCGTGACGTCTACCGGCGGACCACAGCACCCAGAAGTGGCATTAGCACGCTGTTGTTGTTTTTCAATCGGCACTAGGAGCTTAGTTGCACTTATTTCATTTATCACAATTGAAGTCATGCGCGAATGGCAATCCAACGTCCTAATTTCTGTGAGTGTCGATAGCCCGGGTGCAACATAAATGAGCCCTATTATGGCTATGGTGTTGATTGAAGCCCTAGGGGTGGGCATTTCCTAGGATTCTGGCAGGGCTCAATGAGTGGTACACCCTAATTCACCGGTGATAAGGACGCCCGCGCAACAGCAGAACAAAGCGCGGCCTCGTGATAAATTGGGCCTGCGATCACACCTGGGCCTGCGACCGTTAGCTTGAAACCTGTTGGGCCTGCGTTTGTCAGGATTTATTGTATGGGCCTGCGGTGGGCCTGCGTTGGAGGCGCCATGGGCCTGCGTGCGGAGCAGCGACAAAGGGCACACTGACGGTCGCACTATTTCTGGGCCTGGGCCTGCGGCCTGCGGCGGTGGGCCTGCGCCCAATGGGCCTGCGATTTGGAAAATACCCCTTCGACAGTGGGCCTGCGAGACGTTATCTGGGCCTGTGGGTGGGCCTGCGCGTTGGGCCTGCGGGGGGGCCCAGCAGGGTCCTGGTGGGCTGGGTGGGCCTGCGTACAAACGACACTGTTTGTGGGCCTGCGGGGAGGTGGGGCGATTCCTACGGATGCATGCACTCAGTGGTTAATAATTTGCTCTGATGGGCCTGCGCTGTGTACCGAATGGGCCTGCGAGCTGGGCCTGCGTACTTTATGTTACAGGGTGGGCCTGCGGCCTGCGGACATGCAATAAGGCGGTGGGCCTGCGGGCATCGGATTACGAAGTTGGTTGAACACCCGCATTCAAAAGAATACGAAGTTGTACGAAGTTGCCTGTGCTCCAATATATACGAAGTTGGGATATTTTCTCCATTACGAAGTTGGTTGTACGAAGTTGGCGGTTACCTACGAAGTTGCAGTGATACGAAGTTGATTGAAAAGCTAGAGCCCTACGAAGTTGGGACAGAACGGTGTACGAAGTTGGCGACATATAGAGGTACATAGTCAGCTCCTACGAAGTTGGATAGCTACGAAGTTACGAAGTTGAATTGATTTAGATGCGTTTGCCAGTAATGGTACGAAGTTGACACTGGTAAGCTTATATTGCTTACGAAGTTGGAGTAACTGCCGCTGTAAACCGGACGTCCCAATTACGAAGTTTACGAAGTTGCCGACTGCCATCGCATACTTTCGGTTGAAAATACTACGAAGTTGAGTTGTTACCAAGTACGAAGGGGTTGAAAATAAAAATATTACGAAGTTGGCAGGGTGTTGAAAATAAGAAACCAGTTGAAAATACCTTAGGCTGACAGTTGAAAATACGAAGTTGTTGTGACGGCCACCTACGAGTTGAAAATAGAAAGGAGTTGAAAATATGCTGGTGCGAGTATCGCAATGGATCGGGGTTACGTTGAAAATAGGGAGGTTGAAAATAAAATACTAAGACAGGTTGAAAATAGTTGAAAATAGACACCCGCGCATCGCGCATTGGTTGAAAAGTTGAAAATACGTTGAAAATAAGGAGCGGGTCGGGCCGGGGTTCGTTGAAAGTTGAAAATATGGTTGAAAATAAGTGGAGGAGGAGAATTTAGGTTGAAAATAGCATTACGTTGAAAATAGTTGAAAATAAAAATACGTTGAGGGCAACACCTGTGGTTGAAAATAGGACACCGTTGAAAATACGACCTGTTGAAAATATAGATGAATTATACTGACGAGGACAGCATTCGTTGAAAATATAAGATGGATTAGGCTCCAAAGTTCCTATGCCGCATTGACGTTGCGTTGCTGGACAGGTTAGTGAACAATTCACCCTGAGTCAACCAACCGAGTACCCTTATTACCATGACTATCACCGGCGTTCGTGATTGAAGATTGGGACGTATAAGTTATTACTTATTACCATTCTTGTCGGCTTATTACCATTACCATCCATGCTTGAACAAGGGTTCGATTGGTATGACTGATTGCATTATTATTACCATATTACCATCCTTATTACCATCCATACCATCGCCTTCAGGACCCCGGTGCGTGTTATTACCATAATTATTACCATTAACATGTCGGCCTTATTACCATTATTACCATACCTTGTCTAGTGATACAATCTTACGTCGGCTTACTACTGCGGATTTATTACCATATTATTACCATCGGCCAATCTGGAAATAAGAGCTATCAGGCTCTGCTGGGACTCGGAATACTTATTACCATGCTAGGTCCCGAGTAAGAGTCGAACCGGTTTTTATTACCATTCCACCTAATCAGGCCCTATCCACATCCACCTTTATTTTATTACCATCATCCACCTTATTACCTTATTACCATAAGCTATTATCCACCTAAAATCCACCTAACTTCCTTATTACCATCTTTTATTACCATCACGCAATCCACCTAAGCCCTGCCTTGATTAAAGCATCCACCTAATCAGCCAACCAATATCCACCTAAACCATCCACCTAATTAGTGATCCACCTAATCCACCTAAAGTCAATCCACCTAAATCCACCTAATTTCCATATCCACCTAAAATCCACCTAAATCAATTTCCAAAATTGCGAATACACCCATCCACCTAATAAACATCCACCTAAGTTTATTTAGAACACCCGGTGAAACTCTACGAACGTTTTATTGCCGCACCAGAGCCAACGAGTCTTCGGCCTTTATTCAATCCACCTAACTATGTGAAGGCGCTAATTCGGGTCGTGGATTCTCGCAGAGTGAAGGCGCCGGTGTGGATGTCGAAATTCCTATACAATCCACCTAATAATCCACCTAATCCAGTGAAGGCGCGCACGCACGATAGCATCACGGTGAAGGCGCGGTGAAGGCGCCTAATTCGGATTGTGTGAAGGCGCTAACTCGCGCACTAGTGAAGGCGCACAAACTATATTTCCCCTCAGCATGGCCAAGTGAAGGCGGTGAAGGCGCGGCGCCGCTCCCGCGGCGAAATGGGGTGAAGGCGCCCGTGAAGGCGCCAAAGGCGGGTGTAGATGACGGACAGCTTGGTGAAGGCGCACAAAGTGTGCTAGTGGGGCTCCCCCAGTATCGCTTGACGGTGAAGGCGCACCAGATACGTGAAGGCGCCAATGACGCGTATCTGTGAAGGCGCCGCGTGAAGGCGCCGAAAAGTGAAGGCGTGAAGGCGCATGAGTGAAGGCGCATTGAGGTGAAGGCGCGGTAGCGGTGAAGGCGCATCTAGTGAGTGAAGGCGCGAGTGAAGGCGCACGCATGGCGGGATAGGTCAGCATGCGGGGAGAAAGGCCAGGGGGAGAGATCGTCTTGCATTCCAAATGAACTATCCACAGCGTCAAGAGTCCTACGCTCCGGGGCCATACTAACTCCCGAGAACTCGGACCATTGTAATCAGACCTGGCGGACAGATGATTGGACCCTCTAAAACATTCCTCGTCTCGTTAAATCCAGCAGAACAAAGTTGGAACTCAAAAACGTCGACACCTGTCAGGCTGCAGTGTACGTGGCGACTAAGTCAGTACGGAGTGGTTGGATCCAGCCGGCTGACTTAATGAGTCTCTGACTCATCCGGCGAGCAGGGGCTTTCTATTTTGTCTTAGATGAGTATAAAACCCTTGGCTTCGTGGTATAAATGTGGTCCCGGTCTCTTTTACGCCCTCAGCTTCACGTATGGGCGTTACTCAAAATTATAATCAGAGACGTGGAAATTTTAATCCGCGATCCATTATGTCGACGGCGGAGGATCTAGACTAGACGGATCTGCGCTCTATAGATGAATGGCCTATAGACGCTTCATAGGCCTGGGCGATAGCGTTCCAACAAAAGGATGTTCCCAGTAGAGTAGGCCCATAAATTATTTACACTTGCGTCGCACTGGTGCACTGTAAGACTTCCGCTCGACTGGATCAGTAATAACGTCGGTAGAAAGTTAAGGATAGCTACAACGTAACTGCGGCTAAAAGAGACCGCAAGCGAGCAAATGTTGACACAGATAAGATACTCATGGCCAACCGAGTGGGATATACAGCCTGCCGTGGCCATAGATGCCCTGCATGGATCTCTTCCGGCAGCTTTGTGCGGACTGAGTATACACCTCTTTGGGGCAGAGCCGGATTGGGGACATTTTGGGCACACACGCGCGATAAACCGCTCGGTTGAAACACCTAACAACGACTATAAACTATGGCTATCCGAGCTCGTCCATATCAATCTTCTACGTATGGTTCTTCCCGGTCGCCCAAGTTACCAACAATAGTCAAACCTTCTTCGAATGTTTTTTCCAATTCCATGCGAAAGCTGAAACATTTTCAAGGTGTGCCACACGCTCGCGCATTGCCGCTTCCGCCCTCAGTGTCTCTGAAGCGGGCCGCGCGCCACAGTCTAATCTGCCTATAAACTATCGGTGGCGGGAAGGGTGGTGGGCAGCAGCTCCTACGTCGTATCGGACGACGAGTAGCGATGACACAGTTGGCTGGGTACCAAACAGCTCCAGGTTCCTGAGCCGTGTTCTGCGACACACCGCAATTTTATTTTCGTGCTTAAGTCATCATCGCTTTGGATCCAGTGAGTCATAGCCTGTAGAATTGATGGAGAAGACCCGAAACTGTTGGGGAAATGACCCCTTCCAAGTTCTATGGTGGGCGGTGTTTTCGTGCTACCGGTGATTCTGGGCGCTGGGGCTTGCCAAATGGGTAGGATAGTTACTTTGAACACTAACATTTTGTGCTGCCGACTGGCGATACGTGGGTGTCAAGCTAACCACTTCGCTGTCTGATACACGTGCCGATGCGCGTTAATGGTTGGGAACCTTGGAATCTTGGTCCTCACGTGGGACGATGTTGACATCGCCCCGGTCATTATAGCCTTAGGACGGCGGTGTACGCCCATCGGAAGCAATCGATGCCTCAGTGACCTCCTGATTGTGCTCGTTTACCGGAGATTCTCTCCAAGTATAATTGCACTCCAGACGGACAGTGTGTCAAGGTAGGGGGACTAGGTGTAGTCGAAGTGCCCTGAGACTCCGTCACGTAAGGGATCGGATATAAGTTTGAACATCTATCAATAGCAAATACGGGGGCACGATAGAGCCGGGGCAGATGGCTAGCGGTGTGCAACTTGGCCAAAGTCACGTACGGCACTTAGAGGGATATGGCGGGCCACCAGCAACTCGGGAACAACTGTTCCCTTGACTCCGACAGTGTGGCTGTGTGTAAGCCGCTCTCTCCTGCTTCCAGGGACGATTACTAGGCATTCGGAGGTTAGGATAAAAGGGTGCAGCGAGGCGGTCAACATTACGTCGTGCCAATTGGGCTCAAGAATGCGCTTCATAAAAGACTCATTCTAGGGGGCTACCATGGCGACGAAATCGAGTGAGAAACCTGGGCAGCTTAGAGAATAGTCTGGTCCGCTATTCATCAGTAGCTGGACGTTAACTGATCTTCTCCTATTGCCTAGTCATTCAGTCTTCTTTTGGACCGCGCCTGACTCCCGGTAGCCATAAAGCCTTAGCGGATGCAAGATTCGTAGTTAGCAAACTCTGGTTCCGTCTGGCTGGCTTCGAAGGCTAATGGGTAAGACCTGCAGACAACTCCACGGACGAACGGGTGTTGAGCGCGGCGGGGCACCGAGGACGGCCCAGCCACCTTAGGAGGTGTGAGCCAAACTTGCAATACTATCAGGGTGCGCCTATGCGGCAGTATATAACCGCACCCTCGGGAACAGAATTTGGGAGAACTCTCGTGCTTGTACTTAACGCAAGTCTGTCCGTTTCTTCGATAGCCCAATCCAAACGAATTGCGCTGACGATAAGTGTAGGTCCAATCGTGGTGCCGTCGCACAAGTCTGTTGGGCCACGGAGTGGCTAGGACGAGGTGGGGTTCGGCAGTCCAGAACGCTCACGCAAGTAGGAGTTCGTTTGAATAGCGGTCTACATACGTTAGCTAACTAGGATATCCCACTATCCCACCGTATCCCACCGTATCCTATCCCACCGCACCGTATCCCACCGTATCCCACCGTATCCCACCGTATCCCACCGTATCCCATATCCCACCGCCTATTATCCCACCGTCCCACCGTATCCCACCGTATCCCACCGTATCCCACCGTATCCCACCGTATCCCACCGTATCCCACCGTTATCCCACCGTATCCCACCGTATCCCACCGTATCCCACCGTATCCCACCGTATCCCACCGTATCCCACCG"

def PatternCount(Text, Pattern):
	count=0
	for i in range(len(Text)-len(Pattern)+1):
		if Pattern == Text[i:i+len(Pattern)]:
			count+=1
	return count

# print PatternCount("ACTGTACGATGATGTGTGTCAAAG", "TGT")

def FrequentWords(Text,k):
	count=[]
	FrequentPatterns=[]
	for i in range(len(Text)-k+1):
		count.append(PatternCount(Text,Text[i:i+k]))
	maxCount = max(count)
	for i in range(len(count)):
		if count[i]==maxCount:
			FrequentPatterns.append(Text[i:i+k])
	return list(set(FrequentPatterns))

# print FrequentWords("TAAACGTGAGAGAAACGTGCTGATTACACTTGTTCGTGTGGTAT",3)


def ReverseComplement(Pattern):
	dict={"A":"T","T":"A","C":"G","G":"C"}	
	return "".join([dict[x] for x in Pattern])[::-1]

# print ReverseComplement("GATTACA")
def PatternMatching(Pattern, Genome):
	k=len(Pattern)
	t=len(Genome)
	return [i for i in range(t-k+1) if Pattern==Genome[i:i+k]]

def Skew(Genome):
	vals = {"A":0,"C":-1, "G":1,"T":0}
	skewArray=[0]
	for i in range(1, len(Genome)+1):
		skewArray.append(skewArray[i-1]+vals[Genome[i-1]])
	return skewArray


# def MinimumSkew(Genome):
# 	vals = {"A":0,"C":-1, "G":1,"T":0}
# 	skewArray=[0]
# 	minValue = 1000
# 	for i in range(1, len(Genome)+1):
# 		skewArray.append(skewArray[i-1]+vals[Genome[i-1]])
# 		if minValue > skewArray[i]:
# 			minValue = skewArray[i]
# 			indexes=[i]
# 		elif minValue ==skewArray[i]:
# 			indexes.append(i)
# 	return indexes

def MinimumSkew(Genome):
	vals = {"A":0,"C":-1, "G":1,"T":0}
	skewArray=[0]
	minValue = 1000
	for i in range(1, len(Genome)+1):
		skewArray.append(skewArray[i-1]+vals[Genome[i-1]])		
	indexes = [i for i in range(len(skewArray)) if skewArray[i]==min(skewArray)]
	return indexes

# print "MIN SKEW: ",MinimumSkew("CATTCCAGTACTTCGATGATGGCGTGAAGA")


def MaximumSkew(Genome):
	vals = {"A":0,"C":-1, "G":1,"T":0}
	skewArray=[0]
	for i in range(1, len(Genome)+1):
		skewArray.append(skewArray[i-1]+vals[Genome[i-1]])		
	indexes = [i for i in range(len(skewArray)) if skewArray[i]==max(skewArray)]
	return indexes

#print Skew("CATTCCAGTACTTCATGATGGCGTGAAGA")
# file = open("dataset_7_6.txt","r")
# text = file.read().strip()
# print MinimumSkew(text)

def HammingDistance(p, q):
	hd = 0
	for pi,qi in zip(p,q):
		if pi!=qi:
			hd+=1
	return hd


# print "HAMMING: ",HammingDistance("CAGAAAGGAAGGTCCCCATACACCGACGCACCAGTTTA","CACGCCGTATGCATAAACGAGCCGCACGAACCAGAGAG")

def ApproximatePatternMatching(Text, Pattern, d):    
	L=len(Text)
	k=len(Pattern)
	return [i for i in range(L-k+1) if HammingDistance(Pattern,Text[i:i+k])<=d]

 # file = open("dataset_9_3.txt","r")
 # l1 = file.readline()
 # l2 = file.readline()
 # print HammingDistance(l1,l2)

# file = open("dataset_9_4.txt","r")
# Pattern=file.readline().strip()
# Text=file.readline().strip()
# d=int(file.readline().strip())
# print ApproximatePatternMatching(Text,Pattern,d)


def ApproximatePatternCount(Text, Pattern, d):
	L=len(Text)
	k=len(Pattern)
	return len([i for i in range(L-k+1) if HammingDistance(Pattern,Text[i:i+k])<=d])
# file = open("dataset_9_6.txt","r")
# Pattern=file.readline().strip()
# Text=file.readline().strip()
# d=int(file.readline().strip())

# print "COUNT1:", ApproximatePatternCount("TACGCATTACAAAGCACA", "AA",1)
# print ApproximatePatternCount("CATGCCATTCGCATTGTCCCAGTGA", "CCC",2)

# print ApproximatePatternCount(Text, Pattern, d)
	
def Neighbors(Pattern, d):
	nucleotides = ["A","C","G","T"]
	if d==0:		
		return [Pattern]	
	if len(Pattern)==1:
		return set(nucleotides)
	Neighborhood = set()
	SuffixNeighbors = Neighbors(Pattern[1:],d)
	for text in SuffixNeighbors:
		if HammingDistance(text,Pattern[1:])<d:
			for nucleotide in nucleotides:
				Neighborhood.add(nucleotide+text)
		else:
			Neighborhood.add(Pattern[0]+text)	
	return Neighborhood

# def ComputingFrequenciesWithMismatches(Text, k, d):
# 	close =[0]*(4**k) #All the posibilities.	
# 	for i in range(len(Text)-k+1):
# 		Pattern = Text[i:i+k]		
# 		Neighborhood=Neighbors(Pattern,d)
# 		print Neighborhood		
# 		for neighbor in Neighborhood:
# 			aproxPattern = ApproximatePatternMatching(Text,neighbor,d)			
# 			for index in aproxPattern:
# 				print Text[index:index+k]
# 				close[PatternToNumber(Text[index:index+k])]+=1	
# 	return close

# def FrequentWordsWithMismatches(Text,k,d):	
# 	FrequentPatterns=[]	
# 	count=ComputingFrequenciesWithMismatches(Text,k,d)
# 	print count
# 	maxCount = max(count)
# 	for i in range(len(count)):
# 		if count[i]==maxCount:
# 			FrequentPatterns.append(Text[i:i+k])
# 	return list(set(FrequentPatterns))


def FrequentWordsWithMismatches(Text, k, d):
	close =[0]*(4**k) #All the posibilities.
	Neighborhood=[]
	for i in range(len(Text)-k+1):
		Pattern = Text[i:i+k]		
		Neighborhood+=Neighbors(Pattern,d)	
	Neighborhood=list(set(Neighborhood))
	for neighbor in Neighborhood:			
		close[PatternToNumber(neighbor)]+=ApproximatePatternCount(Text,neighbor,d)
	maximum = max(close)
	return [NumberToPattern(i,k) for i in range(len(close)) if close[i]==maximum]


def ComputingFrequentWordsWithMismatches(Text, k, d):
	close =[0]*(4**k) #All the posibilities.
	Neighborhood=[]
	for i in range(len(Text)-k+1):
		Pattern = Text[i:i+k]		
		Neighborhood+=Neighbors(Pattern,d)	
	Neighborhood=list(set(Neighborhood))
	for neighbor in Neighborhood:			
		close[PatternToNumber(neighbor)]+=ApproximatePatternCount(Text,neighbor,d)
	return close


def FrequentWordsWithMismatchesAndReverseComplements(Text, k, d):		
	array1 = ComputingFrequentWordsWithMismatches(Text, k, d)
	array2 = ComputingFrequentWordsWithMismatches(ReverseComplement(Text), k, d)
	close = [array1[i]+array2[i] for i in range(len(array1))]
	maximum = max(close)
	return [NumberToPattern(i,k) for i in range(len(close)) if close[i]==maximum]



# Text = "AGTAGCAGCATTAAGCATTAAAGTTGCAGCATTGCATAAGAAAGTTAAAGAGGCATTGCAGCATTGCAGCATTTAAGAGGCATAAGAGGCAAGTTAATTGCAGCAAGTAAGAATAGCAAAAGAGTAGCAAGGCATTAAGCAAAGCAAATTAGTATATAAGAGGCATTAGGCAAAAATAAGGCAGCAAGAAGCAAGAATATAGCAAATTTATAAGTTAAAGAGAAAAGCAGCAGCAAGTTAGAGAAAG"
# k= 7
# d= 2
# "AAA","AAT","ACA","AGA","ATA","ATC","ATG","ATT","CAT","CTA","GAT","GTA","TAA","TAC","TAG","TAT","TCT","TGT","TTA","TTT"
# Text = "ACGTTGCATGTCGCATGATGCATGAGAGCT"
# k= 4
# d= 1
# output=["ACAT","ATGT"]
# output2 = ['ATGC', 'ATGT', 'GATG']
# # print FrequentWordsWithMismatches(Text,k,d)
# print " ".join(sorted(FrequentWordsWithMismatchesAndReverseComplements(Text,k,d)))




def MotifEnumeration(Dna,k,d):
	Patterns=[0]*(4**k)	
	count=0
	Neighborhood=[]	
	lines=0
	for line in Dna:
		lines+=1
		for i in range(len(line)-k+1):
			Neighborhood+=(Neighbors(line[i:i+k],d))	
	Neighborhood=list(set(Neighborhood))
	for neighbor in Neighborhood:		
		for line in Dna:			
			if ApproximatePatternCount(line,neighbor,d)>0:
				Patterns[PatternToNumber(neighbor)]+=1
	return [NumberToPattern(i,k) for i in range(len(Patterns)) if Patterns[i]>=lines]





def DistanceBetweenPatternAndStrings(Pattern, Dna):
	k = len(Pattern)
	distance = 0
	for line in Dna:
		hm = 200000
		for i in range(len(line)-k+1):
			p = line[i:i+k]
			hm2=HammingDistance(p,Pattern)
			if hm > hm2:
				hm = hm2
		distance+=hm
	return distance


# file = open("dataset_5164_1.txt","r")
# Pattern = file.readline().strip()
# Dna=file.readline().split()

# print Pattern
# print Dna
# print DistanceBetweenPatternAndStrings(Pattern,Dna)


def MedianString(Dna,k):
	distance = 100000
	median=[]
	for i in range(4**k):
		Pattern = NumberToPattern(i,k)
		d = DistanceBetweenPatternAndStrings(Pattern,Dna)
		if distance > d:
			median = [Pattern]
			distance = d
		elif distance==d:
			median.append(Pattern)
	return median

k= 7
Dna = ["CTCGATGAGTAGGAAAGTAGTTTCACTGGGCGAACCACCCCGGCGCTAATCCTAGTGCCC",
"GCAATCCTACCCGAGGCCACATATCAGTAGGAACTAGAACCACCACGGGTGGCTAGTTTC",
"GGTGTTGAACCACGGGGTTAGTTTCATCTATTGTAGGAATCGGCTTCAAATCCTACACAG"]

print "MediaString: ",MedianString(Dna,k)


def Pr(Text,Profile):
	multi = 1
	for i in range(len(Text)):		
		multi *= Profile[Text[i]][i]
	return multi


Profile={"A": [0.4, 0.3, 0.0, 0.1, 0.0, 0.9],"C": [0.2, 0.3, 0.0, 0.4, 0.0, 0.1],"G": [0.1, 0.3, 1.0, 0.1, 0.5, 0.0],"T": [0.3, 0.1, 0.0, 0.4, 0.5, 0.0]}

print "Pr( Pr(TCGGTA|Profile): ", Pr("TCGGTA",Profile)

def ProfileMostProbableKmer(text, k, profile):
	kmer = ""
	maximum = -1    
	for i in range(len(text)-k+1):
		pr = Pr(text[i:i+k],profile)
		if(maximum<pr):
			maximum = pr
			kmer = text[i:i+k]    
	return kmer


text="TACCTCCCGGGGTTCCATCTCACCATCACGCCCCGTCCTACGCGGTAGAACGACGCAGTGTGGCCCCTATCGTCGAGTCTCGGCCTCTATGATCGTTACTAAGCCGAGGAGGGCGCATGGACGCTGAGCACGTCAACACCTACCATGTCGGCCGGTACTCACGCACTACATCCGAGACCTTTGTACCGTACTTCAAAACGTTTACGTTGGTCTGCTGATGGGCTAAAATTCAGTGGTGCCATTACACTCCGATCGGCCCGTTAGATCCCCCAGAATCTGATCTTAGTAGTGCTTCACCGCCTCGACCCTACTCGGGGCGTATAGTCCTGTACCCACCCCCTTACAACAGACAATAGACCGGGCACAAGTCGAGTGAGATAAAGACCCCACGGGAGTGTTCGTAATGTTGGCAGCCTTCTTCGGTTAAATGACAAATATGCATACCATTTGTGTTAGTAAATATAAGAGGGGTCCTAATTCTCGCCGAGTTGAACTCATGAATACCACGTGAAGCGTTATTCCGGAAAGATTCTAGGATCTCGAAACTTGTACGCTGCTCTCTAATGAACCGATGCGGCCTACGATGATTACAAACCCTCGCACACAATTGCTTACTATCGCCTCTCAGGTCCAGAACGGTAGCTAACAGTCGGATGGCGCTCTATTAAACAAGTTCAGACTTGAAGGCCCACAGCCCGGGCTTAACGTTACTCCCATGAGCATGCGTGTAGCACGACACGTGCGTGCTACAATTTCCCCAAAGATATTTATCCTGGTTAGGCATGCAGTTTTATCGACCACTAGCCCGACATCCAATCTATATCTGCAATTTCTAGCCAGGTCGTTTTAGAAGCGAGCGTATTAGCGACTAGCGGATAACCTGCTTTGACTGGTTCTATCCCCAAAGAGTCAGACATAGTCGCATCAAACCTGCAAGAAAGTTGTCCACATTGTCGTCCATGAGCTACGGGTCCGATCTCTGAATATCTGAGCGTGTAAC"
k=12
profile={"A": [0.325,0.277,0.205,0.313,0.289,0.253,0.373,0.289,0.325,0.241,0.229,0.229],
"C":[0.217,0.313,0.325,0.193,0.229,0.277,0.241,0.217,0.253,0.277,0.217,0.241],
"G":[0.253,0.169,0.193,0.289,0.253,0.217,0.229,0.145,0.205,0.253,0.229,0.313],
"T":[0.205,0.241,0.277,0.205,0.229,0.253,0.157,0.349,0.217,0.229,0.325,0.217]}

# print ProfileMostProbableKmer(text,k,profile)



# Copy your Consensus(Motifs) function here.
def Consensus(Motifs):
	t = len(Motifs)
	k = len(Motifs[0])
	profile = Profile(Motifs)
	consensus = [""]*k	
	for i in range(k):
		maximum = -1
		for key in profile:			
			if maximum< profile[key][i]:
				consensus[i] = key
				maximum = profile[key][i]
	return "".join(consensus)
# Copy your Count(Motifs) function here.
def Profile(Motifs):	
	t = len(Motifs)
	k = len(Motifs[0])
	profile = {"A":[0]*k,"C":[0]*k,"G":[0]*k,"T":[0]*k}
	for i in range(t):		
		for j in range(k):
			# if not(Motifs[i][j] in profile):
			# 	profile[Motifs[i][j]]=[0]*k
			profile[Motifs[i][j]][j]+=1.0/t
	return profile
# Input:  A set of k-mers Motifs
# Output: The score of these k-mers.
def Score(Motifs):
	# Insert code here
	score=0
	consensus = Consensus(Motifs)	
	for row in Motifs:
		for c1,r1 in zip(consensus,row):			
			if c1!=r1:
				score+=1
	return score


def GreedyMotifSearch(Dna, k, t):
	# type your GreedyMotifSearch code here.
	#It creates a matrix with the first nucleotides of each string    
	BestMotifs = []     
	for i in range(0, t):    	
		BestMotifs.append(Dna[i][0:k])    
	n = len(Dna[0])
	for i in range(n-k+1):
		Motifs = []
		Motifs.append(Dna[0][i:i+k])        
		for j in range(1, t):        	        	            
			P = Profile(Motifs[0:j])
			Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
		if Score(Motifs) < Score(BestMotifs):
			BestMotifs = Motifs
	return BestMotifs



# file = open("dataset_159_5.txt","r")
# kt=file.readline().split()
# Dna=[]
# for line in file:
# 	Dna.append(line.strip())

# print len(Dna)
# print " ".join(GreedyMotifSearch(Dna,int(kt[0]),int(kt[1])))

# k=3
# t= 5
# Dna=["GGCGTTCAGGCA","AAGAATCAGTCA","CAAGGAGTTCGC","CACGTCAATCAC","CAATAATATTCG"]
# print " ".join(GreedyMotifSearchWithPseudocounts(Dna,k,t,1))


def CountWithPseudocounts(Motifs):
	t = len(Motifs)
	k = len(Motifs[0])
	# insert your code here
	count = {"A":[1]*k,"C":[1]*k,"G":[1]*k,"T":[1]*k}
	# # your code here	
	for i in range(t):		
		for j in range(k):			
			count[Motifs[i][j]][j]+=1
	return count


def ProfileWithPseudocounts(Motifs):	
	t = len(Motifs)
	k = len(Motifs[0])	
	#profile = {}	
	count = CountWithPseudocounts(Motifs)	
	profile={}
	for key in count:
		profile[key]= [x / (4.0+t) for x in count[key]]
	return profile

def Motifs(Profile, Dna):
	return [ProfileMostProbableKmer(text,len(Profile["A"]),Profile) for text in Dna]


# def RandomMotifs(k,t):	
# 	limit = 4**k-1
# 	return [NumberToPattern(random.randint(0,limit),k) for i in range(t)]


def RandomMotifs(Dna, k, t):
	return [text[random.randint(0,len(text)-k):][:k] for text in Dna ]

def RandomizedMotifSearch(Dna, k, t):
	# insert your code here
	M = RandomMotifs(Dna,k, t)	
	BestMotifs = M
	score=Score(M)
	# for i in range(1000):
	while True:
		Profile = ProfileWithPseudocounts(M)		
		M = Motifs(Profile, Dna)		
		score_BM = Score(M)
		if score>score_BM:
			score = score_BM 
			BestMotifs = M
		else:
			return BestMotifs



def thousandTimes(Dna,k,t):
	BestMotif = RandomizedMotifSearch(Dna,k,t)
	score = Score(BestMotif)
	for i in range(1000):
		M = RandomizedMotifSearch(Dna,k,t)
		score_M = Score(M)
		if score>score_M:
			score = score_M
			BestMotif=M
	return BestMotif




# kt=[8,5]
# Dna=["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA","GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG","TAGTACCGAGACCGAAAGAAGTATACAGGCGT","TAGATCAAGTTTCAGGTGCACGTCGGTGAACC","AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]


# print "\n".join(thousandTimes(Dna,int(kt[0]),int(kt[1])))
def Normalize(Probabilities):
	return {key : Probabilities[key] / sum(Probabilities.values()) for key in Probabilities}


def WeightedDie(Probabilities):	
	prob = random.uniform(0,1)
	a =0
	for item in Probabilities:		
		a += Probabilities[item]
		if a>prob:
			return item


def ProfileGeneratedString(Text, profile, k):
	n = len(Text)
	probabilities = {} 
	for i in range(0,n-k+1):
		probabilities[Text[i:i+k]] = Pr(Text[i:i+k], profile)
	probabilities = Normalize(probabilities)	
	return WeightedDie(probabilities)



def GibbsSampler(Dna, k, t, N):
	BestMotifs = [] # output variable
	# your code here
	Motifs = RandomMotifs(Dna,k,t)
	BestMotifs = Motifs
	for j in range(N):		
		i = random.randint(0,t-1)				
		Motifsi= Motifs[:i]+Motifs[i+1:]		
		Profile = ProfileWithPseudocounts(Motifsi)				
		Motifs[i] = ProfileGeneratedString(Dna[i],Profile,k)		
		if Score(Motifs)<Score(BestMotifs):			
			BestMotifs=Motifs
	return BestMotifs



# ktN=[8, 5, 100]
# Dna=["CGCCCCTCTCGGGGGTGTTCAGTAACCGGCCA","GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG","TAGTACCGAGACCGAAAGAAGTATACAGGCGT","TAGATCAAGTTTCAGGTGCACGTCGGTGAACC","AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]


def NTimes(times,Dna,k,t,N):
	BestMotif = RandomizedMotifSearch(Dna,k,t)
	score = Score(BestMotif)
	for i in range(times):
		M = GibbsSampler(Dna,k,t,N)
		score_M = Score(M)
		if score>score_M:
			score = score_M
			BestMotif=M
	return BestMotif


file = open("dataset_163_4.txt","r")
k,t,N=[int(x) for x in file.readline().split()]
Dna=[]
for line in file:
	Dna.append(line.strip())

print "\n".join(NTimes(20,Dna,k,t,N))

