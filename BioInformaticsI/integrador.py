# import the random package here
import random

# Insert necessary subroutines here, including RandomMotifs(), ProfileWithPseudocounts(), Motifs(), Score(),
# and any subroutines that these functions need.
def Consensus(Motifs):	
	t = len(Motifs)
	k = len(Motifs[0])
	profile = ProfileWithPseudocounts(Motifs)
	consensus = [""]*k	
	for i in range(k):
		maximum = -1
		for key in profile:			
			if maximum< profile[key][i]:
				consensus[i] = key
				maximum = profile[key][i]
	return "".join(consensus)

def Score(Motifs):
	# Insert code here	
	score=0
	consensus = Consensus(Motifs)	
	for row in Motifs:
		for c1,r1 in zip(consensus,row):			
			if c1!=r1:
				score+=1
	return score

def Pr(Text,Profile):	
	multi = 1.0
	for i in range(len(Text)):
		multi *= Profile[Text[i]][i]
	return multi


def ProfileMostProbableKmer(text, k, profile):
	kmer = text[0:k]
	maximum = -1
	for i in range(len(text)-k+1):
		pr = Pr(text[i:i+k],profile)
		if(maximum<pr):
			maximum = pr
			kmer = text[i:i+k]
	return kmer

def ProfileWithPseudocounts(Motifs):	
	t = len(Motifs)
	k = len(Motifs[0])	
	#profile = {}	
	count = CountWithPseudocounts(Motifs)	
	profile={}
	for key in count:
		profile[key]= [x / (4.0+t) for x in count[key]]
	return profile


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

def Motifs(Profile, Dna):
	return [ProfileMostProbableKmer(text,len(Profile["A"]),Profile) for text in Dna]

def RandomMotifs(Dna, k, t):
	return [text[random.randint(0,len(text)-k-1):][:k] for text in Dna ]

# Next, copy your RandomizedMotifSearch function (along with all required subroutines)
# from Motifs.py below this line
# Input:  Positive integers k and t, followed by a list of strings Dna
# Output: RandomizedMotifSearch(Dna, k, t)
def RandomizedMotifSearch(Dna, k, t):
	# insert your code here
	M = RandomMotifs(Dna, k, t)	
	BestMotifs = M
	while True:
		Profile = ProfileWithPseudocounts(M)		
		M = Motifs(Profile, Dna)		
		if Score(M) < Score(BestMotifs):
			BestMotifs = M
		else:
			return BestMotifs





# # Copy the ten strings occurring in the hyperlinked DosR dataset below.
# Dna = ["GCGCCCCGCCCGGACAGCCATGCGCTAACCCTGGCTTCGATGGCGCCGGCTCAGTTAGGGCCGGAAGTCCCCAATGTGGCAGACCTTTCGCCCCTGGCGGACGAATGACCCCAGTGGCCGGGACTTCAGGCCCTATCGGAGGGCTCCGGCGCGGTGGTCGGATTTGTCTGTGGAGGTTACACCCCAATCGCAAGGATGCATTATGACCAGCGAGCTGAGCCTGGTCGCCACTGGAAAGGGGAGCAACATC","CCGATCGGCATCACTATCGGTCCTGCGGCCGCCCATAGCGCTATATCCGGCTGGTGAAATCAATTGACAACCTTCGACTTTGAGGTGGCCTACGGCGAGGACAAGCCAGGCAAGCCAGCTGCCTCAACGCGCGCCAGTACGGGTCCATCGACCCGCGGCCCACGGGTCAAACGACCCTAGTGTTCGCTACGACGTGGTCGTACCTTCGGCAGCAGATCAGCAATAGCACCCCGACTCGAGGAGGATCCCG","ACCGTCGATGTGCCCGGTCGCGCCGCGTCCACCTCGGTCATCGACCCCACGATGAGGACGCCATCGGCCGCGACCAAGCCCCGTGAAACTCTGACGGCGTGCTGGCCGGGCTGCGGCACCTGATCACCTTAGGGCACTTGGGCCACCACAACGGGCCGCCGGTCTCGACAGTGGCCACCACCACACAGGTGACTTCCGGCGGGACGTAAGTCCCTAACGCGTCGTTCCGCACGCGGTTAGCTTTGCTGCC","GGGTCAGGTATATTTATCGCACACTTGGGCACATGACACACAAGCGCCAGAATCCCGGACCGAACCGAGCACCGTGGGTGGGCAGCCTCCATACAGCGATGACCTGATCGATCATCGGCCAGGGCGCCGGGCTTCCAACCGTGGCCGTCTCAGTACCCAGCCTCATTGACCCTTCGACGCATCCACTGCGCGTAAGTCGGCTCAACCCTTTCAAACCGCTGGATTACCGACCGCAGAAAGGGGGCAGGAC","GTAGGTCAAACCGGGTGTACATACCCGCTCAATCGCCCAGCACTTCGGGCAGATCACCGGGTTTCCCCGGTATCACCAATACTGCCACCAAACACAGCAGGCGGGAAGGGGCGAAAGTCCCTTATCCGACAATAAAACTTCGCTTGTTCGACGCCCGGTTCACCCGATATGCACGGCGCCCAGCCATTCGTGACCGACGTCCCCAGCCCCAAGGCCGAACGACCCTAGGAGCCACGAGCAATTCACAGCG","CCGCTGGCGACGCTGTTCGCCGGCAGCGTGCGTGACGACTTCGAGCTGCCCGACTACACCTGGTGACCACCGCCGACGGGCACCTCTCCGCCAGGTAGGCACGGTTTGTCGCCGGCAATGTGACCTTTGGGCGCGGTCTTGAGGACCTTCGGCCCCACCCACGAGGCCGCCGCCGGCCGATCGTATGACGTGCAATGTACGCCATAGGGTGCGTGTTACGGCGATTACCTGAAGGCGGCGGTGGTCCGGA","GGCCAACTGCACCGCGCTCTTGATGACATCGGTGGTCACCATGGTGTCCGGCATGATCAACCTCCGCTGTTCGATATCACCCCGATCTTTCTGAACGGCGGTTGGCAGACAACAGGGTCAATGGTCCCCAAGTGGATCACCGACGGGCGCGGACAAATGGCCCGCGCTTCGGGGACTTCTGTCCCTAGCCCTGGCCACGATGGGCTGGTCGGATCAAAGGCATCCGTTTCCATCGATTAGGAGGCATCAA","GTACATGTCCAGAGCGAGCCTCAGCTTCTGCGCAGCGACGGAAACTGCCACACTCAAAGCCTACTGGGCGCACGTGTGGCAACGAGTCGATCCACACGAAATGCCGCCGTTGGGCCGCGGACTAGCCGAATTTTCCGGGTGGTGACACAGCCCACATTTGGCATGGGACTTTCGGCCCTGTCCGCGTCCGTGTCGGCCAGACAAGCTTTGGGCATTGGCCACAATCGGGCCACAATCGAAAGCCGAGCAG","GGCAGCTGTCGGCAACTGTAAGCCATTTCTGGGACTTTGCTGTGAAAAGCTGGGCGATGGTTGTGGACCTGGACGAGCCACCCGTGCGATAGGTGAGATTCATTCTCGCCCTGACGGGTTGCGTCTGTCATCGGTCGATAAGGACTAACGGCCCTCAGGTGGGGACCAACGCCCCTGGGAGATAGCGGTCCCCGCCAGTAACGTACCGCTGAACCGACGGGATGTATCCGCCCCAGCGAAGGAGACGGCG","TCAGCACCATGACCGCCTGGCCACCAATCGCCCGTAACAAGCGGGACGTCCGCGACGACGCGTGCGCTAGCGCCGTGGCGGTGACAACGACCAGATATGGTCCGAGCACGCGGGCGAACCTCGTGTTCTGGCCTCGGCCAGTTGTGTAGAGCTCATCGCTGTCATCGAGCGATATCCGACCACTGATCCAAGTCGGGGGCTCTGGGGACCGAAGTCCCCGGGCTCGGAGCTATCGGACCTCACGATCACC"]
# # set t equal to the number of strings in Dna, k equal to 15, and N equal to 100.
# t=10
# k=15
# N=100
# # Call RandomizedMotifSearch(Dna, k, t) N times, storing the best-scoring set of motifs
# # resulting from this algorithm in a variable called BestMotifs
# BestMotifs = RandomizedMotifSearch(Dna,k,t)
# for i in range(N-1):
#     M = RandomizedMotifSearch(Dna,k,t)
#     if Score(BestMotifs)>Score(M):
#         BestMotifs = M
# # Print the BestMotifs variable
# print(BestMotifs)
# # Print Score(BestMotifs)
# print(Score(BestMotifs))


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





# Dna=["CGCCCCTCTCGGGGGTGTTCAGTAAACGGCCA","GGGCGAGGTATGTGTAAGTGCCAAGGTGCCAG","TAGTACCGAGACCGAAAGAAGTATACAGGCGT","TAGATCAAGTTTCAGGTGCACGTCGGTGAACC","AATCCACCAGCTCCACGTGCAATGTTGGCCTA"]

# print GibbsSampler(Dna,8,5,100)

# Dna =["TGACGTTC","TAAGAGTT","GGACGAAA","CTGTTCGC"]
# M = ["TGA","GTT","GAA","TGT"]
# P= ProfileWithPseudocounts(M)
# M = Motifs(P, Dna)
# print M
