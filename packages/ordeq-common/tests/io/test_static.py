from ordeq_common import Static






def test_it_is_unique():
    a, b = Static(""), Static("")
    assert a is not b
    assert a != b
    assert hash(a) != hash(b)
