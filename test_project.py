from project import calc_wpm


def test_calc_wpm():
    assert calc_wpm(5,5,10) == 5
    assert calc_wpm(7,3,10) == 7


test_calc_wpm()
