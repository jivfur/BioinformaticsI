import sys
import os
import numpy as np

def N50(contigs):
	sorted(contigs)
	S = np.sum(contigs)
	threshold=S/2
	aux=0
	i = len(contigs)-1
	while(aux<=threshold):
		aux += contigs[i]
		i-=1
	return contigs[i+1]

def loadContigsLength(fileName):
	contigs=[]
	f = open(fileName,"r")
	count=0
	S=0
	for line in f:
		if line.startswith(">NODE"):
			contigs.append(int(line.split("_")[3]))
			if contigs[-1]>= 1000:
				count+=1
				S+=contigs[-1]
	print "#Long Contigs",count
	print "Total Length:",S
	return contigs


contings=loadContigsLength(os.path.join(".","25","contigs.fasta"))
print N50(contings)
contings=loadContigsLength(os.path.join(".","55","contigs.fasta"))
print N50(contings)
contings=loadContigsLength(os.path.join(".","85","contigs.fasta"))
print N50(contings)


