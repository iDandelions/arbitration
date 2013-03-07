#!/usr/bin/python

import arbitration

# setup an arbitration bet
myArbitration = arbitration.ArbitrationBet('Example Arbitration Bet')

# setup the place side of the arbitration bet
myArbitration.placeBet.odds  = 2.84
myArbitration.placeBet.stake = 40

# calculate stake needed to equalize profit on win or loose with the lay odds
myArbitration.calculateLayBetStake(1.8)

# display the results
print myArbitration