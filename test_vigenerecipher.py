from crypto_app.vigenerecipher_algo import VigenereCipher


def test_vigenerecipher():

    algo = VigenereCipher()
    msg = "Message"
    key = "adtjcopr"
    result = "Mhlbcut"

    encrypted = algo.encrypt(msg, key)
    assert encrypted == result
    decrypted = algo.decrypt(encrypted, key)
    assert decrypted == msg


if __name__ == '__main__':
    test_vigenerecipher()
