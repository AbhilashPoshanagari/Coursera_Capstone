from hello import more_hello, more_good_bye


def test_more_hello():
    assert "Hi" == more_hello()


def test_more_bye():
    assert "good bye" == more_good_bye()
