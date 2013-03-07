# A single bet object
class Bet(object):
    
    def __init__(self,name):
        self.name = name
        
    def __str__(self):
        id = str.rjust(self.name,10) + '->'
        id += '%.2f' % self.stake
        id += ' at ' + '%.2f' % self.odds
        return id
        
# Arbitration bet, contains two bets, a lay and a place, which form both sides of the arbitration
class ArbitrationBet(object):
    
    def __init__(self,name):
        self.name     = name
        self.placeBet = Bet('To Win')
        self.layBet   = Bet('To Loose')

    def __str__(self):
        id = self.name + '\n'
        id += str(self.placeBet) + '\n'
        id += str(self.layBet) + '\n'
        id += 'Profit:' + '%.2f' % (self.layBet.stake - self.placeBet.stake) +'\n'
        id += 'Profit as a Percentage of Stake:'
        id += '%.2f%%' % ((self.layBet.stake - self.placeBet.stake) / self.placeBet.stake * 100)
        return id    
        
    # Calculate the lay bet stake needed to equalize the profit on both a win and a lose
    # The place bet and the lay bet odds need to be initialise before calling
    def calculateLayBetStake(self,odds):
        self.layBet.odds  = odds
        self.layBet.stake = round(((self.placeBet.stake*self.placeBet.odds)+self.placeBet.stake)/(1+odds),2)
        
    # Calculate the place bet stake needed to equalize the profit on both a win and a lose
    # The lay bet and the place bet odds need to be initialise before calling
    def calculatePlaceBetStake(self,odds):
        self.placeBet.odds  = odds
        self.placeBet.stake = round(((self.LayBet.stake*self.LayBet.odds)+self.LayBet.stake)/(1+odds),2)


