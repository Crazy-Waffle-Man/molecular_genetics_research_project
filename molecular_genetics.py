#Dynamic imports go brrr

try: 
    import pgone
    has_pgone = True
except ModuleNotFoundError:
    print("pgone.py is missing. DNA and RNA cannot be rendered.")
    has_pgone = False

if has_pgone:
    try:
        pgone.Sprite
    except Exception as e:
        print(f"Error using pgone: {e}")

#Dynamic imports no longer go brr

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
        self.main_strand = main_strand
        self.complement_strand = ""
        if self.complement_strand == "" and self.main_strand != "":
            for base_pair in self.main_strand:
                match base_pair.lower():
                    case "a":
                        self.complement_strand += "t"
                    case "t":
                        self.complement_strand += "a"
                    case "c":
                        self.complement_strand += "g"
                    case "g":
                        self.complement_strand += "c"
                    case " ":
                        self.complement_strand += " "
                    case _:
                        raise ValueError("Encountered error while reading self.main_strand:\nDNA strands must only contain base pairs a, t, c, g, and space")
        if has_pgone:
            self.reload_renderer()
    
    def reload_renderer(self):
        """
        Updates the object's attributes to contain the appropriate SpriteActors. Chainable method.
        """
        if not has_pgone:
            print("This method needs pgone.py to function properly. If you want to use it, you must install it from the github repo.")
            return self
        else:
            try:
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
            except pygame.error:
                pass
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
        if not has_pgone:
            print("This method needs pgone.py to function properly. If you want to use it, you must install it from the github repo.")
            return self
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
                case "A" | "T" | "C" | "G" | " ":
                    to_return.append(i)
                case _:
                    raise TypeError(f"Malformed {self}.main_strand[{i}] ({self.main_strand[i-2, i+2]}): Bases must contain a, t, c, or g")
        return to_return
    
    def base_excision_repair(self, index):
        """
        fix a damaged base at index. The strand is automatically determined.
        """
        main_pair = self.main_strand[index]
        comp_pair = self.complement_strand[index]
        self.main_strand = list(self.main_strand)
        self.complement_strand = list(self.complement_strand)
        if main_pair in ["A", "T", "C", "G"] and comp_pair in ["A", "T", "C", "G"]:
            print("Oh dear, it does indeed seem that you have reached the point where both strands have damaged bases and are not valid for base excision repair")
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
            self.complement_strand[index] = comp_pair
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
            self.main_strand[index] = main_pair
        else:
            print("This DNA is just fine. Not at all a candidate for base excision repair.")
        main = ""
        comp = ""
        for i in range(len(self.main_strand)):
            main += self.main_strand[i]
            comp += self.complement_strand[i]
        self.main_strand = main
        self.complement_strand = comp
        #Chainable method
        return self

    def nucleotide_excision_repair(self, start_index, end_index, main_strand = True):
        """
        Fix multiple damaged nucleotides. Often needed due to UV radiation hitting the DNA.
        args:
            start_index (int): the first damaged index of the DNA 
            end_index (int): The last damaged index of the DNA
            main_strand (bool): Is the damaged strand the main strand?
        """
        if main_strand:
            self.main_strand = list(self.main_strand)
            #I decided to do it this way here because this is how it works IRL; the nucleotides are all removed, then replaced.
            for i in range(start_index-5, end_index+5):
                self.main_strand[i] = " "
            for i in range(start_index-5, end_index+5):
                match self.complement_strand[i]:
                    case "a":
                        self.main_strand[i] = "t"
                    case "t":
                        self.main_strand[i] = "a"
                    case "c":
                        self.main_strand[i] = "g"
                    case "g":
                        self.main_strand[i] = "c"
                    case "A"|"C"|"T"|"G"|" ":
                        raise ValueError(f"Could not repair DNA due to damaged or missing nucleotide {i}:{self.complement_strand[i]}")
                    case _:
                        raise ValueError(f"Could not parse self.complement strand at index {i}: ...{self.main_strand[i-2:i]} HERE--> {self.main_strand[i]} <--HERE {self.main_strand[i+1:i+2]}...")
            self.main_strand = str(self.main_strand)
            return self
        else:
            self.complement_strand = list(self.complement_strand)
            #I decided to do it this way here because this is how it works IRL; the nucleotides are all removed, then replaced.
            for i in range(start_index-5, end_index+5):
                self.complement_strand[i] = " "
            for i in range(start_index-5, end_index+5):
                match self.main_strand[i]:
                    case "a":
                        self.complement_strand[i] = "t"
                    case "t":
                        self.complement_strand[i] = "a"
                    case "c":
                        self.complement_strand[i] = "g"
                    case "g":
                        self.complement_strand[i] = "c"
                    case "A"|"C"|"T"|"G"|" ":
                        raise ValueError(f"Could not repair DNA due to damaged or missing nucleotide {i}:{self.main_strand[i]}")
                    case _:
                        raise ValueError(f"Could not parse self.complement strand at index {i}: ...{self.main_strand[i-2:i]} HERE--> {self.main_strand[i]} <--HERE {self.main_strand[i+1:i+2]}...")
            self.complement_strand = str(self.complement_strand)
            return self

        

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
        if has_pgone:
            self.reload_renderer()
    def draw(self, top_left_pos):
        """
        Draws the object's SpriteActors in a line.
        Args: 
            start_pos (list of length 2): the (x, y) to start drawing the dna strand at
        """
        if not has_pgone:
            print("This method needs pgone.py to function properly. If you want to use it, you must install it from the github repo.")
            return self
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
        if not has_pgone:
            print("This method needs pgone.py to function properly. If you want to use it, you must install it from the github repo.")
            return self
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
    
    def translate(self):
        codons = []
        protein = []
        for i in range(0, len(self.strand), 3):
            codons.append(self.strand[i:i+3])
        try:
            for codon in codons:
                match codon[0]:
                    case "a":
                        match codon[1]:
                            case "a":
                                if codon[2] == "a" or codon[2] == "g":
                                    protein.append("Lys")
                                elif codon[2] == "c" or codon[2] == "u":
                                    protein.append("Asn")
                            case "g":
                                if codon[2] == "g" or codon[2] == "a":
                                    protein.append("Arg")
                            case "c":
                                protein.append("Thr")
                            case "u":
                                if codon[2] == "g":
                                    protein.append("Met")
                                else: 
                                    protein.append("Ile")
                    case "u":
                        match codon[1]:
                            case "u":
                                if codon[2] == "u" or codon[2] == "c":
                                    protein.append("Phe")
                                else:
                                    protein.append("Leu")
                            case "c":
                                protein.append("Ser")
                            case "a":
                                if codon[2] == "u" or codon[2] =="c":
                                    protein.append("Tyr")
                                else:
                                    protein.append("stop")
                                    break
                            case "g":
                                if codon[2] == "u" or codon[2] == "c":
                                    protein.append("Cys")
                                elif codon[2] == "a":
                                    protein.append("stop")
                                    break
                                elif codon[2] == "g":
                                    protein.append("Trp")
                    case "c":
                        match codon[1]:
                            case "u":
                                protein.append("Leu")
                            case "c":
                                protein.append("Pro")
                            case "g":
                                protein.append("Arg")
                            case "a":
                                if codon[2] == "g" or codon[2] == "a":
                                    protein.append("Gln")
                                else:
                                    protein.append("His")
                    case "g":
                        match codon[1]:
                            case "g":
                                protein.append("Gly")
                            case "c":
                                protein.append("Ala")
                            case "u":
                                protein.append("Val")
                            case "a":
                                if codon[2] == "u" or codon[2] == "c":
                                    protein.append("Asp")
                                else:
                                    protein.append("Glu")
        except IndexError:
            print("Ran out of information to read before reaching a stop codon.")
        return protein