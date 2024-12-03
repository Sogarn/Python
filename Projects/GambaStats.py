from pathlib import Path

# Lowest possible roll
base_roll = 11111

# Stat collection
five_kinds = 0
four_kinds = 0
full_house = 0
straight = 0
three_kinds = 0
two_pair = 0
pair = 0
high_nine = 0
high_eight = 0
high_seven = 0
high_six = 0
high_five = 0


# expects an int list size 5 does calculations to convert roll to the card outcome
def check_roll(roll):
    # grab global variables
    global five_kinds, four_kinds, full_house, three_kinds, straight, two_pair, pair,\
        high_nine, high_eight, high_seven, high_six, high_five
    # sorting helps figure out straights later
    sorted_roll = sorted(roll, reverse=True)
    # loop through digits and distribute numbers to array
    digits = [0]*10
    # add digit to respective spot in array
    for iteration in sorted_roll:
        digits[iteration] += 1
    # create copy and sort array to figure out pairs, descending order
    ordered_pairs = sorted(digits, reverse=True)
    # switch statement to knock out most of the checks
    match ordered_pairs[0]:
        case 5:
            five_kinds += 1
        case 4:
            four_kinds += 1
        case 3:
            # check for full house
            if ordered_pairs[1] == 2:
                full_house += 1
            else:
                three_kinds += 1
        case 2:
            # check for two pair
            if ordered_pairs[1] == 2:
                two_pair += 1
            else:
                pair += 1
        # check straights and high cards
        case 1:
            # check cards 1 - 4 vs their adjacent card and add the difference
            difference = 0
            for i in range(0, 4, 1):
                difference += sorted_roll[i] - sorted_roll[i+1]
            # if total difference is 4 it is a straight
            if difference == 4:
                straight += 1
            else:
                # they will already be sorted high to low. At this point it is the highest card
                match sorted_roll[0]:
                    case 9:
                        high_nine += 1
                    case 8:
                        high_eight += 1
                    case 7:
                        high_seven += 1
                    case 6:
                        high_six += 1
                    case 5:
                        high_five += 1


# actual test
while base_roll <= 99999:
    currentRoll = [int(x) for x in str(base_roll)]
    base_roll += 1
    check_roll(currentRoll)

# output data
total_count = 88889
print("Poker gamba odds:")
print(f"Five of a kind: {five_kinds / total_count * 100:.2f}%")
print(f"Four of a kind: {four_kinds / total_count * 100:.2f}%")
print(f"Full house: {full_house / total_count * 100:.2f}%")
print(f"Straight: {straight / total_count * 100:.2f}%")
print(f"Three of a kind: {three_kinds / total_count * 100:.2f}%")
print(f"Two pair: {two_pair / total_count * 100:.2f}%")
print(f"Pair: {pair / total_count * 100:.2f}%")
print(f"High card nine: {high_nine / total_count * 100:.2f}%")
print(f"High card eight: {high_eight / total_count * 100:.2f}%")
print(f"High card seven: {high_seven / total_count * 100:.2f}%")
print(f"High card six: {high_six / total_count * 100:.2f}%")
print(f"High card five: {high_five / total_count * 100:.2f}%")