from crypto_app.aes_algo import AdvancedEncryptionStandard

def test_aes():

    algo = AdvancedEncryptionStandard()
    msg = "Message"
    key = "justineisthebest"

    encrypted = algo.encrypt(msg, key)
    #print(encrypted)
    assert encrypted == "3d87266b6f76d9"
    decrypted = algo.decrypt(encrypted, key)
    #print(decrypted)
    assert decrypted == "Message"

if __name__ == '__main__':
    test_aes()
