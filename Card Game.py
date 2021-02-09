
#CARD GAME USING PYTHON 

#CARD CLASS
#SUIT,RANK,VALUE


suits  = ('Hearts', 'Diamonds', 'Spades', 'Clubs')
rank = ('Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack',
        'Queen', 'King', 'Ace')
values = {"Two":2, "Three":3,"Four":4, "Five":5, "Six":6, "Seven":7, "Eight":8, "Nine":9, "Ten":10,
         "Jack":11, "Queen":12, "Kimg":13, "Ace":14}

class card():
    
    def __init__(self,suits,rank):
        self.suits = suits
        self.rank = rank
        self.value = values[rank]
        
    def __str__(self):
        return self.rank + " of " +self.suits

class Deck():
    
    def __init__(self):
        self.all_cards = [ ]
        
        for suit in suits:
            for rank in ranks:
                #CREATING CARD OBJECT
                created_cards = card(suit,rank)
                self.all_cards.append(created_cards)
                
     def shuffle(self):
        
        random.shuffle(self.all_cards)
        
     def deal_one(self):
        
        return self.all_cards.pop()
