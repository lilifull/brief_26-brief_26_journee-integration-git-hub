from crypto_app.vigenerecipher_algo import VigenereCipher


def test_vigenerecipher():

    algo = VigenereCipher()
    msg = "Message"
    key = "adtjcopr"

    encrypted = algo.encrypt(msg, key)
    assert encrypted == "Mhlbcut"
    #print(encrypted)
    decrypted = algo.decrypt(encrypted, key)
    #print(decrypted)
    assert decrypted == "Message"

if __name__ == '__main__':
    test_vigenerecipher()
