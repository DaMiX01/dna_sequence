import numpy as np

NAcids = ('A', 'C', 'T', 'G')

def random_dna_sequence(length):
    return ''.join(np.random.choice(NAcids) for _ in range(length))

with open('dna.txt', 'w+') as txtout:
    for _ in range(10):
        dna = random_dna_sequence(100)
        
        Acount = dna.count("A")
        Tcount = dna.count("T")
        Gcount = dna.count("G")
        Ccount = dna.count("C")
        
        txtout.write(dna)
        txtout.write("\n")
        
        txtout.write("A-Count=")
        txtout.write(str(Acount))
        txtout.write("\n")

        txtout.write("T-Count=")
        txtout.write(str(Tcount))
        txtout.write("\n")

        txtout.write("G-Count=")
        txtout.write(str(Gcount))
        txtout.write("\n")

        txtout.write("C-Count=")
        txtout.write(str(Ccount))
        txtout.write("\n")
        txtout.write("\n")
        

        print (dna)
        print ("G-Count=", Gcount)
        print ("C-Count=", Ccount)