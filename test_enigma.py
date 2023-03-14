from crypto_app.enigmam3_algo import EnigmaM3


def test_enigma():

    algo = EnigmaM3()
    msg = "Message"
    key = [
        ('A', 'C', 'N'),
        (2, 4, 1),
        ('F', 'H', 'K'),
        [('A', 'K')]
    ]

    encrypted = algo.encrypt(msg, key)
    assert encrypted == "FUTALDK"
    decrypted = algo.decrypt(encrypted, key)
    assert decrypted == "MESSAGE"


if __name__ == '__main__':
    test_enigma()
