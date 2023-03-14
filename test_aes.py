from crypto_app.aes_algo import AdvancedEncryptionStandard


def test_aes():

    algo = AdvancedEncryptionStandard()
    msg = "Message"
    key = "justineisthebest"
    result = "3d87266b6f76d9"

    encrypted = algo.encrypt(msg, key)
    assert encrypted == result
    decrypted = algo.decrypt(encrypted, key)
    assert decrypted == msg


if __name__ == '__main__':
    test_aes()
