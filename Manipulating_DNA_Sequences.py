#############################################################################################################
#													        #
#					Manipulating DNA Sequences        				        #
#													        #
#############################################################################################################

################################        Part.1     ####################################################

# Function that calculates the GC rate of a given nucleotidic sequence


def Calculate_GC_percentage (Seq):

    Seq = Seq.upper()
    nb_GC = 0.0
 
    GC = {
    "A": 0.0 , "T" :0.0 , "G" : 1.0, "C" : 1.0
    }

    for nucl in Seq:
        nb_GC += GC[nucl]
        GC_rate = (nb_GC/len(Seq))*100
    return (GC_rate)
    
#testing the function that calculate the GC rate
print (" This program calculates the GC rate of a given nucleotidic sequence ")
seq1 = input ("Enter your Sequence:")
p = Calculate_GC_percentage (seq1)
print ("The GC rate of he given Sequence is : ",p)

# GC rate with window
print("THis program calculates the GC rate with a given window size")
Sequence = input ("Enter your sequence:")
calcuulated_rate = []
window_size = 10
for i in range (len(Sequence)-window_size):
    window = Sequence [i:i+10]
    result = Calculate_GC_percentage (window)
    calcuulated_rate += [result]
print (calcuulated_rate)





##################################      Part.2    ###################################################

# Alignment Score
Sequence_1 = "AGCTGCTCTGATA"
Sequence_2 = "A--T-C-AT-A--"
Sequence_3 = "AG-TGC-ATGA-A"

#function that calculates the matching score
def match (seq1,seq2):
    zipped = zip (seq1,seq2)
    score_app = 0
    for n1, n2 in zipped:
        if n1 == n2 and n1 != "-" and n2 != "-":
            score_app += 2
    return (score_app)

#function that calculates the mismatching score
def mismatch (seq1,seq2):
    zipped = zip (seq1,seq2)
    score_mismatch = 0
    for n1, n2 in zipped:
        if n1 != n2:
            score_mismatch += 0
    return (score_mismatch)

#function that calculates the gap score
def gap (seq1,seq2):
    zipped = zip (seq1,seq2)
    score_gap = 0
    for n1, n2 in zipped:
        if n1 == "-" and n2 != "-" or n1 != "-" and n2 == "-":
            score_gap += -3
        elif n1 == "-" and n2 == "-":
            score_gap += 0
    return (score_gap)


#############################################        Calcul des scores      ################################           
#Sequence_1 et Sequence_2
print ("=======  THIS PROGRAM CALCULATES THE ALIGNEMENT'S SCORE ==========")
#match
Sequence_1 = input("Enter Sequence_1:")
Sequence_2 = input("Enter Sequence_2")
app_1 = match(Sequence_1,Sequence_2)      

#mismatch
m_1 = mismatch (Sequence_1,Sequence_2)       

#gap 
gap_1 = gap(Sequence_1,Sequence_2)            
tot_1= app_1 + m_1 + gap_1
print ('Alignement score Sequence_1 and Sequence_2 ----> ',tot_1)

#Sequence_2 et Sequence_3
#match
Sequence_2 = input("Enter Sequence_2:")
Sequence_3 = input("Enter Sequence_3")
app_2 = match(Sequence_2,Sequence_3)       

#mismatch
m_2 = mismatch (Sequence_2,Sequence_3)        

#gap 
gap_2 = gap(Sequence_2,Sequence_3)              
tot_2= app_2 + m_2 + gap_2
print ('Alignement score Sequence_2 and Sequence_3 ----> ', tot_2)
#Sequence_1 et Sequence_3
#match
Sequence_1 = input("Enter Sequence_1:")
Sequence_3 = input("Enter Sequence_3")
app_3 = match(Sequence_2,Sequence_3)       

#mismatch
m_3 = mismatch (Sequence_1,Sequence_3)      

#gap 
gap_3 = gap(Sequence_1,Sequence_3)               
tot_3=  app_3 + m_3 + gap_3
print ('Score alignment Sequence_1 and Sequence_3 ----> ', tot_3)
best_score = max(tot_1,tot_2,tot_3)
print ("The best alignement is the one with the following alignement score:", best_score)

print ("================    THIS IS THE END OF THE PROGRAM  ==================")
