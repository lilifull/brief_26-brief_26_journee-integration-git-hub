from crypto_app.caesarcipher_algo import CaesarCipher

def test_caesarcipher():

    algo = CaesarCipher()
    msg = "Message"
    key = 10

    encrypted = algo.encrypt(msg, key)
    #print(encrypted)
    assert encrypted == "Wocckqo"
    decrypted = algo.decrypt(encrypted, key)
    #print(decrypted)
    assert decrypted == "Message"

if __name__ == '__main__':
    test_caesarcipher()