#python3 sequencias_Biologicas.py
def verificacao_sequencia(seq):
    for i in range(len(seq)):       
        if i not in ["A", "T", "C", "G"]:
            seq = seq.replace(i, "")
            verificacao_sequencia(seq)

class Sequence(object):

    def __init__(self, seq):
        self.seq = verificacao_sequencia(seq)

    # Count
    def Count(self,seq,Nucleotide):
        count = 0
        for N in range(len(seq)):
            if seq[N] == Nucleotide:
                count+= 1
        return count

    # Frequence
    def Frequence(self,seq,Nucleotide):
        count = Count(seq,Nucleotide)
        frequence = round(count/len(seq) * 100)
        #print('The Nucleotide',Nucleotide,'contains',frequence,'%')
        return frequence
    # Endswith
    def endswith(self,seq,end):
        if seq[-1] == end:
            return True
        return False
    # startwith
    def startwith(self,seq, start):
        if seq[0] == start:
            return True
        return False

    def Percentage_GC(self,seq):
        return Frequence(seq,'G') + Frequence(seq,'C')

    def molecular_mass(self,seq):
        if 'T' in seq:
            seq = transcribe(seq)
        seq = translate(seq)
        dicionary = {'Ala': 89.094,
        'Arg': 174.203,
        'Asn': 132.119,
        'Asp': 133.104,
        'Cys': 121.154,
        'GIn': 146.146,
        'Glu': 147.131,
        'Gly': 75.067,
        'His': 155.156,
        'Ile': 131.175,
        'Leu': 131.175,
        'Lys': 146.189,
        'Met': 149.208,
        'Phe': 165.195,
        'Pro': 115.132,
        'Ser': 105.093,
        'Thr': 119.119,
        'Trp': 204.228,
        'Tyr': 181.191,
        'Val': 117.148}
        sum = 0
        for i in range(0,len(seq),3):
            codon = seq[i:i+3]
            sum = sum + dicionary[codon]
        return sum


    # ungap
    def ungap(self,seq,gap):
        for i in range(len(seq)):
            if gap in seq:
                index_gap = seq.find(gap)
                seq = seq[:index_gap] + seq[(index_gap+1):]
        print('Sequence without','"',gap,'"')
        return seq

    # Complement
    def complement(self,seq):
        seq = seq.replace('A','t').replace('T','a').replace('G','c').replace('C','g').upper()
        print('----------------Complement:',seq)
        return seq

    # Reverse complement
    def reverse_complement(self,seq):
        seq = seq[::-1]
        complement(seq)
        print('------------------Reverse_complement:',seq)
        return seq
    # transcribe
    def transcribe(self,seq):
        seq = seq.replace('T','U')
        return seq

    #  Clipping sequence
    def clipping(self,seq):
        for i in range(0,len(seq),3):
            if seq[i:i+3] == 'AUG':
                seq = seq[i:]
        return seq
    # translate
    def translate(self,seq):
        question = input('Do you want cut non-coding parts ? [s/n]').upper()
        if question == 'S':
            seq = clipping(seq)

        dicionary = {'GCU':'Ala','GCC':'Ala','GCA':'Ala','GCG':'Ala',
        'CGU':'Arg','CGC':'Arg','CGA':'Arg','CGG':'Arg','AGA':'Arg','AGG':'Arg',
        'AAU':'Asn','AAC':'Asn',
        'GAU':'Asp', 'GAC':'Asp',
        'UGU':'Cys', 'UGC':'Cys',
        'CAA':'GIn','CAG':'GIn',
        'GAA':'Glu','GAG':'Glu',
        'GGU':'Gly','GGC':'Gly','GGA':'Gly','GGG':'Gly',
        'CAU':'His','CAC':'His',
        'AUU':'Ile','AUC':'Ile','AUA':'Ile',
        'UUA':'Leu','UUG':'Leu','CUU':'Leu','CUC':'Leu','CUA':'Leu','CUG':'Leu',
        'AAA':'Lys','AAG':'Lys',
        'AUG':'Met',
        'UUU':'Phe','UUC':'Phe',
        'CCU':'Pro','CCC':'Pro','CCA':'Pro','CCG':'Pro',
        'UCU':'Ser','UCC':'Ser','UCA':'Ser','UCG':'Ser','AGU':'Ser','AGC':'Ser',
        'ACU':'Thr','ACC':'Thr','ACA':'Thr','ACG':'Thr',
        'UGG':'Trp',
        'UAU':'Tyr','UAC':'Tyr',
        'GUU':'Val','GUC':'Val','GUA':'Val','GUG':'Val',
        'UAG':'STOP','UGA':'STOP','UAA':'STOP'}
        protein = ''
        for i in range(0,len(seq),3):
            if dicionary[seq[i:i+3]] == 'STOP':
                continue
            else:
                protein = protein + dicionary[seq[i:i+3]]
        return protein

    def nt_search(self,seq,search_sequence):
        size = len(search_sequence)
        list_position = [search_sequence]
        if search_sequence < seq:
            for i in range(len(seq)-size):
                if seq[i:size+i] == search_sequence:
                    list_position.append(i)
        print(list_position)
        return list_position

    def splicing(self,seq,introns):
        if 'T' in seq:
            seq = transcribe(seq)
        for i in introns:
            seq = seq.replace(i,'')
        seq_translate = translate(seq)
        print(seq, '\n\n',seq_translate)
        return seq, seq_translate








