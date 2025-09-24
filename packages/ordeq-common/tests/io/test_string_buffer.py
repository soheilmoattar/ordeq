


















def test_it_is_unique():
    a, b = StringBuffer(""), StringBuffer("")
    assert a is not b
    assert a != b
    assert hash(a) != hash(b)
