import pgone
class DNA:
    def __init__(self, main_strand, complement_strand = 0):
        """
        A dna strand.
        Args:
            main_strand (string): the strand that RNA polymerase reads
            complement_strand (string, default 0): The other strand. \nThis is automatically defined from main_strand if not given.
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
                else:
                    raise ValueError("Encountered error while reading self.main_strand:\nDNA strands must only contain base pairs a, t, c, and g.")
        self.complement_strand = complement_strand.lower()
        self.reload_renderer()
    
    def reload_renderer(self):
        """
        Updates the object's attributes to contain the appropriate SpriteActors
        """
        self.color_bases_main = []
        self.letters_main = []
        self.color_bases_complement = []
        self.letters_complement = []
        #Create a SpriteActor of corresponding color
        for base in self.main_strand:
            if base == "a":
                self.color_bases_main.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 0, 1, 1)))
                self.letters_main.append(pgone.SpriteActor(pgone.Sprite("atcg.png", 7, 9, 0, 1, 1)))
            elif base == "t":
                self.color_bases_main.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 1, 1, 1)))
                self.letters_main.append(pgone.SpriteActor(pgone.Sprite("atcg.png", 7, 9, 1, 1, 1)))
            elif base == "c":
                self.color_bases_main.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 2, 1, 1)))
                self.letters_main.append(pgone.SpriteActor(pgone.Sprite("atcg.png", 7, 9, 2, 1, 1)))
            elif base == "g":
                self.color_bases_main.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 3, 1, 1)))
                self.letters_main.append(pgone.SpriteActor(pgone.Sprite("atcg.png", 7, 9, 3, 1, 1)))
        for base in self.complement_strand:
            if base == "a":
                self.color_bases_complement.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 0, 1, 1)))
                self.letters_complement.append(pgone.SpriteActor(pgone.Sprite("atcg.png", 7, 9, 0, 1, 1)))
            elif base == "t":
                self.color_bases_complement.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 1, 1, 1)))
                self.letters_complement.append(pgone.SpriteActor(pgone.Sprite("atcg.png", 7, 9, 1, 1, 1)))
            elif base == "c":
                self.color_bases_complement.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 2, 1, 1)))
                self.letters_complement.append(pgone.SpriteActor(pgone.Sprite("atcg.png", 7, 9, 2, 1, 1)))
            elif base == "g":
                self.color_bases_complement.append(pgone.SpriteActor(pgone.Sprite("bases.png", 7, 9, 3, 1, 1)))
                self.letters_complement.append(pgone.SpriteActor(pgone.Sprite("atcg.png", 7, 9, 3, 1, 1)))
        for sprite_actor in self.color_bases_complement:
            #Turn over the complement strand
            sprite_actor.angle = 180
        
    def draw(self, top_left_pos):
        """
        Draws the object's SpriteActors in a line.
        Args: 
            start_pos (list of length 2): the (x, y) to start drawing the dna strand at
        """
        for index, nucleotide in enumerate(self.color_bases_main):
            nucleotide.topleft = top_left_pos
            nucleotide.draw()
            self.letters_main[index].topleft = top_left_pos
            self.letters_main[index].draw()
            top_left_pos[0] += 7
        for i in range(len(self.color_bases_main)):
            top_left_pos[0] -= 7
        top_left_pos[1] += 7
        for index, nucleotide in enumerate(self.color_bases_complement):
            nucleotide.topleft = top_left_pos
            nucleotide.draw()
            self.letters_complement[index].topleft = top_left_pos
            self.letters_complement[index].draw()
            top_left_pos[0] += 7