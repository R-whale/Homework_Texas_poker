

def hand_to_numeric(cards):
    card_rank = {"2": 0, "3": 1, "4": 2, "5": 3, "6": 4, "7": 5, "8": 6,
                 "9": 7, "T": 8, "J": 9, "Q": 10, "K": 11, "A": 12,
                 "t": 8, "j": 9, "q": 10, "k": 11, "a": 12}
    card_suit = {"d": 0, "D": 0, "s": 1, "S": 1, "h": 2, "H": 2,
                 "c": 3, "C": 3}
    card_list = []
    for i in range(len(cards) // 3 + 1):
        card_list.append([card_rank[cards[i * 3]], card_suit[cards[((i * 3) + 1)]]])
    card_list.sort()
    card_list.reverse()
    return card_list


# 同花色
def check_flush(hand):
    hand_suit = [hand[0][1], hand[1][1], hand[2][1], hand[3][1], hand[4][1]]
    for i in range(4):
        if hand_suit.count(i) == 5:
            return True, [hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]]
    return False, [13, 13, 13, 13, 13]


# 顺子
def check_straight(hand):
    if hand[0][0] == (hand[1][0]+1) == (hand[2][0]+2) == (hand[3][0]+3) == (hand[4][0]+4):
        return True, [hand[0][0]]
    if hand[0][0] == 12 and hand[1][0] == 3 and hand[2][0] == 2 and hand[3][0] == 1 and hand[4][0] == 0:
        return True, [hand[0][0]]
    return False, [13]


# 同花顺
def check_flush_straight(hand):
    if check_flush(hand)[0] and check_straight(hand)[0]:
        return True, [hand[0][0]]
    return False, [13]


# 铁支
def check_fourofakind(hand):
    hand_rank = [hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]]
    for quad_card in range(13):
        if hand_rank.count(quad_card) == 4:
            for kicker in range(13):
                if hand_rank.count(kicker) == 1:
                    return True, [quad_card]
    return False, [13]


# 葫芦
def check_fullhouse(hand):
    hand_rank = [hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]]
    for trip_card in range(13):
        if hand_rank.count(trip_card) == 3:
            for kicker in range(13):
                if hand_rank.count(kicker) == 2:
                    return True, [trip_card]
    return False, [13]


# 三条
def check_threeofakind(hand):
    hand_rank = [hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]]
    for trip_card in range(13):
        if hand_rank.count(trip_card) == 3:
            for kicker1 in range(13):
                if hand_rank.count(kicker1) == 1:
                    for kicker2 in range(kicker1 + 1, 13):
                        if hand_rank.count(kicker2) == 1:
                            return True, [trip_card]
    return False, [13]


# 两对
def check_twopair(hand):
    hand_rank = [hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]]
    for pair_card_low in range(13):
        if hand_rank.count(pair_card_low) == 2:
            for pair_card_high in range(pair_card_low+1, 13):
                if hand_rank.count(pair_card_high) == 2:
                    for kicker in range(13):
                        if hand_rank.count(kicker) == 1:
                            return True, [pair_card_high, pair_card_low, kicker]
    return False, [13, 13, 13]


# 一对
def check_onepair(hand):
    hand_rank = [hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]]
    for pair_card in range(13):
        if hand_rank.count(pair_card) == 2:
            for kicker1 in range(13):
                if hand_rank.count(kicker1) == 1:
                    for kicker2 in range(kicker1 + 1, 13):
                        if hand_rank.count(kicker2) == 1:
                            for kicker3 in range(kicker2 + 1, 13):
                                if hand_rank.count(kicker3) == 1:
                                    return True, [pair_card, kicker3, kicker2, kicker1]
    return False, [13, 13, 13, 13]


# 散牌
def check_scattered(hand):
    if check_flush_straight(hand)[0] or check_fourofakind(hand)[0] or check_fullhouse(hand)[0] or\
            check_flush(hand)[0] or check_straight(hand)[0] or check_threeofakind(hand)[0] or\
            check_twopair(hand)[0] or check_onepair(hand)[0]:
        return False, [13, 13, 13, 13, 13]
    return True, [hand[0][0], hand[1][0], hand[2][0], hand[3][0], hand[4][0]]


# 对比
def compare_list(lis1, lis2):
    if lis1 == lis2:
        return 0
    if lis1 > lis2:
        return 1
    if lis1 < lis2:
        return 2


# 判断牌的类型
def get_kind(hand):
    # 同花顺＞铁支＞葫芦＞同花＞顺子＞三条＞两对＞对子＞散牌
    if check_flush_straight(hand)[0]:return 8,check_flush_straight(hand)[1]
    if check_fourofakind(hand)[0]:return 7,check_fourofakind(hand)[1]
    if check_fullhouse(hand)[0]:return 6,check_fullhouse(hand)[1]
    if check_flush(hand)[0]:return 5,check_flush(hand)[1]
    if check_straight(hand)[0]:return 4,check_straight(hand)[1]
    if check_threeofakind(hand)[0]:return 3,check_threeofakind(hand)[1]
    if check_twopair(hand)[0]:return 2,check_twopair(hand)[1]
    if check_onepair(hand)[0]:return 1,check_onepair(hand)[1]
    if check_scattered(hand)[0]:return 0,check_scattered(hand)[1]


# 两手牌对比
def compare_hands(cardblack, cardwhite):
    handwhite = hand_to_numeric(cardwhite)
    handblack = hand_to_numeric(cardblack)
    (levelwhite, listwhite) = get_kind(handwhite)
    (levelblack, listblack) = get_kind(handblack)
    if levelblack > levelwhite:
        return "Black wins"
    if levelblack < levelwhite:
        return "White wins"
    if levelwhite == levelblack:
        if compare_list(listwhite, listblack) == 1:
            return "White wins"
        if compare_list(listwhite, listblack) == 2:
            return "Black wins"
        if compare_list(listwhite, listblack) == 0:
            return "Tie"


if __name__ == "__main__":
    cardBlack = "2H 3D 5S 9C KD"
    cardWhite = "2D 3H 5C 9S KH"
    result = compare_hands(cardBlack, cardWhite)
    print(result)


