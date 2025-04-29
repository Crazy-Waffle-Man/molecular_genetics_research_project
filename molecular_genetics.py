class DNA:
    def __init__(self, main_strand, complement_strand = 0):
        """
        A dna strand.
        Args:
            main_strand (string): the strand that RNA polymerase reads
            complement_strand (string, default 0): The other strand. \nThis is automatically defined from main_strand if not given.
        """
        self.main_strand = main_strand.lower()
        while not isinstance(complement_strand, str):
            complement_strand = ""
            for base_pair in self.main_strand:
                if base_pair == "a":
                    complement_strand += "t"
                elif base_pair == "t":
                    complement_strand += "a"
                elif base_pair == "c":
                    complement_strand += "g"
                elif base_pair == "g":
                    complement_strand += "c"
                else:
                    raise ValueError(f"Encountered error while reading a DNA.main_strand:\nDNA strands must only contain base pairs a, t, c, and g.")
        self.complement_strand = complement_strand
    
    # def render