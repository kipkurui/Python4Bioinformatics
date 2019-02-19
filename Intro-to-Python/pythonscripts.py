def get_genes(infile,outfile):
    """
    Function to extract a list of genes and write to file
    """
    gene_list = []
    with open(infile) as  gene:
        tag = False
        for line in gene:
            if line.startswith('name'):
                tag = True
                pass
            if tag:
                items = line.split()
                if len(items) > 0:
                    gene_list.append(items[0])
    gene_list = gene_list[1:-7]
    with open(outfile, 'w') as outfile:
        for i in gene_list:
            outfile.write(i+'\n')
            

def dnatest(dnaseq):
    testdna =[]
    dna = dnaseq.upper()
    for i in dna:
        result = str(i) in ['T', 'A', 'G', 'C']
        testdna.append(result)
    if testdna.count(False) > 0:
        return False
    else:
        return True

    def dnaTest(x):
    dnaset = set("AGCT")
    y = set(x.upper()).union(dnaset) == dnaset
    return y

def percentGC(dna):
    '''calculates the percentage GC content, given a DNA sequence'''
    if dnacheck(dna):
        dna_len= len(dna)
        gs = dna.count('G')
        cs = dna.count('C')
        
        return (gs+cs)/dna_len*100
        
        #print("The sequence input is not a valid DNA")

def dnacheck(dna):
    counter = 0
    check = True
    valid_dna = 'ACGT'
    for i in dna.upper():
        counter += 1
        if i in valid_dna:
            pass
        else:
            check = False
            print("There is an invalid base '%s' at position %d"
                  % (i,counter))
    return check

dna = 'ACZGTCYTTgZCABG'
dnacheck(dna)
dnaseq ='acgtaaqat'
dnatest(dnaseq)