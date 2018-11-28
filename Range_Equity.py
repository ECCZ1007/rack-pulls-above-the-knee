import Classes
from Showdown import winShowdown

def rangeEquity(range1, range2, board = []):
    assert len(board) in [0, 3, 4, 5]
    if len(board) == 5:

    elif len(board) == 4:

    elif len(board) == 3:

    else:

    equity = 0.5
    return equity

def riverRangeEquity(range1, range2, board):
    assert len(board) == 5
    wins = 0
    total = 0
    for hand1 in range1:
        for hand2 in range2:
            temp = winShowdown(hand1, hand2, board)
            if temp == 1:
                wins = wins + 1
            elif temp == 0:
                wins = wins + 0.5
            total = total + 1
    return wins/total




