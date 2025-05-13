import pgone as pgone
class DNA:
    def __init__(self, main_strand, complement_strand = 0):
        """
        A dna strand. Capital letters for a base pair indicate that it is damaged.
        Args:
            main_strand (str): the strand that RNA polymerase reads
            complement_strand (str, optional): The other strand. \nThis is automatically defined from main_strand if not given.
        """
        self.color_bases_main = []
        self.letters_main = []
        self.SpriteActors = []
        self.color_bases_complement = []
        self.letters_complement = []
        while not isinstance(complement_strand, str):
            complement_strand = ""
            for base_pair in self.main_strand:
                match base_pair.lower():
                    case "a":
                        complement_strand += "t"
                    case "t":
                        complement_strand += "a"
                    case "c":
                        complement_strand += "g"
                    case "g":
                        complement_strand += "c"
                    case " ":
                        complement_strand += " "
                    case _:
                        raise ValueError("Encountered error while reading self.main_strand:\nDNA strands must only contain base pairs a, t, c, g, and space")
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
            match base:
                case "a":
                    self.color_bases_main.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 0, 1, 1)))
                    self.letters_main.append(pgone.SpriteActor(pgone.Sprite("atcgu.png", 7, 9, 0, 1, 1)))
                case "t":
                    self.color_bases_main.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 1, 1, 1)))
                    self.letters_main.append(pgone.SpriteActor(pgone.Sprite("atcgu.png", 7, 9, 1, 1, 1)))
                case "c":
                    self.color_bases_main.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 2, 1, 1)))
                    self.letters_main.append(pgone.SpriteActor(pgone.Sprite("atcgu.png", 7, 9, 2, 1, 1)))
                case "g":
                    self.color_bases_main.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 3, 1, 1)))
                    self.letters_main.append(pgone.SpriteActor(pgone.Sprite("atcgu.png", 7, 9, 3, 1, 1)))
        for base in self.complement_strand:
            match base:
                case "a":
                    self.color_bases_complement.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 0, 1, 1)))
                    self.letters_complement.append(pgone.SpriteActor(pgone.Sprite("atcgu.png", 7, 9, 0, 1, 1)))
                case "t":
                    self.color_bases_complement.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 1, 1, 1)))
                    self.letters_complement.append(pgone.SpriteActor(pgone.Sprite("atcgu.png", 7, 9, 1, 1, 1)))
                case "c":
                    self.color_bases_complement.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 2, 1, 1)))
                    self.letters_complement.append(pgone.SpriteActor(pgone.Sprite("atcgu.png", 7, 9, 2, 1, 1)))
                case"g":
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
            match self.main_strand[i]:
                case "a":
                    output += "u"
                case "t":
                    output += "a"
                case "c":
                    output += "g"
                case "g":
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
            match self.main_strand[i]:
                case "a":
                    if self.complement_strand[i] != "t":
                        to_return.append(i)
                case "t":
                    if self.complement_strand[i] != "a":
                        to_return.append(i)
                case "c":
                    if self.complement_strand[i] != "g":
                        to_return.append(i)
                case "g":
                    if self.complement_strand[i] != "c":
                        to_return.append(i)
                case "A" | "T" | "C" | "G":
                    to_return.append(i)
                case _:
                    raise TypeError(f"Malformed {self}.main_strand[{i}] ({self.main_strand[i-2, i+2]}): Bases must contain a, t, c, or g")
        for i in range(len(self.main_strand)):
            if self.complement_strand[i] in ["A", "T", "C", "G"] or self.main_strand[i] in ["A", "T", "C", "G"]:
                to_return.append(i)
        return to_return
    
    def base_excision_repair(self, index):
        main_pair = self.main_strand[index]
        comp_pair = self.complement_strand[index]
        if main_pair in ["A", "T", "C", "G"] and comp_pair in ["A", "T", "C", "G"]:
            print("Oh dear, it does indeed seem that you have reached the point where both strands have damaged bases and are not valid for base excision repair")
            return self
        elif main_pair not in ["A", "T", "C", "G"] and comp_pair in ["A", "T", "C", "G"]:
            match main_pair:
                case "a":
                    comp_pair = "t"
                case "t":
                    comp_pair = "a"
                case "c":
                    comp_pair = "g"
                case "g":
                    comp_pair = "c"
        elif comp_pair not in ["A", "T", "C", "G"] and main_pair in ["A", "T", "C", "G"]:
            match comp_pair:
                case "a":
                    main_pair = "t"
                case "t":
                    main_pair = "a"
                case "c":
                    main_pair = "g"
                case "g":
                    main_pair = "c"
        else:
            print("This DNA is just fine. Not at all a candidate for base excision repair.")
            
        

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
            match base:
                case "a":
                    self.color_bases.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 0, 1, 1)))
                    self.letters.append(pgone.SpriteActor(pgone.Sprite("atcgu.png", 7, 9, 0, 1, 1)))
                case "u":
                    self.color_bases.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 4, 1, 1)))
                    self.letters.append(pgone.SpriteActor(pgone.Sprite("atcgu.png", 7, 9, 4, 1, 1)))
                case "c":
                    self.color_bases.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 2, 1, 1)))
                    self.letters.append(pgone.SpriteActor(pgone.Sprite("atcgu.png", 7, 9, 2, 1, 1)))
                case "g":
                    self.color_bases.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 3, 1, 1)))
                    self.letters.append(pgone.SpriteActor(pgone.Sprite("atcgu.png", 7, 9, 3, 1, 1)))