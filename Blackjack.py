
import random







class Card:

    def __init__(self,val,name):
        self.value = val
        self.name = name

class Deck:
    deck = []

    def shuffle(self):
        for i in range(1000):
            randIndA = random.randrange(52)
            randIndB = random.randrange(52)

            while randIndA == randIndB:
                 randIndB = random.randrange(52)
            
            cardHold = self.deck[randIndA]
            self.deck[randIndA] = self.deck[randIndB]
            self.deck[randIndB] = cardHold

    def draw(self, nCards):
        cards = []
        for i in range(nCards):
            cards.append(self.deck.pop())
        return cards

    def nCardsInDeck(self):
        return len(self.deck)

    def reset(self):
        self.deck = []
        for i in range(52):
            cardPartA = ''
            cardPartB = ''


            cardVal = i%13 + 1

            cardPartA = str(cardVal)
            if cardVal == 1:
                cardPartA = 'Ace'
            if cardVal > 10:
                if cardVal == 11:

                    cardPartA = 'Jack'
                elif cardVal == 12:
                    cardPartA = 'Queen'
                elif cardVal == 13:
                    cardPartA = 'King'
                cardVal = 10

            suitVar = i // 13
            if suitVar == 0:
                cardPartB = "Spades"
            if suitVar == 1:
                cardPartB = 'Hearts'
            if suitVar == 2:
                cardPartB = 'Clubs'
            if suitVar == 3:
                cardPartB = 'Diamonds'


            cardName = cardPartA + ' of ' + cardPartB
            self.deck.append(Card(cardVal, cardName))

bjDeck = Deck()
hjDeck = Deck()
bjDeck.reset()
hjDeck.reset()
print(bjDeck.deck[19].name)
bjDeck.shuffle()
print(bjDeck.deck[19].name)
print(bjDeck.nCardsInDeck())
hand = bjDeck.draw(2)
for card in hand:
    print(card.name)
print(bjDeck.nCardsInDeck())
print(hjDeck.nCardsInDeck())
