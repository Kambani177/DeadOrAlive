


from cards import *

class Player(object):
    """This class represents a player in
    a blackjack game."""

    def __init__(self, cards):
        self._cards = cards

    def __str__(self):
        """Returns string rep of cards and points."""
        result = ", ".join(map(str, self._cards))
        result += "\n A total of " + str(self.getPoints()) + " points"
        return result
    
    def getPoints(self):
        """Returns the number of points in the hand."""
        count = 0
        for card in self._cards:
            count+= card.rank + Card.SUITS.index(card.suit)
        return count


#inherits method from player class
class Dealer(Player):
    """Like a Player, but with some restrictions."""

    def __init__(self, cards):
        """Initial state: show one card only."""
        Player.__init__(self, cards)
        self._showOneCard = True

    def __str__(self):
        """Return just one card if not hit yet."""
        return Player.__str__(self)
   
    


class Deadoralive(object):

    def __init__(self):
        self._deck = Deck()
        self._deck.shuffle()
        self._player = Player([self._deck.deal()])
        self._dealer = Dealer([self._deck.deal()])

    def play(self):
        wins= 0
        losses=0
        ties = 0
        while len(self._deck) !=0: 
            print("Player:\n", self._player)
            print("Dealer:\n", self._dealer)
            playerPoints = self._player.getPoints()
            dealerPoints = self._dealer.getPoints()
            if playerPoints > dealerPoints:
                print('Player Wins')
                wins+=1
            elif playerPoints < dealerPoints:
                print('Dealer Wins')
                losses+=1
            else:
                print("We have a tie!")
                ties+=1
            self._player = Player([self._deck.deal()])
            self._dealer = Dealer([self._deck.deal()])
        print("Total wins: {0}, Total losses: {1}, Ties: {2}."
              .format(wins, losses, ties))


                
def main():
    game = Deadoralive()
    game.play()

main()
  
