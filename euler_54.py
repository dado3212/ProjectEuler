# Problem 54
# Answer: 

'''
In the card game poker, a hand consists of five cards and are ranked, from lowest to highest, in the following way:

High Card: Highest value card. (0)
One Pair: Two cards of the same value. (1)
Two Pairs: Two different pairs. 
Three of a Kind: Three cards of the same value.
Straight: All cards are consecutive values.
Flush: All cards of the same suit.
Full House: Three of a kind and a pair.
Four of a Kind: Four cards of the same value.
Straight Flush: All cards are consecutive values of same suit.
Royal Flush: Ten, Jack, Queen, King, Ace, in same suit.
The cards are valued in the order:
2, 3, 4, 5, 6, 7, 8, 9, 10, Jack, Queen, King, Ace.

If two players have the same ranked hands then the rank made up of the highest value wins; for example, a pair of eights beats a pair of fives (see example 1 below). But if two ranks tie, for example, both players have a pair of queens, then highest cards in each hand are compared (see example 4 below); if the highest cards tie then the next highest cards are compared, and so on.

The file, poker.txt, contains one-thousand random hands dealt to two players. Each line of the file contains ten cards (separated by a single space): the first five are Player 1's cards and the last five are Player 2's cards. You can assume that all hands are valid (no invalid characters or repeated cards), each player's hand is in no specific order, and in each hand there is a clear winner.

How many hands does Player 1 win?
'''

rankings = {
	"2": 0,
	"3": 1,
	"4": 2,
	"5": 3,
	"6": 4,
	"7": 5,
	"8": 6,
	"9": 7,
	"T": 8,
	"J": 9,
	"Q": 10,
	"K": 11,
	"A": 12
}

def sortCards(c1, c2):
	return rankings[c1] - rankings[c2]

def royalFlush(hand1, hand2):
	cards1 = ''.join(sorted(map(lambda x: x[0], hand1), cmp=sortCards))
	cards2 = ''.join(sorted(map(lambda x: x[0], hand2), cmp=sortCards))
	if isFlush(hand1) and cards1 == "AJKQT":
		return -1
	elif isFlush(hand2) and cards2 == "AJKQT":
		return 1
	return 0

def straightFlush(hand1, hand2):
	cards1 = ''.join(sorted(map(lambda x: x[0], hand1), cmp=sortCards))
	cards2 = ''.join(sorted(map(lambda x: x[0], hand2), cmp=sortCards))
	oneStraight = isStraight(hand1)
	oneFlush = isFlush(hand1)
	twoStraight = isStraight(hand2)
	twoFlush = isFlush(hand2)
	if not (oneStraight and oneFlush) and not (twoStraight and twoFlush):
		return 0
	else:
		if (oneStraight and oneFlush) and (twoStraight and twoFlush):
			return rankings[cards2[-1]] - rankings[cards1[-1]]
		elif (oneStraight and oneFlush):
			return -1
		else:
			return 1

def fourOfAKind(hand1, hand2):
	cards1 = sorted(map(lambda x: x[0], hand1), cmp=sortCards)
	cards2 = sorted(map(lambda x: x[0], hand2), cmp=sortCards)
	oneFour = ''.join(cards1).count(cards1[0]) == 4 or ''.join(cards1).count(cards1[-1]) == 4
	twoFour = ''.join(cards2).count(cards2[0]) == 4 or ''.join(cards2).count(cards2[-1]) == 4
	if not oneFour and not twoFour:
		return 0
	else:
		if (oneFour and twoFour):
			oneFourCard = cards1[0] if ''.join(cards1).count(cards1[0]) == 4 else cards1[-1]
			twoFourCard = cards2[0] if ''.join(cards2).count(cards2[0]) == 4 else cards2[-1]
			if rankings[oneFourCard] != rankings[twoFourCard]:
				return rankings[twoFourCard] - rankings[oneFourCard]
			else:
				oneSingleCard = cards1[0] if ''.join(cards1).count(cards1[0]) == 1 else cards1[-1]
				twoSingleCard = cards2[0] if ''.join(cards2).count(cards2[0]) == 1 else cards2[-1]
				return rankings[twoSingleCard] - rankings[oneSingleCard]
		elif oneFour:
			return -1
		else:
			return 1

def fullHouse(hand1, hand2):
	cards1 = sorted(map(lambda x: x[0], hand1), cmp=sortCards)
	cards2 = sorted(map(lambda x: x[0], hand2), cmp=sortCards)
	oneFull = (''.join(cards1).count(cards1[0]) == 2 and ''.join(cards1).count(cards1[-1]) == 3) or (''.join(cards1).count(cards1[0]) == 3 and ''.join(cards1).count(cards1[-1]) == 2)
	twoFull = (''.join(cards2).count(cards2[0]) == 2 and ''.join(cards2).count(cards2[-1]) == 3) or (''.join(cards2).count(cards2[0]) == 3 and ''.join(cards2).count(cards2[-1]) == 2)
	if not oneFull and not twoFull:
		return 0
	else:
		if (oneFull and twoFull):
			oneLarger = cards1[0] if ''.join(cards1).count(cards1[0]) == 3 else cards1[-1]
			twoLarger = cards2[0] if ''.join(cards2).count(cards2[0]) == 3 else cards2[-1]
			if rankings[oneLarger] != rankings[twoLarger]:
				return rankings[twoLarger] - rankings[oneLarger]
			else:
				oneSmaller = cards1[0] if ''.join(cards1).count(cards1[0]) == 2 else cards1[-1]
				twoSmaller = cards2[0] if ''.join(cards2).count(cards2[0]) == 2 else cards2[-1]
				return rankings[twoSmaller] - rankings[oneSmaller]
		elif oneFull:
			return -1
		else:
			return 1

def flush(hand1, hand2):
	if not isFlush(hand1) and not isFlush(hand2):
		return 0
	else:
		if isFlush(hand1) and isFlush(hand2):
			cards1 = sorted(map(lambda x: x[0], hand1), cmp=sortCards)
			cards2 = sorted(map(lambda x: x[0], hand2), cmp=sortCards)
			for i in xrange(0,5):
				if rankings[cards1[4-i]] != rankings[cards2[4-i]]:
					return rankings[cards2[4-i]] - rankings[cards1[4-i]]
			print "Failed!"
			return -1 # Should never be reached
		elif isFlush(hand1):
			return -1
		else:
			return 1

def straight(hand1, hand2):
	if not isStraight(hand1) and not isStraight(hand2):
		return 0
	else:
		if isStraight(hand1) and not isStraight(hand2):
			oneLargest = sorted(map(lambda x: x[0], hand1), cmp=sortCards)[-1]
			twoLargest = sorted(map(lambda x: x[0], hand2), cmp=sortCards)[-1]
			return rankings[twoLargest] - rankings[oneLargest]
		elif isStraight(hand1):
			return -1
		else:
			return 1

def threeOfAKind(hand1, hand2):
	cards1 = sorted(map(lambda x: x[0], hand1), cmp=sortCards)
	cards2 = sorted(map(lambda x: x[0], hand2), cmp=sortCards)
	oneThree = ''.join(cards1).count(cards1[0]) == 3 or ''.join(cards1).count(cards1[1]) == 3 or ''.join(cards1).count(cards1[2]) == 3
	twoThree = ''.join(cards2).count(cards2[0]) == 3 or ''.join(cards2).count(cards2[1]) == 3 or ''.join(cards2).count(cards2[2]) == 3
	if not oneThree and not twoThree:
		return 0
	else:
		if (oneThree and twoThree):
			if ''.join(cards1).count(cards1[0]) == 3:
				oneThreeCard = cards1[0]
			elif ''.join(cards1).count(cards1[1]) == 3:
				oneThreeCard = cards1[1]
			else:
				oneThreeCard = cards1[2]

			if ''.join(cards2).count(cards2[0]) == 3:
				twoThreeCard = cards2[0]
			elif ''.join(cards2).count(cards2[1]) == 3:
				twoThreeCard = cards2[1]
			else:
				twoThreeCard = cards2[2]

			if rankings[oneThreeCard] != rankings[twoThreeCard]:
				return rankings[twoThreeCard] - rankings[oneThreeCard]
			else:
				oneOther = [y for y in cards1 if y != oneThreeCard]
				twoOther = [y for y in cards2 if y != twoThreeCard]
				for i in xrange(0,2):
					if rankings[oneOther[1-i]] != rankings[twoOther[1-i]]:
						return rankings[twoOther[1-i]] - rankings[oneOther[1-i]]
		elif oneThree:
			return -1
		else:
			return 1

def twoPairs(hand1, hand2):
	cards1 = sorted(map(lambda x: x[0], hand1), cmp=sortCards)
	cards2 = sorted(map(lambda x: x[0], hand2), cmp=sortCards)
	oneData = {x: cards1.count(x) for x in cards1}
	twoData = {x: cards2.count(x) for x in cards2}
	if oneData.values().count(2) != 2 and twoData.values().count(2) != 2:
		return 0
	else:
		if oneData.values().count(2) == 2 and twoData.values().count(2) == 2:
			onePairs = sorted(filter(lambda x: oneData[x] == 2, oneData), cmp=sortCards)
			twoPairs = sorted(filter(lambda x: twoData[x] == 2, twoData), cmp=sortCards)
			for i in xrange(0,2):
				if rankings[onePairs[1-i]] != rankings[twoPairs[1-i]]:
					return rankings[twoPairs[1-i]] - rankings[onePairs[1-i]]
			oneSingle = [y for y in x if cards1.count(y) == 1][0]
			twoSingle = [y for y in x if cards2.count(y) == 1][0]
			return rankings[twoSingle] - rankings[oneSingle]
		elif oneData.values().count(2) == 2:
			return -1
		else:
			return 1

def onePair(hand1, hand2):
	cards1 = sorted(map(lambda x: x[0], hand1), cmp=sortCards)
	cards2 = sorted(map(lambda x: x[0], hand2), cmp=sortCards)
	oneData = {x: cards1.count(x) for x in cards1}
	twoData = {x: cards2.count(x) for x in cards2}
	if oneData.values().count(2) != 2 and twoData.values().count(2) != 2:
		return 0
	else:
		if oneData.values().count(2) == 2 and twoData.values().count(2) == 2:
			onePairs = sorted(filter(lambda x: oneData[x] == 2, oneData), cmp=sortCards)
			twoPairs = sorted(filter(lambda x: twoData[x] == 2, twoData), cmp=sortCards)
			for i in xrange(0,2):
				if rankings[onePairs[1-i]] != rankings[twoPairs[1-i]]:
					return rankings[twoPairs[1-i]] - rankings[onePairs[1-i]]
			oneSingle = [y for y in x if cards1.count(y) == 1][0]
			twoSingle = [y for y in x if cards2.count(y) == 1][0]
			return rankings[twoSingle] - rankings[oneSingle]
		elif oneData.values().count(2) == 2:
			return -1
		else:
			return 1

def isFlush(hand):
	suits = ''.join(map(lambda x: x[-1], hand))
	return suits.count(suits[0]) == 5

def isStraight(hand):
	hands = sorted(map(lambda x: x[0], hand), cmp=sortCards)
	for i in range(0,3):
		if rankings[hands[i]] + 1 != rankings[hands[i+1]]:
			return False
	return True

def oneWon(hand1, hand2):
	s = royalFlush(hand1,hand2)
	if s != 0:
		return s < 0
	else:
		s = straightFlush(hand1,hand2)
		if s != 0:
			return s < 0
		else:
			s = fourOfAKind(hand1,hand2)
			if s != 0:
				return s < 0
			else:
				s = fullHouse(hand1,hand2)
				if s != 0:
					return s < 0
				else:
					s = flush(hand1,hand2)
					if s != 0:
						return s < 0
					else:
						s = straight(hand1,hand2)
						if s != 0:
							return s < 0
						else:
							s = threeOfAKind(hand1,hand2)
							if s != 0:
								return s < 0
							else:
								s = twoPairs(hand1,hand2)
								if s != 0:
									return s < 0
								else:
									return False

total = 0
with open('poker.txt','r') as f:
	for line in f:
		p1 = line.split(" ")[:5]
		p2 = line[:-1].split(" ")[5:]
		if oneWon(p1,p2):
			total += 1
print total