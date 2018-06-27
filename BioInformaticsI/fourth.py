def CountWithPseudocounts(Motifs,ps):
    t = len(Motifs)
    k = len(Motifs[0])
    # insert your code here
    count = {"A":[ps]*k,"C":[ps]*k,"G":[ps]*k,"T":[ps]*k}
	# # your code here	
    for i in range(t):		
        for j in range(k):			
            count[Motifs[i][j]][j]+=1
    return count

def ProfileWithPseudocounts(Motifs,ps):	
	t = len(Motifs)
	k = len(Motifs[0])	
	#profile = {}	
	count = CountWithPseudocounts(Motifs,ps)	
	profile={}
	for key in count:
		profile[key]= [x / (4.0*ps+t) for x in count[key]]
	return profile

def Consensus(Motifs,ps):
	t = len(Motifs)
	k = len(Motifs[0])
	profile = ProfileWithPseudocounts(Motifs,ps)
	consensus = [""]*k	
	for i in range(k):
		maximum = -1
		for key in profile:			
			if maximum< profile[key][i]:
				consensus[i] = key
				maximum = profile[key][i]
	return "".join(consensus)

def Score(Motifs,ps):
	# Insert code here
	score=0
	consensus = Consensus(Motifs,ps)	
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

def GreedyMotifSearchWithPseudocounts(Dna, k, t, ps):
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
			P = ProfileWithPseudocounts(Motifs[0:j],ps)
			Motifs.append(ProfileMostProbableKmer(Dna[j], k, P))
		if Score(Motifs,ps) < Score(BestMotifs,ps):
			BestMotifs = Motifs
	return BestMotifs


file = open("dataset_160_9.txt","r")
kt=file.readline().split()
Dna=[]
for line in file:
	Dna.append(line.strip())

print len(Dna)

print " ".join(GreedyMotifSearchWithPseudocounts(Dna,int(kt[0]),int(kt[1]),1))