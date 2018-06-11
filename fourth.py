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
	multi = 1
	for i in range(len(Text)):
		if not (Text[i] in Profile):
			return 0
		multi *= Profile[Text[i]][i]
	return multi

def ProfileMostProbableKmer(text, k, profile):
	kmer = ""
	maximum = -1    
	for i in range(len(text)-k+1):
		pr = Pr(text[i:i+k],profile)
		if(maximum<pr):
			maximum = pr
			kmer = text[i:i+k]    

	return kmer

def GreedyMotifSearchWithPseudocounts(Dna, k, t):
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
			P = ProfileWithPseudocounts(Motifs[0:j])
			Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
		if Score(Motifs) < Score(BestMotifs):
			BestMotifs = Motifs
	return BestMotifs

print  GreedyMotifSearchWithPseudocounts(["GGCGTTCAGGCA","AAGAATCAGTCA","CAAGGAGTTCGC","CACGTCAATCAC","CAATAATATTCG"],3,5)
# Your output:
# {'A': [0.2222222222222222, 0.3333333333333333, 0.3333333333333333, 0.3333333333333333, 0.2222222222222222, 0.3333333333333333], 
# 'C': [0.5555555555555556, 0.3333333333333333, 0.2222222222222222, 0.5555555555555556, 0.3333333333333333, 0.5555555555555556, 0.3333333333333333, 0.5555555555555556, 0.3333333333333333], 
# 'G': [0.3333333333333333, 0.3333333333333333, 0.2222222222222222, 0.2222222222222222, 0.2222222222222222, 0.2222222222222222], 
# 'T': [0.5555555555555556, 0.5555555555555556, 0.3333333333333333, 0.5555555555555556, 0.3333333333333333, 0.2222222222222222, 0.5555555555555556, 0.2222222222222222, 0.2222222222222222]}
# Correct output:
# {'A': [0.2222222222222222, 0.3333333333333333, 0.2222222222222222, 0.1111111111111111, 0.1111111111111111, 0.3333333333333333], 'C': [0.3333333333333333, 0.2222222222222222, 0.5555555555555556, 0.3333333333333333, 0.1111111111111111, 0.1111111111111111], 'G': [0.2222222222222222, 0.2222222222222222, 0.1111111111111111, 0.3333333333333333, 0.2222222222222222, 0.2222222222222222], 'T': [0.2222222222222222, 0.2222222222222222, 0.1111111111111111, 0.2222222222222222, 0.5555555555555556, 0.3333333333333333]}