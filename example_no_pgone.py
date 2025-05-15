import molecular_genetics


#Note that, if pgone exists, you will need to import pgzrun

#auto complement strand
damaged_dna = molecular_genetics.DNA("agttgccgggcggGggagggcgcgtccggtttttctcaggggacgttgaaattatttttgtaacgggagtcgggagaggacggggcgtgccccgacgtgcgcgcgcgtcgtcctccccggcgctcctccacagctcgctggctcccgccgcggaaaggcgtcatgccgcccaaaaccccccgaaaaacggccgccaccgccgccgctgccgccgcggaacccccggcaccgccgccgccgccccctcctgaggaggacccagagcaggacagcggcccggaggacctgcctctcgtcagg")
print(damaged_dna.main_strand)
print(damaged_dna.complement_strand)
print(damaged_dna.transcribe().strand)
print(damaged_dna.transcribe().translate())

errors = damaged_dna.find_error_indices()
print(errors)

for error in errors:
    #all errors in this example are for base excision.
    damaged_dna.base_excision_repair(error)
print(damaged_dna.main_strand)
print(damaged_dna.transcribe().strand)
print(damaged_dna.transcribe().translate())