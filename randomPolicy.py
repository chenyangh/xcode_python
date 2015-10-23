import blackjack
from pylab import *

numEpisodes = 2000
returnSum = 0.0
for episodeNum in range(numEpisodes):
    G = 0
    G, s=blackjack.sample(0,0)
    while s != -1:
        action = randint(0,blackjack.numActions(s))
        G, s=blackjack.sample(s,action)
    print "Episode: ", episodeNum, "Return: ", G
    returnSum = returnSum + G
print "Average return: ", returnSum/numEpisodes