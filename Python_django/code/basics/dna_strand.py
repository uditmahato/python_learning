def DNA_strand(dna):
    # code here
    list=[]
    for i in dna:
        if i=='A':
            list.append('T')
        elif i=='T':
            list.append('A')
        elif i=='G':
            list.append('C')
        else:
            list.append('G')
    return ''.join(list)
DNA_strand('ATCGT')