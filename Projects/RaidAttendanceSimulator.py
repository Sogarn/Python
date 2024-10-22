import random

# raid attendance stats
raidProbabilities = [100, 100, 100, 100, 92, 92, 92, 92, 84, 84, 76, 76, 76, 61, 53, 53, 46]
# lateness version
#raidProbabilities = [100, 100, 92, 92, 92, 92, 92, 92, 84, 84, 76, 76, 76, 61, 53, 46, 46]

# trim raid attendance stats that are guaranteed
guaranteedCount = 0
while 100 in raidProbabilities:
    guaranteedCount += 1
    raidProbabilities.remove(100)

# all raid count possibilities accounting for guaranteeds
totalCount = len(raidProbabilities) + 1 + guaranteedCount

# number of distinct possibilities (plus one to account for 0)
raiderSamples = [0] * totalCount

iterations = 5000000

# run (simulator iterations) number of times
for x in range(iterations):
    raiders = guaranteedCount
    # Loop through raid probabilites and add 1 to raiders if it hits
    for y in raidProbabilities:
        if (random.randint(0, 100) <= y):
            raiders += 1
    # Add 1 to the outcome with that many raiders accounting for guaranteed count
    raiderSamples[raiders] += 1

# divide all entries by simulator iterations
outcome = [float(x) / float(iterations) for x in raiderSamples]
print("Raider count | Probability")
# start stats at guaranteed count
for x in range(guaranteedCount, totalCount):
    print(f"{x} | {outcome[x]:.1%}")