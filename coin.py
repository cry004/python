import random
class Coin:
    def __init__(self,rare=False,clean=True, heads = True, **kwargs):
        self.is_rare = rare
        self.is_clean = clean
        self.heads = heads

        if self.is_rare:
            self.value = self.original_value * 1.25
        else:
            self.value = self.original_value
        if self.is_clean:
            self.colour = self.clean_colour
        else:
            self.colour = self.rusty_colour

        def rust(self):
            self.colour = self.rusty_colour
            
        def clean(self):
            self.colour = self.clean_colour

        def __del__(self):
        print("Coin Spent!")

        def flip(self):
        options = [True,False]
        choice = random.choice(options)
        self.heads = choice

        
class Pound(Coin):
    def __init__(self):
        data = {
            "original_value": 1.00,
            "clean_colour": "gold",
            "rusty_colour": "greenish".
            "num_edges": 1,
            "diameter": 22.5,
            "thickness": 3.15,
            "mass": 9.5
        super().__init__(**data)
    
#      def __init__(self, rare=False):
#       self.rare = rare
#        if self.rare:
#            self.value =  1.25
#        else:
#            self.value = 1.00
#        
#        self.value = 1.00
#        self.colour = "gold"
#        self.num = 1
#        self.diameter = 22.5
#        self.thickness = 3.15
#        self.heads = True

#    def __del__(self):
#        print("Coin Spent!")
        
#    def rust(self):
#       self.colour = "greenish"

#    def clean(self):
#       self.colour = "gold"

#   def flip(self):
#       options = [True,False]
#       choice = random.choice(options)
#       self.heads = choice
    
