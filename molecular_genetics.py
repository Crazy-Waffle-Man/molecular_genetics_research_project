import pgone
class DNA:
    def __init__(self, main_strand, complement_strand = 0):
        """
        A dna strand.
        Args:
            main_strand (str): the strand that RNA polymerase reads
            complement_strand (str, optional): The other strand. \nThis is automatically defined from main_strand if not given.
        """
        self.color_bases_main = []
        self.letters_main = []
        self.SpriteActors = []
        self.color_bases_complement = []
        self.letters_complement = []
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
                elif base_pair == " ":
                    complement_strand += " "
                else:
                    raise ValueError("Encountered error while reading self.main_strand:\nDNA strands must only contain base pairs a, t, c, g, and space")
        self.complement_strand = complement_strand.lower()
        self.reload_renderer()
    
    def reload_renderer(self):
        """
        Updates the object's attributes to contain the appropriate SpriteActors. Chainable method.
        """
        self.color_bases_main = []
        self.letters_main = []
        self.color_bases_complement = []
        self.letters_complement = []
        #Create a SpriteActor of corresponding color
        for base in self.main_strand:
            if base == "a":
                self.color_bases_main.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 0, 1, 1)))
                self.letters_main.append(pgone.SpriteActor(pgone.Sprite("atcgu.png", 7, 9, 0, 1, 1)))
            elif base == "t":
                self.color_bases_main.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 1, 1, 1)))
                self.letters_main.append(pgone.SpriteActor(pgone.Sprite("atcgu.png", 7, 9, 1, 1, 1)))
            elif base == "c":
                self.color_bases_main.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 2, 1, 1)))
                self.letters_main.append(pgone.SpriteActor(pgone.Sprite("atcgu.png", 7, 9, 2, 1, 1)))
            elif base == "g":
                self.color_bases_main.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 3, 1, 1)))
                self.letters_main.append(pgone.SpriteActor(pgone.Sprite("atcgu.png", 7, 9, 3, 1, 1)))
        for base in self.complement_strand:
            if base == "a":
                self.color_bases_complement.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 0, 1, 1)))
                self.letters_complement.append(pgone.SpriteActor(pgone.Sprite("atcgu.png", 7, 9, 0, 1, 1)))
            elif base == "t":
                self.color_bases_complement.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 1, 1, 1)))
                self.letters_complement.append(pgone.SpriteActor(pgone.Sprite("atcgu.png", 7, 9, 1, 1, 1)))
            elif base == "c":
                self.color_bases_complement.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 2, 1, 1)))
                self.letters_complement.append(pgone.SpriteActor(pgone.Sprite("atcgu.png", 7, 9, 2, 1, 1)))
            elif base == "g":
                self.color_bases_complement.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 3, 1, 1)))
                self.letters_complement.append(pgone.SpriteActor(pgone.Sprite("atcgu.png", 7, 9, 3, 1, 1)))
        for sprite_actor in self.color_bases_complement:
            #Turn over the complement strand
            sprite_actor.angle = 180
        return self
    
    def transcribe(self):
        """
        Returns an RNA object from self.main_strand
        """
        output = ""
        for i in range(len(self.main_strand)):
            if self.main_strand[i] == "a":
                output += "u"
            elif self.main_strand[i] == "t":
                output += "a"
            elif self.main_strand[i] == "c":
                output += "g"
            elif self.main_strand[i] == "g":
                output += "c"
        return RNA(output)

    def draw(self, top_left_pos):
        """
        Draws the object's SpriteActors in a line. Chainable method.
        Args: 
            start_pos (list of length 2): the (x, y) to start drawing the dna strand at
        """
        for index, nucleotide in enumerate(self.color_bases_main):
            nucleotide.topleft = top_left_pos
            nucleotide.draw()
            self.letters_main[index].topleft = [top_left_pos[0], top_left_pos[1] - 1]
            self.letters_main[index].draw()
            top_left_pos[0] += 7
        top_left_pos[0] -= 7 * len(self.color_bases_main)
        top_left_pos[1] += 7
        for index, nucleotide in enumerate(self.color_bases_complement):
            nucleotide.topleft = top_left_pos
            nucleotide.draw()
            self.letters_complement[index].topleft = top_left_pos
            self.letters_complement[index].draw()
            top_left_pos[0] += 7
        return self

    def find_error_indices(self) -> list:
        """
        Finds any errors between start and stop indices, inclusive of both values.
        Chainable method.
        """
        to_return = []
        for i in range(len(self.main_strand)):
            if self.main_strand[i] == "a":
                if self.complement_strand[i] != "t":
                    to_return.append(i)
            elif self.main_strand[i] == "t":
                if self.complement_strand[i] != "a":
                    to_return.append(i)
            elif self.main_strand[i] == "c":
                if self.complement_strand[i] != "g":
                    to_return.append(i)
            elif self.main_strand[i] == "g":
                if self.complement_strand[i] != "c":
                    to_return.append(i)
            else:
                raise TypeError(f"Malformed {self}.main_strand[{i}] ({self.main_strand[i-2, i+2]}): Bases must contain a, t, c, or g")
        return to_return
    
    def single_nucleotide_mismatch_repair(self, index):
        complement_strand = list(self.complement_strand)
        match self.main_strand[index]:
            case "a":
                complement_strand[index] = "t"
            case "t":
                complement_strand[index] = "a"
            case "c":
                complement_strand[index] = "g"
            case "g":
                complement_strand[index] = "c"
        self.complement_strand = ""
        for i in complement_strand:
            self.complement_strand += i
        return self







class RNA:
    def __init__(self, strand):
        """
        An RNA strand.
        Args: 
            strand (str): The nucleotides. Raises a ValueError if it has stuff other than a, u, c, or g.
        """
        strand = strand.lower()
        for i in range(len(strand)):
            if strand[i] != "a" and strand[i] != "u" and strand[i] != "c" and strand[i] != "g":
                raise ValueError("RNA strand has nucleotides other than A, U, C, and G")
        self.strand = strand
        self.color_bases = []
        self.letters = []
        self.reload_renderer()
    def draw(self, top_left_pos):
        """
        Draws the object's SpriteActors in a line.
        Args: 
            start_pos (list of length 2): the (x, y) to start drawing the dna strand at
        """
        for index, nucleotide in enumerate(self.color_bases):
            nucleotide.topleft = top_left_pos
            nucleotide.draw()
            self.letters[index].topleft = top_left_pos
            self.letters[index].draw()
            top_left_pos[0] += 7
    def reload_renderer(self):
        """
        Updates the object's attributes to contain the appropriate SpriteActors
        """
        self.color_bases = []
        self.letters = []
        #Create a SpriteActor of corresponding color
        for base in self.strand:
            if base == "a":
                self.color_bases.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 0, 1, 1)))
                self.letters.append(pgone.SpriteActor(pgone.Sprite("atcgu.png", 7, 9, 0, 1, 1)))
            elif base == "u":
                self.color_bases.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 4, 1, 1)))
                self.letters.append(pgone.SpriteActor(pgone.Sprite("atcgu.png", 7, 9, 4, 1, 1)))
            elif base == "c":
                self.color_bases.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 2, 1, 1)))
                self.letters.append(pgone.SpriteActor(pgone.Sprite("atcgu.png", 7, 9, 2, 1, 1)))
            elif base == "g":
                self.color_bases.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 3, 1, 1)))
                self.letters.append(pgone.SpriteActor(pgone.Sprite("atcgu.png", 7, 9, 3, 1, 1)))