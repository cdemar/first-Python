# Programmer: Cory DeMar
# ComSc 20
# Assognment #15
# Dictionaries
# 5-3-17

dna_code_dict = { # This is the Ditionary
        'TTT': 'Phe', 'TCT': 'Ser', 'TGT': 'Cys', 'TAT': 'Tyr',
        'TTC': 'Phe', 'TCC': 'Ser', 'TGC': 'Cys', 'TAC': 'Tyr',
        'TTG': 'Leu', 'TCG': 'Ser', 'TGG': 'Trp', 'TAG': '***',
        'TTA': 'Leu', 'TCA': 'Ser', 'TGA': '***', 'TAA': '***',
              
        'CTT': 'Leu', 'CCT': 'Pro', 'CGT': 'Arg', 'CAT': 'His',
        'CTC': 'Leu', 'CCC': 'Pro', 'CGC': 'Arg', 'CAC': 'His',
        'CTG': 'Leu', 'CCG': 'Pro', 'CGG': 'Arg', 'CAG': 'Gln',
        'CTA': 'Leu', 'CCA': 'Pro', 'CGA': 'Arg', 'CAA': 'Gln',
              
        'GTT': 'Val', 'GCT': 'Ala', 'GGT': 'Gly', 'GAT': 'Asp',
        'GTC': 'Val', 'GCC': 'Ala', 'GGC': 'Gly', 'GAC': 'Asp',
        'GTG': 'Val', 'GCG': 'Ala', 'GGG': 'Gly', 'GAG': 'Glu',
        'GTA': 'Val', 'GCA': 'Ala', 'GGA': 'Gly', 'GAA': 'Glu',
              
        'ATT': 'Ile', 'ACT': 'Thr', 'AGT': 'Ser', 'AAT': 'Asn',
        'ATC': 'Ile', 'ACC': 'Thr', 'AGC': 'Ser', 'AAC': 'Asn',
        'ATG': 'Met', 'ACG': 'Thr', 'AGG': 'Arg', 'AAG': 'Lys',
        'ATA': 'Ile', 'ACA': 'Thr', 'AGA': 'Arg', 'AAA': 'Lys'}

#This take out all of the junk
def clean_sequence(is_seq):
    out_seq = ''
    for char in is_seq:
        if char.isalpha():
            out_seq = out_seq + char.upper()
    return out_seq

#This starts the proses        
#sequence = input("Enter a nucleotide sequence, or just press ENTER to quit: ")
sequence = 'ttt'
while sequence != '':
    sequence = clean_sequence(sequence)
    n_chars = len(sequence)
    if n_chars % 3 == 0:
        while sequence != '': #when there are all three amounts it starts to proces the answer
            triple = sequence [0:3]
            sequence = sequence [3:]
            if triple in dna_code_dict:
                amino = dna_code_dict[triple]
            else:
                amino = "Invalid Sequence"
            print(triple, amino)
    else:
        print("Error: You must give complete triples.")

    print() #Lets the user do this as many times at they need
    sequence = input("Enter a nucleotide sequence, or just press ENTER to quit: ")
    
