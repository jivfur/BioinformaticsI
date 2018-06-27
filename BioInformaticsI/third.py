def Count(Motifs):
	count = {} # initializing the count dictionary
	# # your code here	
	for i in range(len(Motifs)):		
		for j in range(len(Motifs[i])):
			if not(Motifs[i][j] in count):
				count[Motifs[i][j]]=[0]*len(Motifs[i])
			count[Motifs[i][j]][j]+=1
	return count
	
def Pr(Text,Profile):
	multi = 1
	for i in range(len(Text)):
		if not (Text[i] in Profile):
			return 0
		multi *= Profile[Text[i]][i]
	return multi


profile = {'A':[0.2, 0.2, 0.0, 0.0, 0.0, 0.0, 0.9, 0.1, 0.1, 0.1, 0.3, 0.0],
'C':[0.1, 0.6, 0.0, 0.0, 0.0, 0.0, 0.0, 0.4, 0.1, 0.2, 0.4, 0.6],
'G':[0.0, 0.0, 1.0, 1.0, 0.9, 0.9, 0.1, 0.0, 0.0, 0.0, 0.0, 0.0],
'T':[0.7, 0.2, 0.0, 0.0, 0.1, 0.1, 0.0, 0.5, 0.8, 0.7, 0.3, 0.4]
}
print Pr("TCGTGGATTTCC",profile)



def ProfileMostProbableKmer(text, k, profile):
	kmer = ""
	maximum = -1    
	for i in range(len(text)-k+1):
		pr = Pr(text[i:i+k],profile)
		if(maximum<pr):
			maximum = pr
			kmer = text[i:i+k]    
	return kmer



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


# print(GreedyMotifSearch([
# "GGCGTTCAGGCA", 
# "AAGAATCAGTCA", 
# "CAAGGAGTTCGC",
# "CACGTCAATCAC", 
# "CAATAATATTCG"
# ],3,5))
# import math
# profile= [[0.2, 0.2, 0, 0, 0, 0, 0.8999999999999999, 0.1, 0.1, 0.1, 0.30000000000000004, 0],
# [0.1, 0.6, 0, 0, 0, 0, 0, 0.4, 0.1, 0.2, 0.4, 0.6],
# [0.7, 0.2, 0, 0, 0.1, 0.1, 0, 0.5, 0.7999999999999999, 0.7, 0.30000000000000004, 0.4],
# [0, 0, 0.9999999999999999, 0.9999999999999999, 0.8999999999999999, 0.8999999999999999, 0.1, 0, 0, 0, 0, 0]]
# entropy = 0
# for j in range(len(profile[0])): #colums
# 	colEntropy = 0
# 	for i in range(len(profile)): #row
# 		if profile[i][j]!=0:
# 			colEntropy+=profile[i][j]*math.log(profile[i][j],2)
# 	entropy-=colEntropy

# print "Entropy: ",entropy

