# Thompson Sampeling
"""d = 10
N = 10000

noRewards1 = [0]*d
noRewards0 = [0]*d

totalReward = 0

selected = []

for n in range(0, N):
    ad = 0
    maxRandom = 0

    for i in range(0, d):
        randomBeta = random.betavariate(noRewards1[i]+1, noRewards0[i]+1)

        if randomBeta > maxRandom:
            maxRandom = randomBeta
            ad = i

    selected.append(ad)
    reward = dataset.values[n, ad]

    if reward == 1:
        noRewards1[ad] = noRewards1[ad] + 1

    else:
        noRewards0[ad] = noRewards0[ad] + 1

    totalReward = totalReward + reward"""