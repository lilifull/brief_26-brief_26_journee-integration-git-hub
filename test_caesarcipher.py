from crypto_app.caesarcipher_algo import CaesarCipher


def test_caesarcipher():

    algo = CaesarCipher()
    msg = "Message"
    key = 10
    result = "Wocckqo"

    encrypted = algo.encrypt(msg, key)
    assert encrypted == result
    decrypted = algo.decrypt(encrypted, key)
    assert decrypted == msg


if __name__ == '__main__':
    test_caesarcipher()
