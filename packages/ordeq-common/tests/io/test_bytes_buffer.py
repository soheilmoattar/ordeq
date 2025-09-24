

















def test_it_is_unique():
    a, b = BytesBuffer(b""), BytesBuffer(b"")
    assert a is not b
    assert a != b
    assert hash(a) != hash(b)
