def DNA_strand(dna):
    # code here
    for i in dna:
        if i=='A':
            return('T')
        elif i=='T':
            return ('A')
        elif i=='G':
            return('C')
        else:
            return('G')
DNA_strand('ATCGT')