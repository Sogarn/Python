import random
lines = 5
megamillions = False    
powerball = True
rng = random

if megamillions:
    print("Megamillions:")
    for x in range(lines):
        print("Line {0}: {1} {2} {3} {4} {5} {6}".format(x+1, rng.randint(1, 14), rng.randint(15,28), rng.randint(29,42), rng.randint(43,56), rng.randint(57,70), rng.randint(1,25)))

if powerball:
    print("Powerball:")
    for x in range(lines):
        print("Line {0}: {1} {2} {3} {4} {5} {6}".format(x+1, rng.randint(1, 14), rng.randint(15,28), rng.randint(29,42), rng.randint(43,56), rng.randint(57,69), rng.randint(1,26)))
