from crypto_app.sha_algo import SHA


def test_sha():

    algo = SHA()
    msg = "Message"
    key = "adtjcopr"
    result = "4fb472dfc43def7a46ad442c58ac532f89e0c8a96f23b672f5fd637652"\
    "eab158d4d589444ef7530a34e6626b40830b4e1ec5364611ae31c599bffa958e8b4c4e"
    encrypted = algo.encrypt(msg, key)
    assert encrypted == result


if __name__ == '__main__':
    test_sha()
