import sys

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
                continue
            if tag:
                items = line.split()
                if len(items) > 0:
                    gene_list.append(items[0])
    gene_list = gene_list[1:-7]
    with open(outfile, 'w') as outfile:
        for i in gene_list:
            outfile.write(i+'\n')
    return True

infile = sys.argv[1]
output = sys.argv[2]
get_genes(infile,output)
