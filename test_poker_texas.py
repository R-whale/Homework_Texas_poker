import pytest
import Poker_texas as pt


def test_check_hands():
    assert pt.check_hands("2s 3c 4d 5h 6S") == True
    assert pt.check_hands("2s 3c 4d 5h") == False
    assert pt.check_hands("2s3c4d5h") == False
    assert pt.check_hands("2s_3c_4d 5h 6S") == False
    assert pt.check_hands("2s 3f dh 4e 8m") == False
    assert pt.check_hands("2s 3c 4d 5h 5h") == False


def test_hand_to_numeric():
    assert pt.hand_to_numeric("2s 3c 4d 5h 6S") == \
        [[4, 1], [3, 2], [2, 0], [1, 3], [0, 1]]


def test_check_flush_straight():
    assert pt.check_flush_straight(pt.hand_to_numeric("As 2s 3s 4s 5s")) == (True, [12])
    assert pt.check_flush_straight(pt.hand_to_numeric("3c 4c 5c 6c 7c")) == (True, [5])
    assert pt.check_flush_straight(pt.hand_to_numeric("Ah 3h 4h 5h 6h")) == (False, [13])
    assert pt.check_flush_straight(pt.hand_to_numeric("As 2s 3s 4s 5h")) == (False, [13])
    assert pt.check_flush_straight(pt.hand_to_numeric("As 6s 3s 4s 5h"))== (False, [13])


def test_check_fourofakind():
    assert pt.check_fourofakind(pt.hand_to_numeric("Ad As Ah Ac 3s")) == (True, [12])
    assert pt.check_fourofakind(pt.hand_to_numeric("Ad As Ah 3c 3s")) == (False, [13])


def test_check_fullhouse():
    assert pt.check_fullhouse(pt.hand_to_numeric("Ad As Ah 3c 3s")) == (True, [12])
    assert pt.check_fullhouse(pt.hand_to_numeric("Ad As 2c 2d 3s")) == (False, [13])


def test_check_flush():
    assert pt.check_flush(pt.hand_to_numeric("Ah 3h 4h 5h 6h")) == (True, [12, 4, 3, 2, 1])
    assert pt.check_flush(pt.hand_to_numeric("Ah 3h 4h 5h 6s")) == (False, [13, 13, 13, 13, 13])


def test_check_straight():
    assert pt.check_straight(pt.hand_to_numeric("4s 5c 6d 7h 8h")) == (True, [6])
    assert pt.check_straight(pt.hand_to_numeric("4s 5c 6d 7h 9c"))== (False, [13])


def test_check_threeofakind():
    assert pt.check_threeofakind(pt.hand_to_numeric("3d 3s 3h 2h 4c")) == (True, [1])
    assert pt.check_threeofakind(pt.hand_to_numeric("3d 3s 3h 2h 2c")) == (False, [13])


def test_check_twopair():
    assert pt.check_twopair(pt.hand_to_numeric("3d 3s 4h 2h 2c")) == (True, [1, 0, 2])
    assert pt.check_twopair(pt.hand_to_numeric("2d 4h 5c 6s 7c")) == (False, [13, 13, 13])


def test_check_onepair():
    assert pt.check_onepair(pt.hand_to_numeric("3d 3s 4h 2h 5s")) == (True, [1, 3, 2, 0])
    assert pt.check_onepair(pt.hand_to_numeric("2d 4h 5c 6s 7c")) == (False, [13, 13, 13, 13])


def test_check_scattered():
    assert pt.check_scattered(pt.hand_to_numeric("2d 4h 5c 6s 7c")) == (True, [5, 4, 3, 2, 0])
    assert pt.check_scattered(pt.hand_to_numeric("2d 2s 3h 3s 5s")) == (False, [13, 13, 13, 13, 13])


def test_get_kind():
    assert pt.get_kind(pt.hand_to_numeric("As 2s 3s 4s 5s")) == (8, [12])
    assert pt.get_kind(pt.hand_to_numeric("2d 2s 2h 2c 3s")) == (7, [0])
    assert pt.get_kind(pt.hand_to_numeric("3d 3s 3h 2h 2c")) == (6, [1])
    assert pt.get_kind(pt.hand_to_numeric("2s 4s 5s 7s 8s")) == (5, [6, 5, 3, 2, 0])
    assert pt.get_kind(pt.hand_to_numeric("4s 5c 6d 7h 8h")) == (4, [6])
    assert pt.get_kind(pt.hand_to_numeric("3d 3s 3h 2h 4c")) == (3, [1])
    assert pt.get_kind(pt.hand_to_numeric("3d 3s 4h 2h 2c")) == (2, [1, 0, 2])
    assert pt.get_kind(pt.hand_to_numeric("3d 3s 4h 2h 5s")) == (1, [1, 3, 2, 0])
    assert pt.get_kind(pt.hand_to_numeric("2d 4h 5c 6s 7c")) == (0, [5, 4, 3, 2, 0])


def test_compare_hands():
    assert pt.compare_hands("2H 3D 5S 9C KD", "2C 3H 4S 8C AH") == "White wins"
    assert pt.compare_hands("2H 4S 4C 2D 4H", "2S 8S AS QS 3S") == "Black wins"
    assert pt.compare_hands("2H 3D 5S 9C KD", "2C 3H 4S 8C KH") == "Black wins"
    assert pt.compare_hands("2H 3D 5S 9C KD", "2D 3H 5C 9S KH") == "Tie"


if __name__ == "__main__":
    pytest.main()